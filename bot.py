import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

# lataa "komento" tiedostot
command_files = [file for file in os.listdir('./commands') if file.endswith('.py')]
commands = {}

for file in command_files:
    command_name = os.path.splitext(file)[0]
    command = getattr(__import__('commands.' + command_name), command_name)
    commands[command_name] = command

@bot.event
async def on_message(message):
    # Jätä bottien lähettämät viestit huomioimatta
    if message.author.bot:
        return

    # Tarkista onko komento
    if message.content.startswith('?'):
        args = message.content[1:].strip().split(' ')
        command_name = args.pop(0).lower()

        # Tarkista onko komentoa olemassa
        if command_name not in commands:
            await message.channel.send(f"{message.author.mention}, Tuntematon komento '{command_name}'. tee komento ?help nähdäksesi käytössä olevat komennot.")
            return

        # Suorita komento
        command = commands[command_name]
        await command.execute(message, args, bot, commands)

        # Poista käyttäjän lähettämä viesti tietyjen komentojen yhteydessä
        if command_name in ['ehdotus','kysely']:  # Lisää tarvitessa myös muita komentoja listaan
            await message.delete()

bot_token = os.getenv('BOT_TOKEN')
if not bot_token:
    print("Botin tokenia ei löytynyt. Määritä 'BOT_TOKEN' environment variable.")
    exit()

bot.run(bot_token)