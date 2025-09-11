from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# If your exception_handlers.py is in the same directory as main.py, use:
from exception_handlers import catch_exception_middleware
# Or, if it's in a subfolder named 'middlewares' inside 'server', ensure the folder has an __init__.py file and the path is correct.
from routes.upload_pdfs import router as upload_router
from routes.ask_question import router as ask_router



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
app.include_router(upload_router)
#2. asking query
app.include_router(ask_router)

