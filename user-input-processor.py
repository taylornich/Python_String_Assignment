def name_processor():
    first_name = input("Enter your first name: ")

    if len(first_name) < 2:
        print("Error, first name not long enough.")
        return
    
    last_name = input("Enter your last name: ")
    if len(last_name) < 2:
        print("Error, last name not long enough.")
        return
    
    print(f"Your first name is {first_name} and your last name is {last_name}")
    
name_processor()
