from YukkiMusic import app
from pyrogram import Client
from utils.groups import get_group_names


@app.on_message()
async def handle_message(client, message):
    if "/grouplist" in message.text:
        group_names = await get_group_names(app)
        if group_names:
            await message.reply_text("\n".join(group_names))
        else:
            await message.reply_text("Bot belum ditambahkan ke grup mana pun.")
