import argparse
from datetime import datetime


def get_args():
    # Add --start-date, --end-date and --output arguments
    # Convert the two dates to datetime objects
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-date', required=True, help='Crawl Start date', dest='start_date')
    parser.add_argument('--end-date', required=True, help='Crawl End date', dest='end_date')
    parser.add_argument('--output', default='crawl.csv', help='Crawl End date', dest='output')
    args = parser.parse_args()
    args.start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
    args.end_date = datetime.strptime(args.end_date, '%Y-%m-%d')
    return args
