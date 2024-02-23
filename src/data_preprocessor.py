import pandas as pd

def preprocess_data(data):
    # Converte dados do MongoDB para DataFrame
    df = pd.DataFrame(data)
    
    # Exemplo de preprocessamento: normalização de uma coluna
    df['gols_normalized'] = df['gols'] / df['gols'].max()
    
    return df

