

class ParamExtractor:

    def __init__(self, diffs):
        self.diffs = diffs

    def get_icapture_vals(self):
        vals = [ diff[1][0] for diff in self.diffs ]
        return '<br>'.join(vals)

    def get_fidstp_vals(self):
        vals = [ diff[1][1] for diff in self.diffs ]
        return '<br>'.join(vals)

    def get_xpaths(self):
        xpaths = [ diff[0] for diff in self.diffs ]
        return '<br>'.join(xpaths)
