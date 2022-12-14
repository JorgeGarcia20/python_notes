import random

# Using the filter function
numbers = [n for n in range(1, random.randint(1, 21))]

is_even = lambda x: x % 2 == 0
evens = list(filter(is_even, numbers))
print(evens)
print(numbers)

# filter function in a dictionary
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

winners = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(len(winners))
print(winners)
