#Setting up files for Project Rubric Assignment

# Imports
import dateutil
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests


### SECTION 1 ###
#This Section is used to show off the dfferent Pyhton skills leanred over the course as per assignment guidelines.

# Using API Scraping to get latest pices from Coinbase.com in EUR(Not used in Visualisations)
#url = 'https://api.coinbase.com/v2/prices/EUR/spot?'
#response = requests.get(url).json()
#print(response)


# Importing CSV using Pandas Dataframe - Data from : https://www.kaggle.com/idoyo92/epl-stats-20192020

#data = pd.read_csv('players_1920_fin.csv', encoding = 'utf-8')

# Checking Data size( Print Col & Row's) using shape
#print(data.shape)

# Prints out first 30  rows
#print(data.head(30))

# Checking for missing data (There is none so no dropping of tables required.)
#print(data.isnull().values.any())


# Checking types of data in the dataframe
#data.info()

# Printing out FPL player names
#player_names = pd.unique(data.full)
#print(player_names)

#Creating List of Top 6 Clubs
#Top_6_Clubs = ['Liverpool','Manchester United','Manchester City','Arsenal','Chelsea','Tottenham']

#Then slice the dataset to just show data from Top 6 Teams
#Top_6_Clubs_Data = data.loc[data['team'].isin(Top_6_Clubs)]

#print(Top_6_Clubs_Data)

# Testing loc method to extract data from rows
# using row name of Full Name of premier League player as index

#data = pd.read_csv("players_1920_fin.csv", index_col="full")
#Player1 = data.loc["John Egan"]
#Player2 = data.loc["Joel Matip"]

#Printing out Player1 , followed by Player 2's stats for all Gameweeks
#print(Player1, "\n\n\n", Player2)


# Sorting Data by Gameweek using kickoff_time

#Restrcuted_Data_By_GW = data.sort_values(['kickoff_time','team'])
#print(Restrcuted_Data_By_GW.head(40))

#Using grouping to find the Mean Bonus Points scored by Mo Salah each time he scored
#Mo_Salah = ['Mohamed Salah']

#Mo_Salah_Stats = data.loc[data['full'].isin(Mo_Salah)]

#Mo_Salah_BPS = Mo_Salah_Stats.groupby('goals_scored').bps.mean()
#print(Mo_Salah_BPS)



# Using For Loop to display Mo Salah's Creativity V's each premier team this season
#print("Creativity, Opponent")
#for i in range(len(Mo_Salah_Stats)) :
   # print((Mo_Salah_Stats.iloc[i,5], Mo_Salah_Stats.iloc[i,14]))


#Sorting Dataframe by Goals scored in a single game
#Goals_Scored_Sort = data.sort_values(by='goals_scored', ascending=False)
#print(Goals_Scored_Sort[["full","goals_scored"]])

# Players scoring 2 or more goals in a game (Hattrick) - using greateer than fromMUPY Package
#Players_Scoring_Over_2 = Goals_Scored_Sort[Goals_Scored_Sort.goals_scored > 2][
    #["full", "goals_scored"]]

#Using Itterows here
#print("Players Scoring a Hat-trick this season:")
#for index, row in Players_Sorring_Over_2.iterrows():
  #  print(str(row[1]) + " Goals were scored by " + row[0])

#Practicing Merging Dataframes

#FPL_Merge = pd.merge(Mo_Salah_Stats,Restrcuted_Data_By_GW[['goals_scored','kickoff_time','full']], on='goals_scored')
#FPL_Merge.head

#Below prints out the shape of both the Datafranes used, and the new Merged Datframe - Inner Merge
#print("Mo_Salah_Stats dimensions: {}".format (Mo_Salah_Stats.shape))
#print("Restrcuted_Data_By_GW: {}".format (Restrcuted_Data_By_GW[['goals_scored','kickoff_time','full']].shape))
#print("FPL_Merge dimensions: {}".format (FPL_Merge.shape))


#SECTION 2 - Visualisations


#Visualisation #1


#sns.set_theme(style="darkgrid")
#ax = sns.barplot(x="goals_scored", y="full", data=Players_Scoring_Over_2)
#ax.set_title('Players to score Hat-tricks')
#ax.set_ylabel('Player Name')
#ax.set_xlabel('Goals Scored')

#plt.show()
#plt.savefig('Players_Scoring_2_or_more_goals_in_a_GW_(Hat-trick).png')



#Visualisation #2
#Plotting the top 5 Players this season, based on their mean points total (total_points)

