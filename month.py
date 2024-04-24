date=int(input("enter date "))
month=int(input("enter month "))
year=int(input("enter year "))
if month < 3:
    month += 12
    year -= 1

c=year//100
d=year%100
if month>=31:
    print("invalied month")
else:
    
    f=(date+ ((13 * (month+ 1)) // 5) + d + (d// 4) + (c // 4) + 5 * c)
    fres=int(f%7)
    day={0:"saturday",1:"sunday",2:"monday",3:"tuesday",4:"wednesdy",5:"thursday",6:"friday",}
    print(day[fres])