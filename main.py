import discord
import json
import random
import requests
import time
import asyncio
import datetime
from discord.ext import commands

intents = discord.Intents.all()
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
async def команды(ctx):
    embed = discord.Embed(title='Команды:', description='рег - команда для регистрации твоего кошелька\n'
    '\n'
    'стат - посмотреть свои статистики(баланс, работу и т.д)\n'
    '\n'
    'работать - заработать денюшек, доступно лишь раз в 6 часов\n'
    '\n'
    'цвета - посмотреть какие роли для увета ника есть в доступе\n'
    '\n'                                                   
    'купить - купить цветную роль для ника (цены смотрите в !цвета)\n'
    '\n'
    'списокп - посмотреть существующие профессии\n'
    '\n'
    'выбратьп - выбрать новую профессию\n'
    '\n'
    'монетка - просто напишет орёл или решка\n'
    '\n'
    'кнб - поиграть в камень, ножницы, бумага (!кнб камень)\n'
    '\n'
    'рандом - даёт рандомное число (!рандом 100)\n'
    '\n'
    'шлёпа - рандомный шлёпа с разными редкостями\n'
    '\n'
    'собака - рандомная пикча собачки\n'
    '\n'
    'шутка - 10 рандомных анекдотов\n'
    '\n'
    'дать - передать кому-то денюжку (!дать Fareor#5428 1000)\n',
                          color=discord.Color.yellow())
    await ctx.send(embed=embed)
@bot.event
async def on_command_error(ctx, error):
    da = (ctx.author.id)
    if isinstance(error, commands.CommandOnCooldown) and users[da]['prof'] != 'нету':
        retry_after = str(datetime.timedelta(seconds=error.retry_after)).split('.')[0]
        embed = discord.Embed(title='На команде установлен cooldown.', description=f'Вы сможете заного воспользоваться командой через: {retry_after}',
                              color=discord.Color.yellow())
        await ctx.send(embed=embed)
    elif users[da]['prof'] == 'нету':
        await ctx.send('Ты ещё не взял работу!\n'
                       'Пропиши команду !выбратьп 1 чтобы ты смог работать!')
