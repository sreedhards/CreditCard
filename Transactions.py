import Database as db
import Constants

def calcPoints(amount,type):
    p = (amount//1000)
    bonus_points = 0
    if type  == Constants.TRANS_ONLINE:
        bonus_points = p*2
    elif type  == Constants.TRANS_SCHD:
        bonus_points = p*3

    return (p*5 + bonus_points)

#name, trans_id, date, amount,trans_type
def ProcessTrans(data):
    db.update(Constants.TRANS_TBL,data)
    #print(data)
    cust_rec = db.read(Constants.CUSTOMER_TBL,data[Constants.T_NAME])
    #print(cust_rec)
    points = calcPoints(data[Constants.T_AMOUNT],data[Constants.T_TYPE])
    cust_rec[Constants.C_POINT_ADDED] += points;
    #cust_rec[Constants.C_NEW_POINTS] += points;
    #cust_rec[Constants.C_PRV_POINTS] += points;
    cust_rec[Constants.C_PRV_OUT_STD] = cust_rec[Constants.C_PRV_OUT_STD] + data[Constants.T_AMOUNT]

    db.update(Constants.CUSTOMER_TBL,cust_rec)
