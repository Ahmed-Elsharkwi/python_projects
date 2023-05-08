def main():
    #split the time into two parts and the first part is the numbers and second part is a.m. or p.m.
    num, date=input("what time is it ?").split(" ")
    #to decide if the number is in 12-hours-time or 24-hours-time
    if convert(num) <= 12:
         time = convert(num) + 12
    else:
         time = convert(num)
    #decide if it the time of breakfast or lunch or dinner
    if 7.00 <= time <= 8.00 and date == "a.m.":
        print("breakfast time")
    elif 12.00 <= time <= 13.00 and date == "p.m.":
        print("lunch time")
    elif 18.00 <= time <= 19.00 and date == "p.m.":
        print("dinner time")
def convert(time):
        #in this line you are gonna split the number section into two number the firt one is hours and second is minutes
        hours, minutes = time.split(":")
        #After splitting we are gonna convert the  number  in from minutes to hours
        #And after that we are gonna all hours numbers to each other
        return int(hours)+float(minutes)/60
if __name__ == "__main__":
    main()
