import sys
import pandas as pd
import matplotlib.pyplot as plt plt.rcdefaults()
import matplotlib.pyplot as plt

df=pd.read_csv('CropsDataFile.csv',usecols=['Year','Crop_Name','Production'])
while(1):
    
    print("Enter 1 to retrive data year wise,")
    print("Enter 2 to retrive cropwise details")
    print("Enter 3 to exit system")
    ch=int(input())
    if ch==1:
       print("Enter year")
       yr=input()
       gk=df.groupby('Year')
       s=gk.get_group(yr)
       print(s) 
    elif ch==2:
       crop=input("Enter crop:",)
       
       #Years=('1997','1998','1999','2000','2001','2002','2003','2004','2005','2007','2008','2009','2010')
       #y_pos = np.arange(len(Years))
       
       #production=[]
       
       #plt.bar(y_pos, production, align='center', alpha=0.5)
       #plt.xticks(y_pos, Years)
       #plt.ylabel('Production')
       #plt.title('Year wise production of crop')
       #plt.show()
       gk=df.groupby('Crop_Name')
       s=gk.get_group(crop)
       print(s)
       
       print("\nenter 1 if you a graph\n")
       print("enter 2 if you want to exit\n")
       ch2=int(input())
       if ch2==1:
           ss=s.groupby('Year')['Production'].apply(lambda x: x.tolist()).to_dict()
           #print(ss)
           pro=list()
           sum=0
           for i in ss.values():
                for j in i:

                    sum+=float(j)
                pro.append(sum)
                sum=0
           #print(pro)
           year=list()
           for x in ss.keys():
               year.append(x)
           #print(year)
       
           plt.bar(year,pro)
           plt.xlabel('year')
           plt.ylabel('production')
           plt.title('Year wise production of crop')
           plt.show()
       else:
           sys.exit(1)
           
           
       #ss=df.to_dict(orient='9plist')
       #print(ss)
       #ss=df.groupby(['Crop_Name','Year'])['Production'].apply(lambda x: x.tolist()).to_dict()
       #print(ss)
       
    elif ch==3:
       print("\nThank you for using our system!\nHave a good day!\n")
       sys.exit(1)
    else:
        print("Wrong Choice!! Try again!")