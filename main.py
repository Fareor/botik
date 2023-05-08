import datetime
import discord
import json
import random
import requests
import time
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
users = {}
with open('savefile.json') as aw:
    users = json.load(aw)
print(users)
def save():
    with open("savefile.json", "w") as f:
        json.dump(users, f)


@bot.command()
async def ноль(ctx):
    da = (ctx.author.name + '#' + ctx.author.discriminator)
    users[da] = ['balance']
    users[da]['balance'] = 0
    users[da] = ['prof']
    users[da]['prof'] = 'none'
    await ctx.send(f'Вы успешно зарегестрировали себя!')
    save()

@bot.command()
async def команды(ctx):
    embed = discord.Embed(title='Команды:', description='ноль - команда для регистрации твоего кошелька \n'
    
    'или обнулирования уже существуещего\n'
    
    'баланс - посмотреть свой баланс, вопросы? \n'
                                                        
    'работать - заработать денюшек, доступно лишь раз в 12 часов \n'
                                                        
    'монетка - просто напишет орёл или решка \n'
                                                        
    'кнб - поиграть в камень, ножницы, бумага (!кнб камень) \n'
                                                        
    'рандом - даёт рандомное число (!рандом 100) \n'
                                                        
    'шлёпа - рандомный шлёпа с разными редкостями \n'
                                                        
    'собака - рандомная пикча собачки \n'
                                                        
    'шутка - 10 рандомных анекдотов \n',
    color=discord.Color.yellow())
    await ctx.send(embed=embed)

@bot.command()
async def баланс(ctx):
    da = (ctx.author.name + '#' + ctx.author.discriminator)
    if da in users:
        await ctx.send(f'Баланс пользователя {ctx.author.name}: '
                            f'{users[da]}')
    else:
        embed = discord.Embed(title='У вас нет кошелька!', description='Просто напиши команду рег и снова воспользуйся командой!', color=discord.Color.yellow())
        await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 720, commands.BucketType.user)
async def работать(ctx):
    da = (ctx.author.name + '#' + ctx.author.discriminator)
    if da in users:
        moneys = random.randint(30, 100)
        await ctx.send(f'За день вы заработали: '
                       f'{moneys}')
        users[da] += moneys
        save()
    else:
        embed = discord.Embed(title='У вас нет кошелька!', description='Просто напиши команду рег и снова воспользуйся командой!', color=discord.Color.yellow())
        await ctx.send(embed=embed)




@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = str(datetime.timedelta(seconds=error.retry_after)).split('.')[0]
        embed = discord.Embed(title='На команде установлен cooldown.', description=f'Вы сможете заного воспользоваться командой через: {retry_after}', color=discord.Color.yellow())
        await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def монетка(ctx):

    flip = random.randint(0, 1)
    time.sleep(1)
    await ctx.send("Выпало...")
    time.sleep(1)
    if flip == 0:
        await ctx.send("**Орёл!**")
    else:
        await ctx.send("**Решка!**")
@bot.command()
async def кнб(ctx, userchoice = 'пусто'):
    choices = 'бумага', 'камень', 'ножницы'
    botchoice = random.choice(choices)
    if userchoice not in choices:
        time.sleep(2)
        await ctx.send('**Ты написал не камень, ножницы или бумага!**')
        return
    time.sleep(1)
    await ctx.send(f'Хороший выбор...')
    time.sleep(2)
    if userchoice == botchoice:
        await ctx.send(f'**Ну ничья как бы**')
    elif userchoice == 'камень':
        if botchoice == 'бумага':
            await ctx.send(f'**Ты выбрал {userchoice}, но я {botchoice}. Я выиграл!**')
        else:
            await ctx.send(f'**Ты выбрал {userchoice}, но я {botchoice}. Ты выиграл!**')
    elif userchoice == 'бумага':
        if botchoice == 'ножницы':
            await ctx.send(f'**Ты выбрал {userchoice}, но я {botchoice}. Я выиграл!**')
        else:
            await ctx.send(f'**Ты выбрал {userchoice}, но я {botchoice}. Ты выиграл!**')
    elif userchoice == 'ножницы':
        if botchoice == 'камень':
            await ctx.send(f'**Ты выбрал {userchoice}, но я {botchoice}. Я выиграл**!')
        else:
            await ctx.send(f'**Ты выбрал {userchoice}, но я {botchoice}. Ты выиграл**!')
    return userchoice

@bot.command()
async def рандом(ctx, maximum = 0):
    time.sleep(1)
    if maximum == 0:
        await ctx.send(f'Ты не написал максимальное число')
    else:
        randomnoe = random.randint(0, maximum)
        await ctx.send(f'{randomnoe}')
    return maximum
