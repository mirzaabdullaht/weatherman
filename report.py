from models import YearlySummaryResult, MonthlyAveragesResult, ChartDay

def print_yearly_summary(result: YearlySummaryResult):
    if not result:
        print("No data for requested year.")
        return
    print(f"Highest: {result.highest_temp}C on {result.highest_day}")
    print(f"Lowest: {result.lowest_temp}C on {result.lowest_day}")
    print(f"Humidity: {result.humidity}% on {result.most_humid_day}")

def print_monthly_averages(result: MonthlyAveragesResult):
    if not result:
        print("No data for requested month.")
        return
    print(f"Highest Average: {result.avg_high}C")
    print(f"Lowest Average: {result.avg_low}C")
    print(f"Average Mean Humidity: {result.avg_humidity}%")

def print_daily_chart(chart_days, year, month):
    import calendar
    month_name = calendar.month_name[month]
    print(f"{month_name} {year}")
    for day in chart_days:
        red_bars = '+' * day.high
        blue_bars = '+' * day.low
        print(f"{day.day:02d} \033[91m{red_bars}\033[0m {day.high}C")
        print(f"{day.day:02d} \033[94m{blue_bars}\033[0m {day.low}C")

def print_combined_chart(chart_days, year, month):
    import calendar
    month_name = calendar.month_name[month]
    print(f"{month_name} {year}")
    for day in chart_days:
        bars = '+' * (day.high + day.low)
        print(f"{day.day:02d} {bars} {day.low}C - {day.high}C")