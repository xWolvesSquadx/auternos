import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'start':
            await message.channel.send('Server is starting ✅')
            os.system("python auternos.py 1")

client = MyClient()
client.run(OTQ0NjA0MDQ0MzMxMTg4MjI0.YhEBEg.iqm-VN1y7DjYFxzh_unK1y7s4rs)
