import random

class Cricket:
    __teamIND = ['Virat Kohli', 'Rohit Sharma', 'KL Rahul', 'Rishabh Pant', 'Hardik Pandya', 'Ravindra Jadeja', 'Jasprit Bumrah', 'Mohammed Shami', 'Yuzvendra Chahal', 'Shikhar Dhawan', 'Ajinkya Rahane']
    __teamPAK = ['Babar Azam', 'Shaheen Afridi', 'Mohammad Rizwan', 'Shadab Khan', 'Fakhar Zaman', 'Sarfraz Ahmed', 'Mohammad Amir', 'Imad Wasim', 'Hassan Ali', 'Asif Ali', 'Haris Sohail']
    __teamSL = ['Dimuth Karunaratne', 'Kusal Perera', 'Angelo Mathews', 'Lasith Malinga', 'Dhananjaya de Silva', 'Nuwan Pradeep', 'Thisara Perera', 'Kusal Mendis', 'Wanindu Hasaranga', 'Isuru Udana', 'Avishka Fernando']
    __teamSA = ['Quinton de Kock', 'Kagiso Rabada', 'Faf du Plessis', 'AB de Villiers', 'David Miller', 'Imran Tahir', 'Lungi Ngidi', 'Anrich Nortje', 'Tabraiz Shamsi', 'Rassie van der Dussen', 'Dean Elgar']
    __teamENG = ['Joe Root', 'Ben Stokes', 'Jofra Archer', 'Eoin Morgan', 'Jos Buttler', 'Jason Roy', 'Jonny Bairstow', 'Mark Wood', 'Chris Woakes', 'Sam Curran', 'Moeen Ali']
    __teamAUS = ['David Warner', 'Pat Cummins', 'Steve Smith', 'Mitchell Starc', 'Aaron Finch', 'Glenn Maxwell', 'Josh Hazlewood', 'Adam Zampa', 'Marcus Stoinis', 'Alex Carey', 'Travis Head']
    __teamNZ = ['Kane Williamson', 'Trent Boult', 'Ross Taylor', 'Martin Guptill', 'Tim Southee', 'Lockie Ferguson', 'Colin de Grandhomme', 'Tom Latham', 'Ish Sodhi', 'Mitchell Santner', 'Jimmy Neesham']
    __teamWI = ['Jason Holder', 'Chris Gayle', 'Shimron Hetmyer', 'Andre Russell', 'Nicholas Pooran', 'Shai Hope', 'Evin Lewis', 'Alzarri Joseph', 'Oshane Thomas', 'Fabian Allen', 'Kieron Pollard']
    __teamBAN = ['Tamim Iqbal', 'Shakib Al Hasan', 'Mustafizur Rahman', 'Mushfiqur Rahim', 'Mahmudullah', 'Liton Das', 'Mehidy Hasan', 'Mohammad Saifuddin', 'Taskin Ahmed', 'Rubel Hossain', 'Soumya Sarkar']
    __teamAFG = ['Rashid Khan', 'Mohammad Nabi', 'Hazratullah Zazai', 'Asghar Afghan', 'Najibullah Zadran', 'Mujeeb Ur Rahman', 'Samiullah Shinwari', 'Gulbadin Naib', 'Rahmat Shah', 'Ikram Alikhil', 'Hashmatullah Shahidi']
    
    def __init__(self):
        self.team1_name = ""
        self.team2_name = ""
        self.team1 = []
        self.team2 = []
        self.over = 0

    def chooseTeam(self, team1_name, team2_name):
        self.team1_name = team1_name.upper()
        self.team2_name = team2_name.upper()
        
        teams = {
            'IND': Cricket.__teamIND,
            'PAK': Cricket.__teamPAK,
            'SL': Cricket.__teamSL,
            'SA': Cricket.__teamSA,
            'ENG': Cricket.__teamENG,
            'AUS': Cricket.__teamAUS,
            'NZ': Cricket.__teamNZ,
            'WI': Cricket.__teamWI,
            'BAN': Cricket.__teamBAN,
            'AFG': Cricket.__teamAFG
        }
        
        self.team1 = teams.get(self.team1_name)
        self.team2 = teams.get(self.team2_name)
        
        if not self.team1 or not self.team2:
            raise ValueError("Invalid team name(s). Please choose from the given options.")
        
    def selectOver(self, over):
        self.over = over
        if self.over not in [5, 10, 20, 50]:
            raise ValueError("Invalid over count. Please choose from 5, 10, 20, or 50.")
            
    def playTeam(self, team):
        runs = 0
        wickets = 0
        balls = 0
        total_balls = self.over * 6
        player_scores = {player: 0 for player in team}
        over_scores = []
        
        striker_index = 0
        non_striker_index = 1
        
        while balls < total_balls and wickets < 10:
            over_run = 0
            over_details = []
            for ball in range(6):
                if balls >= total_balls or wickets >= 10:
                    break
                striker = team[striker_index]
                result = random.choice(['Dot Ball', 1, 2, 3, 4, 6, 'Wicket'])
                if result == 'Dot Ball':
                    over_details.append('0')
                elif result == 'Wicket':
                    over_details.append('W')
                    wickets += 1
                    striker_index = max(striker_index, non_striker_index) + 1
                    if striker_index >= 11:
                        break
                else:
                    runs += result
                    over_run += result
                    player_scores[striker] += result
                    over_details.append(str(result))
                    if result in [1, 3]:
                        striker_index, non_striker_index = non_striker_index, striker_index
                
                balls += 1
            over_scores.append(over_details)
        
        return runs, wickets, player_scores, over_scores
    
    def playMatch(self):
        self.team1_runs, self.team1_wickets, self.team1_scores, self.team1_over_scores = self.playTeam(self.team1)
        self.team2_runs, self.team2_wickets, self.team2_scores, self.team2_over_scores = self.playTeam(self.team2)
        
        if self.team1_runs > self.team2_runs:
            return f"{self.team1_name} wins!"
        elif self.team2_runs > self.team1_runs:
            return f"{self.team2_name} wins!"
        else:
            return "It's a tie!"