@bot.command()
@commands.cooldown(1, 21600, commands.BucketType.user)
async def работать(ctx):
    da = (ctx.author.id)
    if da in users:
        if users[da]['prof'] == '1.Подработки':
            plus = random.randint(10, 20)
            exp = 5
            await ctx.send('Решив поискать подработки...')
        elif users[da]['prof'] == '2.Уборщик':
            plus = 50
            exp = 10
            await ctx.send('Вы пошли убираться на улице...')
        elif users[da]['prof'] == '3.Доставщик':
            plus = 80
            exp = 13
            await ctx.send('Вы надели форму и взяли рюкзак...')
        elif users[da]['prof'] == '4.Таксист':
            plus = 100
            exp = 15
            await ctx.send('Вы завели свою машину...')
        elif users[da]['prof'] == '5.Кассир':
            plus = 150
            exp = 20
            await ctx.send('Пойдя на свою работу...')
        elif users[da]['prof'] == '6.Бармен':
            plus = 200
            exp = 25
            await ctx.send('Протерев все бокалы и поговорив со всеми...')
        elif users[da]['prof'] == '7.Официант':
            plus = 225
            exp = 30
            await ctx.send('Разнося всем подносы с едой и записывая заказы...')
        elif users[da]['prof'] == '8.Повар':
            plus = 250
            exp = 35
        elif users[da]['prof'] == '9.Дизайнер интерьера':
            plus = 300
            exp = 45
            await ctx.send('Посмотрев запросы и отправившись к месту...')
        time.sleep(2)
        await ctx.send(f'За день вы заработали {plus} монет\n'
                       f'и {exp} опыта!')
        users[da]['balance'] += plus
        users[da]['exp'] += exp
        cho = users[da]['exp']
        ur = users[da]['lvl']
        time.sleep(1)
        if ur == 0 and cho >= 10:
            users[da]['lvl'] = 1
            users[da]['exp'] -= 10
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 1 and cho >= 15:
            users[da]['lvl'] = 2
            users[da]['exp'] -= 15
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 2 and cho >= 25:
            users[da]['lvl'] = 3
            users[da]['exp'] -= 25
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 3 and cho >= 35:
            users[da]['lvl'] = 4
            users[da]['exp'] -= 35
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 4 and cho >= 40:
            users[da]['lvl'] = 5
            users[da]['exp'] -= 40
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 5 and cho >= 45:
            users[da]['lvl'] = 6
            users[da]['exp'] -= 45
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 6 and cho >= 50:
            users[da]['lvl'] = 7
            users[da]['exp'] -= 50
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 7 and cho >= 60:
            users[da]['lvl'] = 8
            users[da]['exp'] -= 60
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 8 and cho >= 75:
            users[da]['lvl'] = 9
            users[da]['exp'] -= 75
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 9 and cho >= 80:
            users[da]['lvl'] = 10
            users[da]['exp'] -= 80
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 10 and cho >= 90:
            users[da]['lvl'] = 11
            users[da]['exp'] -= 90
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 11 and cho >= 110:
            users[da]['lvl'] = 12
            users[da]['exp'] -= 110
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 12 and cho >= 120:
            users[da]['lvl'] = 13
            users[da]['exp'] -= 120
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 13 and cho >= 130:
            users[da]['lvl'] = 14
            users[da]['exp'] -= 130
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 14 and cho >= 140:
            users[da]['lvl'] = 15
            users[da]['exp'] -= 140
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 15 and cho >= 150:
            users[da]['lvl'] = 16
            users[da]['exp'] -= 150
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 16 and cho >= 165:
            users[da]['lvl'] = 17
            users[da]['exp'] -= 165
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 17 and cho >= 180:
            users[da]['lvl'] = 18
            users[da]['exp'] -= 180
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 18 and cho >= 195:
            users[da]['lvl'] = 19
            users[da]['exp'] -= 195
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 19 and cho >= 225:
            users[da]['lvl'] = 20
            users[da]['exp'] -= 225
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 20 and cho >= 245:
            users[da]['lvl'] = 21
            users[da]['exp'] -= 245
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 21 and cho >= 265:
            users[da]['lvl'] = 22
            users[da]['exp'] -= 265
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 22 and cho >= 285:
            users[da]['lvl'] = 23
            users[da]['exp'] -= 285
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 23 and cho >= 305:
            users[da]['lvl'] = 24
            users[da]['exp'] -= 305
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 24 and cho >= 325:
            users[da]['lvl'] = 25
            users[da]['exp'] -= 325
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 25 and cho >= 350:
            users[da]['lvl'] = 26
            users[da]['exp'] -= 350
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 26 and cho >= 375:
            users[da]['lvl'] = 27
            users[da]['exp'] -= 375
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 27 and cho >= 400:
            users[da]['lvl'] = 28
            users[da]['exp'] -= 400
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 28 and cho >= 425:
            users[da]['lvl'] = 29
            users[da]['exp'] -= 425
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 29 and cho >= 450:
            users[da]['lvl'] = 30
            users[da]['exp'] -= 450
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 30 and cho >= 350:
            users[da]['lvl'] = 31
            users[da]['exp'] -= 475
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 31 and cho >= 375:
            users[da]['lvl'] = 32
            users[da]['exp'] -= 500
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 32 and cho >= 400:
            users[da]['lvl'] = 33
            users[da]['exp'] -= 525
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 33 and cho >= 425:
            users[da]['lvl'] = 34
            users[da]['exp'] -= 550
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        if ur == 34 and cho >= 450:
            users[da]['lvl'] = 35
            users[da]['exp'] -= 600
            await ctx.send(f'Вы повысили свой уровень до {users[da]["lvl"]}!')
        save()
    else:
        embed = discord.Embed(title='У вас нет кошелька!',
                              description='Просто напиши команду рег и снова воспользуйся командой!',
                              color=discord.Color.yellow())
        await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if message.content.lower() == 'привет кот':
        await message.channel.send('Привет, как дела?')
    await bot.process_commands(message)
@bot.command()
async def рег(ctx):
    da = (ctx.author.id)
    if da in users:
        await ctx.send('У тебя уже есть кошелёк!')
        return
    users[da] = {'balance': 0, 'prof': 'нету', 'lvl': 0, 'exp': 0}
    await ctx.send(f'Вы успешно зарегестрировали себя')
    save()
@bot.event
async def on_boost(member):
    channel = bot.get_channel(1093039174468239450)
    await channel.send(f"{member.mention} только что забустил сервер!")

