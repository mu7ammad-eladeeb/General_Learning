def contact_details(mobile):
    try:
        if not (mobile.isdigit() and len(mobile) == 12):
            raise ValueError("Invalid")
    except ValueError as obj:
        print(obj)
    else:
        print("valid")


# Test Cases
contact_details("123456789012")   # valid
contact_details("12345abc9012")   # Invalid
contact_details("1234567890")     # Invalid
