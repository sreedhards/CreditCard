import Transactions
import Payments
import Customers
import Database as db
import Constants

#name,prv_out_standing, payments_recvd, outstd_bal, old_points, points_added, new_points
Customers_test_data = [["Jhon",30000,0,30000,100,0,100],
                       ["Ram",50000,0,50000,200,0,200],
                       ["Raj",450000,0,450000,600,0,600],
                       ["Ian",26000,0,26000,400,0,400],
                       ["Sachin",110000,0,110000,500,0,500]]

#name, date, amount
Payments_data = [["Jhon","10-06-2016",1000],
                 ["Jhon","10-07-2016",2000],
                 ["Jhon","10-09-2016",10000],
                 ["Ram","10-11-2016",11200],
                 ["Ram","10-12-2016",5000]]
#name, trans_id, date, amount,trans_type
Transactions_data = [["Jhon",112,"1-06-2016",5000,Constants.TRANS_SCHD],
                     ["Jhon",113,"2-06-2016",3000,Constants.TRANS_SWIPE],
                     ["Jhon",114,"3-06-2016",4000,Constants.TRANS_ONLINE],
                     ["Ram",1,"1-06-2016",5000,Constants.TRANS_ONLINE],
                     ["Ram",2,"2-06-2016",7000,Constants.TRANS_SWIPE]]



def main():
    print("Hello World!")
    for row in Customers_test_data:
    #    print(row)
        Customers.AddCustomer(row)
    #db.printTable(Constants.CUSTOMER_TBL)

    for row in Transactions_data:
        print("Transaction:", row)
        Transactions.ProcessTrans(row)
    #db.printTable(Constants.TRANS_TBL)
    #db.printTable(Constants.CUSTOMER_TBL)

    for row in Payments_data:
        print("Payment : ", row)
        Payments.ProcessPayments(row)
    #db.printTable(Constants.TRANS_TBL)
    #db.printTable(Constants.PAYMENTS_TBL)
    #db.printTable(Constants.CUSTOMER_TBL)
    Customers.generateStatment();

    for row in Transactions_data:
        print("Transaction:",row)
        Transactions.ProcessTrans(row)
    #db.printTable(Constants.TRANS_TBL)
    #db.printTable(Constants.CUSTOMER_TBL)

    for row in Payments_data:
        print("Payment : ", row)
        Payments.ProcessPayments(row)
    #db.printTable(Constants.TRANS_TBL)
    #db.printTable(Constants.PAYMENTS_TBL)
    #db.printTable(Constants.CUSTOMER_TBL)
    Customers.generateStatment();


if __name__ == "__main__":
    main()