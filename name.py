from datetime import datetime

def calculate_days_between_dates(begin, end, fmt="%Y-%m-%d"):
    d1 = datetime.strptime(begin, fmt)
    d2 = datetime.strptime(end, fmt)
    return abs((d2 - d1).days)