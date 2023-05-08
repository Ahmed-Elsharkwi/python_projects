n = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
match n.strip():
    case "42" | "forty-two" | "forty two" | "FoRty TwO":
        print("Yes")
    case _:
        print("NO")
