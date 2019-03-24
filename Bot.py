import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='ap!')
@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    await Bot.change_presence(game=discord.Game(name="the portals! 🌀", type=3))

bot.remove_command('help')

@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

bot.run('NTU4NTQyODkwMzA2MTA5NDUy.D3lPpA.yBZoL0UCcBb9ilQUuDVo1XaGJoU')
