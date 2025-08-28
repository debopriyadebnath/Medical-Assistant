from fastapi import FastAPI

app = FastAPI()

# Example route
@app.get("/")
def read_root():
    return {"message": "Hello, Medical Assistant!"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root ():
    return {"message":"hello world"} 
