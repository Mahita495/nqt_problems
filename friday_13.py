import datetime

def find_friday(month, year):

    try:
        date_obj = datetime.datetime(year,month,13)
        if date_obj.weekday==4:
            return True
        return False
    except ValueError:
        return False
    
month=4
year=2033
print(find_friday(month,year))


    