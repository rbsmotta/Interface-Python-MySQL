
class produto:
    idproduto = ""
    idfornecedor = ""
    descricao = ""
    preco = ""
    quant_estoque = ""
    
    def __init__(self, idproduto_id, idfornecedor_id, descricao_id, preco_id, quant_estoque_id):
        try:
            self.idproduto = idproduto_id
            self.idfornecedor = idfornecedor_id
            self.descricao = descricao_id
            self.preco = preco_id        
            self.quant_estoque = quant_estoque_id
        except Exception as e:
            print(str(e))
            
    def get_idproduto_id(self):
        return self.idproduto
    def get_idfornecedor_id(self):
        return self.idfornecedor
    def get_descricao_id(self):
        return self.descricao
    def get_preco_id(self):
        return self.preco_id
    def get_quant_estoque_id(self):
        return self.quant_estoque_id