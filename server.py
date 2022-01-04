from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from parserSportBox import*

class Server:
    def __init__(self, longpoll, vk):
        self.__longpoll = longpoll
        self.vk = vk
        self.SportBox = SportBox('https://news.sportbox.ru/Vidy_sporta/plavanie')
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
        # keyboard.add_line()
        help_text = [f'👉 {value}: {self.commands[value]["description"]}' for number_iteration, value in enumerate(self.commands.keys())]
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
