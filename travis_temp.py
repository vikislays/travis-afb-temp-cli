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

elif user_input == "3":
    first_year = int(input("Enter the first year: "))
    second_year = int(input("Enter the second year: "))

    # with open('74516_monthly.csv', newline='') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')

    #     for row in reader:


else:
    print("Please choose one of the options.")

def monthly_temps():
    pass

# What do you want to do?

# View daily temperatures for a month (2025 only)
# View monthly temperatures for a year
# Compare two years

