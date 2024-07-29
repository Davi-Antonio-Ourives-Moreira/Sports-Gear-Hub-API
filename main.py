import fastapi
from repository import Banco_Produtos_Loja_Esportiva
import uvicorn
import os

app = fastapi.FastAPI()

@app.get("/dados_produtos_destaque")
def dados_produtos_destaque():
    dados_produtos_destaque = Banco_Produtos_Loja_Esportiva()

    return dados_produtos_destaque.Ver_Dados_Produtos_Destaque()

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
    
    return "Produto Adicionado"

@app.get("/categoria_produtos/{categoria}")
def filtra_produtos(categoria:str):
    filtro_produtos = Banco_Produtos_Loja_Esportiva()

    produtos_filtrados = filtro_produtos.Filtrar_Dados_Produtos(categoria=categoria)

    return produtos_filtrados

@app.get("/pesquisa_produtos/{produto}")
def pesquisa_produtos(produto:str):
    pesquisa_produto = Banco_Produtos_Loja_Esportiva()

    produtos_pesquisados = pesquisa_produto.Pesquisar_Dados_Produtos(nome_produto=produto)

    return produtos_pesquisados

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info", reload=True)