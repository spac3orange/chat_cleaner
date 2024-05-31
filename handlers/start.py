from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from config import aiogram_bot

from config import logger

router = Router()


async def get_chat_administrators(chat_id: int):
    chat_administrators = await aiogram_bot.get_chat_administrators(chat_id)
    admin_list = [admin.user.id for admin in chat_administrators]
    print(admin_list)
    return admin_list


@router.message(Command(commands='start'))
async def start(message: Message, state: FSMContext):
    logger.info(f'user {message.from_user.username} connected')


@router.message(lambda message: message.chat.type in ['group', 'supergroup'])
async def monitor_messages(message: Message):
    admin_list = await get_chat_administrators(message.chat.id)
    print(admin_list)
    if message.from_user.id in admin_list:
        pass
    else:
        if message.text != '+':
            logger.info(f'message deleted {message.text}')
            await aiogram_bot.delete_message(message.chat.id, message.message_id)
        else:
            pass