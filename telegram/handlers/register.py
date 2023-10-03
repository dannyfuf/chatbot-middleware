from telethon import events, Button

import telegram.handlers.client
import re

client = telegram.handlers.client.client

# Define Register for user.
@client.on(events.NewMessage(pattern='/(?i)register$')) 
async def registerHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    message = 'To become part of the farm please type: \n /name farmer \n /pass 123 \n with farmer, 123 your name and password'
    await client.send_message(SENDER, message, parse_mode="HTML")

#Obtencion de nombre
@client.on(events.NewMessage(pattern='/(?i)name')) 
async def nameHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    match = re.search(r'/name\s+(.+)', mensaje)
    if match:
        secuencia = match.group(1)
        await event.respond(f"Name save: {secuencia}")

#Obtencion de password.
@client.on(events.NewMessage(pattern='/(?i)pass')) 
async def passHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    match = re.search(r'/pass\s+(.+)', mensaje)
    if match:
        secuencia = match.group(1)
        await event.respond(f"Password save: {secuencia}")