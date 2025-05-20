@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python plant_disease_detector_app.py
