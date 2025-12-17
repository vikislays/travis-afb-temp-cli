import csv

# with open('74516_monthly.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         print(row[0])

def get_month_name(month_number):
    if month_number == 1:
        return "Jan"
    elif month_number == 2:
        return "Feb"
    elif month_number == 3:
        return "Mar"
    elif month_number == 4:
        return "Apr"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "Jun"
    elif month_number == 7:
        return "Jul"
    elif month_number == 8:
        return "Aug"
    elif month_number == 9:
        return "Sep"
    elif month_number == 10:
        return "Oct"
    elif month_number == 11:
        return "Nov"
    elif month_number == 12:
        return "Dec"
    else:
        return str(month_number)


user_input = input("Choose one of the three options:\n" \
"(1) View daily temperatures for a month (2025 only)\n" \
"(2) View monthly temperatures for a year\n" \
"(3) Compare two years\n")

if user_input == "1":
    month = int(input("Enter month (1-12): "))

    daily_temps = []

    min_daily_temp = None
    min_day = None

    max_daily_temp = None
    max_day = None

    with open('74516_daily_2025.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            try:
                file_month = int(row[1])
                file_day = int(row[2])
                file_daily_temp = float(row[3])
                if file_month == month:
                    daily_temps.append(file_daily_temp)
                    
                    if min_daily_temp == None:
                        min_daily_temp = file_daily_temp
                        min_day = file_day
                    
                    else:
                        if file_daily_temp < min_daily_temp:
                            min_daily_temp = file_daily_temp
                            min_day = file_day

                    if max_daily_temp == None:
                        max_daily_temp = file_daily_temp
                        max_day = file_day
                    
                    else:
                        if file_daily_temp > max_daily_temp:
                            max_daily_temp = file_daily_temp
                            max_day = file_day

            except ValueError:
                pass

        month_average = round(sum(daily_temps)/len(daily_temps), 1)
        print("\n")
        print("Travis AFB - Daily Summary")
        print("Year: 2025")
        print(f"Min: {get_month_name(month)} {min_day}, {min_daily_temp}°C")
        print(f"Max: {get_month_name(month)} {max_day}, {max_daily_temp}°C")
        print(f"Avg: {month_average}°C")
        print("\n")

elif user_input == "2":
    year = int(input("Enter year (e.g. 2025): "))

    year_temepratures = []
    
    min_temp = None
    min_month = ""

    max_temp = None
    max_month = ""

    with open('74516_monthly.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        print("Travis AFB - Monthly Averages")        
        print("\n")
        print("Month\t| Avg Temp (°C)")
        print("-----\t| ------------")
        for row in reader:
            try:
                file_year = int(row[0])
                file_month = int(row[1])
                file_temp = float(row[2])
                
                if file_year == year:
                    print(f"{get_month_name(file_month)}\t| {file_temp}")

                    year_temepratures.append(file_temp)
                    if min_temp == None:
                        min_temp = file_temp
                        min_month = file_month

                    else:
                        if file_temp < min_temp:
                            min_temp = file_temp
                            min_month = file_month

                    if max_temp == None:
                        max_temp = file_temp
                        max_month = file_month

                    else: 
                        if file_temp > max_temp:
                            max_temp = file_temp
                            max_month = file_month 

            except ValueError:
                pass


        year_average = round(sum(year_temepratures)/len(year_temepratures), 1)
        print("\n")
        print(f"Lowest temperature in {year} was: {min_temp}°C in {get_month_name(min_month)}.")
        print(f"Highest temperature in {year} was: {max_temp}°C in {get_month_name(max_month)}.")
        print(f"Average temperature in {year} was: {year_average}°C")
        print("\n")

elif user_input == "3":
    first_year = int(input("Enter the first year: "))
    second_year = int(input("Enter the second year: "))
    
    difference = None
    first_year_temp = []
    second_year_temp = []
    difference_in_temps = []
    month_temp_first_year = []
    month_temp_second_year = [] 

    with open('74516_monthly.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            try:
                file_year = int(row[0])
                file_month = int(row[1])
                file_temp = float(row[2])
                
                if first_year == file_year:
                    first_year_temp.append(file_temp)
                    month_temp_first_year.append(file_month)

                if second_year == file_year:
                    second_year_temp.append(file_temp)
                    month_temp_second_year.append(file_month)

            except ValueError:
                pass

    if len(first_year_temp) == len(second_year_temp) and len(first_year_temp) > 0:
        for temp1, temp2 in zip(first_year_temp, second_year_temp):
            difference = temp2 - temp1
            difference_in_temps.append(round(difference, 1))

        print(f"\nTRAVIS AFIB - Monthly Avg Comparison: {first_year} vs {second_year}")
        print(f"Month\t|  {first_year}\t| {second_year}\t| Diff")
        print("-" * 35)

        for month_index in month_temp_first_year:
            print(f"{get_month_name(month_index)}\t|  {first_year_temp[month_index - 1]}\t| {second_year_temp[month_index - 1]}\t| {difference_in_temps[month_index - 1]}")
    else:
        print("Error: The data for the two years could not be properly compared (e.g., missing months).") 
else:
    print("Invalid option selected.")