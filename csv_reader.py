
import csv


class CSVReader:
    
    def __init__(self, file_name):
        self.file_name = file_name

    def get_trades(self):
        trades = {}
        with open(self.file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                trade_id = row['TradeID']
                message = row['DestinationMSG']
                if trade_id not in trades:
                    trades[trade_id] = {}
                trades[trade_id] = message
        return trades