#Top_5_Scoring_Players = data.groupby('full')['total_points'].mean().sort_values(ascending=False).index.values
#sns.catplot(data=data, x='total_points',  y='full',kind='bar',ci=None, legend_out=False, order=Top_5_Scoring_Players[1:6])
#plt.xlabel('% Average Gameweek Points')
#plt.ylabel('Player Name')
#plt.title('Top Scoring Players (avg)')
#plt.show()
#plt.savefig('Top_5_Highest_Players_by_GW_AVG_Points.png')

#Visualisation #3
# Plotting the Most Selected 11  players on average over the entire season

#Top_11_Selected_Players = data.groupby('full')['selected'].mean().sort_values(ascending=False).index.values
#ax =sns.catplot(data=data, x='selected',  y='full',kind='bar',ci=None, legend_out=False, order=Top_11_Selected_Players[1:11])
#plt.title("Most selected FPL Player %")
#ax.set(xlabel='% Selected by', ylabel='Player')

#plt.show()
#plt.savefig('Most_Selected_11_Players_This_Season.png')


#Visualisation #4

# When choosing Goalkeepers for FPL team, Clean Sheet Percentage is a top factor

#Defining Top 4 teams Goalkeepers:

#DavidDeGea=data[data['full']=='David de Gea']
#BerndLeno=data[data['full']=='Bernd Leno']
#Alisson=data[data['full']=='Alisson Ramses Becker']
#Ederson=data[data['full']=='Ederson Santana de Moraes']


#labels_pie_1 = ['Clean Sheet', 'No Clean Sheet']
#colors = ['gold','lightcoral']
#CS_Probabibility = [DavidDeGea['clean_sheets'].value_counts()[1],
#         DavidDeGea['clean_sheets'].value_counts()[0],

#        ]
#fig1, ax1 = plt.subplots()
#ax1.pie(CS_Probabibility, labels=labels_pie_1, autopct='%1.1f%%',colors=colors)
#ax1.set_title('David De Gea Clean Sheet %')


#plt.show()
#plt.savefig('David_De_Gea_Clean_Sheet_Percentage.png')

#labels_pie_2 = ['Clean Sheet', 'No Clean Sheet']
#colors = ['gold','lightcoral']
#CS_Probabibility = [BerndLeno['clean_sheets'].value_counts()[1],
#         BerndLeno['clean_sheets'].value_counts()[0],

 #       ]
#fig2, ax1 = plt.subplots()
#ax1.pie(CS_Probabibility, labels=labels_pie_2, autopct='%1.1f%%',colors=colors)
#ax1.set_title('Bernd Leno Clean Sheet %')


#plt.show()
#plt.savefig('Bernd_Leno_Clean_Sheet_Percentage.png')


#labels_pie_3 = ['Clean Sheet', 'No Clean Sheet']
#colors = ['gold','lightcoral']
#CS_Probabibility = [Alisson['clean_sheets'].value_counts()[1],
#         Alisson['clean_sheets'].value_counts()[0],

#        ]
#fig3, ax1 = plt.subplots()
#ax1.pie(CS_Probabibility, labels=labels_pie_3, autopct='%1.1f%%',colors=colors)
#ax1.set_title('Alisson Becker Clean Sheet %')


#plt.show()
#plt.savefig('Alisson_Clean_Sheet_Percentage.png')

#labels_pie_4 = ['Clean Sheet', 'No Clean Sheet']
#colors = ['gold','lightcoral']
#CS_Probabibility = [Ederson['clean_sheets'].value_counts()[1],
     #    Ederson['clean_sheets'].value_counts()[0],

     #   ]
#fig4, ax1 = plt.subplots()
#ax1.pie(CS_Probabibility, labels=labels_pie_4, autopct='%1.1f%%',colors=colors)
#ax1.set_title('Ederson Clean Sheet %')

#plt.show()
#plt.savefig('Ederson_Clean_Sheet_Percentage.png')


#Visualisation #5

#Plotting different stats for Mo Salah ( Goals Scored, Bonus Points, Influence and Creativity)



#Mo_Salah_Stats.plot.scatter(x ='creativity', y ="bps",marker='*')
#plt.xlabel('Creativity')
#plt.ylabel('Bonus Points')
#plt.title('Mo_Salah_Creativity_V_BPS_Scatter')
#plt.show()
#plt.savefig('Mo_Salah_Creativity_V_BPS_Scatter.png')


#Mo_Salah_Stats.plot.scatter(x ='influence', y ="goals_scored", marker='*')
#plt.xlabel('Influence')
#plt.ylabel('Goals Scored')
#plt.title('Mo_Salah_Influence_V_Goals_Scored_Scatter')
#plt.show()
#plt.savefig('Mo_Salah_Influence_V_Goal_Scored_Scatter.png')