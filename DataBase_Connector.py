from mysql.connector import connect,Error


def db_creating(db_name):
    try:
        with connect(host="localhost",user="root",password="Soheil0014") as db:
            myCursor=db.cursor()

            myCursor.execute("create database "+str(db_name))
            db.commit()

    except Error as error:
        print(error)
        db.rollback()
        db.close()
    else:
        print(f"'{db_name}' has been created successfully")



def db_table(db_name,command):
    try:
        with connect(host="localhost",user="root",password="Soheil0014",database=str(db_name)) as db:
            myCursor=db.cursor()

            myCursor.execute("SET time_zone = '+03:30'")
            myCursor.execute(command)
            db.commit()

    except Error as error:
        print(error)
        db.rollback()
        db.close()
    else:
        print(f"Input command has been ran successfully")



def update_by_id(db_name,db_table,name_value,value,id):
    try:
        with connect(host="localhost",user="root",password="Soheil0014",database=str(db_name)) as db:
            myCursor=db.cursor()

            myCursor.execute(f"Update {db_table} set {name_value}={value} where ID={id}")

    except Error as error:
        print(error)
        db.rollback()
        db.close()
    else:
        print(f"'{name_value}' was updated to {value}")



def deleting_record(db_name,db_table,id):

    try:
        with connect(host="localhost",user="root",password="Soheil0014",database=str(db_name)) as db:
            myCursor=db.cursor()
            
            
            myCursor.execute(f"Delete from {db_table} where ID={id}")
            db.commit()

    except Error as error:
        print(error)
        db.rollback()
        db.close()
    else:
        print(f"ID: '{id}' was deleted successfully")



def search_by_id(db_name,db_table,id):
    try:
        with connect(host="localhost",user="root",password="Soheil0014",database=str(db_name)) as db:
            myCursor=db.cursor()

            myCursor.execute(f"Select * from {db_table} where id={id}")
            result=myCursor.fetchall()
            print(result)
 
    except Error as error:
        print(error)
        db.rollback()
        db.close()


def showing_records(db_name,db_table):
    try:
        with connect(host="localhost",user="root",password="Soheil0014",database=str(db_name)) as db:
            myCursor=db.cursor()

            myCursor.execute("Select * from "+str(db_table))
            result=myCursor.fetchall()
            for value in result:
                print(value)
            

    except Error as error:
        print(error)
        db.rollback()
        db.close()