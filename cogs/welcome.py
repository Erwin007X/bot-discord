import discord
import datetime
from discord.ext import commands

class welcum_cmd(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('welcome_commands Cog has been loaded\n---------------------------')
    

    @commands.Cog.listener()
    async def on_member_join(self,member):

        embed = discord.Embed(
            title = f'Welcome {member.name}',
            description = f"Hi! {member.mention}\n\nWelcome to server **Erwin's server**",
            color = 0x2ecc71
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        auto_role = member.guild.get_role(923923525176295454)
        await member.add_roles(auto_role)
        await self.client.get_channel(923916841355714601).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self,member):

        embed = discord.Embed(
            title = f'Leave {member.name}',
            description = f"Bye! {member.name} Just left server",
            color = 0x2ecc71
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await self.client.get_channel(923916943931617291).send(embed=embed)




def setup(client):
    client.add_cog(welcum_cmd(client))