@bot.command()
async def дать(ctx, comu='', skolko=0):
    da = (ctx.author.id)
    if da in users:
        if comu not in users:
            await ctx.send('Ты не написал кому скинуть деньги!Или у пользователя нету кошелька.\n'
                           'если что --> !дать Fareor#5428 1000')
        elif users[da]['balance'] < skolko:
            await ctx.send(f'У тебя нет такой суммы!\n Если что твой баланс: {users[da]["balance"]}')
        elif skolko <= 0:
            await ctx.send('Ты не правильно написал какую сумму скинуть!\n'
                           'если что --> !дать Fareor#5428 1000')
        elif skolko <= 99:
            await ctx.send('Мимальная суммма которую ты можешь скинуть: 100')
        elif comu == da:
            await ctx.send('Так не работает💀')
        elif comu in users and skolko >= 100 <= users[da]["balance"] and comu != da:
            users[da]["balance"] -= skolko
            users[comu]['balance'] += skolko
            await ctx.send(f'Пользователь {da} отправил {comu} целых {skolko} coems🤑')
            save()
    else:
        embed = discord.Embed(title='У вас нет кошелька!',
                              description='Просто напиши команду рег и снова воспользуйся командой!',
                              color=discord.Color.yellow())
        await ctx.send(embed=embed)


@bot.command()
async def цвета(ctx):
    emoji = discord.utils.get(bot.emojis, name="coems")
    embed = discord.Embed(title=f'Список товаров:{emoji}',
                          description='1.Цвет ника - (<@&1105503917355303015>)\n'
                                      '\n'
                                      '2.Цвет ника - (<@&1105503952197390387>)\n'
                                      '\n'
                                      '3.Цвет ника - (<@&1105503956651741205>)\n'
                                      '\n'
                                      '4.Цвет ника - (<@&1105503959059284060>)\n'
                                      '\n'
                                      '5.Цвет ника - (<@&1105503962414731364>)\n'
                                      '\n'
                                      '6.Цвет ника - (<@&1105503966030205049>)\n'
                                      '\n'
                                      '7.Цвет ника - (<@&1105503969700233267>)\n'
                                      '\n'
                                      '8.Цвет ника - (<@&1105503973621891102>)\n'
                                      '\n'
                                      '9.Цвет ника - (<@&1105503977061224451>)\n'
                                      '\n'
                                      '10.Цвет ника - (<@&1105503983377846332>)\n'
                                      '**(Все ники по 500 монет стоят)**\n'
                                      '\n'
                                      '11.Не придумал (пока что)'
                          ,
                          color=discord.Color.yellow())
    await ctx.send(embed=embed)


@bot.command()
async def купить(ctx, otvet=0):
    da = (ctx.author.id)
    role = discord.utils.get(ctx.guild.roles, name=f'цвет {otvet}')
    odin = discord.utils.get(ctx.guild.roles, name='цвет 1')
    dva = discord.utils.get(ctx.guild.roles, name='цвет 2')
    tri = discord.utils.get(ctx.guild.roles, name='цвет 3')
    chet = discord.utils.get(ctx.guild.roles, name='цвет 4')
    pat = discord.utils.get(ctx.guild.roles, name='цвет 5')
    shes = discord.utils.get(ctx.guild.roles, name='цвет 6')
    sem = discord.utils.get(ctx.guild.roles, name='цвет 7')
    vos = discord.utils.get(ctx.guild.roles, name='цвет 8')
    dev = discord.utils.get(ctx.guild.roles, name='цвет 9')
    des = discord.utils.get(ctx.guild.roles, name='цвет 10')
    if da not in users:
        yes = discord.Embed(title='У вас нет кошелька!',
                            description='Просто напиши команду рег и снова воспользуйся командой!',
                            color=discord.Color.yellow())
        await ctx.send(embed=yes)
        return
    if otvet > 10 or otvet < 1:
        await ctx.send('Такого цвета ещё нету!')
        return
    if users[da]['balance'] < 500:
        await ctx.send('Тебе не хватает монет!')
        return
    await ctx.author.add_roles(role)
    users[da]['balance'] -= 500
    await ctx.send('Ты получил новую окраску!')
    if otvet != 1:
        await ctx.author.remove_roles(odin)
        if odin in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 2 and dva in ctx.author.roles:
        await ctx.author.remove_roles(dva)
        if dva in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 3 and tri in ctx.author.roles:
        await ctx.author.remove_roles(tri)
        if tri in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 4 and chet in ctx.author.roles:
        await ctx.author.remove_roles(chet)
        if chet in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 5 and pat in ctx.author.roles:
        await ctx.author.remove_roles(pat)
        if pat in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 6 and shes in ctx.author.roles:
        await ctx.author.remove_roles(shes)
        if shes in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 7 and sem in ctx.author.roles:
        await ctx.author.remove_roles(sem)
        if sem in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 8 and vos in ctx.author.roles:
        await ctx.author.remove_roles(vos)
        if vos in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 9 and dev in ctx.author.roles:
        await ctx.author.remove_roles(dev)
        if dev in ctx.author.roles:
            users[da]['balance'] += 500
    if otvet != 10 and des in ctx.author.roles:
        await ctx.author.remove_roles(des)
        if des in ctx.author.roles:
            users[da]['balance'] += 500
    save()



