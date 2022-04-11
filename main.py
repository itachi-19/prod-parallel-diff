#! /usr/bin/env python3


import sys
from reader.trade_reader import TradeReader


if __name__=='__main__':
    icapture = sys.argv[1]
    fidstp = sys.argv[2]

    reader = TradeReader(icapture, fidstp)
    missing_trades = reader.get_missing_trades()
    trades = reader.get_merged_trades()
    print(trades)
    #diffs = trade_differ.get_diffs(trades)
