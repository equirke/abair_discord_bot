from discord.ext import commands 
from discord import Intents, File
import os
import io
from request_abair import get_pronounciation
intents = Intents(messages=True, guilds=True)

bot = commands.Bot(command_prefix='a!', intents=intents)

@bot.command(name='abair')
async def say(ctx, dialect, phrase):
	if len(phrase) > 2000:
		await ctx.send("uasmhéid 2000 caractar")
	text, sound = get_pronounciation(phrase)
	await ctx.send(text, file=File(io.BytesIO(sound), filename="abair.mp3"))
	
bot.run(os.getenv("BOT_TOKEN"))