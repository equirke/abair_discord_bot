import io

from discord import File
from discord.ext import commands

from .bruidhinn_utils.bruidhinn_request import get_pronunciation_text_and_voice, get_recommendations


class Bruidhinn(commands.Cog):
    """This Cog allows enables a discord bot to transcribe individual Scots Gàidhlig words
     providing an IPA transcription as well as a voice recording"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bruidhinn(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Feumaidh mi nì-eigin a bhruidhinn.")
            return

        if len(args) > 1:
            await ctx.send("Chan urrainn dhomh ach aon fhocal a lorg anns an àm cheudna.")
            return

        word = args[0]

        result = await get_pronunciation_text_and_voice(word)

        if result is None:
            recommendations = await get_recommendations(word)
            if recommendations is None:
                await ctx.send("Cha do lorg mi am focal sin")
                return
            await ctx.send(f"Cha do lorg mi am focal \"{word}\" ach lorg mi:\n{recommendations}.")
            return

        (ipa_text, sound) = result

        if sound is None:
            await ctx.send(word + "\n" + ipa_text)
            return

        if ipa_text is None:
            await ctx.send("", file=File(io.BytesIO(sound), filename="bruidhinn.mp3"))
            return


        await ctx.send(word + "\n" + ipa_text, file=File(io.BytesIO(sound), filename="bruidhinn.mp3"))
        return


def setup(bot):
    bot.add_cog(Bruidhinn(bot))