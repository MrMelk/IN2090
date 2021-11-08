
def frontend():
    conn = None
    ch = 0
    username = ""
    while (username == ""):
        print("-- USER FRONTEND --")
        print("Please choose an option:\n 1. register\n "
              "2. Login\n 3. Exit:")
        ch = get_int_from_user("option: ", True)
    pass


def get_int_from_user(msg, needed):
    while True:
        numStr = input(msg)
        if (numStr == "" and not needed):
            return None;
        try:
            return int(numStr)
        except:
            print("Please provide an integer or leave blank.");
