# どうぶつ将棋の棋譜コードサンプル

## 環境構築方法
### conda
```
conda create --name dobutsu python=3.11.2
conda activate dobutsu
conda install -c apple tensorflow-deps
```

### venv
```
python -m venv .venv
source .venv/bin/activate
```
### package install
```
pip install -r requirements_mac.txt
```
```
pip install -r requirements_linux.txt
```

## 実行方法
### 関数実行方法
```
python -m src.main
```
### テスト実行方法
```
pytest tests
```

## submodule
### 同期方法
```
git submodule init
git submodule update
```
### mpi実行方法
```
mpirun -np 20 ./cps/cps train_multi.sh
```

## 仕様

### マスの情報

* 0 空白
* 1 ライオン(先手) L
* 2 ぞう(先手) E
* 3 きりん(先手) G
* 4 ひよこ(先手) C
* 5 にわとり(先手) H
* 6 ライオン(後手) l
* 7 ぞう(後手) e 
* 8 きりん(後手) g
* 9 ひよこ(後手) c
* 10 にわとり(後手) h

### 持ち駒 

ライオンとニワトリは持ち駒にならず、2つまで取る可能性がある。
例えば`captured[0]`は、先手が何個「ぞう」を持っているかの数を表す

* 0 ぞう (先手の持ち駒)
* 1 きりん (先手の持ち駒)
* 2 ひよこ (先手の持ち駒)
* 3 ぞう (後手の持ち駒)
* 4 きりん (後手の持ち駒)
* 5 ひよこ (後手の持ち駒)

## その他
### インテリセンスの効かせ方(VSCode)
設定から`settings.json`を開き、以下のような項目を追加する。
```
"python.autoComplete.extraPaths": [
    "/Users/ishii/.local/share/virtualenvs/dobutsu-n43e7yYG/lib/python3.11/site-packages/"
],
```
