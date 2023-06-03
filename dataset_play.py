from datasets import load_dataset
from pyarrow.parquet import read_table

tr1 = read_table('/home/birch/ml-data/prm800k/critique-all/data/phase1_train.stepwise-critique.parquet')
tr2 = read_table('/home/birch/ml-data/prm800k/critique-all/data/phase2_train.stepwise-critique.parquet')

te1 = read_table('/home/birch/ml-data/prm800k/critique-all/data/phase1_test.stepwise-critique.parquet')
te2 = read_table('/home/birch/ml-data/prm800k/critique-all/data/phase2_test.stepwise-critique.parquet')

print(len(tr1) + len(tr2), len(te1) + len(te2))

d = load_dataset("Birchlabs/openai-prm800k-stepwise-critic")
pass