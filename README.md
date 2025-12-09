# Travis AFB Temperature Explorer (CLI)

A simple command-line program that lets users explore historical temperature data from **one weather station: Travis Air Force Base** using **Meteostat bulk CSV data**.

This is a student project focused on:
- working with real-world datasets
- user-driven program flow
- statistics over time ranges
- reading CSV files **without external libraries**

## Data Source

We use Meteostat’s Bulk Data service:  
https://dev.meteostat.net/bulk/

Id for Travis AFB station is **74516**. This can be in json file from https://bulk.meteostat.net/v2/stations/full.json.gz.

Temperature data(csv) are downloadble using station id: 
1. https://data.meteostat.net/daily/{year}/{station}.csv.gz
2. https://data.meteostat.net/monthly/{station}.csv.gz


## Features

When you start the program, it asks:

**What do you want to do?**
1. View **daily temperatures for a month (2025 only)**
2. View **monthly temperatures for a year**
3. **Compare two years**

---

## 1) View daily temperatures for a month

**Inputs**
- Year
- Month

**Returns**
- **Min temperature**
- **Max temperature**
- **Average temperature**
- **Median temperature**

Example output:
```
Travis AFB - Daily Summary
Period: 2023-07

Min: 12.3°C
Max: 36.1°C
Avg: 24.8°C
Median: 24.5°C
```

---

## 2) View monthly temperatures for a year

**Input**
- Year

**Returns**

### A) Year summary (based on daily data)
- **Min temperature**
- **Max temperature**
- **Average temperature**
- **Median temperature**

### B) Text table of monthly averages
A simple console table replaces charts.

Example:
```
Travis AFB - Monthly Averages
Year: 2023

Month | Avg Temp (°C)
----- | ------------
Jan   |  9.8
Feb   | 10.4
Mar   | 12.2
Apr   | 14.8
May   | 18.9
Jun   | 22.1
Jul   | 24.8
Aug   | 24.0
Sep   | 22.3
Oct   | 18.0
Nov   | 12.7
Dec   |  9.4
```

---

## 3) Compare two years

**Inputs**
- Year 1
- Year 2

**Returns**


### A) Month-by-month comparison text table

Example:
```
Travis AFB - Monthly Avg Comparison

Month | 2023  | 2024  | Diff
----- | ----- | ----- | ----
Jan   |  9.8  | 10.1  | +0.3
Feb   | 10.4  | 11.0  | +0.6
Mar   | 12.2  | 12.9  | +0.7
...
Jul   | 24.8  | 25.6  | +0.8
...
Dec   |  9.4  |  9.1  | -0.3
```

---

