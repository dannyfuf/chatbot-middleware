from discord.ext import commands

class RenderingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def render(self, ctx):
        await ctx.send(f'this is your farm!')