@bot.command()
async def выбратьп(ctx, otvet='0'):
    odin = discord.utils.get(ctx.guild.roles, name="1.Подработки")
    dva = discord.utils.get(ctx.guild.roles, name="2.Уборщик")
    tri = discord.utils.get(ctx.guild.roles, name="3.Доставщик")
    chet = discord.utils.get(ctx.guild.roles, name="4.Таксист")
    pat = discord.utils.get(ctx.guild.roles, name="5.Кассир")
    shes = discord.utils.get(ctx.guild.roles, name="6.Бармен")
    sem = discord.utils.get(ctx.guild.roles, name="7.Официант")
    vos = discord.utils.get(ctx.guild.roles, name="8.Повар")
    dev = discord.utils.get(ctx.guild.roles, name="9.Дизайнер интерьера")
    da = (ctx.author.id)
    if da in users:
        await asyncio.sleep(1.5)
        if otvet == '2' and users[da]["lvl"] < 2 or otvet == '3' and users[da]["lvl"] < 5 or otvet == '4' and users[da]["lvl"] < 10:
            await ctx.send('У вас не хватает уровня для этого!')
        elif otvet == '5' and users[da]["lvl"] < 15 or otvet == '6' and users[da]["lvl"] < 20 or otvet == '7' and users[da]["lvl"] < 25:
            await ctx.send('У вас не хватает уровня для этого!')
        elif otvet == '8' and users[da]["lvl"] < 30 or otvet == '9' and users[da]["lvl"] < 35:
            await ctx.send('У вас не хватает уровня для этого!')
        else:
            if otvet == '1':
                users[da]["prof"] = '1.Подработки'
                await ctx.author.add_roles(odin)
            if otvet == '2':
                users[da]["prof"] = '2.Уборщик'
                await ctx.author.add_roles(dva)
            if otvet == '3':
                users[da]["prof"] = '3.Доставщик'
                await ctx.author.add_roles(tri)
            if otvet == '4':
                users[da]["prof"] = '4.Таксист'
                await ctx.author.add_roles(chet)
            if otvet == '5':
                users[da]["prof"] = '5.Кассир'
                await ctx.author.add_roles(pat)
            if otvet == '6':
                users[da]["prof"] = '6.Бармен'
                await ctx.author.add_roles(shes)
            if otvet == '7':
                users[da]["prof"] = '7.Официант'
                await ctx.author.add_roles(sem)
            if otvet == '8':
                users[da]["prof"] = '8.Повар'
                await ctx.author.add_roles(vos)
            if otvet == '9':
                users[da]["prof"] = '9.Дизайнер интерьера'
                await ctx.author.add_roles(dev)
            await ctx.send(f'Теперь у вас работа: {users[da]["prof"]}!')
            if users[da]['prof'] != '1.Подработки':
                await ctx.author.remove_roles(odin)
            if users[da]['prof'] != '2.Уборщик':
                await ctx.author.remove_roles(dva)
            if users[da]['prof'] != '3.Доставщик':
                await ctx.author.remove_roles(tri)
            if users[da]['prof'] != '4.Таксист':
                await ctx.author.remove_roles(chet)
            if users[da]['prof'] != '5.Кассир':
                await ctx.author.remove_roles(pat)
            if users[da]['prof'] != '6.Бармен':
                await ctx.author.remove_roles(shes)
            if users[da]['prof'] != '7.Официант':
                await ctx.author.remove_roles(sem)
            if users[da]['prof'] != '8.Повар':
                await ctx.author.remove_roles(vos)
            if users[da]['prof'] != '9.Дизайнер интерьера':
                await ctx.author.remove_roles(dev)
            save()
    else:
        yes = discord.Embed(title='У вас нет кошелька!',
                            description='Просто напиши команду рег и снова воспользуйся командой!',
                            color=discord.Color.yellow())
        await ctx.send(embed=yes)


