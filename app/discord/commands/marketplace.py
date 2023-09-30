from discord.ext import commands

class MarketplaceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def buy(self, ctx):
        item = ctx.message.content.split()[1::]
        await ctx.send(f'You have bought {item}!')
    
    @commands.command()
    async def sell(self, ctx):
        item = ctx.message.content.split()[1::]
        await ctx.send(f'You have sold {item}!')