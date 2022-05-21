#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [GetAnyID bot by TeLe TiPs] (https://github.com/teletips/GetAnyID-TeLeTiPs)

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

GetAnyIDBot=Client(
    "GetAnyIDBot",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@GetAnyIDBot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
Heya {message.from_user.mention},
My name is <b>GetAnyID</b>. I am here to provide user and chat ID.

To get an ID, simply send the command <code>/id</code> directly to any chat or send it as a reply to any kind of message.

I can also work in group chats.

🏠 | [Home](https://t.me/teletipsofficialchannel)
            """
    await GetAnyIDBot.send_message(message.chat.id, text, disable_web_page_preview=True)


@GetAnyIDBot.on_message(filters.command('id'))
async def get_id(client, message):
    try:

        if (not message.reply_to_message) and (message.chat):
            await message.reply(f"User {message.from_user.first_name}'s ID is <code>{message.from_user.id }</code>.\nThis chat's ID is: <code>{message.chat.id}</code>.") 

        elif not message.reply_to_message:
            await message.reply(f"User {message.from_user.first_name}'s ID is <code>{message.from_user.id }</code>.") 

        elif message.reply_to_message.forward_from_chat:
            await message.reply(f"The forwarded {str(message.reply_to_message.forward_from_chat.type)[9:].lower()}, {message.reply_to_message.forward_from_chat.title} has an ID of <code>{message.reply_to_message.forward_from_chat.id}</code>.") 

        elif message.reply_to_message.forward_from:
            await message.reply(f"The forwarded user, {message.reply_to_message.forward_from.first_name} has an ID of <code>{message.reply_to_message.forward_from.id   }</code>.")

        elif message.reply_to_message.forward_sender_name:
            await message.reply("Sorry, you cannot get the forwarded user ID because of their privacy settings")

        else:
            await message.reply(f"User {message.reply_to_message.from_user.first_name}'s ID is <code>{message.reply_to_message.from_user.id}</code>.")   

    except Exception:
            await message.reply("An error occured while getting the ID.")

print("GetAnyIDBot is alive!")
GetAnyIDBot.run()

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
