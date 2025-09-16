from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exceptions_middleware
from routes.upload_pdfs import router as upload_router
from routes.ask_question import router as ask_router

app = FastAPI(title="Medical Assistant API", description="API for Medical Assistant chatbot")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handlers middleware
app.middleware("http")(catch_exceptions_middleware)

# Routers
app.include_router(upload_router)
app.include_router(ask_router)

# A simple GET route
@app.get("/")
def root():
    return {"message": "Welcome to the Medical Assistant API"}
