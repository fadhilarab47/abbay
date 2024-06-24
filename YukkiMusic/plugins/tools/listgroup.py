from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPrivileges, Message
import time
import asyncio
from pymongo import MongoClient
from config import MONGO_DB_URI
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS

# Inisialisasi MongoDB client
mongo_client = MongoClient(MONGO_DB_URI)
db = mongo_client.grouplist
groups_collection = db.groups

@app.on_message(filters.group & filters.new_chat_members)
async def new_group_handler(client: Client, message: Message):
    chat_id = message.chat.id
    chat_name = message.chat.title

    # Cek apakah grup sudah ada di database
    if not groups_collection.find_one({"chat_id": chat_id}):
        # Menyimpan grup ke database
        groups_collection.insert_one({"chat_id": chat_id, "chat_name": chat_name})
        await message.reply_text(f"Grup '{chat_name}' dengan ID {chat_id} telah ditambahkan ke database.")

@app.on_message(filters.command("listgroups") & SUDOERS)
async def list_groups_handler(client: Client, message: Message):
    # Ambil daftar grup dari database
    groups = groups_collection.find()
    response = "Daftar grup yang menggunakan bot ini:\n"
    for group in groups:
        response += f"{group['chat_name']} (ID: {group['chat_id']})\n"
    await message.reply_text(response)
    
