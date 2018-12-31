import sys
import pandas as pd
sys.path.append('../common')
from custom import CustomFile


def main(filename):
  t = pd.read_csv(filename)
  t_settlement = t[t['DESCRIPTION'].str.contains('Settlement')]

  out = CustomFile()

  for i in range(0, len(t_settlement), 2):
    buy_row  = t_settlement.iloc[i]
    sell_row = t_settlement.iloc[i+1]
    out.append(buy_row['DATE'], 'BUY', 'Bitfinex(custom)', buy_row['CURRENCY'], '', '', buy_row['AMOUNT'], abs(sell_row['AMOUNT'] / buy_row['AMOUNT']), sell_row['CURRENCY'], 0, 'JPY', 'Bitfinex Mergin Settlement')

  out.write()


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print ('usage : python3 main.py filename')
    sys.exit(1)
  main(sys.argv[1])
