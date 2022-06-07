
class vendas:
    idvenda = ""
    idproduto = ""
    idvendedor = ""
    valortotal = ""
    comissao = ""
    
    def __init__(self, idvenda_id, idproduto_id, idvendedor_id, valortotal_id, comissao_id):
        try:
            self.idvenda = idvenda_id
            self.idproduto = idproduto_id
            self.idvendedor = idvendedor_id
            self.valortotal = valortotal_id
            self.comissao = comissao_id
        except Exception as e:
            print(str(e))
       
    def get_idvenda_id(self):
        return self.idvenda
    def get_idproduto_id(self):
        return self.idproduto
    def get_idvendedor_id(self):
        return self.idvendedor
    def get_valortotal_id(self):
        return self.valortotal
    def get_comissao_id(self):
        return self.comissao