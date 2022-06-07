

class fornecedor_mais_utilizado:
    idfornecedor = ""
    nome = ""
    contagem = ""

    
    def __init__(self, idfornecedor_id, nome_id, contagem_id):
        try:
            self.idfornecedor = idfornecedor_id
            self.nome = nome_id
            self.valor = contagem_id

        except Exception as e:
            print(str(e))
            
    def get_idfornecedor_id(self):
        return self.idfornecedor
    def get_nome_id(self):
        return self.nome
    def get_contagem_id(self):
        return self.contagem