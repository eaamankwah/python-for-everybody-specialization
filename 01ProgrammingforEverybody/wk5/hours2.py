hrs = raw_input("Enter Hours: ")
Hours = float(hrs)
rat = raw_input("Enter Rate: ")
Rate = float(rat)
if Hours > 40 :
    pay = 40 * Rate + (Hours - 40) * 1.5 * Rate
else :
    pay = Hours * Rate
print pay