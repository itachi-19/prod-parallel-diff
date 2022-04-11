from string import Template
from writer.param_extractor import ParamExtractor


class HTMLDiffBuilder:

    def __init__(self, top_file, diff_file, not_found_file):
        self.string_builder = []

        with open(top_file) as file:
            self.string_builder.append(file.read())

        with open(diff_file) as file:
            self.diff_html = file.read()

        with open(not_found_file) as file:
            self.not_found_html = file.read()

        self.not_found_template = Template(self.not_found_html)
        self.diff_template = Template(self.diff_html)


    def append_diffs(self, all_diffs):
        for trade in all_diffs:
            param_extractor = ParamExtractor(trade[1])
            trade_id = trade[0]
            xpaths = param_extractor.get_xpaths()
            icapture_vals = param_extractor.get_icapture_vals()
            fidstp_vals = param_extractor.get_fidstp_vals()
            d = {
                'trade_id': trade_id,
                'xpaths': xpaths,
                'icapture_vals': icapture_vals,
                'fidstp_vals': fidstp_vals
            }
            diff = self.diff_template.substitute(d)
            self.string_builder.append(diff)

    def append_not_found(self, missing_trades):
        d = { 'missing_len': len(missing_trades) }
        string = '<br>'.join(map(lambda x: '- ' + str(x), missing_trades))
        d['missing_trades'] = string
        not_found = self.not_found_template.substitute(d)
        self.string_builder.append(not_found)

    def get_diff_html(self, all_diffs, missing_trades):
        self.append_diffs(all_diffs)
        # print(self.string_builder)
        self.append_not_found(missing_trades)
        #print(self.string_builder)
        return ''.join(self.string_builder)

