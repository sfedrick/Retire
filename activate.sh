#!/bin/bash

# same as source env/bin/activate
activate () {
  . env/bin/activate
}
activate
pip3 install -r requirements.txt
pip freeze > requirements.txt
