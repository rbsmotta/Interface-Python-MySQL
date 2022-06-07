
class com_devida:
    nome = ""
    comissao_devida = ""

    
    def __init__(self, nome_id, comissao_devida_id):
        try:
            self.nome = nome_id
            self.comissao_devida = comissao_devida_id

        except Exception as e:
            print(str(e))
            
    def get_nome_id(self):
        return self.nome
    def get_comissao_devida_id(self):
        return self.comissao_devida