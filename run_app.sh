#!/bin/bash

# same as source env/bin/activate
activate () {
  . env/bin/activate
}
activate
pip3 install -r requirements.txt
python3 My_App/main.py -q
