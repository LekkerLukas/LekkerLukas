keuze = int(input("do you want to convert to miles(1) or to kilometers(2):"))

if keuze == 1:
  kilometers = int(input("how many kilometers do you want to convert to miles:"))
  miles = kilometers / 1.609
  print("this is ",miles, "miles")
else:
  if keuze == 2:
     miles = int(input("how many miles do you want to convert to kilometers:"))
     kilometers = miles * 1.609
     print("this is", kilometers, "kilometers")


