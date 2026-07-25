import sys

age = {
    'Peter': 23,
    'Lopez': 24,
    'Glenn': 27,
    'Jay': 29
}

def fetch(key):
    try:
        value = age[key]
    except:
        print(sys.exc_info()[0:2])
    else:
        print(value)
