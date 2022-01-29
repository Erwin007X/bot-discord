import discord
import asyncio
import datetime
from discord.ext import commands

class admin_cmd(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('adimin_commands Cog has been loaded\n---------------------------')
    

    @commands.command(aliases=['c'])
    @commands.has_permissions(administrator=True)
    async def clear(self,ctx,amount=1):
        if amount > 100:
            embed = discord.Embed(
                title = 'ห้ามเกิน 100 ข้อความ',
                color =  0x2ecc71
            )
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed,delete_after=3)
        elif amount <= 100:
            await ctx.channel.purge(limit = amount+1)
            embed = discord.Embed(
                title = f'I deleted {amount} messages.',
                color =  0x2ecc71
            )
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
            embed.timestamp = datetime.datetime.utcnow()
            msg = await ctx.send(embed=embed,delete_after=3)
            await asyncio.sleep(2)
            await msg.delete()


    @commands.command(aliases=['k'])
    @commands.has_permissions(administrator=True)
    async def kick(self,ctx,member : discord.Member,*,reason = 'No reason provided'):
        embed = discord.Embed(
            title = (f'Kick {member}'),
            description = ('You have been kicked \nBecause : '+reason),
            color = 0x2ecc71
        )
        embed.set_thumbnail(url='https://c.tenor.com/esCHs7tm78UAAAAM/spongebob-squarepants-get-out.gif')
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')
        embed.timestamp = datetime.datetime.utcnow()
        await member.kick(reason=reason)
        await ctx.send(embed=embed)
        await member.send(embed=embed)



    @commands.command(aliases=['b'])
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx,member : discord.Member,*,reason = 'No reason provided'):
        embed = discord.Embed(
            title = (f'Ban {member}'),
            description = ('You have been Baned \nBecause : '+reason),
            color = 0x2ecc71
        )
        embed.set_thumbnail(url='https://c.tenor.com/SipkXgk-Kd8AAAAC/anime-mad.gif')
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')
        embed.timestamp = datetime.datetime.utcnow()
        await member.ban(reason=reason)    
        await ctx.send(embed=embed)  
        await member.send(embed=embed)


    @commands.command(aliases=['m'])
    @commands.has_permissions(administrator=True)
    async def mute(self,ctx,member:discord.Member,*,reason= 'No reason provided'):
        embed = discord.Embed(
            title = (f'Mute {member}'),
            description = ('You have been Mute \nBecause : '+reason),
            color = 0x2ecc71
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
        embed.timestamp = datetime.datetime.utcnow()
        mute_role = ctx.guild.get_role(919927662552694795)
        await member.add_roles(mute_role)
        await ctx.send(embed=embed)
        await member.send(embed=embed)


    @commands.command(aliases = ['um'])
    @commands.has_permissions(administrator=True)
    async def unmute(self,ctx,member: discord.Member):
        embed = discord.Embed(
            title = ('Success!'),
            description = (f'{member} has successfully been unmuted'),
            color = 0x2ecc71
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
        embed.timestamp = datetime.datetime.utcnow()
        ummute_role = ctx.guild.get_role(919927662552694795)
        await member.remove_roles(ummute_role)
        await ctx.send(embed=embed)
        await member.send(embed=embed)



    @commands.command(aliases=['ub'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):

            banned_members = await ctx.guild.bans()
            member_name, member_discord = member.split('#')

            for banned_entry in banned_members:
                user = banned_entry.user

                if (user.name, user.discriminator) == (member_name,member_discord):
                    await ctx.guild.unban(user)        
                    embed = discord.Embed(
                        title = ('Success!'),
                        description = (f'{user} has successfully been unbanned'),
                        color = 0x2ecc71
                    )
                    embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=embed)
                    await user.send(embed=embed)
                    return

def setup(client):
    client.add_cog(admin_cmd(client))