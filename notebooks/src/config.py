from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
DADOS_ORIGINAIS = PASTA_DADOS / "mkt_data.csv"
DADOS_TRATADOS = PASTA_DADOS / "df_tratado.parquet"

# coloque abaixo outros caminhos que você julgar necessário
PASTA_IMAGENS = PASTA_PROJETO / "imagens"
