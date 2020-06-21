def main():
    #Taking input for no of test cases
    noc = int(input()) 
    
    #check for validity of no of test cases
    if noc < 1 or noc > 1000:
        print("Invalid no of Test cases. Please try again")  
        return      
    else:
        for item in range(noc):
            cal_gs()
  
def cal_gs():
    #Taking input from user
    bsal=float(input())

    # checking for salary range
    if bsal < 1 or bsal > 100000:
        print("Invalid Salary")
        return 

    #calculating gs    
    if bsal < 1500:
        da = 0.9 * bsal
        hra = 0.1 * bsal
    else:
        da = 0.98 * bsal
        hra = 500
    gs = bsal + da + hra
    print(gs)        


if __name__=="__main__":
    main()
