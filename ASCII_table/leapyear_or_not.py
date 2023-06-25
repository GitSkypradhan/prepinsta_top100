# check for leap year or not
year = int(input("aur bhai ek year de: "))
# agar year centurian hua jese 2000,3000,1600 tho usko 400 se divide krn pe zero ans hona chahiye
if year % 400 == 0:
  print("It's a Leap year.")
# har 4 saal baad ek leap year hota hai  
elif year % 4 == 0 and year%100 != 0:
  print("It's a Leap year. ")
else:
  print("It's not a leap year")

