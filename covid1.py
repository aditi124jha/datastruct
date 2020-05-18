#IIIT DHARWAD
#COVID TRACKER 1
import pandas as pd
import matplotlib.pyplot as plt
import sys
import requests
from bs4 import BeautifulSoup
import datetime
import os
#creating variables for urls of the datasets and parsing the necessary information
confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
eath_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
r = requests.get("https://en.wikipedia.org/wiki/Developing_country")
soup = BeautifulSoup(r.text, 'html.parser')
contentTable  = soup.find('div', { "class" : "div-col columns column-width"})
a_tags = contentTable.find_all('a')
#creating a list of under-developed or developing countries
developing_countries=list()
for each in a_tags:
    names=each.get('title')
    if names!=None:
        developing_countries.append(names)
        developing_countries.extend(['Gambia','Sao Tome and Principe','Taiwan*','Burma','MS Zaandam'])
#reading the csv file and shaping it into a 2D dataframe
df_c=pd.read_csv(confirmed_url, error_bad_lines=False)
df_d=pd.read_csv(death_url, error_bad_lines=False)
#removing the province column
df_c=df_c.loc[:,'Country/Region':]
df_d=df_d.loc[:,'Country/Region':]
#summing the values, so that theres only one row for each country
df_c=df_c.groupby('Country/Region').sum()
df_d=df_d.groupby('Country/Region').sum()
#making countries as index and all the dates as columns
df_c=df_c.loc[:,'1/22/20':]
df_d=df_d.loc[:,'1/22/20':]

#writing all the country names into a list
countries=list(df_c.index)
while (1):
    print("\nEnter 1 to display graphs")
    print("Enter 2 to display the top high-risk countries that are to be avoided for internships")
    print("Enter 3 to exit\n")
    num=int(input())
    if (num==1):
        print("\nEnter the country for which the graph is to be displayed\n")
        c=str(input())
        dates=list(df_c.columns.values.tolist())
        death_growth_per_day=list()
        if c in countries:
            for i,j in zip(df_c,df_d):
                if (df_c.loc[c][i])==0:
                    temp=0
                else:
                    temp=float((df_d.loc[c][j]/df_c.loc[c][i])*100)
                    death_growth_per_day.append(temp)
            plt.plot(dates, death_growth_per_day)
            plt.ylabel("Death rate wrt confirmed cases")
            ax=plt.gca()
            ax.axes.xaxis.set_ticks([dates[x] for x in range(0,len(dates),15)])
            ax.tick_params(axis='x', labelrotation=90)
            plt.show()
        else:
            print("\nThe country name isn't valid")

    if (num==2):
        high_risk_countries=list()
        high_risk_countries_dict=dict()

        for i in countries:
            for j,x in zip(df_c,df_d):
                if (df_d.loc[i][x]==0) | (df_c.loc[i][j]==0):
                    death_rate=0
                elif df_c.loc[i][j]!=0:
                     death_rate = (df_d.loc[i][x]/df_c.loc[i][j])*100
                else:
                    death_rate=0
                two_percen=(2/100)*df_c.loc[i][j]
                if (death_rate!=0)&(death_rate>=two_percent):
                    if i in high_risk_countries:
                        break
                    else:
                        high_risk_countries.append(i)

        for i in high_risk_countries:
            if (df_c.loc[i][-1]==0):
                f_death_rate=0
            else:
                f_death_rate=(df_d.loc[i][-1]/len(df_d.columns))*100
                high_risk_countries_dict.update( { i : f_death_rate } )

        filename=datetime.datetime.now()

        print("Top high-risk countries that are to be avoided when applying for internships:\n", file=f)
        while (high_risk_countries_dict):
            my_my=max( high_risk_countries_dict, key=high_risk_countries_dict.get )
            if my_my not in developing_countries:
                print(my_my+" - "+"death ("+str(df_d.loc[my_my][-1])+")"+" -"+"confirmed ("+str(df_c.loc[my_my][-1])+")", file=f)
            high_risk_countries_dict.pop(my_my)
        f.close()
        print("This output has been saved to a text file")
        file=filename.strftime("%d %B %Y")+".txt"
        os.startfile(file)
    if (num==3):
        sys.exit(1)