from email import message
import discord
import random
TOKEN = 'OTc4NTA2MTMzMzYwNzcxMTcz.GDxHEV.HLWUG3VA-Kt7DWZ_AARhfFI22oKVf279C02YGg'

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as user {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    lst = ["Hey, don't ever say you hate life, that's blasphemy."
    ,"You ever feel like nothing good was ever gonna happen to you?"
    ,"Wait here, I'll get you viagra."
    ,"In My Thoughts, I Used A Technique Of Positive Visualization. How Come I Always Feel Undermined?"
    ,"I Don’t Care If They Shove A Scud Missile Up Your Ass. This Is My Corner. You Pay Anyone But Me, I’m Coming Back For Your Thumb."
    ]


    
    if message.channel.name == 'sopranos':
        if user_message.lower() == '$quote':
            await message.channel.send(random.choice(lst))
            return





client.run(TOKEN)


    