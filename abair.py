from discord.ext import commands 
from discord import Intents, File
import os
import io
from request_abair import get_pronounciation
from constants import map_dialect
intents = Intents(messages=True, guilds=True)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='abair')
async def say(ctx, *args):

	dialect = args[0]
	if map_dialect(dialect.upper()) == None:
		await ctx.send("Roghnaigh canúint led thoil. Tá trí rogha agat. GM (Gaolainn na Mumhan, Corca Dhuibhne), GU (Gaeilig Uladh, Gaoth Dobhair) agus GC (Gaeilge Chonnacht, Conamara)")
		
	if len(phrase) > 2000:
		await ctx.send("uasmhéid 2000 caractar")
	
	phrase = ""
	for word in args[1:]:
		phrase += word + " "
	
	phrase = phrase[:-1]
	ipa_text, sound = get_pronounciation(phrase, map_dialect(dialect))
	await ctx.send(phrase + "\n" + ipa_text, file=File(io.BytesIO(sound), filename="abair.mp3"))
	
bot.run(os.getenv("BOT_TOKEN"))