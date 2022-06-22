import nextcord
from nextcord.ext import commands
import config

bot = commands.Bot(command_prefix='!', intents=nextcord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {str(bot.user)}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass

bot.run(config.TOKEN)