@bot.command()
async def списокп(ctx):
    da = (ctx.author.id)
    if da in users:
        embed = discord.Embed(title='Вот список всех профессий',
                              description='1. Подработки - не требует опыта\n'
                                          'даёт 5 опыта и 10-20 монет\n'
                                          '(с 0 lvl)\n'
                                          '2. Уборщик - очень грязная работа\n'
                                          'даёт 10xp и 50 монет\n'
                                          '(с 2 lvl)\n'
                                          '3. Доставщик - приносит всем обедик\n'
                                          'даёт 13xp и 80 монет\n'
                                          '(с 5 lvl)\n'
                                          '4. Таксист - главное будь тихим\n'
                                          'даёт 15xp и 100 монет\n'
                                          '(с 10 lvl)\n'
                                          '5. Кассир - будь адекватным🙏\n'
                                          'даёт 20xp и 150 монет\n'
                                          '(с 15 lvl)\n'
                                          '6. Бармен - наливай напитки и слушай истории\n'
                                          'даёт 25xp и 200 монет\n'
                                          '(с 20 lvl)\n'
                                          '7. Официант - будь аккуратней с подносами\n'
                                          'даёт 30 xp и 225 монет\n'
                                          '(с 25 lvl)\n'
                                          '8. Повар - делает всем вкусный обед🥗\n'
                                          'даёт 35 опыта и 250 монет\n'
                                          '(с 30 lvl)\n'
                                          '9. Дизайнер интерьера - помогай людям проектировать их\n'
                                          'дизайн квартиры\n'
                                          'даёт 45 опыта и 300 монет\n'
                                          '(с 35 lvl)\n'
                                          f'**Это будет дополнятся (до 15 возможно)**\n'
                                          f'Ваша текущая работа: {users[da]["prof"]}',
                              color=discord.Color.yellow())
        await ctx.send(embed=embed)
    else:
        yes = discord.Embed(title='У вас нет кошелька!',
                            description='Просто напиши команду рег и снова воспользуйся командой!',
                            color=discord.Color.yellow())
        await ctx.send(embed=yes)


@bot.command()
async def стат(ctx):
    da = (ctx.author.id)
    emoji = discord.utils.get(bot.emojis, name="shock3right")
    if da in users:
        max_values = {
            0: 10,
            1: 15,
            2: 25,
            3: 35,
            4: 40,
            5: 45,
            6: 50,
            7: 60,
            8: 75,
            9: 80,
            10: 90,
            11: 110,
            12: 120,
            13: 130,
            14: 140,
            15: 150,
            16: 165,
            17: 180,
            18: 195,
            19: 225,
            20: 245,
            21: 35,
            22: 265,
            23: 285,
            24: 305,
            25: 325,
            26: 350,
            27: 375,
            28: 400,
            29: 425,
            30: 450,
            31: 475,
            32: 500,
            33: 525,
            34: 550,
            35: 600
        }
        embed = discord.Embed(title=f'{emoji}Ваши статистики:',
                              description=f'Ваш баланс: **{users[da]["balance"]}**\n'
                                          f'Ваша работа: **{users[da]["prof"]}**\n'
                                          f'Ваш уровень: **{users[da]["lvl"]}**\n'
                                          f'Ваш опыт: **{users[da]["exp"]}/{max_values[users[da]["lvl"]]}**\n',
                              color=discord.Color.yellow())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='У вас нет кошелька!',
                              description='Просто напиши команду рег и снова воспользуйся командой!',
                              color=discord.Color.yellow())
        await ctx.send(embed=embed)


@bot.command
async def монетка(ctx):
    flip = random.randint(0, 1)
    await asyncio.sleep(1)
    await ctx.send("Выпало...")
    await asyncio.sleep(1)
    if flip == 0:
        await ctx.send("**Орёл!**")
    else:
        await ctx.send("**Решка!**")


@bot.command()
async def кнб(ctx, userchoice='пусто'):
    choices = 'бумага', 'камень', 'ножницы'
    botchoice = random.choice(choices)
    if userchoice not in choices:
        await asyncio.sleep(2)
        await ctx.send('**Ты написал не камень, ножницы или бумага!**')
        return
    await asyncio.sleep(1)
    await ctx.send(f'Хороший выбор...')
    await asyncio.sleep(2)
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
async def рандом(ctx, maximum=0):
    await asyncio.sleep(1)
    if maximum == 0:
        await ctx.send(f'Ты не написал максимальное число')
    else:
        randomnoe = random.randint(0, maximum)
        await ctx.send(f'{randomnoe}')
    return maximum


@bot.command()
async def шлёпа(ctx):
    await asyncio.sleep(1)
    await ctx.send(f'Тебе выпал...')
    await asyncio.sleep(1.5)
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


@bot.command
async def собака(ctx):
    image_url = chto()
    await ctx.send(image_url)


bot.run("Your token")
