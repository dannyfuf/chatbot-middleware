from scanf import scanf
from discord.ext import commands

# custom modules
from discord.command_parser import command_parser

class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def signup(self, ctx):
        user = ctx.message.author.name
        password = command_parser(ctx.message.content)
        await ctx.send(f'Hey `{user}`!, you have been signed up with password: {password}')
    
    @commands.command()
    async def login(self, ctx):
        user = ctx.message.author.name
        password = command_parser(ctx.message.content)
        await ctx.send(f'Hey `{user}`!, you have been logged in with password: {password}')

    @commands.command()
    async def access(self, ctx):
        print("add access")
        user = ctx.message.author.name
        access, = command_parser(ctx.message.content)
        await ctx.send(f'Hey `{user}`!, you now have acess to: {access}')
