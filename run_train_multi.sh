#!/bin/bash
#PBS -l nodes=1:ppn=20

cd $PBS_O_WORKDIR
source ./.venv/bin/activate
mpirun -np 20 ./cps/cps train_multi.sh
