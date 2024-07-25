import fastapi
from repository import Banco_Produtos_Loja_Esportiva
import uvicorn

app = fastapi.FastAPI()

@app.get("/dados_produtos")
def ver_dados_produtos():
    dados_produtos = Banco_Produtos_Loja_Esportiva()

    return dados_produtos.Ver_Dados_Produtos()

@app.post("/adicionar/{nome_produto}/{preco_produto}/{imagem_produto}/{id_produto}")
def adicionar_produto_api(nome_produto:str, preco_produto:float, imagem_produto:str, id_produto:str):
    banco_produtos = Banco_Produtos_Loja_Esportiva()

    banco_produtos.Adicionar_Produto(nome_produto=nome_produto,
                                     preco_produto=preco_produto,
                                     imagem_produto=imagem_produto,
                                     id_produto=id_produto)
    
    return {"Adicionado": True}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)