import asyncio
import datetime
from telethon import events
from telethon.tl import functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="print ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "repo":
        await event.edit("Click [here](https://github.com/Priyam005/TelegramUserBot/) to goto the custom github repo.")
    elif input_str == "deploy":
        await event.edit("Click [here](https://dashboard.heroku.com/apps/userbot-telegram/deploy/github) to goto the heroku deploy page.")
    elif input_str == "mf":
        await event.edit("""
....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
    """)
    else:
        await event.edit("variable not defined.")
