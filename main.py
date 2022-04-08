#! /usr/bin/env python3


import xml_msg
import sys
from trade_reader import TradeReader
from xml_msg import XMLMsg


if __name__=='__main__':
    icapture = sys.argv[1]
    fidstp = sys.argv[2]

    reader = TradeReader(icapture, fidstp)
    missing_trades = reader.get_missing_trades()
    trades = reader.get_trades()
    diffs = trade_differ.get_diffs(trades)
