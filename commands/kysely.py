# commands/kysely.py
import discord

async def execute(message, args, client, commands):
    question = ' '.join(args)

    if not question:
        return await message.reply('Esitä kysymys kyselyä varten.') # error handling

    author = message.author
    avatar_url = author.avatar.url if author.avatar else discord.Embed.Empty

    kysely_embed = discord.Embed(
        title='Kysely', # Viestin Otsikko
        description=f'**{question}**', # Viestin kuvaus
        color=0x7F00FF,  # Voit vaihtaa värin haluamaksesi joka näkyy botin lähettämässä viestissä
    )
    kysely_embed.set_footer(text=f'Kyselyn loi: {author.display_name}', icon_url=avatar_url) # Botin lähettämän viestin alateksti

    kysely_message = await message.channel.send(embed=kysely_embed)
    for emoji in ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']: # reaktiot botin lähettämään viestiin.
        await kysely_message.add_reaction(emoji)

# Määrittää funktion suorittamisen 'kysely' attribuutille
execute.__command_name__ = 'kysely'