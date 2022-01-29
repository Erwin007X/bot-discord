import discord
import asyncio
from discord.ext import commands
import urllib.parse
import re
from discord.player import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError, ExtractorError
import validators
import urllib.request
from utils.embed_function import success_embed , error_embed
from utils.emoji import Emoji
from utils.color import Color
from utils.youtubedl_stuff import FFMPEG_OPTIONS,YDL_OPTIONS

import json

def load():
    with open("database/prefix.json", "r") as file:
        return json.load(file)

data = load()

class music_cum(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.music_title = []
        self.music_url = []
        self.music_thumbnail = []
        self.queue = []
        self.repeat = 'none'

    @commands.Cog.listener()
    async def on_ready(self):
        print('music_cum Cog has been loaded\n---------------------------')
        
      
    def player(self,ctx, voice):
      global music_title # Those we defined earlier on YoutubeDL 
      global music_thumbnail # Those we defined earlier on YoutubeDL 
      global music_url # Those we defined earlier on YoutubeDL 
      global client_activity # Those we defined earlier on YoutubeDL 

      
  # 📲 EXTRACTING THE INFORMATIONS 📲

      with YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(self.queue[0], download=False)
      URL = info['formats'][0]['url']
      client_activity = info.get('title', None)
      music_url = self.queue[0]
      music_title = info.get('title', None)
      music_thumbnail = info.get('thumbnail')

      voice.play(FFmpegPCMAudio(
          URL, executable="ffmpeg", **FFMPEG_OPTIONS), after=lambda e: self.play_queue(ctx, voice))
      voice.is_playing()

    def play_queue(self,ctx, voice):
        global repeat
        try:
            if self.repeat == 'yes':
                self.player(ctx, voice)
            elif len(self.queue) >= 1:
                del self.queue[0]
                self.player(ctx, voice)
        except IndexError:
            print(f'Queue finished')

    @commands.command(name='play', aliases=['p','ply','yt','P','PLAY'])
    async def play(self,ctx, *, url: str):
        channel = ctx.message.author.voice.channel
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice is None:
                await channel.connect()
                await ctx.guild.change_voice_state(channel=channel,self_mute = False,self_deaf=True)
                voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        y_link = 'https://www.youtube.com/results?search_query='
        query_string = urllib.parse.urlencode({'search_query': url})
        htm_content = urllib.request.urlopen(y_link + query_string)
        y_link + url.replace(' ', '+')
        search_results = re.findall(
            r"watch\?v=(\S{11})", htm_content.read().decode())
        top_result = 'http://www.youtube.com/watch?v=' + search_results[0]

        valid_url = validators.url(url)
        try:
            if not voice.is_playing():
                if valid_url == True:
                    try:
                        self.queue.append(url)
                        music_url = url
                        await ctx.send(f'**{Emoji.main} กำลังค้นหา {Emoji.search}**'+f'`{url}`')
                        self.player(ctx, voice)
                        embed=discord.Embed(title=music_title, url=music_url, description=f'> กำลังเล่นเพลง {music_title}', color = Color.main)
                        embed.set_footer(text=f'คำสั่งนี้ใช้โดย {ctx.message.author}')
                        embed.set_image(url=music_thumbnail)
                        await ctx.send(embed=embed)
                    except ExtractorError:
                        await error_embed(ctx, 'ลิงก์ ไม่ถูกต้อง')
                    except DownloadError:
                        await error_embed(ctx, 'ลิงก์ ไม่ถูกต้อง')
                else:
                    self.queue.append(top_result)
                    music_url = top_result
                    await ctx.send(f'**{Emoji.music} กำลังค้นหา {Emoji.search}**'+f'`{url}`')
                    self.player(ctx, voice)
                    embed=discord.Embed(title=music_title, url=music_url, description=f'> กำลังเล่นเพลง {music_title}', color = Color.main)
                    embed.set_footer(text=f'คำสั่งนี้ใช้โดย {ctx.message.author}')
                    embed.set_image(url=music_thumbnail)
                    await ctx.send(embed=embed)
            else:
                if valid_url == True:
                    self.queue.append(url)
                    await success_embed(ctx, f'{Emoji.main} เพิ่มในคิวเพลงแล้ว!')
                else:
                    self.queue.append(top_result)
                    await success_embed(ctx, f'{Emoji.main} เพิ่มในคิวเพลงแล้ว!')
        except AttributeError:
            await ctx.send('คุณไม่ได้อยู่ในช่องเสียง,คุณต้องอยู่ในช่องเสียงเพื่อเรียกใช้คำสั่งนี้!')



    @commands.command(name='join', aliases=['j'])
    async def join(self,ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if not ctx.message.author.voice:
              await error_embed(ctx, f'{ctx.author.name} คุณไม่ได้อยู่ในช่องเสียง')

        else:
            if voice is None:
                channel = ctx.message.author.voice.channel
                await channel.connect()
                await ctx.guild.change_voice_state(channel=channel, self_mute=False, self_deaf=True)
                await ctx.send(f'**{Emoji.ok} เข้าช่องเสียง <#{channel.id}>**')
            else:
                await error_embed(ctx , f'{self.client.user.name} คุณไม่ได้อยู่ในช่องเสียง,คุณต้องอยู่ในช่องเสียงเพื่อเรียกใช้คำสั่งนี้!')



    @commands.command(name='nowplaying', aliases=['np'])
    async def now(self,ctx):
        global music_title
        global music_url
        global music_thumbnail
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice:
            if voice.is_playing():
                        embed=discord.Embed(title=music_title, url=music_url, description=f'> กำลังเล่นเพลง {music_title}', color = Color.main)
                        embed.set_footer(text=f'คำสั่งนี้ใช้โดย {ctx.message.author}')
                        embed.set_thumbnail(url=music_thumbnail)
                        await ctx.send(embed=embed)
            else:
                await error_embed(ctx , f'{ctx.author.name} ไม่พบว่ามีเพลงกำลังเล่นอยู่!')
        else:
            await error_embed(ctx, f'{self.client.user.name} คุณไม่ได้อยู่ในช่องเสียง,คุณต้องอยู่ในช่องเสียงเพื่อเรียกใช้คำสั่งนี้!')


    @commands.command(name='queue', aliases=['q','list','qlist'])
    async def queue_display(self,ctx):
        global queue_list
        if len(self.queue) == 0:
            await error_embed(ctx, f'{ctx.author.name} คิวเพลงว่างเปล่า!')
        else:
            i = 0
            for x in self.queue:
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info=ydl.extract_info(x, download=False)
                i = i + 1
                title = str(info.get('title'))
                self.queue_list = f'```\n{i}. {title}\n```'
                await ctx.send(embed = discord.Embed(title =f"{Emoji.music} รายการคิวเพลง" ,description = self.queue_list, color = Color.main))



    @commands.command(name='skip', aliases=['s','sk'])
    async def skip(self,ctx):
        global music_title
        global music_url
        global music_thumbnail
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            try:
                if self.repeat == 'yes':
                    await success_embed(ctx, f'{ctx.author.name} ได้ข้ามเพลง {music_title}')
                    voice.pause()
                    del self.queue[0]
                    self.play_queue(ctx, voice)
                    embed=discord.Embed(title=music_title, url=music_url, description=f'> กำลังเล่นเพลง {music_title}', color = Color.main)
                    embed.set_footer(text=f'คำสั่งนี้ใช้โดย {ctx.message.author}')
                    embed.set_image(url=music_thumbnail)
                    await ctx.send(embed=embed)
                elif self.repeat == 'none':
                    await success_embed(ctx, f'{ctx.author.name} ได้ข้ามเพลง {music_title}')
                    voice.pause()
                    # del queue[0]
                    self.play_queue(ctx, voice)
                    embed=discord.Embed(title=music_title, url=music_url, description=f'> กำลังเล่นเพลง {music_title}', color = Color.main)
                    embed.set_footer(text=f'คำสั่งนี้ใช้โดย {ctx.message.author}')
                    embed.set_image(url=music_thumbnail)
                    await ctx.send(embed=embed)
            except IndexError:
                await error_embed(ctx, f'{ctx.author.name} ไม่มีเพลงอยู่ในคิว!')
        else:
            await error_embed(ctx, f'{ctx.author.name} ไม่พบว่ามีเพลงกำลังเล่นอยู่!')

    @commands.command(name='loop', aliases=['repeat'])
    async def loop(self,ctx):
        global repeat
        global music_title
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            if self.repeat == 'none':
                self.repeat = 'yes'
                await success_embed(ctx, f'{ctx.author.name} เพลง {music_title} วนซ้ำ ```เปิด```')
            elif self.repeat == 'yes':
                self.repeat = 'none'
                await error_embed(ctx, f'{ctx.author.name}  เพลง {music_title} วนซ้ำ ```ปิด```')
        else:
            await error_embed(ctx, f'{ctx.author.name} ไม่พบว่ามีเพลงกำลังเล่นอยู่!')


    @commands.command(name='pause', aliases=['ps'])
    async def pause(self,ctx):
        global music_title
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await success_embed(ctx, f'{ctx.author.name} เพลงหยุดชั่วคราว {music_title}')
        else:
            await error_embed(ctx, f'{ctx.author.name} ไม่พบว่ามีเพลงกำลังเล่นอยู่!')



    @commands.command(name='resume', aliases=['r'])
    async def resume(self,ctx):
        global music_title
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            
            await success_embed(ctx, f'{ctx.author.name} เล่นเพลงต่อ {music_title}')
        else:
            await success_embed(ctx, f'{ctx.author.name} เพลงไม่ได้ถูกใช้คำสั่ง '+data["prefix"]+'pause จึงไม่สามารถ ใช้คำสั่ง '+data["prefix"]+'resume เพื่อเล่นเพลงต่อได้!! ._.')


    @commands.command(name='stop', aliases=['st'])
    async def stop(self,ctx):
        global queue
        global queue_list
        global music_title
        global client_activity
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        self.queue.clear()
        self.queue_list = ''
        voice.stop()
        client_activity = 'Musicord'
        await success_embed(ctx, f'{ctx.author.name} หยุดเพลงถาวร {music_title}')


    @commands.command(name='leave', aliases=['disconnect','discon','lev'])
    async def leave(self,ctx):
        global queue
        global queue_list
        global client_activity
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            self.queue.clear()
            self.queue_list = ''
            client_activity = 'Musicord'
            await voice.disconnect()
            await success_embed(ctx, f'{self.client.user.name} ออกช่องเสียง!')
        else:
            await error_embed(ctx, f'{self.client.user.name} คุณไม่ได้อยู่ในช่องเสียง,คุณต้องอยู่ในช่องเสียงเพื่อเรียกใช้คำสั่งนี้!')


def setup(client):
    client.add_cog(music_cum(client))