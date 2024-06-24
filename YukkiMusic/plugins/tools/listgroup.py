
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPrivileges
import time

from YukkiMusic import app
from YukkiMusic.misc import SUDOERS

@app.on_message(filters.command("listgroup") & SUDOERS)
async def list_groups(client, message):
    try:
        group_list = []
        async for dialog in client.get_dialogs():
            if dialog.chat.type in ["group", "supergroup"]:
                group_list.append(dialog.chat)

        if not group_list:
            await message.reply("Bot tidak ada di grup manapun.")
            return

        response = "Daftar grup yang menggunakan bot:\n"
        for group in group_list:
            response += f"- {group.title} (ID: {group.id})\n"

        await message.reply(response)

    except Exception as e:
        await message.reply(f"Terjadi kesalahan: {str(e)}")
