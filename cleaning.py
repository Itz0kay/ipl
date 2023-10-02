import pandas as pd
from batsman import Batsman

# Load the datasets
deliveries = pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
matches = pd.read_csv("IPL_Matches_2008_2022.csv")

# Filter the deliveries dataset
deliveries = deliveries[deliveries.batsman_run != 'DNB'] # filter the data by not considering Did not bat
deliveries = deliveries[deliveries.batsman_run != 'TDNB'] # filter the data by not considering Team did not bat
deliveries = deliveries[deliveries.batsman_run != 'sub'] # filter the data by not considering substitute player

# Sample the deliveries dataset
# deliveries = deliveries.sample(frac=0.1, random_state=1) # take 10% sample of the data

# Join the two datasets
merged_df = pd.merge(deliveries, matches, on='ID', how='inner')
merged_df = merged_df.sort_values(by='ID', ascending=False)
merged_df.drop('Date', inplace=True, axis=1)
merged_df.to_csv(r'merged.csv')

teams = merged_df['Team1'].unique()
for i, team in enumerate(teams):
    print(i,')',team)

n = int(input("select your team:"))

batsmans = merged_df[merged_df['BattingTeam'] == teams[n]]['batter'].unique()
for i, batsman in enumerate(batsmans):
    print(i,')',batsman)

b = int(input("Choose your batsman:"))
venues = merged_df['Venue'].unique()
for i, venue in enumerate(venues):
    print(i,')',venue)

v  = int(input("Select Venue:"))

# Show the data
# print(merged_df.columns)

# Create a new DataFrame with the player names and runs scored
# batsman_df = merged_df.groupby(['batter']).agg({'batsman_run': 'sum'}).reset_index()
# batsman_df['innings'] = merged_df.groupby('batter')['ID'].transform('nunique')
# batsman_df['out'] = merged_df.groupby('batter')['player_out'].transform('count')

# # Rename the columns
# batsman_df.columns = ['batsman', 'runs', 'innings', 'out']
# batsman_df['average'] = batsman_df['runs'] / batsman_df['out'] 
# batsman_df = batsman_df.sort_values(by='runs', ascending=False)

batter = Batsman(batsmans[b], venues[v], merged_df)
print(batter.career_stats())

# print(batsman_df)
