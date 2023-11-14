    #*Importação das bibliotecas 
import pandas as pd
import numpy as np

#*Criação da classe DataProcessor
class DataProcessor:

#*=============================== Leitura dos dados ==================================================================    
    try:    
        def __init__(self, file_path, filial):
            self.data = pd.read_excel(file_path)
            self.filiais = pd.read_excel(filial)
            print('Leitura realizada com sucesso')
    except KeyError:
        print('Leitura de dados inválida')
    
#*=============================== Exibir todos os dados / Faturamento ================================================       
    
    try:
        def show_data(self):
            print(self.data)
    except KeyError:
        print('Dados não encontrados')
        
#*===================================== dados / Filiais ==============================================================       
    
    try:
        def show_filial(self):
            print(self.filiais)
    except KeyError:
        print('Dados não encontrados')    
        

    def show_info_filial(self):
        print(self.filiais.info())
                
    try:   
        def type_str_filial(self, column_name):
            self.filiais[column_name] = self.filiais[column_name].astype(str)
            print('Coluna alterado para tipo str')
    except KeyError:
        print('Alteração de tipo invalida')
                                 
#*=============================== Exibir informações do dataframe ====================================================

    def show_info(self):
        print(self.data.info())
        
#*=============================== Exibir coluna específica ===========================================================

    try:    
        def column_speficie(self, column_name):
            print(self.data[column_name])  
    except KeyError:
        print('Coluna nao encontrada')
               
#*=============================== Exibir coluna condicional ===========================================================

    try:    
        def column_condicional(self, column_name, value):
            print(self.data[self.data[column_name] == value])  
    except KeyError:
        print('Coluna nao encontrada')
                
#*=============================== Converter para str =================================================================  
    try:   
        def type_str(self, column_name):
            self.data[column_name] = self.data[column_name].astype(str)
            print('Coluna alterado para tipo str')
    except KeyError:
        print('Alteracao de tipo invalida')
        
#*========================== Remover caracteres especiais ============================================================       
    try:
        def remove_strings(self, column_name):
            self.data[column_name] = self.data[column_name].str.replace('[./-]', '', regex = True)
            self.data[column_name] = self.data[column_name].str.replace('-', '', regex = True)
            print('Carateres removidos com sucesso')
    except KeyError:
        print('Erro ao remover caracteres')
        
#*=============================== Salvar em excel ====================================================================       
    try:    
        def save_to_excel(self, file_name):
            self.data.to_excel(file_name, index = False)
            print('Arquivo salvo com sucesso')
    except KeyError:
        print('Erro ao salvar arquivo')

#*=========================== Converter para tipo numérico ===========================================================

    try:
        def type_numeric(self, column_name):
            self.data[column_name] = pd.to_numeric(self.data[column_name], errors = 'coerce')
            print('Coluna alterada para tipo numerico')
    except KeyError:
        print('Erro ao alterar coluna para tipo numerico')
        
#*=========================== Converter para int64 ===================================================================

    try:
        def type_int(self, column_name):
            self.data[column_name] = self.data[column_name].astype(np.int64)
            print('Coluna alterada para int64')
    except KeyError:
        print('Erro ao alterar coluna para int64')
                      
#*==================== Converter para maiúscula e remover espaços vazios =============================================       
    try:
        def column_upper(self, column_name):
            for i in self.data[column_name]:
                self.data[column_name] = self.data[column_name].str.upper()
                self.data[column_name] = self.data[column_name].str.strip()
            print('Valores alterados para maiuscula com sucesso')
    except KeyError:
        print('Erro ao alterar valores para maiuscula')
        
#*==================== Converter para minúscula e remover espaços em branco ========================================== 
    try:
        def column_lower(self, column_name):
            for i in self.data[column_name]:
                self.data[column_name] = self.data[column_name].str.lower()
                self.data[column_name] = self.data[column_name].str.strip()
            print('Valores alterados para minuscula com sucesso')
    except KeyError:
        print('Erro ao alterar valores para minuscula')
        
#*=============================== Combinar dados pd.merge ============================================================
    try:
        def combinar_merge(self, column_name1, column_name2, new_column):
            self.result = pd.merge(self.data, self.filiais[[column_name1, column_name2]], on=column_name1, how='left')
            self.data[new_column] = self.result[column_name2]
    except KeyError:
        print('Erro ao combinar valores')

#*=============================== Substituir nome da coluna ==========================================================   
    try:
        def trocar_nome_coluna(self,nome_antigo, novo_nome):
            self.data.rename(columns={nome_antigo : novo_nome}, inplace = True)
            print('Coluna renomeada com sucesso')
    except KeyError:
        print('Erro ao renomear coluna')

#*=============================== Remover 0 a esquerda ===============================================================
    try:
        def remover_0(self, column_name):   
            self.data[column_name] = self.data[column_name].apply(lambda x: x.lstrip('0') if len(x) > 11 else x)
            print('0 removido com sucesso')
    except KeyError:
        print('Erro ao remover os 0')

