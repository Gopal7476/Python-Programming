# Check if a Year is a Leap Year or Not.

year = int(input())
if((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print("Leap Year")
else:
    print("Not Leap Year")