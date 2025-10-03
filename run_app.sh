#!/bin/bash

# same as source env/bin/activate
activate () {
  . env/bin/activate
}
activate
python3 My_App/main.py 
