import telebot

bot = telebot.TeleBot("6310861018:AAEsFQjGMhAJH1OnQum-AO1JwKi_5SIbQ9w")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Готовлю колы!")

@bot.message_handler(content_types=["text"])
def echo_message(message):
    try:
        if message.text == 'На хуй' or message.text.lower() == 'Посадить на хуй':
            bot.send_message(message.chat.id, 'Себя нахуй посади')
        if message.text == "Посадить на кол" or message.text.lower() == "На кол":
            reply_user_id = message.reply_to_message.from_user.id
            reply_user_name = message.reply_to_message.from_user.username

            if reply_user_name == "Indra_0000":
                bot.send_message(message.chat.id, 'Индру на кол нельзя!!!')
            elif reply_user_name == "zarinsiki":
                bot.send_message(message.chat.id, "Любимую Каночку нельзя!!!!")

            elif reply_user_name == None:
                bot.send_message(message.chat.id, f"@{message.reply_to_message.from_user.first_name} был посажен на кол @{message.from_user.username}")
            else:
                bot.send_message(message.chat.id, f"@{reply_user_name} был посажен на кол @{message.from_user.username}")
    except:
        bot.send_message(message.chat.id, "Ответь на сооб, гений")


bot.polling()
