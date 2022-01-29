from discord.ext import commands
from utils.gif import punch_gifs,punch_names,slap_gifs,slap_names,hug_gifs,hug_names,kick_gifs,kick_names,sad_gifs
import discord
import random

class fun_cmd(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('funcommand Cog has been loaded\n---------------------------')



    @commands.command()
    async def punch(self,ctx,member : discord.Member):
      embed = discord.Embed(
              color = ctx.author.color,
              description = f'{ctx.author.mention} {(random.choice(punch_names))} {member.mention}'
              )
      embed.set_image(url=(random.choice(punch_gifs)))
      await ctx.send(embed=embed)



    @commands.command()
    async def slap(self,ctx,member : discord.Member):
      embed = discord.Embed(
        color = ctx.author.color,
        description = f'{ctx.author.mention} {(random.choice(slap_names))} {member.mention}'
      )
      embed.set_image(url=(random.choice(slap_gifs)))
      await ctx.send(embed=embed)


    @commands.command()
    async def hug(self,ctx,member : discord.Member = None):
      if member is not None:
        embed = discord.Embed(
          color = ctx.author.color,
          description = f'{ctx.author.mention} {(random.choice(hug_names))} {member.mention}'
        )
        embed.set_image(url=(random.choice(hug_gifs)))
      else:
        embed = discord.Embed(
            color = ctx.author.color,
            description = f'{ctx.author.mention} ลำโพงมันดัง ลำพังมันเหงา ข้างเธอมีเขา ข้างเราไม่มีใคร'
        )
        embed.set_image(url=(random.choice(sad_gifs)))
      await ctx.send(embed=embed)



    @commands.command()
    async def kic(self,ctx,member : discord.Member):
      embed = discord.Embed(
        color = ctx.author.color,
        description = f'{ctx.author.mention} {(random.choice(kick_names))} {member.mention}'
      )
      embed.set_image(url=(random.choice(kick_gifs)))
      await ctx.send(embed=embed)


    @commands.command()
    async def gay(self,ctx,member : discord.Member):
      a = random.randint(1,100)
      embed = discord.Embed(
        color = ctx.author.color,
        description = f'{member.mention}you are gay {a}% By{ctx.author.mention}'
      )
      await ctx.send(embed=embed)

    
    @commands.command()
    async def ask(self,ctx):
      ms = ['Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No']
      embed = discord.Embed(
        color = ctx.author.color,
        description = f'{random.choice(ms)}'
      )
      await ctx.send(embed=embed)
      

      
def setup(client):
    client.add_cog(fun_cmd(client))