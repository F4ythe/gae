import discord
import random
import youtube_dl
import os
import time
from discord import File
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    print('online')
    await client.change_presence(activity=discord.Game(name='.help for commands!'))

def is_it_me(ctx):
    return ctx.author.id == 274342185376415744

def birthen_check(ctx):
    return ctx.author.id == 513629977309085717

@client.command(pass_context=True)
@commands.check(is_it_me)
async def give(ctx, role: discord.Role, user: discord.Member):
    await user.add_roles(role)
    await ctx.channel.purge(limit=1)

@client.command(pass_context=True)
@commands.check(is_it_me)
async def remove(ctx, role: discord.Role, user: discord.Member):
    await user.remove_roles(role)
    await ctx.channel.purge(limit=1)

@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'ping: {round(client.latency * 100)}ms')

@client.command(pass_context=True)
async def hi(ctx):
    await ctx.send('say hi to ur mum for me ; )')

@client.command(pass_context=True)
async def gae(ctx, user):
    await ctx.send(f'{user} is gae')

@client.command(pass_context=True)
async def noban(ctx):
    await ctx.send('**NO UR MUM IS GAE U CANNOT BAN ME AHAHAHAHA**')

@client.command(pass_context=True)
async def no(ctx):
    await ctx.send('https://media1.giphy.com/media/d10dMmzqCYqQ0/giphy-downsized-large.gif')

@client.command(pass_context=True)
async def nou(ctx):
    await ctx.send('https://i.kym-cdn.com/photos/images/facebook/001/441/633/3c5.jpg')

@client.command(pass_context=True, name='69')
async def _69(ctx):
    await ctx.send('||haha u thought||')

@client.command(pass_context=True)
async def botjc(ctx):
    await ctx.send('**BOT JC IS GAE AHAHAHAHA**')

@client.command(pass_context=True)
async def music(ctx):
    await ctx.send('im not a music bot u gae')

@client.command(pass_context=True)
async def gaebot(ctx):
    await ctx.send('**IM THE BEST BOT FIGHT ME**')

@client.command(pass_context=True)
async def rushb(ctx):
    await ctx.send('https://upload.wikimedia.org/wikipedia/commons/7/76/Prussian_infantry_advancing_to_meet_the_Russian_Army_before_the_Battle_of_Zorndorf_25th_August_1758_in_the_Seven_Years_War_picture_by_Carl_R%C3%B6chling.jpg')

@client.command(pass_context=True)
async def rusha(ctx):
    await ctx.send('negative.')

@client.command(pass_context=True)
async def ok(ctx):
    await ctx.send('ok boomer')

@client.command(pass_context=True)
async def jc(ctx):
    await ctx.send('jc is gae')

