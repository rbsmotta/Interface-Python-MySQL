from modules.conector import interface_db
from modules.total_de_vendas import total_de_vendas
from modules.maior_venda import maior_venda
from modules.fornecedor_mais_utilizado import fornecedor_mais_utilizado
from modules.maior_qtd_vendas import maior_qtd_vendas
from modules.com_devida import com_devida

if __name__ == "__main__":
    
    try:
        while True:
            
            print("1 - CADASTRAR VENDA \n2 - BUSCAR TABELA \n3 - TOTAL DE VENDAS \n4 - MAIOR VENDA \n5 - MAIOR QUANTIDADE DE VENDAS \n6 - FORNECEDOR MAIS UTILIZADO \n7 - TOTAL COMISSAO \n8 - SAIR")      
            selecao = input("Digite a opcao desejada: ")
            
            if selecao == "1":  #CADASTRAR VENDA
                idproduto = input("Informe o id do produto: ")
                idvendedor = input("Informe o id do vendedor: ")
                valortotal = input("Informe o valor total: ")
                comissao = input("Informe a comissao: ")
                valores = "( {}, {}, {}, {})".format(idproduto, idvendedor, valortotal, comissao)
                query = "INSERT INTO vendas (idproduto, idvendedor, valortotal, comissao) VALUES" + valores+";"
                print(query)
                interface_db.executar(query)            

            elif selecao == "2":    #BUSCAR TABELA
                query = "SELECT * FROM {};" .format(input("Informe a tabela que deseja consultar: "))
                dados = interface_db.buscar(query)
                for linha in dados:
                    print(linha)    
            
            elif selecao == "3":    #TOTAL DE VENDAS
                interface_banco = interface_db("robson", "R0350njose*123", "127.0.0.1", "souldrugs")
                dados = interface_banco.selecionar("sum(valortotal)", "vendas", "")
                try:
                    lista_totalvendas = []
                    for vnd in dados:
                        item = total_de_vendas(vnd[0])
                        lista_totalvendas.append(item)
                        print("Total de vendas: ", vnd[0])
                except Exception as e:
                    print(str(e))
                    
            elif selecao == "4":    #MAIOR VENDA
                interface_banco = interface_db("robson", "R0350njose*123", "127.0.0.1", "souldrugs")
                dados = interface_banco.selecionar("a.nome, b.valortotal", "vendedor a, vendas b where a.idvendedor = b.idvendedor order by valortotal desc limit 1", "")
                try:
                    lista_maior_venda = []
                    for mvnd in dados:
                        item = maior_venda(mvnd[0], mvnd[1])
                        lista_maior_venda.append(item)
                        print("Vendedor que realizou maior venda: ", mvnd[0], "\nValor da venda: ", mvnd[1])   
                except Exception as e:
                    print(str(e))
                    
            elif selecao == "5":      #MAIOR QUANTIDADE DE VENDAS             
                interface_banco = interface_db("robson", "R0350njose*123", "127.0.0.1", "souldrugs")
                dados = interface_banco.selecionar("a.nome, count(b.idvendedor) as qtdvendas", "vendedor a, vendas b where b.idvendedor = a.idvendedor group by a.nome order by qtdvendas desc limit 1", "") 
                try:
                    lista_maior_qtd_vendas = []
                    for mqtd in dados:
                        item = maior_qtd_vendas(mqtd[0], mqtd[1])
                        lista_maior_qtd_vendas.append(item)
                        print("Vendedor que realizou a maior quantidade de vendas: ", mqtd[0], "\nQuantidade de vendas: ", mqtd[1])
                except Exception as e:
                    print(str(e))
                    
            elif selecao == "6":    #FORNECEDOR MAIS UTILIZADO
                interface_banco = interface_db("robson", "R0350njose*123", "127.0.0.1", "souldrugs")
                dados = interface_banco.selecionar("p.idfornecedor, f.nome, count(p.idfornecedor) as contagem", "fornecedor f, produto p WHERE f.idfornecedor = p.idfornecedor GROUP BY idfornecedor ORDER BY contagem desc limit 1", "")
                try:
                    lista_fornecedor_mais_utilizado = []
                    for fmu in dados:
                        item = fornecedor_mais_utilizado(fmu[0], fmu[1], fmu[2])
                        lista_fornecedor_mais_utilizado.append(item)
                        print("ID do fornecedor: ",fmu[0], "\nNome do fornecedor: ", fmu[1], "\nVezes que foi utilizado: ", fmu[2])   
                except Exception as e:
                    print(str(e))
            
            elif selecao == "7":    #COMISSAO DEVIDA
                
                interface_banco = interface_db("robson", "R0350njose*123", "127.0.0.1", "souldrugs")
                dados = interface_banco.selecionar("a.nome, SUM(b.valortotal)*0.08 AS comissao_devida", "vendedor a, vendas b WHERE a.idvendedor = b.idvendedor GROUP BY nome ORDER BY comissao_devida DESC", "")
                try:
                    lista_comissao_devida = []
                    for dvd in dados:
                        item = com_devida(dvd[0], dvd[1])
                        lista_comissao_devida.append(item)
                        print("Vendedor", dvd[0], "tem a receber", dvd[1], "de comissao.")
                except Exception as e:
                    print(str(e))
                    
            elif selecao == "8":
                break
                                        
    except Exception as e:
        print(str(e))