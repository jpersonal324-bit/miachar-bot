import os
import json
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION_STRING"]

MENSAJE = "Hola bb\nVideollamada 45 dolares 20 min\n30 dolares 10 min\n30 dolares 10 videos\nAcepto PayPal Zelle y Remitly"
ARCHIVO = "respondidos.json"

if os.path.exists(ARCHIVO):
      with open(ARCHIVO) as f:
            respondidos = set(json.load(f))
else:
      respondidos = set()

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handler(event):
      sender_id = event.sender_id
      if sender_id not in respondidos:
            respondidos.add(sender_id)
            await event.respond(MENSAJE)
            with open(ARCHIVO, "w") as f:
                  json.dump(list(respondidos), f)

print("Userbot iniciado...")
client.start()
client.run_until_disconnected()