import psycopg2

dbname = "atslotte"
username = "atslotte_priv"
password = "eeje0Aebie"

connection = "host='dbpg-ifi-kurs01.uio.no' " + \
    "dbname='" + dbname + "' " + \
    "user='" + username + "' " + \
    "password='" + password + "' " +\
    "port='5432'"

def frontend():
    conn = psycopg2.connect(connection)
    ch = 0
    username = ""
    while username == "":
        print("-- USER FRONTEND --")
        print("Please choose an option:\n 1. register\n "
              "2. Login\n 3. Exit:")
        ch = get_int_from_user("option: ", True)

        if ch == 1:
            register(conn)  # Register new user
        elif ch == 2:
            username = login(conn)  # Login with existing user
        elif ch == 3:
            return  # Exit program
    # Once logged in, can now search for products
    search(conn, username)


def register(conn):
    tf = False  #for registration later on
    #put a while tf = False
    print("-- REGISTER USER --")
    username = input("Username: ")
    password = input("Password: ")
    #Make a repeat password test
    #if repeated password not correct redo register
    name = input("Name: ")
    adress = input("Adress: ")
    return



def login(conn):
    return ""


def search(conn, username):
    return


def order_products(conn, username, product):
    return


def get_int_from_user(msg, needed):
    while True:
        numStr = input(msg)
        if (numStr == "" and not needed):
            return None;
        try:
            return int(numStr)
        except:
            print("Please provide an integer or leave blank.");


frontend()
