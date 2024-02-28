import math

s1 = [3]
s2 = [3]

def input (s1,s2) :
    s1[0] = str(input("Enter Predicate"))
    s2[0] = str(input("Enter Predicate"))
    
    s1[1] = str(input("Enter 1st Literal"))
    s1[2] = str(input("Enter 2nd literal"))
    
    s2[1] = str(input("Enter 1st Literal"))
    s2[2] = str(input("Enter 2nd literal"))
    
def unify(s1,s2):
    if(s1[0] != s2[0]):
        if(s1[1] == s2[1] & s1[2] == s2[2]):
            return None
                
        elif(s1[1] != int & s1[1] != s2[1]):
            s1[1] = s2[1]
                    
        
        elif(s2[1] != int & s1[1] != s2[1]):
            s2[1] = s1[1]
        
        elif(s1[2] != int & s1[2] != s2[2]):
            s1[2] = s2[2]
                    
        
        elif(s2[2] != int & s1[2] != s2[2]):
            s2[2] = s1[2]
    
    return(s1,s2)s
        