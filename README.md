# FootballStatsComparator
O FootballStatsComparator é um projeto de análise de dados para classificar jogadores de futebol com base em estatísticas e títulos, usando pesos diferenciados para cada conquista. Ele permite comparações abrangentes, destacando contribuições e impacto no esporte.
# FootballStatsComparator

## Descrição
O FootballStatsComparator é um projeto de análise de dados e machine learning focado em classificar e comparar jogadores de futebol com base em suas estatísticas de jogo e conquistas. Utilizando um conjunto de dados detalhado de estatísticas de jogadores, este projeto atribui pesos diferenciados a diferentes títulos para calcular uma pontuação agregada para cada jogador, permitindo uma comparação abrangente de seu impacto e contribuições para o esporte.

## Como Funciona
O projeto analisa dados de jogadores, incluindo gols, assistências, passes, além de títulos individuais e coletivos. Atribuímos pesos específicos a diferentes títulos para refletir sua importância e impacto no futebol mundial. Esses pesos são usados para calcular uma pontuação total para cada jogador, que serve como uma métrica abrangente de sua performance e conquistas.

### Pesos dos Títulos
- Copa do Mundo: Peso 3
- Champions League: Peso 2
- Libertadores: Peso 1.5
- Mundial de Clubes: Peso 1.5
- Demais títulos (nacionais, continentais menores): Peso 1

### Estrutura de Dados
Cada jogador é representado por um documento no MongoDB contendo seu nome, equipe, posição, estatísticas detalhadas de jogo, lista de títulos com quantidades e os pesos correspondentes, e uma pontuação total calculada.

```json
{
  "nome": "Nome do Jogador",
  "equipe": "Nome da Equipe",
  "posicao": "Posição do Jogador",
  "estatisticas": {
    "gols": 0,
    "assistencias": 0,
    "passes": 0
  },
  "titulos": [
    {"nome": "Copa do Mundo", "quantidade": 0, "peso": 3},
    {"nome": "Champions League", "quantidade": 0, "peso": 2},
    ...
  ],
  "pontuacaoTotal": 0
}
