FROM python:3.13

WORKDIR /autofilterbot

COPY . /autofilterbot

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
