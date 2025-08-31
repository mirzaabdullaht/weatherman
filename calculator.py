from models import YearlySummaryResult, MonthlyAveragesResult, ChartDay

def yearly_summary(readings, year):
    year_readings = [r for r in readings if r.year == year]
    if not year_readings:
        return None
    high = max(year_readings, key=lambda x: x.max_temp)
    low = min(year_readings, key=lambda x: x.min_temp)
    humid = max(year_readings, key=lambda x: x.humidity)
    return YearlySummaryResult(
        highest_temp=high.max_temp,
        highest_day=f"{high.month_name()} {high.day}",
        lowest_temp=low.min_temp,
        lowest_day=f"{low.month_name()} {low.day}",
        humidity=humid.humidity,
        most_humid_day=f"{humid.month_name()} {humid.day}"
    )

def monthly_averages(readings, year, month):
    month_readings = [r for r in readings if r.year == year and r.month == month]
    if not month_readings:
        return None
    avg_high = round(sum(r.max_temp for r in month_readings) / len(month_readings))
    avg_low = round(sum(r.min_temp for r in month_readings) / len(month_readings))
    avg_hum = round(sum(r.humidity for r in month_readings) / len(month_readings))
    return MonthlyAveragesResult(avg_high, avg_low, avg_hum)

def chart_data(readings, year, month):
    chart_days = []
    for r in sorted([r for r in readings if r.year == year and r.month == month], key=lambda x: x.day):
        chart_days.append(ChartDay(r.day, r.max_temp, r.min_temp))
    return chart_days

def combined_chart_data(readings, year, month):
    return chart_data(readings, year, month)