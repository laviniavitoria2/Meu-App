from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "App rodando no GitHub 🚀"}

@app.get("/post")
def gerar_post(tema: str):
    return {"post": f"{tema}: quem entende isso, sai na frente."}
