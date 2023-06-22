# cpsの使い方
## git clone
```
git submodule update -i
```

## make
```
cd cps && make
```

## run
```
mpirun -np 20 ./cps/cps task.sh
```

## jobに投げる
以下のファイルを生成
```
#!/bin/bash
#PBS -l nodes=1:ppn=20

cd $PBS_O_WORKDIR
hostname
mpirun -np 20 ./cps/cps task.sh
```

jobのqueに投げる
```
***.sh
```
