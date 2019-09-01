import Database as db
import Constants


def AddCustomer(data):
    db.update(Constants.CUSTOMER_TBL,data)

def generateStatment():
    db.printTable(Constants.CUSTOMER_TBL)