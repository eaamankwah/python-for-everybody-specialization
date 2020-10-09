try:
    score = raw_input("Enter Score: ")
    Score = float(score)
except:
    print "Error, please enter correct input"
    quit()
    
# print grade, aphabet
if Score >= 0.9 and Score < 1 :
    print "A"
elif Score >= 0.8 and Score < 0.9 :
    print "B"
elif Score >= 0.7 and Score < 0.8 :
    print "C" 
elif Score >= 0.6 and Score < 0.7 :
    print "D"    
else :
    print "F"