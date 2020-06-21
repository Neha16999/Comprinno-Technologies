

def main():
    #Taking input for no of test cases
    noc = int(input()) 

    #check for validity of no of test cases
    if noc < 1 or noc > 1000:
        print("Invalid no of Test cases. Please try again")  
        return
    else:
        matchclass(noc)


def matchclass(noc):   
    for item in range(noc):
        #taking id as input
        id = input()  

        #Converting id to uppercase as dict contains only uppercase keys
        up = id.upper()    

        #Printing the value if key mathes otherwise displaying message "Not found"
        print(dict.get(up,"Not Found. Please check the class ID."))


if __name__ == "__main__":
    #storing class id and string description
    dict = {'B':'BattleShip', 'C' : 'Cruiser', 'D': 'Destroyer', 'F':'Frigate'} 
    main()