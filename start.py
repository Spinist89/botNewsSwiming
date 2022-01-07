import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

from server import Server

vk_session = vk_api.VkApi(token='b91894e7092986217ae561849990caa9721f45d61831c7db5ea8984f4f0347243f3eace1d9282346a61c7')
longpoll = VkBotLongPoll(vk_session, 209919290)

vk = vk_session.get_api()

server = Server(longpoll, vk)

COMMANDS = {
    'Помощь': {
        'function': server.command_help,
        'description': 'Команда для получения информации по боту'
    },
    'Начать': {
        'function': server.command_help,
        'description': ''
    },
    'НовостиSportBox': {
        'function': server.news_SportBox,
        'description': 'Команда для получения новостей с сайта SportBox.'
    },
    'НовостиSportExpress': {
        'function': server.news_SportExpress,
        'description': 'Команда для получения новостей с сайта SportBox.'
    },
}

while True:
    try:
        server.start(COMMANDS)
    except:
        pass
