from datetime import datetime, date, timedelta

def get_birthdate():
    while True:
        try:
            birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
            birthdate = datetime.strptime(birth_str, "%Y-%m-%d").date()
            if birthdate >= date.today():
                print("You can't be born in the future! Try again.")
                continue
            return birthdate
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD.")

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

def next_birthday(birthdate):
    today = date.today()
    next_bday = date(today.year, birthdate.month, birthdate.day)
    if next_bday < today:
        next_bday = date(today.year + 1, birthdate.month, birthdate.day)
    return next_bday

def main():
    birthdate = get_birthdate()
    age = calculate_age(birthdate)
    next_bday = next_birthday(birthdate)

    days_remaining = (next_bday - date.today()).days
    hours_remaining = days_remaining * 24

    print(f"\n🎂 You are {age} years old.")
    print(f"⏳ {days_remaining} days ({hours_remaining} hours) until your next birthday on {next_bday.strftime('%A, %B %d')}.")

if __name__ == "__main__":
    main()