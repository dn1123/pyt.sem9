import commands
from aiogram import Dispatcher


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_game, commands = ['start'])
    dp.register_message_handler(commands.player_turn)