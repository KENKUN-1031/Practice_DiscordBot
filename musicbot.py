import discord
from discord.ext import commands
import youtube_dl
import os
from pydub import AudioSegment

client = commands.Bot(command_prefix="!")

@client.command()
async def play(ctx, url : str):
    print(ctx)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("wait for the current playing music to end or use 'stop' comand")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)


    ydl_opts ={
        'format' : 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        print("^^^^^^^^^^^^")
        print(file)
        if file.endswith(".mp3"):
            print("--------------")
            os.rename(file, "song.mp3")
            print("¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥")
            break
    #sleep を入れてちゃんとファイルが作れてるのを確認する
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    # discord.FFmpegPCMAudio("song.mp3")

    # voice.play(discord.AudioSegment.from_mp3('song.mp3'))
    print("sssssssssssssssssss")



@client.command()
async def leave(ctx):
    print("/////////////")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    print(voice)
    if voice == None:
        print("^^^^^^^^^^^^^^^^^")
        await voice.disconnect()
    else:
        print("1111111111111111111111")
        await ctx.send("The bot is not connected to a voice channel")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("no audio played")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("no audio paused")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


client.run('#Discord-Token')
