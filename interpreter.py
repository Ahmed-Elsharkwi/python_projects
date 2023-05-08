#split the number into three parts x is the first number y is the sign z is the second number
x, y, z = input("Expression: ").split(" ")
x = int(x) # convert x from str to int
z = int(z) # convert z from str to int

match y:
     #in every case y will be compared with every case and if that case is correct the code inside that case will be executed
    case "+":
        l = x + z
        # print the l in float shap with the nearest number for the result
        print(f"{l :.1f}")
    case "-":
            l = x - z
            # print the l in float shap with the nearest number for the result
            print(f"{l :.1f}")
    case "*":
        l = x * z
        # print the l in float shap with the nearest number for the result
        print(f"{l :.1f}")
    case "/":
        if z != 0:
            l = x / z
            # print the l in float shap with the nearest number for the result
            print(f"{l :.1f}")
    case _:
        #if y does not equale to any thign from any above cases y will get in this case and it will print Expression again
        print("Expression: ")
