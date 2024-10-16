#1
def counter_closure():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter = counter_closure()
print(counter())
print(counter())
print(counter())
#2
def multiplier_closure(factor):
    def multiply(number):
        return number * factor
    return multiply
times_three = multiplier_closure(3)
result = times_three(5)
print(result)
#3
def sum_closure():
    total = 0
    def add_number(num):
        nonlocal total
        total += num
        return total
    return add_number
sum_tracker = sum_closure()
print(sum_tracker(5))
print(sum_tracker(10))
print(sum_tracker(3))
#4
def create_adder(x):
    def adder(y):
        return x + y
    return adder
def create_subtractor(x):
    def subtractor(y):
        return x - y
    return subtractor
add_five = create_adder(5)
subtract_three = create_subtractor(3)
print(add_five(10))
print(subtract_three(10))
#5
def discount_calculator(discount_percentage):
    def apply_discount(price):
        discount_amount = price * (discount_percentage / 100)
        new_price = price - discount_amount
        return new_price
    return apply_discount
ten_percent_discount = discount_calculator(10)
new_price = ten_percent_discount(100)
print(f"New price after discount: {new_price}")
#6
from datetime import datetime

def create_login_tracker():
    login_count = 0
    login_times = []
    def login():
        nonlocal login_count
        login_count += 1
        login_times.append(datetime.now())
        return login_count, login_times

    return login
tracker = create_login_tracker()
print(tracker())
print(tracker())
#7
def create_password_checker(correct_password):
    def check_password(user_password):
        if user_password == correct_password:
            return "to'g'ri"
        else:
            return "noto'g'ri"
    return check_password
correct_password = "my_secret"
password_checker = create_password_checker(correct_password)
print(password_checker("my_secret"))
print(password_checker("wrong_password"))
#8
'''
botsilka:t.me/Userstodo_bot
'''
import telebot
from telebot import types

API_TOKEN = '7902653676:AAFmpDRgFrG3Nm5Muelx6SrudedEdGS6OIs'
bot = telebot.TeleBot(API_TOKEN)

user_plans = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    add_plan_btn = types.KeyboardButton('Reja qo\'shish')
    view_plan_btn = types.KeyboardButton('Rejani ko\'rish')
    markup.add(add_plan_btn, view_plan_btn)
    bot.send_message(message.chat.id, "Salom! Nima qilishni xohlaysiz?", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id

    if message.text == 'Reja qo\'shish':
        msg = bot.send_message(chat_id, "Rejangizni kiriting:")
        bot.register_next_step_handler(msg, add_plan)
    elif message.text == 'Rejani ko\'rish':
        plans = user_plans.get(chat_id, [])
        if plans:
            bot.send_message(chat_id, "\n".join(plans))
        else:
            bot.send_message(chat_id, "Sizda hech qanday reja yo'q.")
    else:
        bot.send_message(chat_id, "Iltimos, tugmalardan birini tanlang.")

def add_plan(message):
    chat_id = message.chat.id
    plan = message.text
    if chat_id not in user_plans:
        user_plans[chat_id] = []
    user_plans[chat_id].append(plan)
    bot.send_message(chat_id, "Reja qo'shildi!")

bot.polling()