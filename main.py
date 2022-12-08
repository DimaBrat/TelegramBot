#Бот с музыкой, фильмами и книгами
import telebot
import time
import config
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_films = types.KeyboardButton(text='Фильмы')
    button_music = types.KeyboardButton(text='Музыка')
    button_books = types.KeyboardButton(text='Книги')
    markup.add(button_films, button_music, button_books)
    bot.send_message(message.chat.id, 'Привет! Меня зовут [ИМЯ]. Я бот, который облегчит тебе жизнь в плане подготовки к путешествию. Всем людям лень скачивать в дорогу музыку, кино и тому подобное и я создан, чтобы помочь с этим. Выбери то, что тебе нужно, и я покажу тебе, что у меня есть.', reply_markup=markup)



@bot.message_handler(func=lambda m: m.text == 'Фильмы')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Комедии')
    button2 = types.KeyboardButton(text='Боевики')
    button3 = types.KeyboardButton(text='Драмы')
    button4 = types.KeyboardButton(text='Мультфильмы')
    button5 = types.KeyboardButton(text='Криминал')
    button6 = types.KeyboardButton(text='Фантастика')
    button7 = types.KeyboardButton(text='Назад')
    markup.add(button1, button2, button3, button4, button5, button6, button7)
    bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Комедии')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Большой Лебовски')
    button2 = types.KeyboardButton(text='Майор Пэйн')
    button3 = types.KeyboardButton(text='Вернуться к жанрам фильмов')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери фильм!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Боевики')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Агенты А.Н.К.Л.')
    button2 = types.KeyboardButton(text='Форсаж')
    button3 = types.KeyboardButton(text='Вернуться к жанрам фильмов')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери фильм!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Драмы')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Побег из Шоушенка')
    button2 = types.KeyboardButton(text='Хатико: Самый верный друг')
    button3 = types.KeyboardButton(text='Вернуться к жанрам фильмов')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери фильм!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Мультфильмы')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='История игрушек')
    button2 = types.KeyboardButton(text='Король Лев')
    button3 = types.KeyboardButton(text='Вернуться к жанрам фильмов')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери фильм!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Криминал')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Легенда')
    button2 = types.KeyboardButton(text='Криминальное чтиво')
    button3 = types.KeyboardButton(text='Вернуться к жанрам фильмов')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери фильм!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Фантастика')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Начало')
    button2 = types.KeyboardButton(text='Матрица')
    button3 = types.KeyboardButton(text='Вернуться к жанрам фильмов')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери фильм!', reply_markup=markup)



@bot.message_handler(func=lambda m: m.text == 'Музыка')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Рок')
    button2 = types.KeyboardButton(text='Рэп и Хип-хоп')
    button3 = types.KeyboardButton(text='Инди')
    button4 = types.KeyboardButton(text='Ретро')
    button5 = types.KeyboardButton(text='Джаз')
    button6 = types.KeyboardButton(text='Спокойная музыка')
    button7 = types.KeyboardButton(text='Советская музыка')
    button8 = types.KeyboardButton(text='Музыка из любимых фильмов')
    button9 = types.KeyboardButton(text='Назад')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Рок')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Русский рок')
    button2 = types.KeyboardButton(text='Зарубежный рок')
    button3 = types.KeyboardButton(text='Вернуться к музыкальным жанрам')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери поджанр!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Рэп и Хип-хоп')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Подборка русских песен')
    button2 = types.KeyboardButton(text='Подборка зарубежных песен')
    button3 = types.KeyboardButton(text='Вернуться к музыкальным жанрам')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери поджанр!', reply_markup=markup)



