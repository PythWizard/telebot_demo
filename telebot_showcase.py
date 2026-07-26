# -*- coding: utf-8 -*-

"""
Telegram AI Assistant - showcase version

Demonstrates:
- Telegram message handling via Telethon
- OpenAI API integration
- Conversation context management
- Human-like typing simulation

Some production features are removed from this public demo.
"""

import asyncio
from collections import defaultdict, deque

from telethon import TelegramClient, events
from telethon.tl.functions.messages import SetTypingRequest
from telethon.tl.types import SendMessageTypingAction

from openai import OpenAI


# ---------------- Configuration ----------------

API_ID = "YOUR_TELEGRAM_API_ID"
API_HASH = "YOUR_TELEGRAM_API_HASH"

OPENAI_KEY = "YOUR_OPENAI_API_KEY"

MODEL = "gpt-4.1-nano"

client = TelegramClient(
    "assistant_session",
    API_ID,
    API_HASH
)

openai_client = OpenAI(api_key=OPENAI_KEY)


# Store recent conversation context
dialog_history = defaultdict(
    lambda: deque(maxlen=20)
)


SYSTEM_PROMPT = """
You are a helpful Telegram AI assistant.

Respond naturally and keep the conversation context.
"""


# ---------------- AI Processing ----------------

async def generate_reply(user_id: int, text: str) -> str:
    """
    Generate response using OpenAI API
    with previous conversation context.
    """

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(dialog_history[user_id])

    messages.append({
        "role": "user",
        "content": text
    })


    response = openai_client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()


    dialog_history[user_id].append({
        "role": "user",
        "content": text
    })

    dialog_history[user_id].append({
        "role": "assistant",
        "content": reply
    })


    return reply



# ---------------- Telegram Handler ----------------

@client.on(events.NewMessage(incoming=True))
async def message_handler(event):

    if not event.is_private:
        return


    user_id = event.sender_id
    text = event.message.message.strip()


    if not text:
        return


    print(f"[IN] {user_id}: {text}")


    reply = await generate_reply(
        user_id,
        text
    )


    # Simulate human typing
    await client(
        SetTypingRequest(
            peer=event.chat_id,
            action=SendMessageTypingAction()
        )
    )

    await asyncio.sleep(2)


    await event.respond(reply)


    print(f"[OUT] {user_id}: {reply}")



# ---------------- Run ----------------

async def main():

    await client.start()

    print(
        "Telegram AI Assistant started..."
    )

    await client.run_until_disconnected()



if __name__ == "__main__":
    asyncio.run(main())
