#! /usr/bin/env python3

import csv

class Reader:
    def __init__(self, icap_file='icapture.csv', fid_file='fidstp.csv'):
        self.data = {}
        self.read_into_dict(icap_file, 'icap_msg')
        self.read_into_dict(fid_file, 'fid_msg')

    def read_into_dict(self, csv_file, msg_type):
        with open(csv_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                trade_id = row['TradeID']
                message = row['DestinationMSG']
                if trade_id not in self.data:
                    self.data[trade_id] = {}
                self.data[trade_id][msg_type] = message

