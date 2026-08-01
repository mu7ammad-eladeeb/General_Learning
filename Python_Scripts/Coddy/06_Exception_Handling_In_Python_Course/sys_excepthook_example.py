import sys


def my_exception(exc_type, exc_value, exc_traceback):
    print("Something Went Wrong!")
    print(exc_value)


sys.excepthook = my_exception


def add(val1, val2):
    print(val1 + val2)
#--------------------------------------------------------------------------------------
# Another Solution:
# import sys

# def my_exception(exc_type, exc_value, exc_traceback):
#     print("Something Went Wrong!")
#     print(exc_value)

# def add(val1, val2):
#     try:
#        result = val1 + val2
#     except Exception as obj:
#         my_exception(obj.__class__, obj, obj.__traceback__)
#     else:
#         print(result)
