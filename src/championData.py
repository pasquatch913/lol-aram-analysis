import requests
import pandas as pd


class ChampionData:
    champion_data = []

    def __init__(self):
        # scrape metasrc.com for aram data
        metasrc_url = 'https://www.metasrc.com/na/aram/champions'
        metasrc_headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.get(metasrc_url, headers=metasrc_headers)
        raw_data = pd.read_html(r.text)[0].values.tolist()  # Returns list of all tables on page

        champion_data = []

        for row in raw_data:
            champion_data.append({
                "name": row[0],
                "primary": row[1],
                "secondary": row[2],
                "tier": row[3],
                "score": row[4],
                "trend": row[5],
                "win%": row[6],
                "pick%": row[7],
                "kda": row[9]
            })
