import sys
import pandas as pd
import matplotlib.pyplot as plt

#Read csv files
death_data = pd.read_csv("time_series_covid_19_deaths.csv", index_col="Country/Region")
recovered_data = pd.read_csv("time_series_covid_19_recovered.csv", index_col="Country/Region")
confirmed_data = pd.read_csv("time_series_covid_19_confirmed.csv", index_col="Country/Region")

#Eliminate unnecessary columns
death_data.drop(["Province/State", "Lat", "Long"], axis=1, inplace=True)
recovered_data.drop(["Province/State", "Lat", "Long"], axis=1, inplace=True)
confirmed_data.drop(["Province/State", "Lat", "Long"], axis=1, inplace=True)

country = input("Enter the country whose average week wise data is required : ")



#confirmed_data.set_index("Country/Region", inplace=True)
confirmed_data=confirmed_data.groupby(confirmed_data.index).sum()
death_data=death_data.groupby(death_data.index).sum()
recovered_data=recovered_data.groupby(recovered_data.index).sum()

week_confirmed = []
week_death = []
week_recovered = []

n1 = len(confirmed_data.loc[country])
n2 = len(death_data.loc[country])
n3 = len(recovered_data.loc[country])

n = min(n1,n2,n3)

death_ind = 0
confirmed_ind = 0
recovered_ind = 0


for i in range(0,n,7):
    count = 0
    s1=0
    s2=0
    s3=0
    while count<7 and (i+count)<n:
        s1 += int(confirmed_data.loc[country][i+count])
        s2 += int(death_data.loc[country][i+count])
        s3 += int(recovered_data.loc[country][i+count])
        count += 1
    week_confirmed.append('%.2f'%(s1/count))
    week_death.append('%.2f'%(s2/count))
    week_recovered.append('%.2f'%(s3/count))

print("Week-wise average data of "+country+" :")
print("Week\tConfirmed\tDeath\tRecovered")
for i in range(len(week_confirmed)):
    print("Week{}\t{}\t\t{}\t\t{}".format((i+1), week_confirmed[i], week_death[i], week_recovered[i]))


for i in range(n1):
    if confirmed_data.loc[country][i] != 0:
        confirmed_ind = i
        break

for i in range(n2):
    if death_data.loc[country][i] != 0:
        death_ind = i
        break

for i in range(n1):
    if recovered_data.loc[country][i] != 0:
        recovered_ind = i
        break

print("\n\n{} took {} days to turn into Death state after a confirmed case".format(country, int(death_ind)-int(confirmed_ind)))
print("{} took {} days to get a Recovery state after a confirmed case".format(country, int(recovered_ind)-int(confirmed_ind)))

print ("Do you want a graph Y/N?\n")
ch=input()
if ch=="N":
    print ("Okay! Thank you for using our system!")
    sys.exit(1)

elif ch=="Y":
    print ("\nEnter the number of which graph you want")
    print("\n\n1.Confirmed vs Recovered\n2. Confirmed vs Deaths\n3. Recovered vs Death\n4. Exit system\n\n")
    choice=int(input())
    if choice==1:
        graph_x = ['%.2f'%float(week_confirmed[0])]
        graph_y = ['%.2f'%float(week_recovered[0])]

        for i in range(1,len(week_confirmed)):
            graph_x.append('%.2f'%(float(week_confirmed[i])))
            graph_y.append('%.2f'%(float(week_recovered[i])))

        plt.plot(graph_x, graph_y)
        plt.xlabel('Week-wise Confirmed cases')
        plt.ylabel('Week-wise Recovered cases')
        plt.title("Confirmed v/s Recovered cases\nfor {}".format(country))
        plt.show()

    elif choice==2:
        graph_x = ['%.2f'%float(week_confirmed[0])]
        graph_y = ['%.2f'%float(week_death[0])]

        for i in range(1,len(week_confirmed)):
            graph_x.append('%.2f'%(float(week_confirmed[i])))
            graph_y.append('%.2f'%(float(week_death[i])))

        plt.plot(graph_x, graph_y)
        plt.xlabel('Week-wise Confirmed cases')
        plt.ylabel('Week-wise Death cases')
        plt.title("Confirmed v/s Death cases\nfor {}".format(country))
        plt.show()

    elif choice==3:
        graph_x = ['%.2f'%float(week_recovered[0])]
        graph_y = ['%.2f'%float(week_death[0])]

        for i in range(1,len(week_recovered)):
            graph_x.append('%.2f'%(float(week_recovered[i])))
            graph_y.append('%.2f'%(float(week_death[i])))

        plt.plot(graph_x, graph_y)
        plt.xlabel('Week-wise Recovered cases')
        plt.ylabel('Week-wise Death cases')
        plt.title("Recovered v/s Death cases\nfor {}".format(country))
        plt.show()

    elif choice==4:
        print ("Okay! Thank you for using our system")
        sys.exit(1)
    
    else:
        print ("Wrong choice! Try again!!")