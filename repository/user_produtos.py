import psycopg2 as ps

class Banco_Produtos_Loja_Esportiva(object):
    def __init__(self) -> None:
        self.dbname = "Sports-Gear-Hub"
        self.host = "localhost"
        self.port = "5432"
        self.user = "postgres"
        self.password = "postgres"

        self.conn = ps.connect(user=self.user,
                               password=self.password,
                               host=self.host,
                               port=self.port,
                               dbname=self.dbname)
        
        self.cursor = self.conn.cursor()

        self.conn.autocommit = True

        self.tabela_produtos = self.cursor.execute("CREATE TABLE IF NOT EXISTS produtos (nome_produto text, preco_produto float, imagem_produto text, id_produto text) ")

    def Adicionar_Produto(self, nome_produto, preco_produto, imagem_produto, id_produto):
        self.cursor.execute("INSERT INTO produtos(nome_produto, preco_produto, imagem_produto, id_produto) VALUES(%s,%s,%s,%s)", (nome_produto, preco_produto, imagem_produto, id_produto))
    
    def Ver_Dados_Produtos(self):
        self.cursor.execute("SELECT * FROM produtos")

        self.dados_produtos = list(self.cursor.fetchall())

        return self.dados_produtos
    
    def Ver_Dados_Produtos_Destaque(self):
        self.cursor.execute("SELECT * FROM produtos LIMIT 10")

        self.dados_produtos_destaque = list(self.cursor.fetchall())

        return self.dados_produtos_destaque
    
    def Filtrar_Dados_Produtos(self, categoria):
        self.cursor.execute("SELECT * FROM produtos WHERE id_produto=%s", (categoria, ))

        self.dados_produtos_filtrados = list(self.cursor.fetchall())

        return self.dados_produtos_filtrados
    
    def Pesquisar_Dados_Produtos(self, nome_produto):
        self.cursor.execute(f"""
        SELECT *
        FROM produtos
        WHERE unaccent(nome_produto) % unaccent('{nome_produto}') OR unaccent(nome_produto) ILIKE unaccent('%{nome_produto}%'); 
        """)

        self.dados_pesquisados = list(self.cursor.fetchall())

        return self.dados_pesquisados


