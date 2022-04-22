import requests
import discord
import json

with open("config.json", "r") as read_file:
  readConfig = json.load(read_file)

class SwiperBot(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.lower() == "yoink" and message.reference is not None:
      msg = await message.channel.fetch_message(message.reference.message_id)
      if msg.attachments:
        channel = await message.author.create_dm()
        for attachment in msg.attachments:
          await channel.send("```\n" + attachment.url + "\n```")

client = SwiperBot()
client.run(readConfig["token"])
