from deepl import translator
import discord
import deepl
from papago import Translator
from discord.ext import commands
import requests
import random
import json
import hashlib
from hashlib import md5
####################################↓[KEY関連]↓#####################################
#Discord
TOKEN = "hogehoge0"

#Deepl
Deepl = "hogehoge1"

#Papago
PapagoID = "hogehogeID1"
PapagoKey = "hogehogeKey1"
url = "https://openapi.naver.com/v1/papago/n2mt"
header = {"X-Naver-Client-Id":PapagoID,"X-Naver-Client-Secret":PapagoKey}

#Baidu
appid = "hogehogeID2" 
secretKey = "hogehogeKey2"
###################################################################################
bot = commands.Bot(command_prefix = "!")

######################################################################
@bot.command()
#help
async def helps(ctx):
    embed = discord.Embed(title="Language support:speaking_head:",color=0x00ff00,description="[Deepl] \n !※1 [Sentence] \n ※1 Please enter the language want to translate.\n [Papago] \n !※2 [Sentence] \n※2 Enter the language want to translate and original language \n[Baidu] \n !※3 [Sentence] \n ※3 Please enter the language want to translate.\n\n Ver:2.1 LastUpdate:2022/1/16")
    embed.add_field(name="Deepl",value=":flag_jp:=jp \n :flag_cn:=ch \n \n :flag_us:=en \n :flag_es:=es \n :flag_it:=it \n :flag_de:=de \n :flag_ru:=ru \n :flag_fr:=fr",inline=True)
    embed.add_field(name="Papago",value=":flag_jp:=j \n :flag_cn:=c \n :flag_kr:=k \n :flag_us:=e",inline=True)
    embed.add_field(name="Baidu",value=":flag_jp:=jpb \n :flag_cn:=chb \n :flag_kr:=krb \n :flag_us:=enb \n :flag_es:=esb \n \n \n \n \n :flag_th:=thb \n :flag_se:=swb",inline=True)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    message = await ctx.send(embed=embed)
    await message.add_reaction("🇯🇵")
    await message.add_reaction("🇰🇷")
    await message.add_reaction("🇨🇳")
    await message.add_reaction("🇺🇸")
    await message.add_reaction("🇮🇹")
    await message.add_reaction("🇪🇸")
    await message.add_reaction("🇩🇪")
    await message.add_reaction("🇫🇷")
    await message.add_reaction("🇷🇺")
    await message.add_reaction("🇸🇪")
    await message.add_reaction("🇹🇭")

######################################################################
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('!helps'))
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓[Deepl API]↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#
@bot.command()
#英語
async def en(ctx, *,msg):
    translator = deepl.Translator(Deepl) 
    result = translator.translate_text(msg,target_lang="EN-US") 
    translated_text = result.text
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/97/e4/99/97e49907-7fdf-57c9-ee01-3b20d055a875/source/512x512bb.jpg")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"English:flag_um: ", value=result.text,inline=False)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#日本語
async def jp(ctx, *,msg):
    translator = deepl.Translator(Deepl) 
    result = translator.translate_text(msg,target_lang="JA") 
    translated_text = result.text
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/97/e4/99/97e49907-7fdf-57c9-ee01-3b20d055a875/source/512x512bb.jpg")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"日本語:flag_jp: ", value=result.text,inline=False)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#スペイン語
async def es(ctx, *,msg):
    translator = deepl.Translator(Deepl) 
    result = translator.translate_text(msg,target_lang="ES") 
    translated_text = result.text
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/97/e4/99/97e49907-7fdf-57c9-ee01-3b20d055a875/source/512x512bb.jpg")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"Español:flag_es: ", value=result.text,inline=False)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#中国語
async def ch(ctx, *,msg):
    translator = deepl.Translator(Deepl) 
    result = translator.translate_text(msg,target_lang="ZH") 
    translated_text = result.text
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/97/e4/99/97e49907-7fdf-57c9-ee01-3b20d055a875/source/512x512bb.jpg")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"汉语:flag_cn: ", value=result.text,inline=False)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#イタリア語
async def it(ctx, *,msg):
    translator = deepl.Translator(Deepl) 
    result = translator.translate_text(msg,target_lang="IT") 
    translated_text = result.text
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/97/e4/99/97e49907-7fdf-57c9-ee01-3b20d055a875/source/512x512bb.jpg")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"italiano:flag_it: ", value=result.text,inline=False)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#ドイツ語
async def de(ctx, *,msg):
    translator = deepl.Translator(Deepl) 
    result = translator.translate_text(msg,target_lang="DE") 
    translated_text = result.text
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/97/e4/99/97e49907-7fdf-57c9-ee01-3b20d055a875/source/512x512bb.jpg")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"Deutsch:flag_de: ", value=result.text,inline=False)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#ロシア語
async def ru(ctx, *,msg):
    translator = deepl.Translator(Deepl) 
    result = translator.translate_text(msg,target_lang="RU") 
    translated_text = result.text
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/97/e4/99/97e49907-7fdf-57c9-ee01-3b20d055a875/source/512x512bb.jpg")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"русский:flag_ru: ", value=result.text,inline=False)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#フランス語
async def fr(ctx, *,msg):
    translator = deepl.Translator(Deepl) 
    result = translator.translate_text(msg,target_lang="FR") 
    translated_text = result.text
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/97/e4/99/97e49907-7fdf-57c9-ee01-3b20d055a875/source/512x512bb.jpg")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"français:flag_fr: ", value=result.text,inline=False)
    embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑[Deepl API]↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓[papago API]↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#
