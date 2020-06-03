class Proxy:
    def __init__(self, ip,type, domain, city, ips, zip, speed, ping, added, price,id_btn):
        self.ip = ip
        self.id_btn = id_btn
        self.domain = domain
        self.city = city
        self.ips = ips
        self.type = type
        self.zip = zip
        self.speed = speed
        self.ping = ping
        self.added = added
        self.price = price

    def __str__(self):
        return f'{self.ip} {self.domain} {self.city} {self.type} {self.ips} {self.zip} {self.speed} {self.ping} {self.added} {self.id_btn} {self.price}'
