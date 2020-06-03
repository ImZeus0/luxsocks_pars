import telebot
import config
import keyboards
from pars import Pars
import db_connection
import qiwi

bot = telebot.TeleBot(config.TOKEN)

def check_user(users,id):
    for user in users:
        if user['id_user']==id:
            return True
        else:
            return False

@bot.message_handler(commands=['start'])
def start(m):
    conn = db_connection.connect()
    if check_user(db_connection.select_users(conn),m.chat.id):
        bot.send_message(m.chat.id, f'Привет <b>{m.from_user.username}</b>', parse_mode='HTML', reply_markup=keyboards.start())
    else:
        db_connection.reg_user(conn,m.chat.id,m.from_user.username)
        bot.send_message(m.chat.id,f'Регистрация прошла успешно \n1111Добро пожаловать <b>{m.from_user.username}</b>',parse_mode='HTML',reply_markup=keyboards.start())


@bot.callback_query_handler(func=lambda call: True)
def menu_callback(call):
    conn = db_connection.connect()
    if call.data == 'usa':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id
                              ,text="Вы выбрали США\nВыберете тип ip",
                              reply_markup=keyboards.choose_type_ip())
        db_connection.input_contry(conn,call.message.chat.id,"USA")
    elif call.data == 'europe':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id
                              ,text="Вы выбрали ЕВРОПА\nВыберете тип ip",
                              reply_markup=keyboards.choose_type_ip())
        db_connection.input_contry(conn, call.message.chat.id, "Europe")
    elif call.data == 'america':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали АМЕРИКА\nВыберете тип ip",
                              reply_markup=keyboards.choose_type_ip())
        db_connection.input_contry(conn, call.message.chat.id, "America")
    elif call.data == 'russia':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id
                              ,text="Вы выбрали РОССИЯ\nВыберете тип ip",
                              reply_markup=keyboards.choose_type_ip())
        db_connection.input_contry(conn, call.message.chat.id, "Russia")
    elif call.data == 'asia':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали АЗИЯ\nВыберете тип ip",
                              reply_markup=keyboards.choose_type_ip())
        db_connection.input_contry(conn, call.message.chat.id, "Asia")
    elif call.data == 'africa':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали АФРИКА\nВыберете тип ip",
                              reply_markup=keyboards.choose_type_ip())
        db_connection.input_contry(conn, call.message.chat.id, "Africa")
    elif call.data == 'all_ip':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали все IP\nВыберете тип Blacklists",
                              reply_markup=keyboards.choose_blacklists())
        db_connection.input_type_ip(conn, call.message.chat.id, 'all')
    elif call.data == 'residential':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Residential\nВыберете тип Blacklists",
                              reply_markup=keyboards.choose_blacklists())
        db_connection.input_type_ip(conn,call.message.chat.id,'Residential')
    elif call.data == 'datacenter/hosting':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Datacenter/hosting\nВыберете тип Blacklists",
                              reply_markup=keyboards.choose_blacklists())
        db_connection.input_type_ip(conn,call.message.chat.id,'Datacenter%2Fhosting')
    elif call.data == 'windows':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Windows\nВыберете тип Blacklists",
                              reply_markup=keyboards.choose_blacklists())
        db_connection.input_type_ip(conn,call.message.chat.id,'3')
    elif call.data == 'android':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Android\nВыберете тип Blacklists",
                              reply_markup=keyboards.choose_blacklists())
        db_connection.input_type_ip(conn,call.message.chat.id,'4')
    elif call.data == 'router':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Router\nВыберете тип Blacklists",
                              reply_markup=keyboards.choose_blacklists())
        db_connection.input_type_ip(conn,call.message.chat.id,'5')
    elif call.data == 'ssh':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали SSH\nВыберете тип Blacklists",
                              reply_markup=keyboards.choose_blacklists())
        db_connection.input_type_ip(conn,call.message.chat.id,'6')
    elif call.data == 'linux':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Linux\nВыберете тип Blacklists",
                              reply_markup=keyboards.choose_blacklists())
        db_connection.input_type_ip(conn,call.message.chat.id,'7')
    elif call.data == 'all_blacklists':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали все blacklists\nНапишите город на английском",
                              reply_markup=keyboards.choose_city())
        db_connection.input_type_blacklists(conn,call.message.chat.id,'all')
    elif call.data == 'clean':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Clean\nНапишите город на английском",
                              reply_markup=keyboards.choose_city())
        db_connection.input_type_blacklists(conn,call.message.chat.id,'1')
    elif call.data == 'extra_clean':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Extra Clean\nгород на английском",
                              reply_markup=keyboards.choose_city())
        db_connection.input_type_blacklists(conn,call.message.chat.id,'2')
    elif call.data == 'black_50_off':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали Black 50%\nгород на английском",
                              reply_markup=keyboards.choose_city())
        db_connection.input_type_blacklists(conn,call.message.chat.id,'3')
    elif call.data == 'all_city':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали все города\nНапишите zip",
                              reply_markup=keyboards.choose_zip())
        db_connection.input_city(conn, call.message.chat.id, 'all')
    elif call.data == 'all_zip':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Вы выбрали все zip")
        db_connection.input_zip(conn, call.message.chat.id, 'all')
        print_res(call.message.chat.id)
    elif call.data == 'donate':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Выберите тип оплаты",
                              reply_markup=keyboards.donate('first'))
    elif call.data.startswith('refaund'):
        comment = call.data.split('_')[1]
        if qiwi.check_pay(comment,call.message.chat.id):
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="Операция прошла успешно")
    elif call.data.startswith('buy'):
        arg = call.data.split('_')
        c = db_connection.connect()
        if db_connection.reduce_funds(c,call.message.chat.id,float(arg[2])):
            buy_proxy(call.message.chat.id,arg[1])
        else:
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="Недостаточно средств",
                                  reply_markup=keyboards.start())
    elif call.data == 'mainmenu':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="В главное меню")
        bot.send_message(call.message.chat.id,'<',reply_markup=keyboards.start())
        db_connection.delete_request(conn,call.message.chat.id)
    else:
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Не верная команда")
        db_connection.delete_request(conn, call.message.chat.id)
    conn.close()

