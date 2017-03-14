import requests
from prettytable import PrettyTable
import click

table = PrettyTable(["Position","Team", "Played Games", "Wins", "Draws", "Losses","Goals For", "Goals Against", "Points"])
premier_league_table = requests.get("https://heisenbug-premier-league-live-scores-v1.p.mashape.com/api/premierleague/table",
  headers={
    "X-Mashape-Key": "hScR2YKaw6mshHF7Swl6Q69gfsGlp1PIyzDjsn7jstFD5qhP91",
    "Accept": "application/json"
  }
)
r = premier_league_table.json()['records']
for index, i in enumerate(r):
    table.add_row([(index + 1), i['team'], i['played'], i['win'], i['draw'], i['loss'], i['goalsFor'], i['goalsAgainst'], i['points']]  )
print(table)
