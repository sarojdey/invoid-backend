`python3 -m venv venv`
Creates a virtual environment named "venv" in the current directory, which provides an isolated Python environment for installing dependencies.

`source venv/bin/activate`
Activates the newly created virtual environment. This ensures that any subsequent Python packages are installed here instead of system-wide.

`pip install fastapi uvicorn`
Installs FastAPI, a web framework for building APIs, and Uvicorn, lighting-fast ASGI server implementation used to run the FastAPI application.

`uvicorn main:app --reload`
Starts the Uvicorn application server locally. It serves the `app` instance defined in `main.py` and `--reload` makes the server automatically restart upon code changes.

`deactivate`
Exits the virtual environment, returning the terminal session back to the default system Python environment.
