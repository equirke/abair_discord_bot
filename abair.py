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
		await ctx.send("Roghnaigh canúint led thoil. Tá trí rogha agat. GM (Gaolainn na Mumhan, Corca Dhuibhne), GU (Gaeilig Uladh, Gaoth Dobhar) agus GC (Gaeilge Chonnacht, Conamara)")
	if len(phrase) > 2000:
		await ctx.send("uasmhéid 2000 caractar")
	ipa_text, sound = get_pronounciation(phrase, map_dialect(dialect))
	await ctx.send(phrase + "\n" + ipa_text, file=File(io.BytesIO(sound), filename="abair.mp3"))
	
bot.run(os.getenv("BOT_TOKEN"))