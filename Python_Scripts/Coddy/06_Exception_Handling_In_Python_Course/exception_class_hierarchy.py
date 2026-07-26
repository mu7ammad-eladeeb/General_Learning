#Click on RUN CODE and observe
def observe(idx):
    try:
        data = [10,20,30,40]
        print(data[idx])  #IndexError
    except Exception as e:
        print(type(e)) #Shows Exception is class
        print(IndexError.mro()) #Shows all parent classes
