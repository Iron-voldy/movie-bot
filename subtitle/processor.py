import pysubs2
import chardet
import gzip
import logging
import re
from io import BytesIO, StringIO
from typing import Optional, Tuple, Dict, List
from config.subtitle_config import SUBTITLE_SETTINGS, ERROR_MESSAGES

logger = logging.getLogger(__name__)

class SubtitleProcessor:
    """Handles subtitle file processing, conversion, and validation"""
    
    def __init__(self):
        self.max_file_size = SUBTITLE_SETTINGS['max_file_size']
        self.supported_formats = SUBTITLE_SETTINGS['supported_formats']
        self.default_encoding = SUBTITLE_SETTINGS['encoding']
    
    def detect_encoding(self, content: bytes) -> str:
        """Detect the encoding of subtitle content"""
        try:
            detection = chardet.detect(content)
            encoding = detection.get('encoding', self.default_encoding)
            confidence = detection.get('confidence', 0)
            
            # If confidence is low, fallback to common encodings
            if confidence < 0.7:
                for fallback_encoding in ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']:
                    try:
                        content.decode(fallback_encoding)
                        encoding = fallback_encoding
                        break
                    except UnicodeDecodeError:
                        continue
            
            logger.info(f"Detected encoding: {encoding} (confidence: {confidence:.2f})")
            return encoding
            
        except Exception as e:
            logger.error(f"Encoding detection failed: {e}")
            return self.default_encoding
    
    def clean_subtitle_content(self, content: str) -> str:
        """Clean and normalize subtitle content"""
        # Remove BOM if present
        if content.startswith('\ufeff'):
            content = content[1:]
        
        # Normalize line endings
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        
        # Remove excessive blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        # Clean up common subtitle artifacts
        content = re.sub(r'<[^>]+>', '', content)  # Remove HTML tags
        content = re.sub(r'\{[^}]+\}', '', content)  # Remove style tags
        
        # Fix common encoding issues
        replacements = {
            'â€™': "'",
            'â€œ': '"',
            'â€': '"',
            'â€¦': '...',
            'â€"': '—',
            'â€"': '–'
        }
        
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        return content.strip()
    
    def validate_subtitle_file(self, content: bytes) -> Tuple[bool, str]:
        """Validate subtitle file content and format"""
        if len(content) > self.max_file_size:
            return False, ERROR_MESSAGES['file_too_large']
        
        if len(content) == 0:
            return False, "Empty subtitle file"
        
        try:
            # Try to decode the content
            encoding = self.detect_encoding(content)
            text_content = content.decode(encoding, errors='replace')
            
            # Check if it looks like a subtitle file
            if self._is_valid_subtitle_format(text_content):
                return True, "Valid subtitle file"
            else:
                return False, "Invalid subtitle format"
                
        except Exception as e:
            logger.error(f"Validation error: {e}")
            return False, f"Validation failed: {str(e)}"
    
    def _is_valid_subtitle_format(self, content: str) -> bool:
        """Check if content appears to be a valid subtitle format"""
        # Check for SRT format
        srt_pattern = r'\d+\s*\n\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}'
        if re.search(srt_pattern, content):
            return True
        
        # Check for VTT format
        if 'WEBVTT' in content[:100]:
            return True
        
        # Check for ASS/SSA format
        if '[Script Info]' in content or '[V4+ Styles]' in content:
            return True
        
        # Check for basic time patterns
        time_pattern = r'\d{2}:\d{2}:\d{2}'
        if len(re.findall(time_pattern, content)) > 2:
            return True
        
        return False
    
    def process_subtitle_file(self, content: bytes, target_format: str = 'srt') -> Tuple[Optional[str], str]:
        """Process subtitle file and convert to target format"""
        try:
            # Validate the file first
            is_valid, validation_message = self.validate_subtitle_file(content)
            if not is_valid:
                return None, validation_message
            
            # Detect encoding and decode
            encoding = self.detect_encoding(content)
            text_content = content.decode(encoding, errors='replace')
            
            # Clean the content
            cleaned_content = self.clean_subtitle_content(text_content)
            
            # Load with pysubs2
            subtitles = pysubs2.SSAFile.from_string(cleaned_content)
            
            # Validate that we have actual subtitle events
            if len(subtitles) == 0:
                return None, "No subtitle entries found"
            
            # Convert to target format
            if target_format.lower() == 'srt':
                output = subtitles.to_string('srt')
            elif target_format.lower() == 'vtt':
                output = subtitles.to_string('webvtt')
            elif target_format.lower() in ['ass', 'ssa']:
                output = subtitles.to_string('ass')
            else:
                # Default to SRT
                output = subtitles.to_string('srt')
            
            # Final cleanup
            output = self.clean_subtitle_content(output)
            
            logger.info(f"Successfully processed subtitle file: {len(subtitles)} entries")
            return output, "Success"
            
        except Exception as e:
            logger.error(f"Processing error: {e}")
            return None, f"Processing failed: {str(e)}"
    
    def extract_subtitle_info(self, content: str) -> Dict[str, any]:
        """Extract metadata information from subtitle content"""
        info = {
            'format': 'unknown',
            'entries_count': 0,
            'duration': 0,
            'language': None,
            'title': None,
            'framerate': None
        }
        
        try:
            # Detect format
            if 'WEBVTT' in content[:100]:
                info['format'] = 'vtt'
            elif '[Script Info]' in content:
                info['format'] = 'ass'
            elif re.search(r'\d+\s*\n\d{2}:\d{2}:\d{2},\d{3}\s*-->', content):
                info['format'] = 'srt'
            
            # Load with pysubs2 to get detailed info
            subtitles = pysubs2.SSAFile.from_string(content)
            info['entries_count'] = len(subtitles)
            
            if subtitles:
                # Calculate duration
                if subtitles.events:
                    last_event = max(subtitles.events, key=lambda x: x.end)
                    info['duration'] = last_event.end / 1000.0  # Convert to seconds
                
                # Extract metadata from SSA/ASS files
                if hasattr(subtitles, 'info'):
                    info['title'] = subtitles.info.get('Title', None)
                    
                # Try to detect language from content
                info['language'] = self._detect_language_from_content(content)
            
        except Exception as e:
            logger.error(f"Info extraction error: {e}")
        
        return info
    
    def _detect_language_from_content(self, content: str) -> Optional[str]:
        """Attempt to detect language from subtitle content"""
        # This is a basic implementation - you could integrate with langdetect library
        # for more accurate detection
        
        # Look for language indicators in the content
        language_indicators = {
            'en': ['the', 'and', 'you', 'that', 'have', 'for', 'not', 'with'],
            'es': ['que', 'de', 'no', 'la', 'el', 'en', 'y', 'a', 'es', 'se'],
            'fr': ['que', 'de', 'je', 'est', 'pas', 'le', 'vous', 'la', 'tu', 'il'],
            'de': ['der', 'die', 'und', 'in', 'den', 'von', 'zu', 'das', 'mit', 'ist'],
            'it': ['che', 'di', 'la', 'il', 'un', 'è', 'per', 'una', 'in', 'del'],
            'pt': ['que', 'de', 'não', 'o', 'a', 'para', 'com', 'uma', 'é', 'do'],
            'ru': ['что', 'не', 'я', 'быть', 'на', 'с', 'как', 'он', 'это', 'но'],
        }
        
        # Count occurrences of language-specific words
        content_lower = content.lower()
        scores = {}
        
        for lang, words in language_indicators.items():
            score = sum(content_lower.count(word) for word in words)
            if score > 0:
                scores[lang] = score
        
        if scores:
            return max(scores, key=scores.get)
        
        return None
    
    def compress_subtitle_content(self, content: str) -> bytes:
        """Compress subtitle content using gzip"""
        try:
            content_bytes = content.encode(self.default_encoding)
            compressed = gzip.compress(content_bytes)
            logger.info(f"Compressed {len(content_bytes)} bytes to {len(compressed)} bytes")
            return compressed
        except Exception as e:
            logger.error(f"Compression error: {e}")
            return content.encode(self.default_encoding)
    
    def decompress_subtitle_content(self, compressed_content: bytes) -> str:
        """Decompress subtitle content"""
        try:
            decompressed = gzip.decompress(compressed_content)
            return decompressed.decode(self.default_encoding)
        except Exception as e:
            logger.error(f"Decompression error: {e}")
            # Assume it's not compressed
            return compressed_content.decode(self.default_encoding, errors='replace')
    
    def convert_format(self, content: str, source_format: str, target_format: str) -> Optional[str]:
        """Convert subtitle from one format to another"""
        try:
            # Load the subtitle
            if source_format.lower() == 'srt':
                subtitles = pysubs2.SSAFile.from_string(content)
            elif source_format.lower() == 'vtt':
                subtitles = pysubs2.SSAFile.from_string(content)
            elif source_format.lower() in ['ass', 'ssa']:
                subtitles = pysubs2.SSAFile.from_string(content)
            else:
                # Try to auto-detect
                subtitles = pysubs2.SSAFile.from_string(content)
            
            # Convert to target format
            if target_format.lower() == 'srt':
                return subtitles.to_string('srt')
            elif target_format.lower() == 'vtt':
                return subtitles.to_string('webvtt')
            elif target_format.lower() == 'ass':
                return subtitles.to_string('ass')
            else:
                return subtitles.to_string('srt')  # Default to SRT
                
        except Exception as e:
            logger.error(f"Format conversion error: {e}")
            return None
    
    def sync_subtitles(self, content: str, offset_seconds: float) -> Optional[str]:
        """Synchronize subtitles by shifting timing"""
        try:
            subtitles = pysubs2.SSAFile.from_string(content)
            
            # Convert offset to milliseconds
            offset_ms = int(offset_seconds * 1000)
            
            # Shift all events
            subtitles.shift(ms=offset_ms)
            
            return subtitles.to_string('srt')
            
        except Exception as e:
            logger.error(f"Sync error: {e}")
            return None
    
    def merge_subtitle_files(self, subtitle_contents: List[str]) -> Optional[str]:
        """Merge multiple subtitle files into one"""
        try:
            merged = pysubs2.SSAFile()
            
            for content in subtitle_contents:
                subtitles = pysubs2.SSAFile.from_string(content)
                merged.extend(subtitles)
            
            # Sort by start time
            merged.sort()
            
            return merged.to_string('srt')
            
        except Exception as e:
            logger.error(f"Merge error: {e}")
            return None
    
    def create_subtitle_preview(self, content: str, max_lines: int = 5) -> str:
        """Create a preview of subtitle content"""
        try:
            subtitles = pysubs2.SSAFile.from_string(content)
            
            preview_lines = []
            for i, event in enumerate(subtitles.events[:max_lines]):
                start_time = self._ms_to_timestamp(event.start)
                text = event.text.replace('\\N', ' ')  # Replace line breaks
                preview_lines.append(f"{start_time}: {text}")
            
            if len(subtitles.events) > max_lines:
                preview_lines.append(f"... and {len(subtitles.events) - max_lines} more entries")
            
            return '\n'.join(preview_lines)
            
        except Exception as e:
            logger.error(f"Preview error: {e}")
            return "Preview not available"
    
    def _ms_to_timestamp(self, milliseconds: int) -> str:
        """Convert milliseconds to timestamp format"""
        seconds = milliseconds // 1000
        ms = milliseconds % 1000
        minutes = seconds // 60
        seconds = seconds % 60
        hours = minutes // 60
        minutes = minutes % 60
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{ms:03d}"