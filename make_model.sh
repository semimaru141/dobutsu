#!/bin/bash

cd $PBS_O_WORKDIR

source .venv/bin/activate
python3 -m src.make_model

