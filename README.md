Very simple project created to verify knowledge about FastAPI and requests libraries.

There's two small apps:
    
    - Terminal app - App which map input from terminal to the emoji (loaded from 3rd party REST API)
    - REST API - App which allow some clients to make requests to it, and get emojis from 3rd party emojis REST API
    
Dependencies:

    - Python 3,
    - FastAPI,
    - Uvicorn (from FastAPI),
    - requests
    
Start:

    - type python3 (or python) terminal-app.py to start terminal app,
    - type uvicorn rest-api:app to run REST API app