fname = raw_input("Enter file name: ") 
fh = open(fname) 
lst = list()                       
for line in fh:                    
     word= line.rstrip().split()     
     for wordlist in word:               
         if wordlist in lst:        
            continue               
         else :                      
             lst.append(wordlist)    
lst.sort()                          
print lst    


    

