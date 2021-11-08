
def frontend():
    conn = None
    ch = 0
    username = ""
    while (username == ""):
        print("-- USER FRONTEND --")
        print("Please choose an option:\n 1. register\n "
              "2. Login\n 3. Exit:")
        ch = get_int_from_user("option: ", True)

        if (ch == 1):
            register(conn)  # Register new user
        elif (ch == 2):
            username = login(conn)  # Login with existing user
        elif (ch == 3):
            return #Exit program
    # Once logged in, can now search for products
    search(conn, username)

def register(conn):
    pass

def login(conn):
    return ""

def get_int_from_user(msg, needed):
    while True:
        numStr = input(msg)
        if (numStr == "" and not needed):
            return None;
        try:
            return int(numStr)
        except:
            print("Please provide an integer or leave blank.");
