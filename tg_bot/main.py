from aiogram import Bot, Dispatcher, executor, types


# нужно вставить токен бота, полученный у @BotFather
API_TOKEN: str = '5585223513:AAH0LsobRTjJK4Uy6R4GYuibd1st_M-ibJI'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
@dp.message_handler()
async def send_echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


#https://api.telegram.org/bot5585223513:AAH0LsobRTjJK4Uy6R4GYuibd1st_M-ibJI/getMe