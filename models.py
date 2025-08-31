from dataclasses import dataclass

@dataclass
class WeatherReading:
    date: str           # 'YYYY-MM-DD'
    year: int
    month: int
    day: int
    max_temp: int       # Celsius
    min_temp: int       # Celsius
    humidity: int       # Percent

    def month_name(self):
        import calendar
        return calendar.month_name[self.month]

@dataclass
class YearlySummaryResult:
    highest_temp: int
    highest_day: str
    lowest_temp: int
    lowest_day: str
    humidity: int
    most_humid_day: str

@dataclass
class MonthlyAveragesResult:
    avg_high: int
    avg_low: int
    avg_humidity: int

@dataclass
class ChartDay:
    day: int
    high: int
    low: int