#*============================== Criar coluna 'Tipo de Pessoa' =======================================================
    try:
        def criar_coluna(self, new_column,column_name):
            self.data[new_column] = np.where(self.data[column_name].str.len() > 11, 'PJ', 'PF')
            print('Coluna TIPO DE PESSOA criada com sucesso')        
    except KeyError:
        print('Erro ao criar coluna TIPO DE PESSOA')
              
#*============================ Formatar coluna de data ===============================================================
    try:
        def format_date(self,column_name):
        #todo -> Varia de acordo com o relatório
            self.data[column_name] = self.data[column_name].str.replace('646.757.009-00', '', regex = True)
            self.data[column_name] = self.data[column_name].str.replace('019.471.491-80', '', regex = True)
            self.data[column_name] = self.data[column_name].str.replace('054.454.851-53', '', regex = True)
        #todo -> converter coluna para tipo datetime 
            self.data[column_name] = pd.to_datetime(self.data[column_name])
        #todo -> extrair somente a data
            self.data[column_name] = self.data[column_name].dt.date
            print('Coluna data formatada com sucesso')
    except KeyError:
        print('Erro ao formatar coluna de data')

#*============================ Criar coluna TIPO DE CONVÊNIO =========================================================
    try:
        def criar_coluna_convenio(self, new_column, column_name):
            condicoes = [(self.data[column_name] == '44649812000138') | (self.data[column_name] == '62550256001606'),
                         (self.data[column_name] == '2668512000156')]
            valores = ['REDE PRÓPRIA', 'HB SAÚDE']
            self.data[new_column] = np.select(condicoes, valores, default='VENDA DE SERVIÇO')
            print('Coluna TIPO DE CONVENIO adicionada com sucesso')
    except KeyError:
        print('Erro ao criar coluna de TIPO DE CONVENIO')        

#*============================ Remover linhas em branco ==============================================================
    try:
        def remover_linhas_vazias(self, column_name):
            self.data = self.data.dropna(subset = column_name, how = "any" , axis = 0)
            print('Valores ausentes removidos com sucesso')
    except KeyError:
        print('Erro ao remover valores ausentes')
        
        
#*============================ Substituir valores ausentes por 0 =====================================================
    try:
        def substituir_valores(self, column_name):
            self.data[column_name] = self.data[column_name].fillna(0)
            print('Valores ausentes substituidos por 0')
    except KeyError:
            print('Erro ao substituir valores ausentes para 0')

#*============================ Exibir valores ausentes ===============================================================
    def valores_ausentes(self, column_name):
        print(self.data[self.data[column_name].isnull()] == True)
        
#?=================================================================================================================================================================        

#*Criação de variável para leitura dos dados 
       
file_path = 'Previa faturamento/rsap001_a - 20231101144807 (2).xlsx'
filial = 'Previa faturamento/Filiais.xlsx'

#*Instanciação da classe
data_processor = DataProcessor(file_path,filial)
        
#!=================================================================================================================================================================
#!Formatando a coluna CNPJ PRESTADOR
data_processor.remove_strings('CPF E OU CNPJ')
data_processor.trocar_nome_coluna('CPF E OU CNPJ', 'CNPJ PRESTADOR')
data_processor.type_str('CNPJ PRESTADOR')
data_processor.remover_0('CNPJ PRESTADOR')

#!Formatando a coluna CNPJ PRESTADOR da base Filial
data_processor.type_str_filial('CNPJ PRESTADOR')

#!Combinando os dois dataframes e criando uma coluna de REGIONAL E UF
data_processor.combinar_merge('CNPJ PRESTADOR', 'REGIONAL', 'REGIONAL')
data_processor.combinar_merge('CNPJ PRESTADOR', 'UF', 'UF')

#!Formatar coluna CNPJ TOMADOR
data_processor.remove_strings('CPF OU CNPJ')
data_processor.trocar_nome_coluna('CPF OU CNPJ', 'CNPJ TOMADOR')
data_processor.type_str('CNPJ TOMADOR')
data_processor.remover_0('CNPJ TOMADOR')

#!Criação da coluna TIPO DE PESSOA
data_processor.criar_coluna('TIPO DE PESSOA', 'CNPJ TOMADOR')

#!Formatando a coluna de DT COMPETENCIA
data_processor.type_str('DT COMPETENCIA')
data_processor.format_date('DT COMPETENCIA')

#!Criar coluna TIPO DE CONVÊNIO
data_processor.criar_coluna_convenio('TIPO DE CONVÊNIO','CNPJ TOMADOR')

#!Tratando valores ausentes da coluna NOTA FISCAL
data_processor.type_numeric('NOTA FISCAL')
data_processor.remover_linhas_vazias('NOTA FISCAL')
data_processor.type_int('NOTA FISCAL')

#!Tratar coluna VALOR LIQUIDO
data_processor.type_numeric('VALOR LIQUIDO')

#!Tratar valores da coluna CEDENTE/SACADO
data_processor.type_int('CEDENTE/SACADO')

#!Tratar valores da coluna EMPRESA COLIGADA

data_processor.substituir_valores('EMPRESA COLIGADA')
data_processor.type_int('EMPRESA COLIGADA')

#!Salvar arquivo em excel
#data_processor.save_to_excel('Arquivo.xlsx')