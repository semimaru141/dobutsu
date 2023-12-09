#!/bin/bash
#PBS -l nodes=1:ppn=20
#PBS -M chiharu.ishii@keio.jp
#PBS -m bea

cd $PBS_O_WORKDIR
source ./.venv/bin/activate

# mctで初期モデルをランダム生成
python3 -m src.run_all 1000 98765 softmax1_1

declare -a PREFIXES=()
declare -a SUFFIXES=()

algorithm="sarsa"

for (( i=2; i<=30; i++ ))
do
    PREFIXES+=("softmax1_$i")
    SUFFIXES+=("softmax1_$(($i-1))")
done

for (( i=1; i<=${#PREFIXES[@]}; i++ ))
do
    param=$(echo "e(3*$i/30*l(10))" | bc -l)
    python3 -m src.create_multi_sh ${PREFIXES[$i]} ${SUFFIXES[$i]} ${param} ${algorithm}
    mpirun -np 20 ./cps/cps train_multi.sh
    python3 -m src.process_data ${PREFIXES[$i]} ${SUFFIXES[$i]}
done
