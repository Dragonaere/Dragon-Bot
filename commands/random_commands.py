import discord
from discord.ext import commands

class Random(commands.Cog):
  @commands.command(name='ping', invoke_without_subcommand=True)
  async def _ping(self, ctx):
    """Test Command"""
    await ctx.send("pong!")

  @commands.command(name='pornpls', invoke_without_subcommand=True)
  async def _pornpls(self, ctx):
    """Horny Boy"""
    await ctx.send("Go to horny jail!")
    await ctx.send(file=discord.File('bonk.jpg'))
