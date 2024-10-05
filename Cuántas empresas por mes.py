# Lista de RFCs
rfc_list = ['MOH820115NI4', 'TGJ850121AI3', 'GAK921218LL2', 'AAA920127BB1', 'BGS920206CC5', 
            'CJD820305DE6', 'SLE720111AB5', 'ABR720525CA4', 'ANZ930622CC4', 'DML720525TT2', 
            'JEO930622TH3', 'IXP720525KI9', 'OOQ930622XD8', 'LAA720525SA7', 'MON930622AA2']

# Diccionario para almacenar la cantidad de empresas por mes
meses = {
    'ENERO': 0, 'FEBRERO': 0, 'MARZO': 0, 'ABRIL': 0, 'MAYO': 0, 
    'JUNIO': 0, 'JULIO': 0, 'AGOSTO': 0, 'SEPTIEMBRE': 0, 'OCTUBRE': 0, 
    'NOVIEMBRE': 0, 'DICIEMBRE': 0
}

# Mapeo de meses para facilitar el acceso
mes_map = {
    '01': 'ENERO', '02': 'FEBRERO', '03': 'MARZO', '04': 'ABRIL', 
    '05': 'MAYO', '06': 'JUNIO', '07': 'JULIO', '08': 'AGOSTO', 
    '09': 'SEPTIEMBRE', '10': 'OCTUBRE', '11': 'NOVIEMBRE', '12': 'DICIEMBRE'
}

# Recorremos la lista de RFCs para contar las empresas por mes
for rfc in rfc_list:
    mes = rfc[5:7]  # Extraemos los dígitos correspondientes al mes
    if mes in mes_map:
        meses[mes_map[mes]] += 1

# Mostramos el resultado
for mes, count in meses.items():
    print(f'{mes}: {count}')

