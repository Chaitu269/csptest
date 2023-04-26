import time
import random
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)




CMD = ["/", "." , ""]




@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("Tʜɪs Bᴏᴛ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛᴇxᴛʙᴏᴏᴋs ᴀɴᴅ ᴘʀᴇᴠɪᴏᴜs ᴏ̨ᴜᴀᴛɪᴏɴ ᴘᴀᴘᴇʀs \n\n\n Jᴜsᴛ ᴇɴᴛᴇʀ ᴛʜᴇ ᴄᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏʀ ᴄᴏᴜʀᴄᴇ ɴᴀᴍᴇ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ᴛᴇxᴛ ʙᴏᴏᴋs ᴀɴᴅ ᴘʀᴇᴠɪᴏᴜs ᴏ̨ᴜᴀᴛɪᴏɴ ᴘᴘᴇʀs ᴏғ ᴛʜᴇ ᴄᴏᴜʀᴄᴇ \n\n\n  Iғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ᴡʀᴏɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɪɴ ᴛʜɪs ʙᴏᴛ ᴄʟɪᴄᴋ /ᴀᴅᴍɪɴ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ   \n\n\n   Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴀɴʏ ɴᴇᴡ ᴄᴏᴜʀᴄᴇ ɪɴ ᴛʜɪs ʙᴏᴛ ᴄʟɪᴄᴋ \ʀᴇᴏ̨ᴜsᴛ ᴛᴏ sᴇɴᴅ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ᴀᴅᴅ ᴄᴏᴜʀᴄᴇ ")

@Client.on_message(filters.command("admin", CMD))
async def admin(_, message):
    await message.reply_text("ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ᴡʀᴏɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɪɴ ᴛʜɪs ʙᴏᴛ  ᴘʟᴇᴀsᴇ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ  \n@myagnasai \n ᴡᴇ ᴡɪʟʟ ᴜᴘᴅᴀᴛᴇ ᴛʜᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀs sᴏɴɴ ᴀs ᴘᴏssɪʙʟᴇ")



@Client.on_message(filters.command(["dl", "deeplearning" , "deep learning"] , CMD))
async def dl(_, message):
    await message.reply_text("Select option",quote=True,reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('Unit 1', callback_data="dlu1"),
                    InlineKeyboardButton('Unit 2', callback_data="dlu1")
                ],[
                    InlineKeyboardButton('Unit 3', url=f"https://t.me/Testkarebot?start=ZmlsZV9CUUFEQlFBREVnb0FBaUZGYVZXN2JIcGxNeFNrSUJZRQ"),
                    InlineKeyboardButton('Unit 4', callback_data='dlu4')
                ],[
                    InlineKeyboardButton('Unit 5', callback_data="dlu5"),
                    InlineKeyboardButton('Previous Quation Papers ', callback_data="dlu1")
                ]]))

@Client.on_message(filters.command("request", CMD))
async def request(_, message):
    await message.reply_text("ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴀɴʏ ᴇxᴛʀᴀ ᴄᴏᴜʀᴄᴇ ɪɴ ᴛʜɪs ʙᴏᴛ  ᴘʟᴇᴀsᴇ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ \n @chaitu_1438 \n ᴡᴇ ᴡɪʟʟ ᴄʜᴇᴄᴋ ᴄᴏᴜʀᴄᴇ ᴅᴇᴛᴀɪʟs ᴀɴᴅ ᴀᴅᴅ ᴀs sᴏᴏɴ ᴀs ᴘᴏssɪʙʟᴇ")                             
