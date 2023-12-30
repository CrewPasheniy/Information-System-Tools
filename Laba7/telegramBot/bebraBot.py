import telebot

botTimeWeb = telebot.TeleBot('6686144516:AAEdxGNE1QfpLbMI62os27v3VqhXxkj9K6s')

from telebot import types

@botTimeWeb.message_handler(commands=['start']) #Объявляется метод обработки входящих сообщений реализуемый через параметр команды /start
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nТы обучаешься в группе БИСЗ20-01?" #Вывод имени и фамилии пользователя, и приветственного сообщения
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes') #Создание кнопки. Кнопка будет отображаться под сообщением
  markup.add(button_yes)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True) #Выполняется проверка на соответствие строки, указанной после == и возвращенной после нажатия кнопки. Так как ранее мы указали значение параметра callback_data = 'yes', то проверка пройдет успешно. 
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Прекрасно! Если ты хочешь быть в курсе того что нам задали на эту сессиию, или ты хочешь посмотреть расписаие пар, то переходи в нашу группу в ВК!" #Переменная second_mess хранит текст ответного сообщения. А далее описана реализация кнопки, которая хранит ссылку на группу в вк.
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Добро пожаловать в семью", url="https://vk.com/club209208622"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id) #Обработка команды закончена

botTimeWeb.infinity_polling() #Строчка отвечает за непрерывное продолжение работы бота