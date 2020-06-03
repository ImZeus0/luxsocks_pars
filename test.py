import telebot
import config
import keyboards
from selenium import webdriver
from pars import Pars
import db_connection
import math
from pars import Pars
from time import sleep
#https://luxsocks.ru/socks/displaymodal/4313952
driwer = Pars()
driwer.login_page(777,'https://luxsocks.ru')
driwer.display_page('4313952')
