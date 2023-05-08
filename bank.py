word = input("Greeting: ").replace("," , " ")
first= word.split()
if first[0] == "Hello":
    print("$0")
elif word[0] == "H" and first[0] != "Hello":
    print("$20")
else:
    print("$100")
