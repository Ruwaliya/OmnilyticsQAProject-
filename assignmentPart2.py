with open("dataStoredFile.py", "r") as dataStored_file:
    for line in dataStored_file:
        data = line.split(',')

        data_string = (".")
        data_string3 = True
        for i in data:
            if i.isdigit() == True:
                print(i + " - Integer Number")#verify integer numbers
            elif data_string in i :
                print(i +" - Real Number")#verify real numbers
            else:
                for character in i:
                    if character.isdigit():
                        data_string3 = True
                        break
                    else:
                        data_string3 = False
                if data_string3 is True:
                    print(i+" - Alphanumeric")#verify alphanumeric
                else:
                    print(i + " - Alphabetical strings")#verify alphabetical strings
