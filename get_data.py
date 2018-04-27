from models import db, Neo
import requests
import random


def get_from_neodys():
    url = 'https://newton.dm.unipi.it/~neodys2/neo_name.list'

    r = requests.get(url)

    neos = []

    for line in r.text.splitlines():
        parts = line.split()
        neo = {}
        if len(parts) == 2:
            neo['name'] = parts[1].strip()
            neo['number'] = parts[0].strip()
        elif len(parts) == 1:
            neo['name'] = parts[0].strip()
            neo['number'] = None
        else:
            continue

        neo['absolute_magnitude'] = float(random.randrange(50, 500)) / 100
        neo['slope_parameter'] = float(random.randrange(10, 100)) / 100
        neo['perihelion'] = float(random.randrange(50, 300)) / 100
        neo['aphelion'] = float(random.randrange(50, 300)) / 100
        neos.append(neo)

    Neo.insert_many(neos).execute()


if __name__ == "__main__":
    db.connect()

    if not Neo.table_exists():
        db.create_tables([Neo])

    get_from_neodys()
