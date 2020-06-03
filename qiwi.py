import pyqiwi
import config
import db_connection

def get_link(comment):
    return pyqiwi.generate_form_link(pid='99', account=config.qiwi_NUBMER,amount=2.0, comment=comment)

def check_pay(comment,id):
    wallet = pyqiwi.Wallet(token=config.qiwi_TOKEN, number=config.qiwi_NUBMER)
    trans = wallet.history(5)
    for t in trans['transactions']:
        if t.comment == comment and t.type == "IN" and t.status == "SUCCESS":
            c = db_connection.connect()
            db_connection.add_funds(c,id,float(t.sum.amount))
            return True


