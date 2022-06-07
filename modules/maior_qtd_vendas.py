
class maior_qtd_vendas:
    nome = ""
    qtdvendas = ""

    def __init__(self, nome_id, qtdvendas_id):
        try:
            self.nome = nome_id
            self.qtdvendas = qtdvendas_id

        except Exception as e:
            print(str(e))
    
    def get_nome_id(self):
        return self.nome        
    def get_qtdvendas_id(self):
        return self.qtdvendas