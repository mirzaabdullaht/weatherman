import sys
from parser import parse_files
from calculator import yearly_summary, monthly_averages, chart_data, combined_chart_data
from report import print_yearly_summary, print_monthly_averages, print_daily_chart, print_combined_chart

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: weatherman.py /path/to/files-dir [options]")
        print("Options: -e YEAR | -a YEAR/MONTH | -c YEAR/MONTH | -b YEAR/MONTH")
        return

    dir_path = args[0]
    readings = parse_files(dir_path)

    i = 1
    while i < len(args):
        if args[i] == '-e' and i+1 < len(args):
            try:
                year = int(args[i+1])
                result = yearly_summary(readings, year)
                print_yearly_summary(result)
            except Exception:
                print("Invalid year for -e")
            i += 2
        elif args[i] == '-a' and i+1 < len(args):
            try:
                y, m = map(int, args[i+1].replace('\\', '/').split('/'))
                result = monthly_averages(readings, y, m)
                print_monthly_averages(result)
            except Exception:
                print("Invalid year/month for -a")
            i += 2
        elif args[i] == '-c' and i+1 < len(args):
            try:
                y, m = map(int, args[i+1].replace('\\', '/').split('/'))
                chart = chart_data(readings, y, m)
                print_daily_chart(chart, y, m)
            except Exception:
                print("Invalid year/month for -c")
            i += 2
        elif args[i] == '-b' and i+1 < len(args):
            try:
                y, m = map(int, args[i+1].replace('\\', '/').split('/'))
                chart = combined_chart_data(readings, y, m)
                print_combined_chart(chart, y, m)
            except Exception:
                print("Invalid year/month for -b")
            i += 2
        else:
            i += 1

if __name__ == "__main__":
    main()