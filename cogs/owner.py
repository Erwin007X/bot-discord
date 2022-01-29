from discord.ext import commands


class owner_cmd(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('owner_commands Cog has been loaded\n---------------------------')




def setup(client):
    client.add_cog(owner_cmd(client))