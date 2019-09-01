import Database as db
import Constants

def ProcessPayments(data):
    db.update(Constants.PAYMENTS_TBL,data)
    cust_rec = db.read(Constants.CUSTOMER_TBL,data[Constants.P_NAME])
    cust_rec[Constants.C_PYT_RCD] += data[Constants.P_AMOUNT]
    #cust_rec[Constants.C_BAL] = cust_rec[Constants.C_PRV_OUT_STD] - data[Constants.P_AMOUNT]
    #cust_rec[Constants.C_PRV_OUT_STD] = cust_rec[Constants.C_PRV_OUT_STD] - data[Constants.P_AMOUNT]
    db.update(Constants.CUSTOMER_TBL, cust_rec)