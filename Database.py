import Constants

Customer_tbl = [] #name,prv_out_standing, payments_recvd, outstd_bal, old_points, points_added, new_points
Payments_tbl = [] #name, date, amount
Trans_tbl = []  #name, trans_id, date, amount,trans_type

def create(tbl,record):
    pass

def update(tbl,record):
    found = False
    if tbl == Constants.CUSTOMER_TBL:
        if len(Customer_tbl) > 0:

            for i in range(len(Customer_tbl)):

                if Customer_tbl[i][Constants.C_NAME] == record[Constants.C_NAME]:
                    Customer_tbl[i]= record
                    found = True
                    break

        if found == False:
             Customer_tbl.append(record)

    elif tbl == Constants.TRANS_TBL:
        Trans_tbl.append(record)
    elif tbl == Constants.PAYMENTS_TBL:
        Payments_tbl.append(record)



def read(tbl,record):

    target_tbl = []
    if tbl == Constants.CUSTOMER_TBL:
        target_tbl = Customer_tbl
    elif tbl == Constants.TRANS_TBL:
        target_tbl  = Trans_tbl
    elif tbl == Constants.PAYMENTS_TBL:
        target_tbl  =  Payments_tbl

    for i in range(len(target_tbl)):
            if target_tbl[i][Constants.C_NAME] == record:
                return target_tbl[i]

    return []


def delete(tbl,record):
    pass
def printTable(tbl):
    target_tbl = [[]]
    if tbl == Constants.CUSTOMER_TBL:
        target_tbl = Customer_tbl
        Out_put= ["Customer name","Previous outstanding", "Payment recieved", "Outstanding balance",
                  "Previous points", "Points added", "New points"]
        for i in range(len(Customer_tbl)):

            Customer_tbl[i][Constants.C_NEW_POINTS] = Customer_tbl[i][Constants.C_PRV_POINTS]+Customer_tbl[i][Constants.C_POINT_ADDED]
            Customer_tbl[i][Constants.C_BAL] = Customer_tbl[i][Constants.C_PRV_OUT_STD] - Customer_tbl[i][Constants.C_PYT_RCD]
            print(list(zip(Out_put,Customer_tbl[i])))
            Customer_tbl[i][Constants.C_PRV_POINTS] = Customer_tbl[i][Constants.C_NEW_POINTS]
            Customer_tbl[i][Constants.C_POINT_ADDED] = 0
            Customer_tbl[i][Constants.C_PRV_OUT_STD] = Customer_tbl[i][Constants.C_BAL]
            Customer_tbl[i][Constants.C_PYT_RCD] = 0
        return
    elif tbl == Constants.TRANS_TBL:
        target_tbl = Trans_tbl
    elif tbl == Constants.PAYMENTS_TBL:
        target_tbl = Payments_tbl

    print(target_tbl)