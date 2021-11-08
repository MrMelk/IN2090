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

    #Make a cursor object to perform SQL ask
    cur = conn.cursor()
    cur.execute("INSERT INTO ws.users(name, username, password, adress) VALUES (%s, %s, %s, %s);",
                (name, username, password, adress))
    conn.commit()
    print("New user " + username + "added!")
    return



def login(conn):
    print("-- LOGIN USER --")
    username = input("Username: ")
    password = input("Password: ")
    cur = conn.cursor()
    cur.execute("SELECT username, name FROM ws.user WHERE username = %s AND password = %s;",
                (username, password))
    rows = cur.fetchall()   #list of tuples from our SQL execution
    if (rows == []):
        print("Incorrect username or password")
        return ""
    else:
        row = rows[0]
        print("Welcome to the thunderdome, ", row[1])
        return row[0]


def search(conn, username):
    # GJØR UKESOPPGAVEN SOM IMPLEMENTERER SORTERING OG
    # LIMIT VED SØKENE :D Fjern denne etterpå
    print("-- SEARCH --")
    name = input("Search: ")
    category = input("Category: ")

    q = "SELECT p.pid, p.name, p.price, c.name AS category, p.description " + \
        "FROM ws.products AS p INNER JOIN categories AS c USING (cid) " + \
        "WHERE p.name LIKE %(name)s"

    if category != "":
        q += " AND c.name = %(category)s"

    q += ";"

    cur = conn.cursor()
    cur.execute(q, {'name' :"%" + name + "%",
                    'category' : category})
    rows = cur.fetchall()   #List of tuples from our SQL execution

    if rows == []:
        print("No results found.")
        return

    print(" -- Results --\n ")

    for row in rows:
        print("=== "+ row[1] + " ===\n"+\
              "Product ID: " + str(row[0]) + "\n"+\
              "Price: "+ str(row[2]) + "\n"+\
              "Category: " + row[3]+  "\n")
        if row[4] != "NULL":
            print("Description: " + row[4])

        print("\n")


    return


def order_products(conn, username, product):
    #UKESOPPGAVE
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
