#!/bin/bash
#PBS -l nodes=1:ppn=20

cd $PBS_O_WORKDIR
source ./.venv/bin/activate
python3 -m src.train_multi 2500000 WAOQgYmMer 1step.pkl
