import time
import random
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)




CMD = ["/", "." , ""]




@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("This Bot will provide you textbooks and previous quation papers \n\n Just enter the cource code or cource name you will get the text books and previous quation ppers of the cource \n\n  If you found any wrong information in this bot click /admin to send message to the admin   \n\n   If you want to add any new cource in this bot click \requst to send request to add cource  ")

@Client.on_message(filters.command("admin", CMD))
async def help(_, message):
    await message.reply_text("if you found any wrong information in this bot  please message here @myagnasai we will update the information as sonn as possible")

@Client.on_message(filters.command("request", CMD))
async def help(_, message):
    await message.reply_text("if you want to add any extra cource in this bot  please message here @Chaitu_1438 we will check cource details and add as soon as possible")

@Client.on_message(filters.command(["dl", "deeplearning"] , CMD))
async def deepl1(_, message):
    await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('Unit 1', callback_data="dlu1"),
                    InlineKeyboardButton('Unit 2', callback_data="dlu1")
                ],[
                    InlineKeyboardButton('Unit 3', url=f"https://t.me/Testkarebot?start=ZmlsZV9CUUFEQlFBREVnb0FBaUZGYVZXN2JIcGxNeFNrSUJZRQ"),
                    InlineKeyboardButton('Unit 4', callback_data='dlu4')
                ],[
                    InlineKeyboardButton('Unit 5', callback_data="dlu5"),
                    InlineKeyboardButton('Previous Quation Papers ', callback_data="dlu1")
               
                ]])


