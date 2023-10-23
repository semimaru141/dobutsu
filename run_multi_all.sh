#!/bin/bash
#PBS -l nodes=1:ppn=20
#PBS -M chiharu.ishii@keio.jp
#PBS -m bea

cd $PBS_O_WORKDIR
source ./.venv/bin/activate

# mctで初期モデルをランダム生成
python3 -m src.run_all 100 12345 test_multi1

python3 -m src.create_multi_sh test_multi2 test_multi1
mpirun -np 20 ./cps/cps train_multi.sh
python3 -m src.process_data test_multi2 test_multi1

python3 -m src.create_multi_sh test_multi3 test_multi2
mpirun -np 20 ./cps/cps train_multi.sh
python3 -m src.process_data test_multi3 test_multi2

python3 -m src.create_multi_sh test_multi4 test_multi3
mpirun -np 20 ./cps/cps train_multi.sh
python3 -m src.process_data test_multi4 test_multi3
