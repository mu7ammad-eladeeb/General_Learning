stored_password = "12345" #fetched from database (Imagine)
class Invalid_Password(Exception):
    pass
def login():
    try:
        password = input()
        if password!=stored_password:
            raise Invalid_Password("Invalid password, try again")
    except Exception as e:
        print(e)
        login()
    else:
        print("session created")
# Another Solution (more efficient):
"""
stored_password = "12345" #fetched from database (Imagine)
class Invalid_Password(Exception):
    pass
def login():
    while True:
        try:
            password = input()
            if password != stored_password:
                raise Invalid_Password("Invalid password, try again")
        except Exception as obj:
            print(obj)
        else:
            print("session created")
            break
"""
