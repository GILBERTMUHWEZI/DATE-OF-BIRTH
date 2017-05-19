import datetime, calendar
current_year=2017
date=input("Enter date of birth (1-31)\n")
Endings=["st","nd","rd"] + 17*["th"] + ["st","nd","rd"] + 7*["th"] + ["st"]
Days=['Monday','Tuesday','Wednesday','Thursay','Friday','saturday','Sunday']
month=int(input("Enter the birth month (1-12)\n"))
months=['january','February','March','April','May','June','July','August','September','October','November','December']
Year=int(input('How old are you?\n'))
G1=months[month-1]
G2=int(date)
G3=(current_year-Year)
G4=date+Endings[G2-1]
G5=calendar.weekday(G3,month,G2)
G6=Days[G5]
This=G1+" ",G2,",",G3
print("You were born 0n ",G6,G4,G1, "of the year", G3)
