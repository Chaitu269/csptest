import time
import random
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)




CMD = ["/", "." , ""]




@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("Tʜɪs Bᴏᴛ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛᴇxᴛʙᴏᴏᴋs ᴀɴᴅ ᴘʀᴇᴠɪᴏᴜs ᴏ̨ᴜesᴛɪᴏɴ ᴘᴀᴘᴇʀs \n\n\n Jᴜsᴛ ᴇɴᴛᴇʀ ᴛʜᴇ ᴄᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏʀ ᴄᴏᴜʀᴄᴇ ɴᴀᴍᴇ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ᴛᴇxᴛ ʙᴏᴏᴋs ᴀɴᴅ ᴘʀᴇᴠɪᴏᴜs ᴏ̨ᴜᴇsᴛɪᴏɴ ᴘᴀᴘᴇʀs ᴏғ ᴛʜᴇ ᴄᴏᴜʀᴄᴇ \n\n\n  Iғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ᴡʀᴏɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɪɴ ᴛʜɪs ʙᴏᴛ ᴄʟɪᴄᴋ /admin ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ   \n\n\n   Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴀɴʏ ɴᴇᴡ ᴄᴏᴜʀᴄᴇ ɪɴ ᴛʜɪs ʙᴏᴛ ᴄʟɪᴄᴋ /request ᴛᴏ sᴇɴᴅ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ᴀᴅᴅ ᴄᴏᴜʀᴄᴇ ")

@Client.on_message(filters.command("admin", CMD))
async def admin(_, message):
    await message.reply_text("ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ᴡʀᴏɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɪɴ ᴛʜɪs ʙᴏᴛ  ᴘʟᴇᴀsᴇ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ  \n@myagnasai \n ᴡᴇ ᴡɪʟʟ ᴜᴘᴅᴀᴛᴇ ᴛʜᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀs sᴏɴɴ ᴀs ᴘᴏssɪʙʟᴇ")

    
    
    
    
    
    
    
    
    
    
    
    
    
@Client.on_message(filters.command(["cd", "compilerdesign" , "compiler design" , "CSE18R274"] , CMD))
async def cd(_, message):
    await message.reply_text("Select option",quote=True,reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('Unit 1', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURhUWtBQXVwSFVWYmVOSFJPWDRWejFoWUU"),
                    InlineKeyboardButton('Unit 2', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURhZ2tBQXVwSFVWWlVpalNHLUJvenhCWUU")
                ],[
                    InlineKeyboardButton('Unit 3', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURiQWtBQXVwSFVWYnVlRldhdEJEZG9CWUU"),
                    InlineKeyboardButton('Unit 4', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURiUWtBQXVwSFVWYlVwR2NGSUlldXVCWUU")
                ],[
                    InlineKeyboardButton('Unit 5', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURiZ2tBQXVwSFVWYjF5bFM2RFRfMEpoWUU"),
                    InlineKeyboardButton('Previous Question Papers ', callback_data="dlu1")
                ]]))
    
 










@Client.on_message(filters.command(["dl", "deeplearning" , "deep learning" , "CSE18R396"] , CMD))
async def dl(_, message):
    await message.reply_text("Select option",quote=True,reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('Unit 1', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURZZ2tBQXVwSFVWYmxhamZaUjJjS0NoWUU"),
                    InlineKeyboardButton('Unit 2', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURZUWtBQXVwSFVWWWh6aTExbnRvMm9CWUU")
                ],[
                    InlineKeyboardButton('Unit 3', url=f"https://t.me/Testkarebot?start=ZmlsZV9CUUFEQlFBREVnb0FBaUZGYVZXN2JIcGxNeFNrSUJZRQ"),
                    InlineKeyboardButton('Unit 4', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURYUWtBQXVwSFVWWjdUVTZjOVNaLW94WUU")
                ],[
                    InlineKeyboardButton('Unit 5', url=f"https://t.me/Testkarebot?start=ZmlsZXBfQlFBREJRQURYd2tBQXVwSFVWWmJFVkhHbThYVHpSWUU"),
                    InlineKeyboardButton('Previous Question Papers ', callback_data="dlu1")
                ]]))

@Client.on_message(filters.command("request", CMD))
async def request(_, message):
    await message.reply_text("ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴀɴʏ ᴇxᴛʀᴀ ᴄᴏᴜʀᴄᴇ ɪɴ ᴛʜɪs ʙᴏᴛ  ᴘʟᴇᴀsᴇ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ \n @chaitu_1438 \n ᴡᴇ ᴡɪʟʟ ᴄʜᴇᴄᴋ ᴄᴏᴜʀᴄᴇ ᴅᴇᴛᴀɪʟs ᴀɴᴅ ᴀᴅᴅ ᴀs sᴏᴏɴ ᴀs ᴘᴏssɪʙʟᴇ")                             
