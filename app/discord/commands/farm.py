from discord.ext import commands

class FarmCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def harvest(self, ctx):
        item = ctx.message.content.split()[1::]
        await ctx.send(f'You have harvested {item}!')
    
    @commands.command()
    async def plant(self, ctx):
        item = ctx.message.content.split()[1::]
        await ctx.send(f'You have planted {item}!')

    @commands.command()
    async def water(self, ctx):
        item = ctx.message.content.split()[1::]
        await ctx.send(f'You have watered {item}!')
