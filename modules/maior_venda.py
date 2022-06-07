
class maior_venda:
    nome = ""
    valor = ""

    
    def __init__(self, nome_id, valor_id):
        try:
            self.nome = nome_id
            self.valor = valor_id

        except Exception as e:
            print(str(e))
            
    def get_nome_id(self):
        return self.nome
    def get_valor_id(self):
        return self.valor