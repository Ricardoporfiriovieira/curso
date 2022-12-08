from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def raiz():
    return {"msg": "Olá mundo!"}

@app.get("/mensagem")
async def mensagem():
    return {"mensagem:" : "Estou a aprender tudo!"}

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)