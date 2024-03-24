import pandas as pd

class DataHandler:
    def __init__(self):
        self.df = None

    def create_dataFrame(self, file):
        print('create_dataFrame Called')
        df = pd.read_csv(file)
        new_df = df.dropna()
        self.df = new_df  # Save the DataFrame to the class attribute
        return new_df

    def get_dataFrame(self):
        return self.df

    def set_date_column(self, date):
        if self.df is not None:
            print('set_date_column Called')
            self.df.loc[:, f'{date}'] = pd.to_datetime(self.df[f'{date}'])

    def set_analysis_field(self, field):
        if self.df is not None:
            print('set_analysis_field Called')
            sold_models = self.df[f'{field}'].value_counts()
            return sold_models

# Instantiate the DataHandler
data_handler = DataHandler()

