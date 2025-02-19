import csv, json

escolas = list()

with open('microdados_ed_basica_2023.csv', 'r') as arquivo:
    reader = csv.reader(arquivo, delimiter=';')
    cabecalho = next(reader)
    #Localização das colunas
    indexEstado = cabecalho.index('SG_UF')
    indexRegiao = cabecalho.index('NO_REGIAO')
    indexMunicipio = cabecalho.index('NO_MUNICIPIO')
    indexMesorregiao = cabecalho.index('NO_MESORREGIAO')
    indexMicrorregiao = cabecalho.index('NO_MICRORREGIAO')
    indexEntidade = cabecalho.index('NO_ENTIDADE')
    #Local das quantidades de matrículas
    indexMatBas = cabecalho.index('QT_MAT_BAS')
    indexMatEja = cabecalho.index('QT_MAT_EJA')
    indexMatEsp = cabecalho.index('QT_MAT_ESP')
    indexMatFund = cabecalho.index('QT_MAT_FUND')
    indexMatInf = cabecalho.index('QT_MAT_INF')
    indexMatMed = cabecalho.index('QT_MAT_MED')
    indexMatProf = cabecalho.index('QT_MAT_PROF')
    
    for row in reader:
        if row[indexEstado] == 'PB':
            escola = dict()
            escola['SG_UF'] = row[indexRegiao]
            escola['NO_REGIAO'] = row[indexEstado]
            escola['NO_MUNICIPIO'] = row[indexMunicipio]
            escola['NO_MESORREGIAO'] = row[indexMesorregiao]
            escola['NO_MICRORREGIAO'] = row[indexMicrorregiao]
            escola['NO_ENTIDADE'] = row[indexEntidade]
            escola['QT_MAT_BAS'] = row[indexMatBas]
            escola['QT_MAT_EJA'] = row[indexMatEja]
            escola['QT_MAT_ESP'] = row[indexMatEsp]
            escola['QT_MAT_FUND'] = row[indexMatFund]
            escola['QT_MAT_INF'] = row[indexMatInf]
            escola['QT_MAT_MED'] = row[indexMatMed]
            escola['QT_MAT_PROF'] = row[indexMatProf]
            
            escolas.append(escola)
    
with open('dados.json', 'w', encoding='utf-8') as dadosJson:
    json.dump(escolas, dadosJson, indent="\t", ensure_ascii=False)
