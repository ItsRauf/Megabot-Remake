import discord
from discord.ext import commands


class Custodians(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client


def setup(client: commands.Bot):
    client.add_cog(Custodians(client))