from discord.ext import commands
from rich.console import Console
import os

client = commands.Bot(command_prefix="*", description=":0")
console = Console()


@client.event
async def on_ready():
    console.print(f"Logged in as {client.user.name}", style="bold green")


@client.command()
async def start(ctx):
    await ctx.send("Hello, I'm a bot!")

print(os.getenv("TOKEN"))

client.run(os.getenv("TOKEN"), bot=True)
