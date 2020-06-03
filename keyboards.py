from telebot import types
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardMarkup
from telebot.types import KeyboardButton
from telebot.types import InlineKeyboardButton
import qiwi


def start():
    k = ReplyKeyboardMarkup()
    k.add(KeyboardButton("Баланс"))
    k.add(KeyboardButton('Поиск прокси'))
    return k


def choose_country():
    k = types.InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text="CША", callback_data='usa'),InlineKeyboardButton(text="Америка", callback_data='america'))
    k.add(InlineKeyboardButton(text="Европа", callback_data='europe'),InlineKeyboardButton(text="Африка", callback_data='africa'))
    k.add(InlineKeyboardButton(text="Росия", callback_data='russia'),InlineKeyboardButton(text="Азия", callback_data='asia'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню",callback_data='mainmenu'))
    return k


def choose_type_ip():
    k = types.InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text="All", callback_data='all_ip'))
    k.add(InlineKeyboardButton(text="Residential", callback_data='residential'))
    k.add(InlineKeyboardButton(text="Datacenter/hosting", callback_data='datacenter/hosting'))
    k.add(InlineKeyboardButton(text="Windows", callback_data='windows'))
    k.add(InlineKeyboardButton(text="Android", callback_data='android'))
    k.add(InlineKeyboardButton(text="Router", callback_data='router'))
    k.add(InlineKeyboardButton(text="SSH", callback_data='ssh'))
    k.add(InlineKeyboardButton(text="Linux", callback_data='linux'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню",callback_data='mainmenu'))
    return k


def choose_blacklists():
    k = types.InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text="All", callback_data='all_blacklists'))
    k.add(InlineKeyboardButton(text="Clean", callback_data='clean'))
    k.add(InlineKeyboardButton(text="Extra Clean", callback_data='extra_clean'))
    k.add(InlineKeyboardButton(text="Black 50% OFF", callback_data='black_50_off'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню",callback_data='mainmenu'))
    return k

def choose_city():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text="All", callback_data='all_city'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню", callback_data='mainmenu'))
    return k

def choose_zip():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text="All", callback_data='all_zip'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню", callback_data='mainmenu'))
    return k

def choose_domain():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text="All", callback_data='all_domains'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню", callback_data='mainmenu'))
    return k

def choose_ip():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text="All", callback_data='all_domains'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню", callback_data='mainmenu'))
    return k
def btn_buy(price,id):
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text='Buy $'+str(price),callback_data='buy_'+str(id)+"_"+str(price)))
    return k
def start_move_menu():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text='➡',callback_data='next'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню", callback_data='mainmenu'))
    return k
def move_menu():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text='⬅',callback_data='prev'),InlineKeyboardButton(text='➡',callback_data='next'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню", callback_data='mainmenu'))
    return k
def end_move_menu():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text='⬅',callback_data='prev'))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню", callback_data='mainmenu'))
    return k

def account():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text='Пополнить', callback_data='donate'))
    k.add(InlineKeyboardButton(text="Закрить", callback_data='close'))
    return k

def donate(comment):
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text='QIWI', url=qiwi.get_link(comment),callback_data='refaund_'+comment))
    k.add(InlineKeyboardButton(text="Вернуться в главное меню", callback_data='mainmenu'))
    return k



def close_keyboard():
    k = types.ReplyKeyboardRemove()
    return k



