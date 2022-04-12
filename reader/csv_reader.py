
import csv


class CSVReader:
    
    def get_trades_for(self, file_name):
        trades = {}
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                trade_id = row['TradeID']
                message = row['DestinationMSG']
                if trade_id not in trades:
                    trades[trade_id] = {}
                trades[trade_id] = message
        return trades
