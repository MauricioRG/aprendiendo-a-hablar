from random import choice
def buscar_respuesta(diccionario):
    respuesta=''
    comp=0
    for key in diccionario:
        if diccionario[key]>=comp:
            comp = diccionario[key]
            respuesta = key
    return respuesta


despedidas = {
    'start' : 0
}
cont=0
while cont == 0:
    despedida_r = raw_input('?Como se despide usted?: ')
    if despedida_r == 'end':
        break
    if despedida_r in despedidas:
        despedidas[despedida_r] +=1/despedidas[despedida_r]
    else:
        despedidas[despedida_r] = 1

despedida_f = raw_input('Despidase: ')
for desp in despedidas:
    if despedida_f == desp:
        print buscar_respuesta(despedidas)
