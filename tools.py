import numpy as np
import pandas as pd
import datetime
from collections import Counter

def load_dataframe():
    file = 'data.txt'
    data = []

    branches = []
    categories = []
    days = []
    hours = []
    count = []
    
    lines = []
    counter = Counter()
    
    FIN = open(file, 'r')
    for line in FIN:
        line = line.strip()
        lines.append(line)
        counter[line] += 1
    FIN.close()

    for line in counter:
        count.append(counter[line])
        line = line.split()
        branches.append(int(line[0]))
        categories.append(line[1])
        days.append(datetime.datetime.strptime(line[2], "%d.%m.%Y").date())
        hours.append(int(line[3]))

    df = pd.DataFrame({
            "SUBBRANCH_ID":  pd.Series(branches),
            "OPCAT_CATEGORY":  pd.Series(categories),
            "DAY":  pd.Series(days),
            "HOUR":  pd.Series(hours),
            "SIZE":  pd.Series(count),
        })
    return df