@bot.command()
async def шлёпа(ctx):
    time.sleep(1)
    await ctx.send(f'Тебе выпал...')
    time.sleep(1.5)
    lan = random.randint(1, 100)
    common = ['8.jpg', '9.jpg', '1.jpg',
              '12.jpg', '5.jpg', '16.jpg']
    rare = ['11.jpg', '2.jpg', '13.jpg',
            '10.jpg', '17.jpg', '15.jpg']
    epic = ['6.jpg', '4.jpg', '7.jpg',
            '18.jpg', '14.gif']
    if lan < 41:
        img_name = random.choice(common)
        if img_name == '8.jpg':
            await ctx.send(f'ОГРОМНЫЙ шлёпа! (common)')
        elif img_name == '9.jpg':
            await ctx.send(f'Злой:rage: шлёпа! (common)')
        elif img_name == '1.jpg':
            await ctx.send(f'Смотрящий в потолок шлёпа! (common)')
        elif img_name == '12.jpg':
            await ctx.send(f'Сидящий на шкафу шлёпа! (common)')
        elif img_name == '5.jpg':
            await ctx.send(f'Сидящий в тазике шлёпа! (common)')
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif lan >= 41:
        img_name = random.choice(rare)
        if img_name == '11.jpg':
            await ctx.send(f'Крутой шлёпа в очках! (rare)')
        elif img_name == '2.jpg':
            await ctx.send(f'Лежащий на диване шлёпа! (rare)')
        elif img_name == '13.jpg':
            await ctx.send(f'Шлёпа с наушниками! (rare)')
        elif img_name == '10.jpg':
            await ctx.send(f'Шлёпа с арбузом! (rare)')
        elif img_name == '17.jpg':
            await ctx.send(f'Шлёпа со своим другом! (rare)')
        elif img_name == '15.jpg':
            await ctx.send(f'ОЧЕНЬ злой шлёпа (:rage:x2)! (rare)')
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif lan >= 71:
        img_name = random.choice(epic)
        if img_name == '6.jpg':
            await ctx.send(f'Шлёпа без ушей:sob:! (epic)')
        elif img_name == '4.jpg':
            await ctx.send(f'Шлёпа с пельмешкой! (epic)')
        elif img_name == '7.jpg':
            await ctx.send(f'Ерутой маленький шлёпа! (epic)')
        elif img_name == '18.jpg':
            await ctx.send(f'Напуганный:scream: шлёпа! (epic)')
        elif img_name == '14.gif':
            await ctx.send(f'GIF шлёпа! (epic)')
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif lan >= 95:
        await ctx.send(f'ЛЕГЕНДАРНЫЙ ШЛЁПА БЕЗ УШЕК В ШАКАЛЬНОМ КАЧЕСТВЕ!! (LEGENDARY)')
        with open(f'images/3.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
def chto():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('собака')
async def собака(ctx):
    image_url = chto()
    await ctx.send(image_url)


@bot.command()
async def шутка(ctx):
    jokes = {1: 'У Сталина было два танка, на которых он катался по очереди, очередь возмущалась, но не расходилась',
            2: 'Сигареты сделали предложение лёгким, лёгкие отказали',
            3: 'Мама любит белый хлеб, дедушка любит серый, а папа черный, он бананы любит',
            4: 'Идёт как то однорукий мимо секондхенда и плачет',
            5: 'Выловили утопленника, захотели допросить, а он как воды в рот набрал',
            6: 'Почему охранники на рынке всегда вежливые? Потому что они следят за базаром',
            7: 'Один кот не любил пылесосы, но потом он втянулся',
            8: 'Утром китайские дети делают зарядку, а вечером относят на рынок',
            9: 'Зачем на французских танках стоят зеркала заднего вида? Чтобы видеть поле боя.',
            10: 'Жили два друга, еврей и американец, обоим по 70 и в приюте. Друг еврей заболевает'
            'и перед смертью говорит: «За километр отсюда, под одиноким деревом, зарыто сокровище с деньгами,'
            'на эти деньги ты сможешь дожить жизнь счастливо» и умирает. Друг американец спрашивает: « Что такое километр»'}
    time.sleep(1)
    joke = random.randint(1, 10)
    await ctx.send(f'{jokes[joke]}')





bot.run("MTA5NzEyNzY5NDY2MTA3MDg1MA.GAhVaC.L8QWWkxteKznkW0KwgikVczR-kG7aTWTrAhaos")
