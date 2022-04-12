from writer.html_diff_builder import HTMLDiffBuilder

class DiffWriter:

    def __init__(self, report_file):
        self.report = open(report_file, 'w')
        self.diff_builder = HTMLDiffBuilder(
            'input/top.html',
            'input/diff.html',
            'input/not_found.html'
        )

    def write(self, all_diffs, missing_trades):
        html = self.diff_builder.get_diff_html(all_diffs, missing_trades)
        self.report.write(html)
        self.report.close()
