from aiogram.utils import executor
import handrels
from t_bot import dp


async def on_startup(_):
    print('Бот запущен')

handrels.registred_handlers(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)    
