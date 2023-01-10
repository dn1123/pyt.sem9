from t_bot import bot



async def start_game(message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}\n' f'Правила игры: На столе лежит 150 конфет. Каждый игрок берет  не более 28ми конфет, игроки ходят по очереди. Тот кто взял последний, тот и выиграл. ')

async def player_take(message):
    await bot.send_message(message.from_user.id, f'Возмите конфеты от 1 до 28:')

async def table_info(message, name1, take, total_count, name2):
    await bot.send_message(message.from_user.id, f'{name1} взял {take} конфет, \nна столе осталось {total_count} конфет.\nХод {name2}')

async def win(message, name, take, total_count):
    await bot.send_message(message.from_user.id, f'{name} взял {take} конфет, \nна столе осталось {total_count} конфет.\nПобедил {name}')

async def wrong_take(message):
    await bot.send_message(message.from_user.id, f'Вы взяли слишком много конфет, попробуйте снова')
