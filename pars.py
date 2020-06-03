from anticaptchaofficial.imagecaptcha import *
import os
import time
from proxy import Proxy
from selenium import webdriver
import json


class Pars:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome('driwers/chromedriver.exe',options=options)

    def get_text_captcha(self,id):
        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key("733328582f6f354a75ad0b771a8ebca0")
        captcha_text = solver.solve_and_return_solution("img_captcha/img"+str(id)+".png")
        if captcha_text != 0:
            return captcha_text
        else:
            print("task finished with error " + solver.error_code)

    def buy(self,id_btn):
        self.driver.get('https://luxsocks.ru/socks/rent/'+id_btn)
        dict = json.loads(self.driver.find_element_by_xpath("//body").text.replace("\n",""))
        return dict.get('CART')[0].get('value')


    def login_page(self,id,url):
        self.driver.get(url)
        login = self.driver.find_element_by_name('LoginForm[username]')
        login.send_keys("Scarce11")
        while 1:
            password = self.driver.find_element_by_name('LoginForm[password]')
            password.send_keys('12345qwerty')
            time.sleep(5)
            img = self.driver.find_element_by_class_name('captcha-img')
            out = open("img_captcha/img"+str(id)+".png", "wb")
            out.write(img.screenshot_as_png)
            out.close()
            captcha = self.driver.find_element_by_name('LoginForm[captcha]')
            print('Send captcha')
            res = self.get_text_captcha(id)
            try:
                captcha.send_keys(res)
                btn = self.driver.find_element_by_name('yt0')
                btn.click()
                time.sleep(10)
                print(self.driver.find_element_by_xpath("//div[@id='socks-grid']/table/tbody/tr"))
                print("Loging")
                os.remove("img_captcha/img"+str(id)+".png")
                break
            except:
                print("Reply")
                os.remove("img_captcha/img"+str(id)+".png")
                time.sleep(3)

    def link_request(self,cont,socks_type_id = "all",blacklisted_search= "all",real_ip = 'all',domain = 'all',
                     city = 'all',zip_city = 'all'):
        url = "https://luxsocks.ru/"
        url += "?Socks%5Bcontinent%5D="+cont
        if socks_type_id != 'all':
            url += "&Socks%5Bsocks_type_id%5D="+ socks_type_id #Datacenter%2Fhosting
        if blacklisted_search != 'all':
            url +="&Socks%5Bblacklisted_search%5D="+ blacklisted_search #clean
        url += "&Socks%5BpageSize%5D=25"
        if real_ip != 'all':
            url += "&&Socks%5Bsock_real_ip%5D="+real_ip
        if domain != 'all':
            url += "&Socks%5Bdomain%5D="+domain
        if city != 'all':
            url += "&Socks%5Bcity%5D="+city
        if zip_city != 'all':
            url += "&Socks%5Bzip%5D="+zip_city
        url += "&Socks_sort=ping.desc&ajax=socks-grid"
        return url

    def select_list_proxy(self):
        res = []
        count = len(self.driver.find_elements_by_xpath("//div[@id='socks-grid']/table/tbody/tr"))
        if self.driver.find_element_by_xpath("//div[@id='socks-grid']/table/tbody/tr").text != 'No socks found by your query.':
            print(f'count: {count}')
            for r in range(1, count + 1):
                try:
                    ip = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 1]").text
                    domain = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 2]").text
                    city = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 3]").text
                    ips = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 4]").text
                    type = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 8]/div").get_attribute('title')
                    zip = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 5]").text
                    speed = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 6]").text
                    ping = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 7]").text
                    added = self.driver.find_element_by_xpath(
                        "//div[@id='socks-grid']/table/tbody/tr[position() = " + str(r) + "]/td[position() = 9]").text
                    price = self.driver.find_element_by_xpath("//tbody/tr[position () = "+str(r)+"]/td[position () = 12]/input").get_attribute('value')[1:]
                    id_btn = self.driver.find_element_by_xpath("//tbody/tr[position () = "+str(r)+"]/td[position () = 12]/input").get_attribute('id')[15:]
                    proxy = Proxy(ip,type ,domain, city, ips, zip, speed, ping, added, price,id_btn)
                    res.append(proxy)
                except:
                    print('EROOR add proxy')
            return res
        else:
            print('No socks found by your query')