@bot.message_handler(regexp=r'[a-z]+')
def choose_city(m):
    conn = db_connection.connect()
    db_connection.input_city(conn,m.chat.id,m.text.strip())
    conn.close()
    bot.send_message(m.chat.id,"Вы ввели "+m.text+"\nВведите ZIP",reply_markup=keyboards.choose_zip())


@bot.message_handler(regexp=r'\d+')
def choose_zip(m):
    if len(m.text) == 5:
        conn = db_connection.connect()
        db_connection.input_zip(conn,m.chat.id,m.text.strip())
        conn.close()
        bot.send_message(m.chat.id,"Вы ввели ZIP: "+m.text)
        print_res(m.chat.id)

    else:
        bot.send_message(m.chat.id, "Вы не правильно ввели ZIP, попробуйте еще раз")


@bot.message_handler(content_types=['text'])
def mainmenu(m):
    if m.text == 'Поиск прокси':
        bot.send_message(m.chat.id, 'OK', reply_markup=keyboards.close_keyboard())
        bot.send_message(m.chat.id,'Выберите континент',reply_markup=keyboards.choose_country())
    elif m.text == 'Баланс':
        conn = db_connection.connect()
        balance = db_connection.get_balanse(db_connection.get_user_dict_balanse(conn,m.chat.id))
        conn.close()
        bot.send_message(m.chat.id,"➖➖➖➖➖➖➖➖➖➖\n"
                                   "👨🏻‍💻 <b>Вaш ID</b> "+str(m.chat.id)+"\n"
                                    "💰 <b>Ваш баланс</b> "+str(balance)+"\n"
                                    "➖➖➖➖➖➖➖➖➖➖",parse_mode='HTML',reply_markup=keyboards.account())
    else:
        bot.send_message(m.chat.id, 'Неверная команда', reply_markup=keyboards.start())

def seach_proxy(id):
    conn = db_connection.connect()
    params = db_connection.select_request(conn,id)
    res = 0
    for r in params:
        if r['id_user'] == id:
            res = r
    driver = Pars()
    driver.login_page(id,driver.link_request(cont = res['contry'],
                                             socks_type_id=res['type_ip'],
                                             blacklisted_search=res['type_blacklists'],
                                             city=res['city'],
                                             zip_city=res['zip']))
    res = driver.select_list_proxy()
    driver.driver.close()
    return res

def buy_proxy(id,id_btn):
    d = Pars()
    d.login_page(id, 'https://luxsocks.ru')
    proxy = d.buy(id_btn)
    d.driver.close()
    bot.send_message(id,proxy,reply_markup=keyboards.start())

def create_proxy_msg(proxy,id):
    msg = f'<b>IP</b> {proxy.ip}\n<b>DOMAIN</b> {proxy.domain}' \
          f'\n<b>TYPE</b>{proxy.type}\n<b>CITY</b> {proxy.city}' \
          f'\n<b>ZIP</b> {proxy.zip}\n<b>PING</b> {proxy.ping}'
    bot.send_message(id,msg,parse_mode='HTML',reply_markup=keyboards.btn_buy(proxy.price,proxy.id_btn))

"""
def start_page_proxy(list_proxy,page,id):
    for i in range(page*5,page*5+5):
        create_proxy_msg(list_proxy[i],id)
    if page == 0:
        bot.send_message(id,'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖',reply_markup=keyboards.start_move_menu())
    elif page == math.ceil(len(list_proxy)/5):
        bot.send_message(id, '➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖', reply_markup=keyboards.end_move_menu())
    else:
        bot.send_message(id, '➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖', reply_markup=keyboards.move_menu())

def edit_page_proxy(list_proxy,page,id,id_m):
    for i in range(page*5,page*5+5):
        count = i - page*5+5
        bot.edit_message_text(edit_msg(list_proxy[i]),id,id_m-count)
    if page == 0:
        bot.send_message(id,'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖',reply_markup=keyboards.start_move_menu())
    elif page == math.ceil(len(list_proxy)/5):
        bot.send_message(id, '➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖', reply_markup=keyboards.end_move_menu())
    else:
        bot.send_message(id, '➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖', reply_markup=keyboards.move_menu())
"""
def send_proxy(list_proxy,id):
    if list_proxy != None:
        if len(list_proxy) >= 10:
            for i in range(10):
                create_proxy_msg(list_proxy[i],id)
        else:
            for i in range(len(list_proxy)):
                create_proxy_msg(list_proxy[i], id)
        bot.send_message(id, '➖➖➖➖➖➖➖➖➖', reply_markup=keyboards.start())
        conn = db_connection.connect()
        db_connection.delete_request(conn, id)
    else:
        bot.send_message(id, 'Нет результатов по запросу', reply_markup=keyboards.start())
        conn = db_connection.connect()
        db_connection.delete_request(conn,id)


def print_res(id):
    proxys = seach_proxy(id)
    send_proxy(proxys,id)

bot.polling()