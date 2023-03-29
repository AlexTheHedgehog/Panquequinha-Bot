import discord
import respostas

async def send_message(message, user_message, is_private):
    try:
        resposta = respostas.handle_response(user_message)
        if is_private:
            await message.author.send(resposta)
        else:
            await message.channel.send(f'{message.author.mention} {resposta}')
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'Seu Token Aqui'

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Game(name='🥞 Fazendo panquecas 🥞'))
        print(f'{client.user.name} está online.')

    
    @client.event
    async def on_message(message):
        if message.author == client.user or not message.content.startswith("$"):
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username}, menção {message.author.mention}, falou: "{user_message}" no canal {channel}')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
