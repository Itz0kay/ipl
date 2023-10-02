class Batsman:
    def __init__(self, name, location, df):
        self.name = name
        self.location = location
        self.df = df[df['batter'] == self.name]
        self.df = df[df['Venue'] == self.location]

    def career_stats(self):
        total_seasons = len(self.df['Season'].unique())
        total_runs_scored = self.df['batsman_run'].sum()
        total_balls_faced = self.df.shape[0]
        strike_rate = (total_runs_scored / total_balls_faced) * 100
        number_of_fours = self.df[self.df['batsman_run'] == 4].shape[0]
        number_of_sixes = self.df[self.df['batsman_run'] == 6].shape[0]
        total_dismissals = self.df[self.df['player_out'] == self.name].shape[0]
        total_innings_played = self.df['ID'].nunique()
        not_out_innings = total_innings_played - total_dismissals
        average = total_runs_scored / (total_innings_played+total_seasons)
        runs_per_match = self.df.groupby(['ID'])[['batsman_run']].sum().reset_index()
        number_of_fifties = runs_per_match[(runs_per_match['batsman_run'] >= 50) & (runs_per_match['batsman_run'] < 100)].shape[0]
        number_of_hundreds = runs_per_match[(runs_per_match['batsman_run'] >= 100)].shape[0]

        data_dict = {
            'total_runs_scored': total_runs_scored, 
            'strike_rate': round(strike_rate, 2), 
            'average': round(average, 2),
            'total_dismissals': total_dismissals,
            'number_of_fifties': number_of_fifties, 
            'number_of_hundreds': number_of_hundreds,
            'number_of_fours': number_of_fours, 
            'number_of_sixes': number_of_sixes,
        }

        return data_dict