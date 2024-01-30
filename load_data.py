# health_data_module.py

import pandas as pd

class Health_data:
    def __init__(self, file_name):
        self.file_path = file_name
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def display_data(self):
        if self.df is not None:
            print(self.df.head())
        else:
            print("Data not loaded. Call load_data() first.")
