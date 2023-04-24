Basketball_data = []
basketball_list = [
    {"id": 1, "name": "Atlanta Hawks", "year_founded": 1949, "championships_won": 1,},
    {"id": 2, "name": "Boston Celtics", "year_founded": 1946, "championships_won": 17,},
    {"id": 3, "name": "Cleveland Cavaliers", "year_founded": 1970, "championships_won": 1,},
    {"id": 4, "name": "New Orleans Pelicans", "year_founded": 2002, "championships_won": 0,},
    {"id": 5, "name": "Chicago Bulls", "year_founded": 1966, "championships_won": 6,},
    {"id": 6, "name": "Dallas Mavericks", "year_founded": 1980, "championships_won": 1,},
    {"id": 7, "name": "Denver Nuggets", "year_founded": 1976, "championships_won": 0,},
    {"id": 8, "name": "Golden State Warriors", "year_founded": 1946, "championships_won": 7,},
    {"id": 9, "name": "Houton Rockets", "year_founded": 1967, "championships_won": 2,},
    {"id": 10, "name": "Los Angeles Clippers", "year_founded": 1970, "championships_won": 0,},
    {"id": 11, "name": "Los Angeles Lakers", "year_founded": 1948, "championships_won": 17,},
    {"id": 12, "name": "Miami Heat", "year_founded": 1988, "championships_won": 3,},
    {"id": 13, "name": "Milwaukee Bucks", "year_founded": 1968, "championships_won": 2,},
    {"id": 14, "name": "Minnesota Timberwolves", "year_founded": 1989, "championships_won": 0,},
    {"id": 15, "name": "Brooklyn Nets", "year_founded": 1976, "championships_won": 0,},
    {"id": 16, "name": "New York Knicks", "year_founded": 1946, "championships_won": 2,},
    {"id": 17, "name": "Orlando Magic", "year_founded": 1989, "championships_won": 0,},
    {"id": 18, "name": "Indiana Pacers", "year_founded": 1976, "championships_won": 0,},
    {"id": 19, "name": "Philadelphia 76ers", "year_founded": 1949, "championships_won": 3,},
    {"id": 20, "name": "Phoenix Suns", "year_founded": 1968, "championships_won": 0,},
    {"id": 21, "name": "Portland Trail Blazers", "year_founded": 1970, "championships_won": 1,},
    {"id": 22, "name": "Sacramento Kings", "year_founded": 1948, "championships_won": 0,},
    {"id": 23, "name": "San Antonio Spurs", "year_founded": 1976, "championships_won": 5,},
    {"id": 24, "name": "Oklahoma City Thunder", "year_founded": 1967, "championships_won": 1,},
    {"id": 25, "name": "Toronto Raptors", "year_founded": 1995, "championships_won": 1,},
    {"id": 26, "name": "Utah Jazz", "year_founded": 1974, "championships_won": 0,},
    {"id": 27, "name": "Memphis Grizzlies", "year_founded": 1995, "championships_won": 0,},
    {"id": 28, "name": "Washington Wizards", "year_founded": 1961, "championships_won": 1,},
    {"id": 29, "name": "Detroit Pistons", "year_founded": 1948, "championships_won": 3,},
    {"id": 30, "name": "Charlotte Hornets", "year_founded": 1988, "championships_won": 0,}
]

def initBasketballs():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in basketball_list:
        Basketball_data.append({"id":item_id,"results":item})
        item_id += 1
        
# Return all jokes from jokes_data
def getBasketballs():
    return(Basketball_data)

# Joke getter
def getBasketball(id):
    return(Basketball_data[id])

# Number of jokes
def countData():
    return len(Basketball_data)

# Test Joke Model
if __name__ == "__main__": 
    initBasketballs()  # initialize jokes