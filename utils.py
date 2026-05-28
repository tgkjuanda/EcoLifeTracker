from datetime import datetime
import pandas as pd
from typing import Dict

class DataProcessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data.astype({'date': 'datetime64[ns]'})

    def filter_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        try:
            datetime.strptime(start_date, '%Y-%m-%d')
            datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Tanggal harus dalam format 'YYYY-MM-DD'") from e
        
        if 'date' not in self.data.columns:
            raise KeyError("DataFrame tidak memiliki kolom bernama 'date'")
        
        filtered_data = self.data[(self.data['date'] >= start_date) & (self.data['date'] <= end_date)]
        return filtered_data

    def aggregate_data(self, group_by: str, agg_func: Dict[str, str]) -> pd.DataFrame:
        missing_cols = [col for col in agg_func if col not in self.data.columns]
        if missing_cols:
            raise KeyError(f"Kolom hilang yang diperlukan untuk agregasi: {missing_cols}")
        
        aggregated_data = self.data.groupby(group_by).agg(agg_func)
        return aggregated_data

class DataExporter:
    @staticmethod
    def export_to_csv(data: pd.DataFrame, file_path: str) -> None:
        try:
            data.to_csv(file_path, index=False)
        except Exception as e:
            print(f"Kesalahan saat mengekspor ke CSV: {e}")

    @staticmethod
    def export_to_excel(data: pd.DataFrame, file_path: str) -> None:
        try:
            data.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Kesalahan saat mengekspor ke Excel: {e}")