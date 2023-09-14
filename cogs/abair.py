import io
import datetime

from discord import File
from discord.ext import commands

from .abair_utils.abair_request import get_pronunciation


class Abair(commands.Cog):
    """This Cog allows enables a discord bot to transcribe Irish text
     providing an IPA transcription as well as TTS voice recording."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def abair(self, ctx):
        await ctx.send(
            """Roghnaigh canúint led thoil. \
Tá trí rogha agat. gm (Gaolainn na Mumhan, Corca Dhuibhne), \
gu (Gaeilig Uladh, Gaoth Dobhair) agus gc (Gaeilge Chonnacht, Conamara)\n\
Formáid !abair <Canúint> <abairt>.""")
        return

    async def say(self, ctx, dialect, *args):
        if len(args) < 1:
            await ctx.send("Caithfidh mé rud éigin a rá.")
            return

        phrase = ""
        for word in args:
            phrase += word + " "

            if len(phrase) > 2000:
                await ctx.send("Uasmhéid 2000 caractar")
                return

        phrase = phrase[:-1]

        ipa_text, sound = await get_pronunciation(phrase, dialect)

        if sound is None:
            await ctx.send(phrase + "\n" + ipa_text)
            return

        filename = "abair_" + datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S%f") + ".mp3"

        if ipa_text is None:
            await ctx.send("", file=File(io.BytesIO(sound), filename=filename))
            return

        await ctx.send(phrase + "\n" + ipa_text, file=File(io.BytesIO(sound), filename=filename))
        return

    @abair.command(name='gm', aliases=['GM', 'Gaolainn', 'Gaelainn'])
    async def connacht(self, ctx, *args):
        await self.say(ctx, 'ga_MU', *args)
        return

    @abair.command(name='gc', aliases=['GC', 'Gaeilge'])
    async def munster(self, ctx, *args):
        await self.say(ctx, 'ga_CO', *args)
        return

    @abair.command(name='gu', aliases=['GU', 'Gaeilic', 'Gaeilig'])
    async def ulster(self, ctx, *args):
        await self.say(ctx, 'ga_UL', *args)
        return


def setup(bot):
    bot.add_cog(Abair(bot))
