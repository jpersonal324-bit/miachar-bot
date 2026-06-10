import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION_STRING"]

MENSAJE = (
          "Hola bb\n"
          "Videollamada 45 dolares 20 min\n"
          "30 dolares 10 min\n"
          "30 dolares 10 videos\n"
          "Acepto PayPal Zelle y Remitly"
)

respondidos = set()

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handler(event):
          sender_id = event.sender_id
          if sender_id not in respondidos:
                        respondidos.add(sender_id)
                        await event.respond(MENSAJE)

      print("Userbot iniciado...")
client.start()
client.run_until_disconnected()
