#to find if year entered by user is leap year

a=int(input('enter a year:'))
if (a%4)==0:
   if (a%100)==0:
      if (a%400)==0:
         print("leap year")
      else:
         print("not leap year")
   else:
         print("not leap year")
         
else:
        print("not leap year")   
