import mysql.connector
from mysql.connector import Error

def create(id,fname,lname,gender,phno,address,adharNo,adharStatus,panCardNo):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            statement = "Insert into karamdb.person"
            colNames = "(person_id, first_name, last_name, gender, phone_number, address,adhar_card_number,adhar_card_status,pan_card)"
            colValues = "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            sql = statement+colNames+colValues

            val = (id,fname,lname,gender,phno,address,adharNo,adharStatus,panCardNo)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def deleteById(id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "delete from karamdb.person where person_id = %s"
            val = (id,)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def updateFirstName(firstName, id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "update karamdb.person set first_name = %s where person_id = %s"
            val = (firstName,id,)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def updateLastName(lastName, id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "update karamdb.person set last_name = %s where person_id = %s"
            val = (lastName,id,)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def updatePhoneNumber(phoneNumber, id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "update karamdb.person set phone_number = %s where person_id = %s"
            val = (phoneNumber, id,)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def updateAddress(address, id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "update karamdb.person set ADDRESS = %s where person_id = %s"
            val = (address, id,)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def updatePanCard(panCard, id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "update karamdb.person set pan_card = %s where person_id = %s"
            val = (panCard, id,)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def updateAdharCardNumber(adharCardNumber, id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "update karamdb.person set adhar_card_number = %s where person_id = %s"
            val = (adharCardNumber, id,)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def updateAdharCardStatus(status, id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "update karamdb.person set adhar_card_status = %s where person_id = %s"
            val = (status, id,)
            cursor.execute(sql,val)
            connection.commit()
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def getAllPerson():
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "select * from karamdb.person"
            cursor.execute(sql);
            rec = cursor.fetchall()
            result = list()
            for x in rec:
                result.append(x)
            return result
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def getPersonById(id):
    try:
        connection = mysql.connector.connect(host='',
                                             database='',
                                             user='',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "select * from karamdb.person where person_id = %s"
            val = (id,)
            cursor.execute(sql,val)
            rec = cursor.fetchall()
            result = list()
            for x in rec:
                result.append(x)
            return result
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
