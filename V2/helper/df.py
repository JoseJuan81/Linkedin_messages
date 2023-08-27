"""Módulo de funciones con Pandas"""

import pandas as pd
from pathlib import Path


def save_to_csv(file_name: str, data: dict) -> None:
    """"Función para guardar datos tipo Dict en un archivo .csv"""
    df = pd.DataFrame(data)

    abs_path = Path().absolute()
    result_dir = Path("LinkedIn_messages", "V2", "result")
    path_to_save = Path(abs_path, result_dir, f"{file_name}.csv")
    df.to_csv(path_to_save, index=False)
