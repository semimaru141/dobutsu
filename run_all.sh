#!/bin/bash
#PBS -l nodes=1:ppn=20
#PBS -M chiharu.ishii@keio.jp
#PBS -m bea

cd $PBS_O_WORKDIR
source ./.venv/bin/activate
python3 -m src.run_all 5000 123456 compressed1 1hour
