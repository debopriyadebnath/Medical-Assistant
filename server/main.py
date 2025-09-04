from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# If your exception_handlers.py is in the same directory as main.py, use:
from exception_handlers import catch_exception_middleware
# Or, if it's in a subfolder named 'middlewares' inside 'server', ensure the folder has an __init__.py file and the path is correct.


app= FastAPI(title="Medical Assistant API", description="API for Medical Assistant chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
#middleware exception handlers
app.middleware("http")(catch_exception_middleware)
#routers
#1.upload pdfs documents
#2. asking query

