import logging
from os import remove
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from pytube import YouTube

API_TOKEN = """Enter your token here"""

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await message.reply("Hi!\nI'm k1t9bot!\nPowered by aiogram.")



download_callback = CallbackData('download', 'yt_stream')
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton





choice = InlineKeyboardMarkup(row_width=2)
download_res = InlineKeyboardButton(text='360p', callback_data=download_callback.new(yt_stream='res_480'))
choice.insert(download_res)
download_high_res = InlineKeyboardButton(text='high resolution', callback_data=download_callback.new(yt_stream='high_res'))
choice.insert(download_high_res)
download_audio_only = InlineKeyboardButton(text='audio only', callback_data=download_callback.new(yt_stream='audio_only'))
choice.insert(download_audio_only)




@dp.message_handler()
async def send_link(message: types.Message):
    try:
        await message.answer(text=message.text, reply_markup=choice)
    except Exception as e:
        await bot.send_message(message.chat.id, e)

@dp.callback_query_handler(text_contains='audio_only')
async def download_audio_only(call: CallbackQuery):
    await call.answer(text='music')
    try:
        link = call.message.text
        yt = YouTube(link)
        yt.streams.get_audio_only().download(output_path='media', filename=f'{yt.title}.mp3')
        await call.message.answer_audio(audio=open(f'media/{yt.title}.mp3','rb'))
        remove(f'media/{yt.title}.mp3')
    except Exception as e:
        await call.message.answer(e)
@dp.callback_query_handler(text_contains='res_480')
async def download_res(call: CallbackQuery):
    await call.answer(text='res_480')
    try:
        link = call.message.text
        yt = YouTube(link)
        yt.streams.get_by_resolution(resolution="360p").download(output_path='media', filename=f'{yt.title}.mp4')
        await call.message.answer_video(video=open(f'media/{yt.title}.mp4','rb'))
        remove(f'media/{yt.title}.mp4')
    except Exception as e:
        await call.message.answer(e)
@dp.callback_query_handler(text_contains='high_res')
async def download_high_res(call: CallbackQuery):
    await call.answer(text='high_res')
    try:
        link = call.message.text
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download(output_path='media', filename=f'{yt.title}.mp4')
        await call.message.answer_video(video=open(f'media/{yt.title}.mp4','rb'))
        remove(f'media/{yt.title}.mp4')
    except Exception as e:
        await call.message.answer(e)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

