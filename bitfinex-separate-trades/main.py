import sys
import pandas as pd
sys.path.append('../common')
from custom import CustomFile


def main(f_trades, f_positions):
  t_trades = pd.read_csv(f_trades, parse_dates=[6])
  t_positions = pd.read_csv(f_positions, parse_dates=[8, 9])

  t_margin = pd.DataFrame(columns=['#', 'PAIR,AMOUNT', 'PRICE,FEE', 'FEE CURRENCY', 'DATE,ORDER ID'])

  for _, pos in t_positions.iterrows():
    w_trades = t_trades[
      (t_trades['PAIR'] == pos['PAIR'])
      & (pos['CREATED'] <= t_trades['DATE'])
      & (t_trades['DATE'] <= pos['UPDATED'])
    ]
    for i, margin in w_trades.iterrows():
      t_margin = t_margin.append(margin, ignore_index=True)
      t_trades = t_trades.drop(i)

  t_margin.to_csv('margin.csv', index=False)
  t_trades.to_csv('spot.csv', index=False)


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print ('usage : python3 main.py trades.csv positions.csv')
    sys.exit(1)
  main(sys.argv[1], sys.argv[2])
