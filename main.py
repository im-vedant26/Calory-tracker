from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Calorie Counter API"}

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    return JSONResponse(content={"filename": file.filename, "message": "Image received!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
