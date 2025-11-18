# function returns a list of users with birthday upcoming in next 7 days

#users list have 'name' and 'birthday' fields
# function for business process: need to return list for birthdays that will be on weekend and on Monday it will appear with tag "birthday on weekend"


from datetime import datetime, timedelta


def get_upcoming_birthdays(users:list, following_days: int = 7) -> list:
    """ Returns a list of users with birthdays in the next 7 days.
    Weekend birthdays (Sat/Sun) are tagged as belated.
    
    Each user must have: {'name': str, 'birthday': 'YYYY-MM-DD'}
    """
    today = datetime.now().date()
    end_date = today + timedelta(days=following_days)
    upcoming_birthdays = []

    for user in users:
        # Extract month and day
        month_day = user["birthday"][5:]

        # Create a date for this year's birthday
        birthday = datetime.strptime(
            f"{today.year}-{month_day}",
            "%Y-%m-%d"
        ).date()

        # If birthday already passed, shift to next year
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        # Check if within upcoming range
        if today <= birthday < end_date:
            if birthday.weekday() in (5, 6):  # Sat/Sun
                upcoming_birthdays.append(f"{user['name']} (birthday on weekend)")
            else:
                upcoming_birthdays.append(user["name"])

    return upcoming_birthdays

'''
test_users = [
 #Weekend birthdays (should show as belated)
    {'name': 'Anna',    'birthday': '1992-10-11'},  # Saturday
    {'name': 'Brian',   'birthday': '1987-11-20'},  # Sunday

    # Monday–Friday birthdays (should show normal)
    {'name': 'Clara',   'birthday': '1990-10-13'},  # Monday
    {'name': 'Derek',   'birthday': '1985-12-14'},  # Tuesday
    {'name': 'Emma',    'birthday': '1991-11-15'},  # Wednesday
    {'name': 'Felix',   'birthday': '1989-11-16'},  # Thursday
    {'name': 'Gina',    'birthday': '1993-09-17'},  # Friday

    # Outside the next 7 days (should not appear)
    {'name': 'Harry',   'birthday': '1984-11-01'},  # far away
]

get_upcoming_birthdays(test_users, following_days=7)
print(get_upcoming_birthdays(test_users, following_days=7))


'''
