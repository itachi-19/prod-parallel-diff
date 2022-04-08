#! /usr/bin/env python3

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 itachi <itachi@ASUS-G14>
#
# Distributed under terms of the MIT license.

from xml_msg import XMLMsg

def TradeDiffer:


    def __init__(self, trades):
        self.trades = trades

    def get_diffs(self):
        diffs = []
        for trade_id in trades:
            diffs.append(trade_id, self.get_xpath_diffs(trades[trade_id]))
        return diffs

    def get_xpath_diffs(self, trade_messages):
        trade_icapture = trade_messages[0]
        trade_fidstp = trade_messages[1]
        xml_icapture = XMLMsg(trade_icapture)
        xml_fidstp = XMLMsg(fidstp)
        return get_diffs_between_xmls(xml_icapture, xml_fidstp)

    def get_diffs_between_xmls(xml1, xml2):
        xpaths1 = xml1.get_xpaths()
        xpaths2 = xml2.get_xpaths()
        union = xpaths1 | xpaths2
        paths_not_in_1 = union - xpath1
        paths_not_in_2 = union - xpaths2
