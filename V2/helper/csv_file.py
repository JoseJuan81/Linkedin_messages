import pandas as pd

def csv_file_contact(file: str):
    """Extrae la informacion de los contactos del archivo y retorna un arreglo de dict"""

    df = pd.read_csv(file).drop(['Unnamed: 0'], axis = 1)
    data = df.to_dict(orient = "records")

    return data
