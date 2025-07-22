import os
import time
from pyrogram import Client
from messages import messages

api_id = 20595958
api_hash = "04115615431eea669cda7949cdf37cf2"
session_string = os.environ["SESSION_STRING"]

bot_usernames = ["@teranr8bot", "@teranr6bot", "@teranr3bot"]

with Client(name="my_account",
            api_id=api_id,
            api_hash=api_hash,
            session_string=session_string) as app:

    message_count = 0

    # loop over messages in steps of 5 (number of bots)
    for i in range(0, len(messages), len(bot_usernames)):
        for bot_index, bot_username in enumerate(bot_usernames):
            try:
                msg_index = i + bot_index
                if msg_index >= len(messages):
                    break  # No more messages to send

                msg = messages[msg_index]
                app.send_message(bot_username, msg)
                print(f"Sent to {bot_username}: {msg}")
                message_count += 1

                if message_count % 80 == 0:
                    print("Pausing for 40 seconds...")
                    time.sleep(40)

                time.sleep(1)

            except Exception as e:
                print(f"Error sending to {bot_username}: {e}")