@bot.message_handler(func=lambda m: m.text == 'Книги')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Фантастические романы')
    button2 = types.KeyboardButton(text='Детектив')
    button3 = types.KeyboardButton(text='История')
    button4 = types.KeyboardButton(text='Научная литература')
    button5 = types.KeyboardButton(text='Романы')
    button6 = types.KeyboardButton(text='Приключения')
    button7 = types.KeyboardButton(text='Назад')
    markup.add(button1, button2, button3, button4, button5, button6, button7)
    bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Фантастические романы')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Ведьмак')
    button2 = types.KeyboardButton(text='2001: Космическая одиссея')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Детектив')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Мальтийский сокол')
    button2 = types.KeyboardButton(text='Азазель')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'История')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Освенцим. Нацисты и "окончательное решение еврейского вопроса"')
    button2 = types.KeyboardButton(text='История Российского государства')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Научная литература')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Пандемия: Всемирная история смертельных вирусов')
    button2 = types.KeyboardButton(text='Космос')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Романы')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Метро 2033')
    button2 = types.KeyboardButton(text='Пикник на обочине')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Приключения')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Остров сокровищ')
    button2 = types.KeyboardButton(text='Путешествие к центру Земли')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def send(message):
    if message.text == 'Большой Лебовски':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Майор Пэйн':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Агенты А.Н.К.Л.':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Форсаж':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Побег из Шоушенка':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Хатико: Самый верный друг':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'История игрушек':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Король Лев':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Легенда':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Криминальное чтиво':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Начало':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Матрица':
        bot.send_video(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Films\\File.mp4", 'rb'))

    elif message.text == 'Русский рок':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Зарубежный рок':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Подборка русских песен':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Подборка зарубежных песен':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Инди':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Ретро':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Джаз':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Спокойная музыка':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Советская музыка':
        bot.send_audio(message.chat.id,(open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Музыка из любимых фильмов':
        bot.send_audio(message.chat.id, (open("C:\\Users\\dimai\\PycharmProjects\\TelegarmBot\\Music\\Audio.mp3", 'rb')))

    elif message.text == 'Ведьмак':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == '2001: Космическая одиссея':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Освенцим. Нацисты и "окончательное решение еврейского вопроса"':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'История Российского государства':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Мальтийский сокол':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Азазель':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Пандемия: Всемирная история смертельных вирусов':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Космос':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Остров сокровищ':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Путешествие к центру Земли':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Метро 2033':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Пикник на обочине':
        bot.send_document(message.chat.id, open("C:\\Users\\dimai\\PycharmProjects\\Telegarm\\Books\\Book.pdf", 'rb'))

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_films = types.KeyboardButton(text='Фильмы')
        button_music = types.KeyboardButton(text='Музыка')
        button_books = types.KeyboardButton(text='Книги')
        markup.add(button_films, button_music, button_books)
        bot.send_message(message.chat.id, 'Выбирай!', reply_markup=markup)

    elif message.text == 'Вернуться к жанрам фильмов':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton(text='Комедии')
        button2 = types.KeyboardButton(text='Боевики')
        button3 = types.KeyboardButton(text='Драмы')
        button4 = types.KeyboardButton(text='Мультфильмы')
        button5 = types.KeyboardButton(text='Криминал')
        button6 = types.KeyboardButton(text='Фантастика')
        button7 = types.KeyboardButton(text='Назад')
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

    elif message.text == 'Вернуться к музыкальным жанрам':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton(text='Рок')
        button2 = types.KeyboardButton(text='Рэп и Хип-хоп')
        button3 = types.KeyboardButton(text='Инди')
        button4 = types.KeyboardButton(text='Ретро')
        button5 = types.KeyboardButton(text='Джаз')
        button6 = types.KeyboardButton(text='Спокойная музыка')
        button7 = types.KeyboardButton(text='Советская музыка')
        button8 = types.KeyboardButton(text='Музыка из любимых фильмов')
        button9 = types.KeyboardButton(text='Назад')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
        bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

    elif message.text == 'Вернуться к жанрам книг':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton(text='Фантастические романы')
        button2 = types.KeyboardButton(text='Детектив')
        button3 = types.KeyboardButton(text='История')
        button4 = types.KeyboardButton(text='Научная литература')
        button5 = types.KeyboardButton(text='Романы')
        button6 = types.KeyboardButton(text='Приключения')
        button7 = types.KeyboardButton(text='Назад')
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Я такой команды не знаю!')

if __name__ == '__main__':
    bot.polling()