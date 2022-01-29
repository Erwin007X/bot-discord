import discord
import requests
import platform
import json
import datetime
from discord.ext import commands


def GET_BTC_PRICE():
    data = requests.get('https://bx.in.th/api/')
    BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    return BTC_PRICE

API_URL = 'https://api.bitkub.com'

endpoint = {
    'status':'/api/status',
    'timestamp':'/api/servertime',
    'symbols':'/api/market/symbols',
    'ticker':'/api/market/ticker',
    'trades':'/api/market/trades'

}

def GET_BTC_PRICE_02(COIN = 'THB_BTC'):
    url = API_URL + endpoint['ticker']
    r = requests.get(url,params = {'sym':COIN})
    data = r.json()
    PRICE_BTC = data[COIN]['last']
    return PRICE_BTC
    
class public_cmd(commands.Cog):

        def __init__(self,client):
            self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print('public_commands Cog has been loaded\n---------------------------')
    

        @commands.command()
        async def ping(self,ctx):
          await ctx.send(f'Pong! In {round(self.client.latency * 1000)}ms')

          
        @commands.command(aliases=['av','pfp'])
        async def avatar(self,ctx,member: discord.Member):
                embed = discord.Embed(
                        title = (f"{member}'s Avatar!"),
                        color = 0x2ecc71
                )
                embed.set_image(url=member.avatar_url)
                await ctx.send(embed=embed)

        @commands.command(aliases=['info'])
        async def userinfo(self,ctx):
                user = ctx.author

                embed = discord.Embed(title = 'UERS INFO', description=f'Here is the info we retrieved about {user}',color = 0x2ecc71)
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name='NAME',value=user.name,inline=True)
                embed.add_field(name='NICKNAME',value=user.nick,inline=True)
                embed.add_field(name='ID',value=user.id,inline=True)
                embed.add_field(name='STATUS',value=user.status,inline=True)
                embed.add_field(name='TOP ROLE',value=user.top_role.name,inline=True)
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

        @commands.command()
        async def cat(self,ctx):
                response = requests.get('https://some-random-api.ml/img/cat')
                json_data = json.loads(response.text) 
                embed = discord.Embed(color = 0xff9900, title = 'Random Cat') 
                embed.set_image(url = json_data['link']) 
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed = embed) 

        @commands.command()
        async def dog(self,ctx):
                response = requests.get('https://some-random-api.ml/img/dog')
                json_data = json.loads(response.text) 
                embed = discord.Embed(color = 0x1A00FF, title = 'Random Dog') 
                embed.set_image(url = json_data['link'])
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed = embed) 
                

        @commands.command()
        async def fox(self,ctx):
                response = requests.get('https://some-random-api.ml/img/fox')
                json_data = json.loads(response.text) 
                embed = discord.Embed(color = 0x00FFFF, title = 'Random Fox')
                embed.set_image(url = json_data['link']) 
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed = embed) 

        @commands.command()
        async def stats(self,ctx):
                pythonversion = platform.python_version()
                dpyversion = discord.__version__
                servercount = len(self.client.guilds)
                membercount = len(set(self.client.get_all_members()))
                embed = discord.Embed(title=f'{self.client.user.name} Stats',description='\uFEFF',color= 0x2ecc71,timestamp = ctx.message.created_at)
                embed.add_field(name='Bot Version:', value='0.0.1')
                embed.add_field(name='Python Version:',value=pythonversion)
                embed.add_field(name='Discord.Py Version',value=dpyversion)
                embed.add_field(name='Total Guild',value=servercount)
                embed.add_field(name='Total User',value=membercount)
                embed.add_field(name='Bot Devlopers',value='<@798823644616458270>')
                embed.set_footer(text=f'หรอยแรง | {self.client.user.name}')
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')        
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed = embed)

                
        @commands.command()
        async def btc(self,ctx):

            msg = (f'ราคา Bitcoin ขณะนี้: {GET_BTC_PRICE_02()} บาท')
            EMBED = discord.Embed(title='Bitcoin price from bitkub',description=msg,color=0x42ff21)
            EMBED.set_thumbnail(url='https://i.pinimg.com/originals/59/50/f0/5950f0a238dae9016bcbc853feb9726d.gif')

            await ctx.channel.send(embed = EMBED)

def setup(client):
    client.add_cog(public_cmd(client))