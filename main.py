def encoder(password):
    list = []
    for i in range(0, len(password)):
        hold = int(password[i])
        hold -= 3
        if hold < 0:
            hold = abs(hold)
        list.append(str(hold))
    string = ''.join(list)
    return string





while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    choice = int(input("\nPlease enter an option: "))
    if choice == 1:
        user_pass = input("Please enter your password to encode: ")
        encoder(user_pass)
        print("Your password has been encoded and stored!\n\n")
    if choice == 2:
        user_pass = input("Please enter your password to decode: ")
    if choice == 3:
        break

