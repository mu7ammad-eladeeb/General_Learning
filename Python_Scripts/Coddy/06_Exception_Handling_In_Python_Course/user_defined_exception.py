class AccessError(Exception):
    pass


def access(age):
    try:
        if age < 18:
            raise AccessError("Access Denied!")
    except Exception as e:
        print(e)
    else:
        print("Session Created!")
