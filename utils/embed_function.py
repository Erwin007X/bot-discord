from utils.emoji import Emoji
from utils.color import Color
import discord

            # Error embed function #
async def error_embed(ctx, msg):
      embed = discord.Embed(description = f'**{Emoji.error} | {msg}**', color = Color.error)
      await ctx.send(embed=embed)


            # Success embed function #
async def success_embed(ctx, msg):
      embed = discord.Embed(description = f'**{Emoji.success} | {msg}**', color = Color.success)
      await ctx.send(embed=embed)


      