@bot.command()
#日本語→韓国語
async def jk(ctx, *,msg):
    data = {'text' : msg,'source' : "ja",'target': 'ko'} 
    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    if(rescode==200):
        t_data = response.json()
        embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
        embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
        embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
        embed.add_field(name=f"한국어:flag_kr: ", value=t_data['message']['result']['translatedText'],inline=False)
        embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
        await ctx.channel.send(embed=embed)
@bot.command()
#韓国語→日本語
async def kj(ctx, *,msg):
    data = {'text' : msg,'source' : "ko",'target': 'ja'} 
    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    if(rescode==200):
        t_data = response.json()
        embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
        embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
        embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
        embed.add_field(name=f"日本語:flag_jp: ", value=t_data['message']['result']['translatedText'],inline=False)
        embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
        await ctx.channel.send(embed=embed)
@bot.command()
#韓国語→英語
async def ke(ctx, *,msg):
    data = {'text' : msg,'source' : "ko",'target': 'en'} 
    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    if(rescode==200):
        t_data = response.json()
        embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
        embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
        embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
        embed.add_field(name=f"English:flag_us: ", value=t_data['message']['result']['translatedText'],inline=False)
        embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
        await ctx.channel.send(embed=embed)
@bot.command()
#英語→韓国語
async def ek(ctx,*,msg):
    data = {'text' : msg,'source' : "en",'target': 'ko'} 
    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    if(rescode==200):
        t_data = response.json()
        embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
        embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
        embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
        embed.add_field(name=f"한국어:flag_kr: ", value=t_data['message']['result']['translatedText'],inline=False)
        embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
        await ctx.channel.send(embed=embed)
@bot.command()
#中国語→日本語
async def cj(ctx, *,msg):
    data = {'text' : msg,'source' : "zh-CH",'target': 'ja'} 
    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    if(rescode==200):
        t_data = response.json()
        embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
        embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
        embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
        embed.add_field(name=f"日本語:flag_jp: ", value=t_data['message']['result']['translatedText'],inline=False)
        embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
        await ctx.channel.send(embed=embed)
@bot.command()
#日本語→中国語
async def jc(ctx, *,msg):
    data = {'text' : msg,'source' : "ja",'target': 'zh-CH'} 
    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    if(rescode==200):
        t_data = response.json()
        embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
        embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
        embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
        embed.add_field(name=f"汉语:flag_cn: ", value=t_data['message']['result']['translatedText'],inline=False)
        embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
        await ctx.channel.send(embed=embed)
@bot.command()
#中国語→英語
async def ce(ctx, *,msg):
    data = {'text' : msg,'source' : "zh-CH",'target': 'en'} 
    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    if(rescode==200):
        t_data = response.json()
        embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
        embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
        embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
        embed.add_field(name=f"English:flag_us: ", value=t_data['message']['result']['translatedText'],inline=False)
        embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
        await ctx.channel.send(embed=embed)
