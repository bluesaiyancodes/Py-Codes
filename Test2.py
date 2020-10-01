def is_leap(year):
    leap = False
    if (year % 4)==0:
        if (year % 100)!=0:
            leap = True
            print("leap yr aita")
        else:
            if(year % 400)==0:
                leap = True
                print("eita b leap year")
            else:
                leap = False
                print("eita leap year nuha")
    return leap


year = int(input())
print(is_leap(year))


