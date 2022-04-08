from csv_reader import CSVReader


class TradeReader():
    
    def __init__(self, icapture, fidstp):
        self.icapture = icapture
        self.fidstp = fidstp
        self.icapture_trades = self.get_trades_for(self.icapture)
        self.fidstp_trades = self.get_trades_for(self.fidstp)

    @staticmethod
    def get_trades_for(file_name):
        reader = CSVReader(file_name)
        return reader.get_trades()

    def get_trades(self):
        trades = self.combine_trades()
        return trades

    @staticmethod
    def get_trade_ids(trades):
        return set(trades)

    def get_missing_trades(self):
        icapture_trade_ids = self.get_trade_ids(self.icapture_trades)
        fidstp_trade_ids = self.get_trade_ids(self.fidstp_trades)
        return icapture_trade_ids - fidstp_trade_ids

    def combine_trades(self):
        trades = {
            trade_id: (self.icapture_trades[trade_id], self.fidstp_trades[trade_id])
            for trade_id in self.fidstp_trades
        }
        return trades
