import requests
import pandas as pd
import datetime

url = "https://prod-public-api.livescore.com/v1/api/app/live/soccer/0?MD=1"
jsonData = requests.get(url).json()

rows = []
for stage in jsonData['Stages']:
    events = stage['Events']
    for event in events:
        gameId = event['Eid']
        url1 = "https://prod-public-api.livescore.com/v1/api/app/statistics/soccer/" + gameId
        stats = requests.get(url1).json()
        
        gameDateTime = event['Esd']
        date_time_obj = datetime.datetime.strptime(str(gameDateTime), '%Y%m%d%H%M%S')
        gameTime = date_time_obj.strftime("%H:%M")
        homeTeam = event['T1'][0]['Nm']
        homeScore = event['Tr1']
        homeCorners = stats['Stat'][0]['Cos']
        #homeCorners = tempStats['Cos']
        
        awayTeam = event['T2'][0]['Nm']
        awayScore = event['Tr2']
        
        matchClock = event['Eps']
        
        row = {
            'GameId':gameId,
            'Home':homeTeam,
            'Home Score':homeScore,
            'Away':awayTeam,
            'Away Score':awayScore,
            'Match Clock':matchClock,
            'Home Corners':homeCorners,
            
}
        rows.append(row)
        
live_df = pd.DataFrame(rows)

print(live_df)
#print(stats)