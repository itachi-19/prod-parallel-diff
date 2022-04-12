from .csv_reader import CSVReader


class TradeReader():
    
    def __init__(self, icapture_file, fidstp_file):
        reader = CSVReader()
        self.icapture_trades = reader.get_trades_for(icapture_file)
        self.fidstp_trades = reader.get_trades_for(fidstp_file)

    @staticmethod
    def get_trade_ids(trades):
        return set(trades)

    def get_missing_trades(self):
        icapture_trade_ids = self.get_trade_ids(self.icapture_trades)
        fidstp_trade_ids = self.get_trade_ids(self.fidstp_trades)
        return icapture_trade_ids - fidstp_trade_ids

    def merge_trades(self):
        trades = {
            trade_id: (self.icapture_trades[trade_id], self.fidstp_trades[trade_id])
            for trade_id in self.fidstp_trades
        }
        return trades

    def get_merged_trades(self):
        return self.merge_trades()


