# Ramzan-Project
This app lets users add timings of prayers for a mosque and also know the timings of other mosque's prayers

Setup:
- git clone repo
- cd ./Ramzan-Project
- python -m venv .venv (to create a virtual env)
- source .venv/bin/activate (activate the virtual env)
- pip install -r requirements.txt (installs dependencies)
- run postgres in docker
- uvicorn main:app --reload
