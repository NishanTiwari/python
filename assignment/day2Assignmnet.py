
socialMediaAccount = {

    "facebook" : {
       "email": "account@facebook.com",
        "password": "22222"},
    
    "gmail" : {
        "email": "account@gmail.com",
        "password": "22222"},

    "istagram": {
        "email": "account@instagram.com",
        "password": "22222"},
    
    "tweeter": {
        "email": "account@tweter.com",
        "password": "22222"},

}

print("which account website you want to see?")

user_input = input("type 1 for facebook, 2 for gmail, 3 for instagram, 4 for tweeter, e for exit, y to continue, n for quit:   " )

while user_input != "e":
    if user_input == "1":
        print(f"site: {socialMediaAccount['facebook']['email']} \npassword {socialMediaAccount['facebook']['password']}")
    elif user_input == "2":
        print(f"site: {socialMediaAccount['gmail']['email']} \npassword {socialMediaAccount['gmail']['password']}")
    elif user_input == "3":
        print(f"site: {socialMediaAccount['instagram']['email']} \npassword {socialMediaAccount['instagram']['password']}")
    elif user_input == "4":
        print(f"site: {socialMediaAccount['tweeter']['email']} \npassword {socialMediaAccount['tweeter']['password']}")
    else:
        print(" Hyy fucker please read givan massage carefully ")


    
    
   






