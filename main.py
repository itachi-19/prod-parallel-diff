#! /usr/bin/env python3


import sys

from reader.trade_reader import TradeReader
from differ.trade_differ import TradeDiffer
from writer.diff_writer import DiffWriter

from pprint import pprint


if __name__=='__main__':
    icapture_file = sys.argv[1]
    fidstp_file = sys.argv[2]
    report_file = sys.argv[3]

    reader = TradeReader(icapture_file, fidstp_file)
    differ = TradeDiffer()
    writer = DiffWriter(report_file)

    print(f'[!] iCapture File: {icapture_file}, FIDSTP File: {fidstp_file}')

    missing_trades = reader.get_missing_trades()
    print(f'[!] Found {len(missing_trades)} Missing Trades')

    trades = reader.get_merged_trades()
    print('[!] Generated Trade Data')

    all_diffs = differ.get_all_diffs(trades)
    print('[!] Generated Trade Diffs')

    writer.write(all_diffs, missing_trades)
    print('[!] Writing Diffs to Report')

    print('[!] Generated Report!')
