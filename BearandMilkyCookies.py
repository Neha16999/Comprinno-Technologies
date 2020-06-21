def main():
    #Taking input for no of test cases
    noc = int(input()) 
    
    #check for validity of no of test cases
    if noc < 1 or noc > 50:
        print("Invalid no of Test cases. Please try again")  
        return      
    else:
        for item in range(noc):
            check_nom()

#check nom are in given range or not
def check_nom():
    nom = int(input())
    if nom < 1 or nom > 50:
       print("Invalid no of Test Minutes. Please try again")  
       return  
    else :
        permit()  


def permit():        
# takes input of cookie and milk 
    cmarray = list(map(str, input().split()))   

    # no of min is 1 and limak eats cookie then he didnt followed his parents instruction.   
    if len(cmarray)==1 and cmarray[0]=="cookie":
        print("NO")

    # no of min is 1 and limak drinks milk then he followed his parents instruction.    
    elif len(cmarray)==1 and cmarray[0]=="milk":
        print("YES") 

    # for multiple inputs     
    else:
        for i in range(len(cmarray)-1):
            #if limak eats 2 cookies continuosly then he didnt followed his parents instruction.
            if cmarray[i]=="cookie" and cmarray[i+1]=="cookie":
                print("NO")
                cnt = 1
                break   
        else :
                print("YES")        
                    
            
if __name__=="__main__":
    main()                