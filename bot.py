import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from functions import GSFunction
from murkups import ikb_categories

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(skip_updates=True)


gs_function = GSFunction('google_data.json')


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    values = set(gs_function.selecting_values_by_key('Категория'))
    await message.answer('Выберите категорию в которой хотите получить скидку ⬇️',
                     reply_markup=ikb_categories(values))


@dp.callback_query(F.data.startswith("Категория_"))
async def cb_category(callback: types.CallbackQuery) -> None:
    callback_data = tuple(callback.data.split('_'))
    data = gs_function.selecting_dicts_by_tuple(callback_data)
    print(data)
    await callback.message.answer('yo')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
