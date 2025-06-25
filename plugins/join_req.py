from hydrogram import Client, filters, enums
from hydrogram.types import ChatJoinRequest
from database.users_chats_db import db
from info import ADMINS, AUTH_CHANNEL
from utils import temp


@Client.on_chat_join_request()
async def join_reqs(client, message: ChatJoinRequest):
  if message.chat.id in temp.AUTH_CHANNEL:
    if not await db.find_join_req(message.from_user.id):
      await db.add_join_req(message.from_user.id)


@Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMINS))
async def del_requests(client, message):
  await db.del_join_req()
  await message.reply('Deleted!')
