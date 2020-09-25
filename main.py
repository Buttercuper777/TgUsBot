from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
 
app = Client("my_account")

 
# Команда love -----------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
@app.on_message(filters.command("love", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".love ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "❤"
    space_symbol = "💓"
    count = 1;

    while (count < 80):
        try:
            msg.edit(typing_symbol + " " + text + " " + typing_symbol)
            sleep(1) # 50 ms
            msg.edit(space_symbol + " " + text + " " + space_symbol)
            count = count + 1
            
        except FloodWait as e:
            sleep(e.x)
    msg.edit(typing_symbol + " " + text + " " + typing_symbol)
 



# .smoke -----------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
@app.on_message(filters.command("smoke", prefixes=".") & filters.me)
def hack(_, msg):

    orig_text = msg.text.split(".smoke ", maxsplit=1)[1]
    text = orig_text
    tbp = "🚬" # to be printed
    k1 = "╔ ╔╗ ─ ║╔ ║║ ╔╗ ║║ ╦ ╠╗"
    k2 = "\n║ ║║ ─ ╠╣ ╚╣ ║║ ║║ ║ ║║"
    k3 = "\n║ ╚╝ ─ ║╚ ═╝ ╠╝ ╚╝ ║ ╚╝"
    k4 = "\nᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠ"
    count = 1;

    while (count < 6):
        try:
            msg.edit(k4 + k2 + k3)
            sleep(0.1)
            msg.edit(k4 + k4 + k3)
            sleep(0.1)
            msg.edit(k4 + k4 + k4)
            sleep(0.1)
            msg.edit(k1+ k4+ k4)
            sleep(0.1)
            msg.edit(k1 + k2 + k4)
            sleep(0.1)
            msg.edit(k1 + k2 + k3)
            sleep(0.1)
            count = count + 1;

        except FloodWait as e:
            sleep(e.x)
            
            
            
# .home -----------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
@app.on_message(filters.command(" h", prefixes=".") & filters.me)
def hack(_, msg):
    
    count = 1
    zs = "5555"
    ns = "ᅠ"

    m1 = "████─████─████─█──█─█──█"
    m2 = "\n█──█─█──█─█──█─█─█──█──█"
    m3 = "\n█────█──█─█──█─██───█─██"
    m4 = "\n█──█─█──█─█──█─█─█──██─█"
    m5 = "\n████─█──█─████─█──█─█──█"
    
    arr_s = [m1, m2, m3, m4, m5]
    
    adr = arr_s[1]
    arr_s[1] = adr + "wecw"
    msg.edit_text(m2)
    

    
    
    
    
app.run()