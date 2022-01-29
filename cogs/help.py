import discord
import datetime
from discord.ext import commands

class help_cmd(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('help_commands Cog has been loaded\n---------------------------')



    @commands.command()
    async def help(self,ctx):
                embed = discord.Embed(title="help bot commands",description="คำสั่งทั้งหมดของบอท",color=0x66ccff)
                embed.add_field(name=";music",value="คำสั่งเพลงทั้งหมด",inline=False) 
                embed.add_field(name=";cat",value="สุ่มภาพแมว",inline=False)
                embed.add_field(name=";dog",value="สุ่มภาพหมา",inline=False)
                embed.add_field(name=";fox",value="สุ่มภาพจิ้งจอก",inline=False)
                embed.add_field(name=";clear",value="ล้างข้อความ(administrator)",inline=False)
                embed.add_field(name=";kick",value="เตะสมาชิก(administrator)",inline=False)
                embed.add_field(name=";ban",value="แบนสมาชิก(administrator)",inline=False)
                embed.add_field(name=";unban",value="ยกเลิกการแบนสมาชิกที่โดนแบน(administrator)",inline=False)
                embed.add_field(name=";mute",value="ปิดเสียงสมาชิก(administrator)",inline=False)
                embed.add_field(name=";unmute",value="ยกเลิกการปิดเสียงสามาชิกที่โดนปิดเสียง(administrator)",inline=False)
                embed.set_thumbnail(url='https://media.discordapp.net/attachments/906560486596825121/923920013935648808/external-content.duckduckgo.jpg')
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

    @commands.command()
    async def music(self,ctx):
                embed = discord.Embed(title="help bot music",description="คำสั่งเพลงทั้งหมดของบอท",color=0x66ccff)
                embed.add_field(name=";play",value="เล่นเพลงวิธีใช้งาน ;play ลิ้งเพลงหรือชื่อเพลงที่ต้องการ",inline=False)
                embed.add_field(name=";join",value="เรียกบอทเข้าช่องเสียงที่คุณอยู่",inline=False)
                embed.add_field(name=";leave",value="คำสั่งให้บอทออกจากช่องเสียง",inline=False)
                embed.add_field(name=";pause",value="หยุดเพลงชั่วคราว",inline=False)
                embed.add_field(name=";resume",value="เล่นเพลงต่อ",inline=False)
                embed.add_field(name=";stop",value="หยุดเพลงถาวร",inline=False)
                embed.add_field(name=";skip",value="ข้ามเพลง",inline=False)    
                embed.add_field(name=";qlist",value="เช็คคิวเพลง",inline=False)
                embed.add_field(name=";loop",value="วนซ้ำ",inline=False)  
                embed.add_field(name=";nowplaying",value="เช็คเพลงที่กำลังเล่น",inline=False)                                            
                embed.set_thumbnail(url='https://media.discordapp.net/attachments/906560486596825121/923920013935648808/external-content.duckduckgo.jpg')
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Command Run by {ctx.author.name}')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)        


def setup(client):
    client.add_cog(help_cmd(client))