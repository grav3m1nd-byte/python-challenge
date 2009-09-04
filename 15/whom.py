from calendar import datetime

for year in range(1000,1996):
    dt = datetime.datetime(year,1,26)
    if "6" == str(year)[-1] and 0 == dt.weekday():
        print dt
        
