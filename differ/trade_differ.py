from differ.xml_differ import XMLDiffer


class TradeDiffer:
    
    @staticmethod
    def get_all_diffs(merged_trades):
        all_diffs = []

        for trade_id in merged_trades:
            trades = merged_trades[trade_id]
            icapture_msg = trades[0]
            fidstp_msg = trades[1]
            xml_differ = XMLDiffer(icapture_msg, fidstp_msg)
            diffs_for_trade = xml_differ.get_diff_between_xpaths()
            all_diffs.append((trade_id, diffs_for_trade))

        return all_diffs;
