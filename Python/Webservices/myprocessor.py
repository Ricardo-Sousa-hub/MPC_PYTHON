class MyProcessor:
    def run(self, df):
        return df.agg(['mean','median', 'min', 'max'])