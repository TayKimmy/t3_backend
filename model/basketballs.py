Basketball_data = []
basketball_list = {
    "id":{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30},
    "name":{"Atlanta Hawks", "Boston Celtics", "Cleveland Cavaliers", "New Orleans Pelicans", "Chicago Bulls", "Dallas Mavericks", "Denver Nuggets", "Golden State Warriors", "Houston Rockets", "Los Angeles Clippers", "Los Angeles Lakers", "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "Brooklyn Nets", "New York Knicks", "Orlando Magic", "Indiana Pacers", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Oklahoma City Thunder", "Toronto Raptors", "Utah Jazz", "Memphis Grizzlies", "Washington Wizards", "Detroit Pistons", "Charlotte Hornets"},
    "year_founded":{1949, 1946, 1970, 2002, 1966, 1980, 1976, 1946, 1967, 1970, 1948, 1988, 1968, 1989, 1976, 1946, 1989, 1976, 1949, 1968, 1970, 1948, 1976, 1967, 1995, 1974, 1995, 1961, 1948, 1988},
    "championships_won":{1, 17, 1, 0, 6, 1, 0, 7, 2, 0, 17, 3, 2, 0, 0, 2, 0, 0, 3, 0, 1, 0, 5, 1, 1, 0, 0, 1, 3, 0}
}

def initBasketball():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in basketball_list:
        Basketball_data.append({"id":item_id,"results":item})
        item_id += 1
        
# Return all jokes from jokes_data
def getBasketball():
    return(Basketball_data)

# Joke getter
def getBasketballs(id):
    return(Basketball_data[id])

# Number of jokes
def countData():
    return len(Basketball_data)

# Test Joke Model
if __name__ == "__main__": 
    initBasketball()  # initialize jokes