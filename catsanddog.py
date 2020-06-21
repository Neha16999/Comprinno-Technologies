def main():
    #Taking input for no of test cases
    noc = int(input()) 
    
    #check for validity of no of test cases
    if noc < 1 or noc > pow (10,5):
        print("Invalid no of Test cases. Please try again")  
        return      
    else:
        test_cdl(noc)
  

def test_cdl(noc):
    for item in range(noc):
        c , d , l = input().split()
        c , d , l = int(c), int(d), int(l)
        
        maxno = 4 * c +  4 * d
        #twocatno = 4 * (c-2) +  4 * d
        minno = 4 * d

        if (l <= maxno or l >= minno ) and (l %4 ==0): 
            print("yes")
        else:
            print("no")


if __name__=="__main__":
    main()