from discord.ext import commands 
from discord import Intents, File
import os
import io
from request_abair import get_pronounciation
from constants import map_dialect
intents = Intents(messages=True, guilds=True)

bot = commands.Bot(command_prefix='a!', intents=intents)

@bot.command(name='abair')
async def say(ctx, dialect, phrase):
	if map_dialect(dialect) == None:
		await ctx.send("Roghnaigh canúint led thoil. Tá trí rogha agat. CD (Corca Dhuibhne), GD (Gaoth Dobhar) agus CO (Conamara)")
	if len(phrase) > 2000:
		await ctx.send("uasmhéid 2000 caractar")
	text, sound = get_pronounciation(phrase, map_dialect(dialect))
	await ctx.send(text, file=File(io.BytesIO(sound), filename="abair.mp3"))
	
bot.run(os.getenv("BOT_TOKEN"))