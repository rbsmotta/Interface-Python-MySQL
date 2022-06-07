
class total_de_vendas:
    valor = ""

    
    def __init__(self, valor_id):
        try:
            self.valor = valor_id

        except Exception as e:
            print(str(e))
            
    def get_idproduto_id(self):
        return self.valor