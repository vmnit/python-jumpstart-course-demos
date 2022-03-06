import datetime


def printAppBanner():
    print("--------------------------------------")
    print("             BIRTHDAY APP             ")
    print("--------------------------------------")


def getBirthday():
    print("What is your birth date?")
    year = int(input("Year [YYY]? "))
    month = int(input("Month [MM]? "))
    day = int(input("Day [DD]? "))
    return datetime.date(year, month, day)


def currDate():
    return datetime.date.today()


def get_days_difference(current_date, birthday):
    #print(current_date)
    #print(birthday)
    this_year_birthday = datetime.date(current_date.year, birthday.month, birthday.day)
    next_year_birthday = datetime.date(current_date.year+1, birthday.month, birthday.day)
    #print(this_year_birthday)
    diffT = this_year_birthday - current_date
    diffN = next_year_birthday - current_date
    if (abs(diffT.days) > diffN.days):
        return diffN.days

    return diffT.days


def printMessage(days_difference):
    if days_difference == 0:
        print("Today is your birthday, Happy Birthday!!!")
    elif days_difference > 0:
        print("Looks like your birthday is in {} days".format(days_difference))
    else:
        print("Looks like your birthday was {} days before".format(abs(days_difference)))


def main():
    printAppBanner()
    birthday = getBirthday()
    current_date = currDate()

    days_difference = get_days_difference(current_date, birthday)
    printMessage(days_difference)


main()
