#!/bin/bash
set -e
rm -rf migrations
rm -rf *.pyc
rm -rf __pycache__
rm -rf app/*.pyc
rm -rf app/admin/*.pyc
rm -rf app/auth/*.pyc
rm -rf app/customer/*.pyc
rm -rf app/expense/*.pyc
rm -rf app/home/*.pyc
rm -rf app/inventory/*.pyc
rm -rf app/product/*.pyc
rm -rf app/sale/*.pyc

export FLASK_CONFIG=development && export FLASK_APP=run.py



