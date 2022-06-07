
class fornecedor:
    idfornecedor = ""
    nome = ""
    cnpj = ""
    
    def __init__(self, idfornecedor_id, nome_id, cnpj_id,):
        try:
            self.idfornecedor = idfornecedor_id
            self.nome = nome_id
            self.cnpj = cnpj_id
        except Exception as e:
            print(str(e))
            
    def get_inventory_id(self):
        return self.idfornecedor
    
    def get_nome_id(self):
        return self.nome
    
    def get_cnpj(self):
        return self.cnpj 