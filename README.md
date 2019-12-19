# ItC-python-hw
* ### Team members:  
  B08902005  
  B06201018
* ### Environment:  
  Ubuntu 18.04, Python 3.6.9
---
__This project crawls the contents from [Announcement system-NTU CSIE](https://www.csie.ntu.edu.tw/news/news.php?class=101) and saves the results to a CSV file.__  

On the command line, run  
```
python3 main.py --start-date [start date] --end-date [end date] --output [out filename]
```
where `--start-date` and `--end-date` specify the date range of your choice, and `--output` is the CSV filename to save.  
Note that `--start-date` and `--end-date` should be in the format of `[Year]-[month]-[day]`.  

For example, running  
```
python3 main.py --start-date 2019-01-01 --end-date 2019-11-04 --output output.csv
```
will give you a CSV file `output.csv` that contains every announcement from 2019/01/01 to 2019/11/04.
