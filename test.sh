#!/bin/bash
#PBS -l nodes=1:ppn=20
#PBS -M chiharu.ishii@keio.jp
#PBS -m e

cd $PBS_O_WORKDIR
source ./.venv/bin/activate
python3 -m src.train_multi_model 5000 123456 test7 test6
