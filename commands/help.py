import discord

# commands/help.py

async def execute(message, args, client, commands):
    # Tekee embed viesitin
    embed = discord.Embed(
        title='Lista saatavilla olevista komennoista🚀',
        color=0xb977ff  # viestin sivun väri
    )

    # Define command categories and associated commands with descriptions
    categories = {
        'Komennot': {
            '?kysely': 'Luo kyselyn',
            '?ehdotus': 'Luo äänestyksen ehdotuksesta',
            '?help': 'Näyttää saatavilla olevat komennot',
        },
    }

    # Add command information to the embed
    for category, commands_dict in categories.items():
        command_list = '\n'.join([f'`{cmd}` - {desc}' for cmd, desc in commands_dict.items()])
        embed.add_field(name=f'**{category}**', value=command_list, inline=False)

    # Add a thumbnail (you can customize this URL)
    embed.set_thumbnail(url='https://i.imgur.com/YourCoolIcon.png')

    # Set the footer with additional information
    embed.set_footer(
        text='taigrpolls | stable',
        icon_url='https://i.imgur.com/FooterIcon.png'  # Customize the footer icon URL
    )

    # Set a timestamp for the embed (current time)
    embed.timestamp = message.created_at

    # Send the embed message
    await message.channel.send(embed=embed)

# Assign the execute function to a 'name' attribute
execute.__command_name__ = 'help'
