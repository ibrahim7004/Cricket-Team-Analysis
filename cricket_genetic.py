import random

class Player:
    def __init__(self, idd, name, gp, gw, gl, lmw, spec):
        self.idd = idd
        self.name = name
        self.gp = gp
        self.gw = gw
        self.gl = gl
        self.lmw = lmw
        self.spec = spec
        
    def fp(self):
        # Define the fitness function of a player
        # This function can be customized to fit specific requirements
        return self.gw / self.gp * self.lmw
        
def avg_fitness(team):
    # Calculate the average fitness of a team
    total_fitness = sum(player.fp() for player in team)
    return total_fitness / len(team)

def crossover(parent1, parent2):
    # Implement the crossover function to produce a child team from two parent teams
    child = []
    parent1_players = random.sample(parent1, len(parent1) // 2)
    for player in parent2:
        if player not in parent1_players:
            parent1_players.append(player)
            if len(parent1_players) == len(parent1):
                break
    return parent1_players

def mutation(team, players):
    # Implement the mutation function to replace one player in a team with a new player
    index = random.randint(0, len(team) - 1)
    available_players = [p for p in players if p not in team]
    new_player = random.choice(available_players)
    team[index] = new_player

def getNewGeneration(current_population, p0, teamSize, c0, mutation_rate, players):
    # Implement the getNewGeneration function to produce a new generation of teams
    sorted_population = sorted(current_population, key=lambda x: avg_fitness(x), reverse=True)
    elite_teams = sorted_population[:c0]
    new_population = []
    while len(new_population) < p0:
        parent1 = random.choice(elite_teams)
        parent2 = random.choice(elite_teams)
        child = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            mutation(child, players)
        new_population.append(child)
    return new_population

def main(players, p0, teamSize, c0, numGenerations, mutation_rate):
    # Initialize the population
    population = []
    for i in range(p0):
        population.append(random.sample(players, teamSize))

    # Evolution process
    for i in range(numGenerations):
        population = getNewGeneration(population, p0, teamSize, c0, mutation_rate, players)

    # Find the best team
    best_team = max(population, key=lambda x: avg_fitness(x))
    print("The best team is:")
    for player in best_team:
        print(player.name)


players = [
Player(1, "Player 1", 10, 6, 4, 3, "Bowler"),
Player(2, "Player 2", 15, 10, 5, 2, "Batsman"),
Player(3, "Player 3", 20, 12, 8, 1, "All-rounder"),
Player(4, "Player 4", 8, 2, 6, 4, "Bowler"),
Player(5, "Player 5", 12, 8, 4, 2, "Batsman"),
Player(6, "Player 6", 18, 14, 4, 3, "All-rounder"),
Player(7, "Player 7", 6, 3, 3, 5, "Bowler"),
Player(8, "Player 8", 14, 6, 8, 2, "Batsman"),
Player(9, "Player 9", 16, 12, 4, 1, "All-rounder"),
Player(10, "Player 10", 4, 1, 3, 6, "Bowler"),
Player(11, "Player 11", 10, 6, 4, 3, "Batsman"),
Player(12, "Player 12", 15, 10, 5, 2, "All-rounder"),
Player(13, "Player 13", 20, 12, 8, 1, "Bowler"),
Player(14, "Player 14", 8, 2, 6, 4, "Batsman"),
Player(15, "Player 15", 12, 8, 4, 2, "All-rounder"),
Player(16, "Player 16", 18, 14, 4, 3, "Bowler"),
Player(17, "Player 17", 6, 3, 3, 5, "Batsman"),
Player(18, "Player 18", 14, 6, 8, 2, "All-rounder"),
Player(19, "Player 19", 16, 12, 4, 1, "Bowler"),
Player(20, "Player 20", 4, 1, 3, 6, "Batsman")]


p0 = 20 # Population size
teamSize = 16 # Number of players per team
c0 = 4 # Number of elite teams to use as parents
numGenerations = 100 # Number of generations to run the algorithm
mutation_rate = 0.1 # Probability of mutation


main(players, p0, teamSize, c0, numGenerations, mutation_rate)    
    





