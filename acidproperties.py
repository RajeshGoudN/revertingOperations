import mysql.connector
import logging

db_config = {
    "host":"localhost",
    "port":"3306",
    "user":"root",
    "password":"Rajesh",
    "database":"bankA"
}

log_file_path =r"C:\Users\Rajesh Goud\OneDrive\Desktop\Final_projects\sql-1stDay\mysql_connection.log"

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def transfer_funds(sender_id,reciever_id,amount):
    try:
        connector=mysql.connector.connect(**db_config)
        if connector.is_connected():
            logging.info("successfully connected")
        cursor=connector.cursor()
        connector.start_transaction()
        cursor.execute("select balane from account where ID = %s",(sender_id,))
        rows=cursor.fetchone()
        sender_amount=rows[0]
        if sender_amount>=amount:
            cursor.execute("update account set balane=balane-%s where ID = %s",(amount,sender_id))
        connector.commit()
    except Exception as E:
        print(E)
        logging.error(E)

if __name__ == "__main__":
    transfer_funds(sender_id="1",reciever_id="2",amount=100)
