import io

from discord import File
from discord.ext import commands

from .bruidhinn_utils.bruidhinn_request import get_pronunciation_text_and_voice, get_recommendations


class Bruidhinn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bruidhinn(self, ctx, *args):
        if len(args) > 1:
            await ctx.send("I must say something")
            return

        word = args[0]

        result = await get_pronunciation_text_and_voice(word)

        if result is None:
            recommendations = await get_recommendations(word)
            if recommendations is None:
                await ctx.send("I cannot find an entry")
                return
            all_recommendations = ""
            for recommendation in recommendations:
                all_recommendations += recommendation + "\n"
            await ctx.send(f"I could not find {word} but I did find:{all_recommendations}")
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