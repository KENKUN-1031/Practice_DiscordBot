# coding: utf-8
# インストールした discord.py を読み込む
import discord
from discord.ext import commands


# 接続に必要なオブジェクトを生成
# client = discord.Client()

client = commands.Bot(command_prefix="!")

@client.command
async def play(ctx, url : str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voiceChannel.connect()


# Botの起動とDiscordサーバーへの接続
client.run('ODkzNzM1NDMyNzYyODM5MDkw.YVfx-w.Z5zrur3XWPRKlPL7LtpsZ01FW-s')









# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('BOTの準備が整いました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

