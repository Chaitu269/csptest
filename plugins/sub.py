import time
import random
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)




CMD = ["/", "." , ""]





@Client.on_message(filters.command("deepl1" , CMD))
async def deepl1(_, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("VIP 1",callback_data = "1cse")], 
        			[InlineKeyboardButton("VIP 2",callback_data = "1cse") ],
		[InlineKeyboardButton("VIP 2",callback_data = "1cse") ],
		[InlineKeyboardButton("VIP 2",callback_data = "1cse") ],
		[InlineKeyboardButton("VIP 2",callback_data = "1cse") ]]))




@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")
