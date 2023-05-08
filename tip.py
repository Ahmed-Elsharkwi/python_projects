def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #here you are gonna calculate the tip
    tip = dollars * percent
    #here you are gonna print the tip in the nearsest number to the resutl of calculation
    print(f"Leave ${tip:.2f}")

#here we will convert dollar to float and we will replace $ with empty space
def dollars_to_float(d):
    d = float(d.replace("$", ""))
    return d
#here we convert the percent to float and we replace % with empty space and after that we will convert percent into fraction
def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    p = p / 100
    return p


main()
