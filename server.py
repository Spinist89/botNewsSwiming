from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from parserSportBox import *
from parserSportExpress import *

# !
class Server:
    def __init__(self, longpoll, vk):
        self.__longpoll = longpoll
        self.vk = vk
        self.SportBox = SportBox('https://news.sportbox.ru/Vidy_sporta/plavanie')
        self.sportexpress = SportExpress('https://www.sport-express.ru/swimming/')
        print('Бот запущен!')

    def start(self, commands):
        self.commands = commands
        self.__command_starter()

    def __command_starter(self):
        for event in self.__longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                try:
                    msg = event.object['text']
                    self.commands[msg]['function'](event.object['peer_id'])
                except Exception as var:
                    print(var)

    def command_help(self, user_id):
        keyboard = VkKeyboard()
        keyboard.add_button(label='НовостиSportBox', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button(label='Ссылка на новостиSportBox', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(label='НовостиSportExpress', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button(label='Ссылка на новостиSportExpress', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(label='Всероссийская федерация плавания', color=VkKeyboardColor.PRIMARY)

        help_text = [f'👉 {value}: {self.commands[value]["description"]}' for number_iteration, value in
                     enumerate(self.commands.keys())]
        help_text = '\n'.join(help_text)
        self.vk.messages.send(
            message=f'Вот мой список команд:\n\n{help_text}',
            peer_id=user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard()
        )

    def news_SportBox(self, user_id):
            msg = "SportBox\n\n"
            for news in self.SportBox.parse():
                msg += f"🏊‍♂🏊‍♀{news['title']} {news['url']}\n\n"
            self.vk.messages.send(
                message=msg,
                peer_id=user_id,
                random_id=get_random_id()
            )
    def All_news_Sport_Box(self, user_id):
            msg = "All_news_Sport_Box\n\n"
            msg += self.vk.messages.send(
                message='https://news.sportbox.ru/Vidy_sporta/plavanie',
                peer_id=user_id,
                random_id=get_random_id()
            )
    def news_SportExpress(self, user_id):
            msg = "SportExpress\n\n"
            for news in self.sportexpress.parse():
                msg += f"🏊‍♂🏊‍♀{news['title']} {news['url']}\n\n"
            self.vk.messages.send(
                message=msg,
                peer_id=user_id,
                random_id=get_random_id()
            )
    def All_news_Sport_Express(self, user_id):
            msg = "All_news_Sport_Express\n\n"
            msg += self.vk.messages.send(
                message='https://www.sport-express.ru/swimming/',
                peer_id=user_id,
                random_id=get_random_id()
            )
    def AllRussian_Swimming_Federation(self, user_id):
            msg = "All-Russian Swimming Federation\n\n"
            msg += self.vk.messages.send(
                message='https://russwimming.ru/',
                peer_id=user_id,
                random_id=get_random_id()
            )
