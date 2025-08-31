import os
from models import WeatherReading

def parse_files(dir_path):
    readings = []
    for file_name in os.listdir(dir_path):
        if not file_name.endswith('.txt'):
            continue
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, encoding='utf-8') as f:
            try:
                next(f)  # skip header
            except StopIteration:
                continue  # skip empty files
            for line in f:
                parts = line.strip().split(',')
                if len(parts) < 4 or not parts[0]:
                    continue
                date, max_temp, min_temp, humidity = parts[:4]
                try:
                    year, month, day = map(int, date.split('-'))
                    readings.append(WeatherReading(
                        date=date,
                        year=year, month=month, day=day,
                        max_temp=int(max_temp),
                        min_temp=int(min_temp),
                        humidity=int(humidity)
                    ))
                except Exception:
                    continue
    return readings