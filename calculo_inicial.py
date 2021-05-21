import json

class Calculo:
    @staticmethod
    def add(x, y):
        """Teste de soma simples (valida funcionamento dos testes)"""
        return x + y

    @staticmethod
    def calcula_taxa_coe(documento, uso, tipificacao="solicitacao", area_final=1, megabytes=0, tem_outorga=False):
        """Taxas para exame e verificação dos pedidos de documentos de controle da atividade edilícia (COE).
        Retorna valor em Reais (R$)"""

        #tipificacao: valor padrão ("solicitacao") é utilizado para manter o padrão em itens da tabela do COE que não possuem tipificação (valor "-")

        # Trata parâmetros de entrada para compatibilizar cálculos
        area_final = float(area_final)
        if not (area_final >= 1):
            return "Não foi possível calcular valor. Verifique a área final informada (valor deve ser informado em metros quadrados)."

        # Importa tabela de valores COE
        with open('tabela_taxas_coe.json') as json_file:
            tabela = json.load(json_file)

        # "uso" (array):
        #   0: "Residência Unifamiliar",
        #   1: "até 1500m²",
        #   2: "de 1500 a 20000m²",
        #   3: "acima de 20000m²"

        # Identifica uso para calcular valor por área construída
        indice_uso = 0
        if (uso != "r1"):
            if (area_final < 1500):
                indice_uso = 1
            elif (area_final < 20000):
                indice_uso = 2
            else:
                indice_uso = 3
        
        multiplicador = tabela[documento][tipificacao][indice_uso]
        
        valorFinal = 2*float(area_final)
        print()
        return valorFinal
