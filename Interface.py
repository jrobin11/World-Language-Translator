import Tree

loop = True
print("Welcome to Hello, World!")
while loop:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    user = input("Enter 1 to find languages of a country.\nEnter 2 to find all countries that speak a language.\nEnter 3 to Translate.\nEnter 4 to List all available countries: \nEnter 5 to List all available Languages: \nEnter 6 to Exit: \n")
    user = int(user)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if user == 1:
        cnt = input("Enter Country to find: ")
        Tree.findAllLangs(cnt)
    elif user == 2:
        lng = input("Enter language to find: ")
        Tree.findAllCountry(lng)
    elif user == 3:
        tar = input("Enter target Language ")
        src = "English"
        query = input("Enter phrase to translate ")
        Tree.Translate(src, tar, query)
    elif user == 4:
        Tree.allCountries()
    elif user == 5:
        Tree.allLanguages()
    elif user == 6:
        loop = False
    else: 
        print("Wrong Choice, Try Again.")
