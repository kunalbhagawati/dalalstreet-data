> Forked from https://github.com/jugaad-py/jugaad-data (https://pypi.org/project/jugaad-data/)

# Introduction

`dalalstreet-data` is a python library to download historical/live stock, index as well as economic data from NSE and RBI website using.


# Features

* Supports [new NSE website](https://www.nseindia.com/), (All libraries based on old NSE website might stop working)
* Powerful CLI (Command line interface), Even non-coders can use it easily
* Built-in caching mechanism to play nice with NSE. Avoid making un-necessary requests to NSE's website and getting blocked
* Optional `pandas` support 

**Road map**

| Website  | Segment    | Supported? |
|----------|------------|------------|
| NSE      | Stocks     | Yes        |
| NSE      | Stocks F&O | Yes        |
| NSE      | Index      | Yes    |
| NSE      | Index F&O  | Yes        |
| RBI	   | Current Rates| Yes |

# Getting started

## Python interface

### Historical data

```python
from datetime import date
from dalalstreet_data.nse import bhavcopy_save, bhavcopy_fo_save

# Download bhavcopy
bhavcopy_save(date(2020, 1, 1), "/path/to/directory")

# Download bhavcopy for futures and options
bhavcopy_fo_save(date(2020, 1, 1), "/path/to/directory")

# Download stock data to pandas dataframe
from dalalstreet_data.nse import stock_df

df = stock_df(symbol="SBIN", from_date=date(2020, 1, 1),
              to_date=date(2020, 1, 30), series="EQ")
```
### Live data

```python
from dalalstreet_data.nse import NSELive

n = NSELive()
q = n.stock_quote("HDFC")
print(q['priceInfo'])
```

```
{'lastPrice': 2635,
 'change': -49.05000000000018,
 'pChange': -1.8274622305843848,
 'previousClose': 2684.05,
 'open': 2661,
 'close': 2632.75,
 'vwap': 2645.57,
 'lowerCP': '2415.65',
 'upperCP': '2952.45',
 'pPriceBand': 'No Band',
 'basePrice': 2684.05,
 'intraDayHighLow': {'min': 2615.6, 'max': 2688.45, 'value': 2635},
 'weekHighLow': {'min': 1473.45,
  'minDate': '24-Mar-2020',
  'max': 2777.15,
  'maxDate': '13-Jan-2021',
  'value': 2635}}
```

## Command line interface

```
$ dalalstreet stock --help

Usage: dalalstreet stock [OPTIONS]

  Download historical stock data

  $dalalstreet stock --symbol STOCK1 -f yyyy-mm-dd -t yyyy-mm-dd --o file_name.csv

Options:
  -s, --symbol TEXT  [required]
  -f, --from TEXT    [required]
  -t, --to TEXT      [required]
  -S, --series TEXT  [default: EQ]
  -o, --output TEXT
  --help             Show this message and exit.
```

```
$ dalalstreet stock -s SBIN -f 2020-01-01 -t 2020-01-31 -o SBIN-Jan.csv
SBIN  [####################################]  100%

Saved file to : SBIN-Jan.csv
```

## Download historical derivatives (F&O) data

```
$ dalalstreet deriviatives --help
Usage: cli.py derivatives [OPTIONS]

  Sample usage-

  Download stock futures-

  dalalstreet derivatives -s SBIN -f 2020-01-01 -t 2020-01-30 -e 2020-01-30 -i FUTSTK -o file_name.csv

  Download index futures-

  dalalstreet derivatives -s NIFTY -f 2020-01-01 -t 2020-01-30 -e 2020-01-30 -i FUTIDX -o file_name.csv

  Download stock options-

  dalalstreet derivatives -s SBIN -f 2020-01-01 -t 2020-01-30 -e 2020-01-30 -i OPTSTK -p 330 --ce -o file_name.csv

  Download index options-

  dalalstreet derivatives -s NIFTY -f 2020-01-01 -t 2020-01-30 -e 2020-01-23 -i OPTIDX -p 11000 --pe -o file_name.csv

Options:
  -s, --symbol TEXT  Stock/Index symbol  [required]
  -f, --from TEXT    From date - yyyy-mm-dd  [required]
  -t, --to TEXT      To date - yyyy-mm-dd  [required]
  -e, --expiry TEXT  Expiry date - yyyy-mm-dd  [required]
  -i, --instru TEXT  FUTSTK - Stock futures, FUTIDX - Index Futures, OPTSTK -
                     Stock Options, OPTIDX - Index Options  [required]

  -p, --price TEXT   Strike price (Only for OPTSTK and OPTIDX)
  --ce / --pe        --ce for call and --pe for put (Only for OPTSTK and
                     OPTIDX)

  -o, --output TEXT  Full path of output file
  --help             Show this message and exit.
```
