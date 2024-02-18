import discord

# commands/help.py

async def execute(message, args, client, commands):
    # Tekee embed viesitin
    embed = discord.Embed(
        title='Lista saatavilla olevista komennoista🚀',
        color=0xb977ff  # viestin sivun väri
    )

    # Määrittää komentojen kategorian ja niihin liittyvät komennot kuvauksien kanssa.
    categories = {
        'Komennot': {
            '?kysely': 'Luo kyselyn',
            '?ehdotus': 'Luo äänestyksen ehdotuksesta',
            '?help': 'Näyttää saatavilla olevat komennot',
        },
    }

    # lisää komennon tietoja embediin
    for category, commands_dict in categories.items():
        command_list = '\n'.join([f'`{cmd}` - {desc}' for cmd, desc in commands_dict.items()])
        embed.add_field(name=f'**{category}**', value=command_list, inline=False)

    # lisää thumbnail
    embed.set_thumbnail(url='https://i.imgur.com/YourCoolIcon.png')

    # aseta footer ja lisä informaatio
    embed.set_footer(
        text='taigrpolls | stable',
        icon_url='https://i.imgur.com/FooterIcon.png'  # Customize the footer icon URL
    )

    # tekee aikaleiman embed viestille
    embed.timestamp = message.created_at

    # lähettää embed viestin
    await message.channel.send(embed=embed)

# Assign the execute function to a 'name' attribute
execute.__command_name__ = 'help'
