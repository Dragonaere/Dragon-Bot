import os
import discord
from pretty_help import PrettyHelp, Navigation
from discord.ext import commands

from commands.random_commands import Random
from commands.music_commands import Music

orange = discord.Color.orange()

bot = commands.Bot(':', description='Official Dragonaere Discord Bot')
nav = Navigation()
bot.help_command = PrettyHelp(navigation=nav, color=orange, active_time=5)
bot.add_cog(Music(bot))
bot.add_cog(Random(bot))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="play.dragonaere.tk | :help"))
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

bot.run(os.getenv("TOKEN"))
