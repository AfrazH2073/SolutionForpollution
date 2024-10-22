''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Necessary Imports
from fastapi import FastAPI, Request, Response    # The main FastAPI import and Request/Response objects
from fastapi.responses import RedirectResponse    # Used to redirect to another route
# from pydantic import BaseModel                    # Used to define the model matching the DB Schema
from fastapi.responses import HTMLResponse        # Used for returning HTML responses (JSON is default)
from fastapi.templating import Jinja2Templates    # Used for generating HTML from templatized files
from fastapi.staticfiles import StaticFiles       # Used for making static resources available to server
import uvicorn                                    # Used for running the app directly through Python
# import dbutils as db                             # Import helper module of database functions!

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Configuration
app = FastAPI()                                     # Specify the "app" that will run the routing
views = Jinja2Templates(directory='views')          # Specify where the HTML files are located
static_files = StaticFiles(directory='public')      # Specify where the static files are located
static_pictures = StaticFiles(directory='pictures') # Specify where the picture files are located
css_files = StaticFiles(directory='css')            # Specify where the css files are located

# Mount the static directory
app.mount('/public', static_files, name='public') # Mount the static files directory to /public for javascripts
app.mount('/pictures', static_pictures, name='pictures') # Mount the static files directory to /pictures for pictures
app.mount('/css', css_files, name='css') # Mount the static files directory to /css for css style to make things pretty


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# This is the homepage
@app.get('/', response_class=HTMLResponse)
def get_home(request:Request) -> HTMLResponse:
  with open("views/homepage.html") as html:
    return HTMLResponse(content=html.read())
  
@app.get('/team', response_class=HTMLResponse)
def get_teams(request:Request) -> HTMLResponse:
  with open("views/teammates.html") as html:
    return HTMLResponse(content=html.read())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=6543)
