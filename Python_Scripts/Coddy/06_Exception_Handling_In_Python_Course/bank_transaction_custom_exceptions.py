balance = 10000  # Imagine it is fetched from database.

class BalanceException(Exception):
    pass

class AttemptException(Exception):
    pass

attempt = 1

def transaction():
    global balance, attempt

    try:
        amt = float(input())

        # Check remaining amount after transaction
        temp = balance - amt

        if temp < 100:
            raise BalanceException("Insufficient balance")

    except Exception as obj:
        print(obj)

        try:
            if attempt == 3:
                raise AttemptException("No more attempts allowed!")

            attempt += 1
            transaction()

        except Exception as e:
            print(e)

    else:
        balance = balance - amt
        print("Transaction is success, Remaining balance is:", balance)
