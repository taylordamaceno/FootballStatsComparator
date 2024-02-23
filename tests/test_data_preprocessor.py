import unittest
from src.data_preprocessor import preprocess_data

class TestDataPreprocessor(unittest.TestCase):
    def test_preprocess_data(self):
        data = [{'gols': 10}, {'gols': 5}]  # Exemplo de dados
        df = preprocess_data(data)
        self.assertEqual(df['gols_normalized'].iloc[0], 1.0)  # Verifica se o valor normalizado está correto

if __name__ == '__main__':
    unittest.main()

