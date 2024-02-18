from discord.ext import commands 
from discord import Intents
import os

intents = Intents(messages=True, guilds=True)

bot = commands.Bot(command_prefix='!', intents=intents)

bot.load_extension('cogs.abair')
bot.load_extension('cogs.bruidhinn')
bot.remove_command("help")
bot.run(os.getenv("BOT_TOKEN"))