@client.command(pass_context=True)
async def on9(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/705357582369292289/751825953344323666/on9.png')

@client.command(pass_context=True)
@commands.check(is_it_me)
async def ez(ctx):
    await ctx.send('ez')
    await ctx.send('ez')
    await ctx.send('ez')
    await ctx.send('ez')
    await ctx.send('ez')

@client.command(pass_context=True)
async def james(ctx):
    await ctx.send('https://i.pinimg.com/originals/e6/c7/cd/e6c7cd101e3966023b5efeb57cf3555b.png')
    await ctx.send('https://www.memesmonkey.com/images/memesmonkey/1e/1e304423dfee474dcf1c3bf291ae8673.jpeg')
    await ctx.send('https://memeguy.com/photos/images/african-americans-100623.jpg')

@client.command(pass_context=True)
async def jamesawp(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/705357582369292289/752067430167216208/james_clutch.mp4')

@client.command(pass_context=True)
async def dingus(ctx):
    await ctx.send('u dingus and gae at the same time')

@client.command(pass_context=True)
async def andrew(ctx):
    await ctx.send('**ANDREW IS THE BEST HAHAHAAHHAHAA**')

@client.command(pass_context=True)
async def yes(ctx):
    await ctx.send('yes u gae boomer')

@client.command(pass_context=True)
async def me(ctx):
    await ctx.send(f'<@{ctx.author.id}> is gae')

@client.command(pass_context=True)
async def asked(ctx):
    responses = ['https://tenor.com/view/askers-no-one-asked-0askers-minecraft-dream-gif-20338555',
                'https://youtu.be/hB3k3g22deY',
                'https://tenor.com/view/me-looking-for-who-tf-asked-looking-around-kid-kazoo-kid-gif-17654948',
                'https://tenor.com/view/nooneasked-gif-10757908']
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def who(ctx):
    responses = ['<@609258302303633439> is gae',
                '<@462559259360493571> is gae',
                '<@457362501521113088> is gae',    
                '<@274342185376415744> is gae',
                '<@652512533290156042> is gae',
                '<@586020520663973898> is gae',
                '<@440395117782630402> is gae',
                '<@392172101538152464> is gae',
                '<@667732531625328641> is gae',
                '<@513629977309085717> is gae',
                '<@396980613120393237> is gae',]
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def rps(ctx):
    responses = ['rock',
                'paper',
                'scissors',]
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def ht(ctx):
    responses = [':slight_smile:',
                ':peach:',]
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def spin(ctx, user, user1, user2):
    responses = [f'{user}',
                f'{user1}',
                f'{user2}',]
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def pog(ctx):
    await ctx.send('https://freepngimg.com/thumb/mouth/92712-ear-head-twitch-pogchamp-emote-free-download-png-hq-thumb.png')

@client.command(pass_context=True)
async def funi(ctx):
    responses = ['https://cdn.discordapp.com/attachments/802905704482209802/809423976816312390/Screenshot_20210211-220133063_1.jpg',
                'https://tenor.com/view/the-office-michael-scott-steve-carrell-unamused-meh-gif-16391448']
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
@commands.check(is_it_me)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)

@client.command(pass_context=True)
async def fuck(ctx):
    await ctx.send('idfk')

#@client.command(pass_context=True)
async def charon(ctx):
    responses = ['https://cdn.discordapp.com/attachments/814992149070217226/815104225746223124/charongaevid.mp4',
                'https://cdn.discordapp.com/attachments/780021032723021869/815107597686013984/charongae5.png']
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def simp2k(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/802908517429674024/815106970871922688/shrimp2k.jpg')

@client.command(pass_context=True)
async def fax(ctx):
    await ctx.send('https://www.myfax.com/sf-images/default-source/pagespeedimages/homepage-new2/step1-fax-sent.png')

@client.command(pass_context=True)
async def battlebus(ctx):
    await ctx.send('dingus chungus mungus fungus battle bus')

@client.command(pass_context=True)
async def cap(ctx):
    responses = ['https://i.redd.it/kq1p6yhrd2r21.jpg',
                'https://i.imgflip.com/4fegy2.jpg',
                'https://www.memecreator.org/static/images/memes/5152079.jpg',
                'https://i.imgflip.com/4ef9us.jpg']
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
@commands.check(is_it_me)
async def ungae(ctx, ungaed):
    await ctx.send(ungaed)
    await ctx.send(file=File('C:/Users/OWNER/Desktop/gaebot.py/files/ungae.png'))

@client.command(pass_context=True)
async def cares(ctx):
    responses = ['https://tenor.com/view/checking-radar-no-one-cares-radar-no-one-cares-who-cares-checking-the-radar-gif-16149872',
                'https://tenor.com/view/no-one-cares-i-dont-care-idc-nobody-cares-gif-8737514',
                'https://tenor.com/view/fuck-who-cares-who-gives-a-fuck-chris-pratt-middle-finger-gif-8101659',
                'https://tenor.com/view/please-please-i-have-no-time-for-any-gossip-i-dont-have-time-for-an-gossip-now-kid-man-angry-gif-17038791']
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def fookouf(ctx):
    await ctx.send('https://tenor.com/view/connor-mc-gregor-gtfo-gtfoh-get-the-fuck-out-of-here-gif-10203692')

@client.command(pass_context=True)
async def jcjob(ctx):
    await ctx.send('https://tenor.com/view/jcgotnext-lc-jc-getajob-jcneedsjob-gif-18730450')

@client.command(pass_context=True)
async def bts(ctx):
    responses = ['https://tenor.com/view/bts-funny-face-bangtan-boys-bangtan-sonyeondan-army-gif-14114289',
                'https://tenor.com/view/taehyung-taetae-cute-bts-bangtanboys-gif-10081353',
                'https://tenor.com/view/dynamite-%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8-bts-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%A7%88%EC%9D%B4%ED%8A%B8-%EB%B0%A9%ED%83%84-gif-18181539',
                'https://tenor.com/view/bts-grammys-cool-pose-kpop-gif-13472361']
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def nahwerd(ctx):
    await ctx.send('<:nahwerd:824836738231828510>')

@client.command(pass_context=True)
@commands.check(is_it_me)
async def spam(ctx, ping_user):
    await ctx.channel.purge(limit=1)
    await ctx.send(ping_user)
    await ctx.send(ping_user)
    await ctx.send(ping_user)
    await ctx.send(ping_user)
    await ctx.send(ping_user)

@client.command(pass_context=True)
async def eih(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/780021032723021869/835512592978018314/unknown.png')

@client.command(pass_context=True)
async def nino(ctx):
    await ctx.send(file=File('C:/Users/OWNER/Desktop/gaebot.py/files/my-names-nino.mp3'))

@client.command(pass_context=True)
async def bongo(ctx):
    await ctx.send(file=File('C:/Users/OWNER/Desktop/gaebot.py/files/bongo cat on9 wtf.gif'))

# help commands

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title = 'Commands', description = 'This is a list of all the commands and what they do.', color = discord.Color.orange())
    embed.add_field(name='.help', value='shows this text', inline=True)
    embed.add_field(name='.help2', value='shows second page of help menu', inline=True)
    embed.add_field(name='.hi', value='`say hi to ur mum for me ; )`', inline=True)
    embed.add_field(name='.gae', value='`word` is gae', inline=True)
    embed.add_field(name='.noban', value='`NO UR MUM IS GAE U CANNOT BAN ME AHAHAHAHA`', inline=True)
    embed.add_field(name='.no', value='inserts a `no` gif', inline=True)
    embed.add_field(name='.nou', value='inserts a `uno reverse card` image', inline=True)
    embed.add_field(name='.69', value='inserts a `nsfw` image', inline=True)
    embed.add_field(name='.botjc', value='`BOT JC IS GAE AHAHAHAHA`', inline=True)
    embed.add_field(name='.music', value='plays a random song', inline=True)
    embed.add_field(name='.gaebot', value='`gaegaegae`', inline=True)
    embed.add_field(name='.rushb', value='`RUSH B CYKA BLYAT`', inline=True)
    embed.add_field(name='.rusha', value='`RUSH A CYKA BLYAT`', inline=True)
    embed.add_field(name='.ok', value='`ok boomer`', inline=True)
    embed.add_field(name='.jc', value='`jc is gae`', inline=True)
    embed.add_field(name='.on9', value='just on9', inline=True)
    embed.add_field(name='.ez', value='spams `ez` 5 times', inline=True)
    embed.add_field(name='.james', value='inserts `african american` memes', inline=True)
    embed.add_field(name='.jamesawp', value='inserts clip of james clutching', inline=True)
    embed.add_field(name='.dingus', value='`u dingus and gae at the same time`', inline=True)
    embed.add_field(name='.andrew', value='`andrew is gae`', inline=True)
    embed.add_field(name='.yes', value='`yes u gae boomer`', inline=True)
    embed.add_field(name='.me', value='`i am gae`', inline=True)
    embed.add_field(name='.asked', value='no one asked', inline=True)
    embed.add_field(name='.who', value='who is gae?', inline=True)
    embed.set_footer(text='By Andrew')
    embed.set_author(name='Page 1')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/802908517429674024/814739551221579846/yes.jpg')
    await ctx.send(embed = embed)

@client.command(pass_context=True)
async def help2(ctx):
    embed = discord.Embed(title = 'Commands', description = 'This is a list of all the commands and what they do.', color = discord.Color.orange())
    embed.add_field(name='.ht', value='heads or tails', inline=True)
    embed.add_field(name='.rps `r/p/s`', value='the bot will play rps with u', inline=True)
    embed.add_field(name='.ping', value='shows latency of bot', inline=True)
    embed.add_field(name='.spin `1` `2` `3`', value='spins the wheel for 3 options', inline=True)
    embed.add_field(name='.pog', value='sends pog', inline=True)
    embed.add_field(name='.funi', value='inserts `funi` gif', inline=True)
    embed.add_field(name='.fuck', value='fuck', inline=True)
    embed.add_field(name='.charon', value='charongae.mp4', inline=True)
    embed.add_field(name='.simp2k', value='inserts simp2k gae image', inline=True)
    embed.add_field(name='.fax', value='big fax', inline=True)
    embed.add_field(name='.battlebus', value='dingus chungus mungus fungus battle bus', inline=True)
    embed.add_field(name='.cap', value='inserts cap', inline=True)
    embed.add_field(name='.ungae `user`', value='be able to ungae users', inline=True)
    embed.add_field(name='.cares', value='no one fucking cares ; )', inline=True)
    embed.add_field(name='.fookouf', value='get the fuck outta here', inline=True)
    embed.add_field(name='.jcjob', value='go get a fucking job jc', inline=True)
    embed.add_field(name='.bts', value='#army', inline=True)
    embed.add_field(name='.nahwerd', value='inserts nsfw `nahwerd` image', inline=True)
    embed.add_field(name='.eih', value='just eih', inline=True)
    embed.add_field(name='.nino', value='inserts `nino` audio file', inline=True)
    embed.add_field(name='.bongo', value='bongo cat on9 wtf', inline=True)
    embed.set_footer(text='By Andrew')
    embed.set_author(name='Page 2')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/802908517429674024/814739551221579846/yes.jpg')
    await ctx.send(embed = embed)
    
client.run('NTg3MjM1NDIyMzU1MDYyNzk0.XPznmg.1j6N8pkL4FYHgOm4CEHRv4lEBRM')