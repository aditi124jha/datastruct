import sys
def main():
    donor = []
    recipient = []
    while True:
        print("\n\n1. Enter Donor data\n2. Enter Recipient data\n3. Retrieve Donor specific data\n4. Retrieve Recipient specific data\n5. Exit system\n\n")
        ch = int(input("Enter your choice : "))
        if ch==1:
            print("\nEnter the following details:")
            name = input("Donor name : ")
            ind = -1
            for i in range(len(donor)):
                if name.lower()==donor[i][0]:
                    ind = i
            if ind > -1:
                donor[ind][2] += 1
            else:
                bGroup = input("Blood group : ")
                hosp = input("Hospital name : ")
                donor.append([name,bGroup,1,hosp])
            print("\nThank you! Donor details successfully updated!")
        elif ch==2:
            print("Enter the following details:")
            name = input("Recipient name : ")
            ind = -1
            for i in range(len(recipient)):
                if name.lower()==recipient[i][0]:
                    ind = i
            amt = int(input("Units of blood received : "))
            if ind > -1:
                recipient[ind][2] += amt
            else:
                bGroup = input("Blood group : ")
                hosp = input("Hospital name : ")
                recipient.append([name,bGroup,amt,hosp])
            print("\nThank you! Recipient details successfully updated!")
        elif ch==3:
            while True:
                print("\n1. Show data of all donors\n2. Show data of specific Hospital branch\n")
                opt = int(input("Enter choice : "))
                if opt==1:
                    print("\n\nNAME\tBLOOD GROUP\tUNITS\tHOSPITAL\n")
                    for i in range(len(donor)):
                        print(donor[i][0]+"\t"+donor[i][1]+"\t"+str(donor[i][2])+"\t"+donor[i][3])
                    break
                elif opt==2:
                    hosp = input("Enter hospital name : ")
                    print("\n\nNAME\tBLOOD GROUP\tUNITS\tHOSPITAL\n")
                    for i in range(len(donor)):
                        if donor[i][3].lower()==hosp.lower():
                            print(donor[i][0]+"\t"+donor[i][1]+"\t"+str(donor[i][2])+"\t"+donor[i][3])
                    break
                else:
                    print("Wrong choice!! Try again!")
        elif ch==4:
            while True:
                print("1. Show data of all Recipients\n2. Show data of specific Hospital branch\n")
                opt = int(input("Enter choice : "))
                if opt==1:
                    print("\n\nNAME\tBLOOD GROUP\tUNITS\tHOSPITAL\n")
                    for i in range(len(recipient)):
                        print(recipient[i][0]+"\t"+recipient[i][1]+"\t"+str(recipient[i][2])+"\t"+recipient[i][3])
                    break
                elif opt==2:
                    hosp = input("Enter hospital name : ")
                    print("\n\nNAME\tBLOOD GROUP\tUNITS\tHOSPITAL\n")
                    for i in range(len(donor)):
                        if recipient[i][3].lower()==hosp.lower():
                            print(recipient[i][0]+"\t"+recipient[i][1]+"\t"+str(recipient[i][2])+"\t"+recipient[i][3])
                    break
                else:
                    print("Wrong choice!! Try again!")
        elif ch==5:
            print("\n\nThank you for using our system!!\nHave a good day!\n")
            sys.exit(1)
        else:
            print("Wrong Choice!! Try again!")