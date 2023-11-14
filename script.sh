#!/usr/bin/bash
pip install -r requirements.txt 
python main.py 
uvicorn main:app --host 0.0.0.0