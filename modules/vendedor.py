
class vendedor:
    idvendedor = ""
    nome = ""
    cpf = ""
    endereco = ""
    telefone = ""
    
    def __init__(self, idvendedor_id, nome_id, cpf_id, endereco_id, telefone_id):
        try:
            self.idvendedor = idvendedor_id
            self.nome = nome_id
            self.cpf = cpf_id
            self.endereco = endereco_id
            self.telefone = telefone_id
        except Exception as e:
            print(str(e))
        
    def get_idvvendedor(self):
        return self.idvendedor
    def get_nome_id(self):
        return self.nome
    def get_cpf_id(self):
        return self.cpf
    def get_endereco_id(self):
        return self.endereco
    def get_telefone_id(self):
        return self.telefone   
