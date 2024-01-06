from fastapi import FastAPI

app = FastAPI()

# im able to add any routes depends on my project requeiremnts

@app.get("/" , description='This is my first get api')
async def root():
    return {"hi , you are in the root get / "}

@app.post("/")
async def root():
    return {"hi , you are in the root post / "}
