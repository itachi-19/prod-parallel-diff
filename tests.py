#! /usr/bin/env python3


from garbage.xml_msg import XMLMsg
from reader.csv_reader import CSVReader
from reader.trade_reader import TradeReader
from tests.test_resources import *
import unittest


class XMLTestCase(unittest.TestCase):

    def setUp(self):
        self.icapture = XMLMsg('<NewTrade><id>324</id></NewTrade>')

    def test_xpaths(self):
        '''Testing XPaths Method'''
        self.assertEqual(self.icapture.get_xpaths(), {'./id'})

    def test_xpath_value(self):
        '''Testing XPath Value Method'''
        self.assertEqual(self.icapture.get_value_for_xpath('./id'), '324')


class CSVReaderTestCase(unittest.TestCase):

    def setUp(self):
        self.reader = CSVReader()

    def test_get_trades_for(self):
        self.assertEqual(self.reader.get_trades_for('input/icapture.csv'), icapture_trades)


class TradeReaderTestCase(unittest.TestCase):

    def setUp(self):
        self.icapture_file = 'input/icapture.csv'
        self.fidstp_file = 'input/fidstp.csv'
        self.reader = TradeReader(self.icapture_file, self.fidstp_file)

    def test_get_icapture_trades(self):
        self.assertEqual(self.reader.icapture_trades['5001'], icapture_msg1)

    def test_get_trade_ids(self):
        s = set()
        s.add('5001')
        s.add('5002')
        s.add('5003')
        self.assertEqual(TradeReader.get_trade_ids(self.reader.icapture_trades), s)

    def test_get_missing_trades(self):
        missing_trades = self.reader.get_missing_trades()
        self.assertEqual(self.reader.get_missing_trades(), {'5003'})



if __name__=='__main__':
    #run_some_tests()
    unittest.main()