@bot.command()
#英語→中国語
async def ec(ctx, *,msg):
    data = {'text' : msg,'source' : "en",'target': 'zh-CH'} 
    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code
    if(rescode==200):
        t_data = response.json()
        embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
        embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
        embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
        embed.add_field(name=f"汉语:flag_cn: ", value=t_data['message']['result']['translatedText'],inline=False)
        embed.set_footer(text="Service provided by Aliky.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
        await ctx.channel.send(embed=embed)
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑[papago API]↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓[baidu API]↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#
@bot.command()
#Baidu日本語
async def jpb(ctx, *,msg):
    httpClient = None
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    from_lang = 'auto'
    to_lang =  'jp'
    q = msg
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    data = {'appid': appid, 'q': q, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=header)
    result = response.json()
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/739364677360025723/931957431129473034/512x512bb.png")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"日本語:flag_jp: ", value=result["trans_result"][0]["dst"],inline=False)
    embed.set_footer(text="Service provided by Aliky. Supported by sorasora.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#Baidu中国語
async def chb(ctx, *,msg):
    httpClient = None
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    from_lang = 'auto'
    to_lang =  'zh'
    q = msg
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    data = {'appid': appid, 'q': q, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=header)
    result = response.json()
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/739364677360025723/931957431129473034/512x512bb.png")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"汉语:flag_cn: ", value=result["trans_result"][0]["dst"],inline=False)
    embed.set_footer(text="Service provided by Aliky. Supported by sorasora.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#Baidu英語
async def enb(ctx, *,msg):
    httpClient = None
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    from_lang = 'auto'
    to_lang =  'en'
    q = msg
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    data = {'appid': appid, 'q': q, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=header)
    result = response.json()
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/739364677360025723/931957431129473034/512x512bb.png")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"English:flag_us: ", value=result["trans_result"][0]["dst"],inline=False)
    embed.set_footer(text="Service provided by Aliky. Supported by sorasora.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#Baidu韓国語
async def krb(ctx, *,msg):
    httpClient = None
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    from_lang = 'auto'
    to_lang =  'kr'
    q = msg
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    data = {'appid': appid, 'q': q, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=header)
    result = response.json()
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/739364677360025723/931957431129473034/512x512bb.png")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"한국어:flag_kr: ", value=result["trans_result"][0]["dst"],inline=False)
    embed.set_footer(text="Service provided by Aliky. Supported by sorasora.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#Baiduタイ語
async def thb(ctx, *,msg):
    httpClient = None
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    from_lang = 'auto'
    to_lang =  'th'
    q = msg
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    data = {'appid': appid, 'q': q, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=header)
    result = response.json()
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/739364677360025723/931957431129473034/512x512bb.png")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"ไทย:flag_th: ", value=result["trans_result"][0]["dst"],inline=False)
    embed.set_footer(text="Service provided by Aliky. Supported by sorasora.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#Baiduスペイン語
async def esb(ctx, *,msg):
    httpClient = None
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    from_lang = 'auto'
    to_lang =  'spa'
    q = msg
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    data = {'appid': appid, 'q': q, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=header)
    result = response.json()
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/739364677360025723/931957431129473034/512x512bb.png")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"Español:flag_es: ", value=result["trans_result"][0]["dst"],inline=False)
    embed.set_footer(text="Service provided by Aliky. Supported by sorasora.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)
@bot.command()
#Baiduスウェーデン語
async def swb(ctx, *,msg):
    httpClient = None
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    from_lang = 'auto'
    to_lang =  'swe'
    q = msg
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    data = {'appid': appid, 'q': q, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=header)
    result = response.json()
    embed = discord.Embed(title="翻訳",color=0x5CD1E5,description="",)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/739364677360025723/931957431129473034/512x512bb.png")
    embed.add_field(name=f":speech_balloon:  ", value=msg,inline=False)
    embed.add_field(name=f"svenska:flag_se: ", value=result["trans_result"][0]["dst"],inline=False)
    embed.set_footer(text="Service provided by Aliky. Supported by sorasora.",icon_url='https://cdn.discordapp.com/attachments/739364677360025723/902368316365078548/unknown.png')
    await ctx.channel.send(embed=embed)

#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑[baidu API]↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#
bot.run(TOKEN)
