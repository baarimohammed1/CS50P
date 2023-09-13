def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]
    months_dict = {
        "January":"01",
        "February":"02",
        "March":"03",
        "April":"04",
        "May":"05",
        "June":"06",
        "July":"07",
        "August":"08",
        "September":"09",
        "October":"10",
        "November":"11",
        "December":"12"
        }
    years, month, day = get_date("Date: ")
    if month in months:
        print(years,"-",months_dict[month],"-",f"{day:02}",sep="" )
    else:
        month =int(month)
        print(years,"-", f"{month:02}","-", f"{day:02}", sep="")







def get_date(phrase):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]
    months_dict = {
        "January":"01",
        "February":"02",
        "March":"03",
        "April":"04",
        "May":"05",
        "June":"06",
        "July":"07",
        "August":"08",
        "September":"09",
        "October":"10",
        "November":"11",
        "December":"12"
    }
    while True:
        try:
            date = input(phrase)
            if " " and "," in date:
                month, day, year = date.split(" ")
                day = day.strip(",")
                day = int(day)
                if int(day) > 31:
                    continue
                if month in months:
                    return year, month, day
                    print(year,"-",months_dict[month],"-",f"{day:02}",sep="" )
            if "/" in date:
                month, day, year = date.split("/")
                if int(month) > 12:
                    continue
                if int(day) > 31:
                    continue
                if int(year) < 1000:
                    continue
                year=int(year)
                day=int(day)
                return year, month, day
        except (KeyError, ValueError, EOFError):
            pass

main()