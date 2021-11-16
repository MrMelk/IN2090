import psycopg2

# MERK: Må kjøres med Python 3!

# Login details for database user
dbname = "atslotte" #Set in your UiO-username
user = "atslotte_priv" # Set in your priv-user (UiO-username + _priv)
pwd = "eeje0Aebie" # Set inn the password for the _priv-user you got in a mail

# Gather all connection info into one string
connection = \
    "host='dbpg-ifi-kurs01.uio.no' " + \
    "dbname='" + dbname + "' " + \
    "user='" + user + "' " + \
    "port='5432' " + \
    "password='" + pwd + "'"

def administrator():
    conn = psycopg2.connect(connection)
    
    ch = 0
    while (ch != 3):
        print("-- ADMINISTRATOR --")
        print("Please choose an option:\n 1. Create bills\n 2. Insert new product\n 3. Exit")
        ch = get_int_from_user("Option: ", True)

        if (ch == 1):
            make_bills(conn)
        elif (ch == 2):
            insert_product(conn)
    
def make_bills(conn):
    # Oppg 2
    print("-- BILLS --\n")
    cur = conn.cursor()
    q = """SELECT u.name, u.address, u.uid, p.price*o.num as \"order_price\"
                FROM ws.orders as o JOIN ws.users as u USING (uid) JOIN ws.products as p USING (pid) 
                WHERE o.payed = 0;"""
    cur.execute(q)
    ask = cur.fetchall()
    #n = max(ask[2])
    #print(ask)
    dic = {}
    owe = 0
    for name, address, uid, price in ask:
        if uid not in dic.keys():
            owe = 0
        owe += price
        dic[uid] = [name, address, owe]

    for key in dic.keys():
        name = dic[key][0]
        address = dic[key][1]
        owed = dic[key][2]
        print("--Bill--")
        print(f"Name: {name} ")
        print(f"Address: {address}")
        print(f"Total due: {owed} Which is {owed/46000 * 100:.2f} percent of kneecap surgery!\n")

    pass

def insert_product(conn):
    # Oppg 3
    cur = conn.cursor()
    get_cat = """SELECT * FROM ws.categories;"""
    cur.execute(get_cat)
    our_categories = cur.fetchall()
    name_to_cid = {}
    for cid, name in our_categories:
        name_to_cid[name.lower] = cid

    prod_name = input("Product name: ")
    price = input("Price: ")
    category = input("Category: ").lower()
    description = input("Description: ")

    if category not in name_to_cid.values():
        print("This category does not exist")
    else:
        q = """INSERT INTO ws.products(name, price, cid, description) 
        VALUES ('%s, %s, %s, %s);"""
        cur.execute(q, (prod_name, price, name_to_cid[category], description))
        print(f"New product {prod_name} has been inserted!")



    pass

def get_int_from_user(msg, needed):
    # Utility method that gets an int from the user with the first argument as message
    # Second argument is boolean, and if false allows user to not give input, and will then
    # return None
    while True:
        numStr = input(msg)
        if (numStr == "" and not needed):
            return None;
        try:
            return int(numStr)
        except:
            print("Please provide an integer or leave blank.");


if __name__ == "__main__":
    administrator()
