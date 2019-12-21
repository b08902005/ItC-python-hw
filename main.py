import os
import pandas as pd
from crawler import Crawler
from args import get_args

if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    content = crawler.crawl(args.start_date, args.end_date)
    df = pd.DataFrame(content, columns=['Post date', 'Title', 'Content'])
    cwd = os.getcwd()
    filename = os.path.join(cwd, args.output)
    df.to_csv(filename, encoding='utf_8_sig')
