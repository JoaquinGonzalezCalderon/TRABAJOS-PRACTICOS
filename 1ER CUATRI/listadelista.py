from listaenla import by_name, show_list, search, by_namelista, searchlista

estaciones = [
    {'nombre': 'A', 'state':'Entre Rios', 'id': 123},
    {'nombre': 'B', 'state':'Salta', 'id': 456},
    {'nombre': 'C', 'state':'Mendoza', 'id': 101}
]

lista_estaciones = []

medicion = {'temp' : 25, 'hum': 80, 'fecha': '20-5-2024', 'station': 'C'}

for estacion in estaciones:
    lista_estaciones.append([estacion,[]])

lista_estaciones.sort(key= by_namelista)

show_list('Lista de estaciones', lista_estaciones)

pos = search(lista_estaciones,'name', medicion['station'])

if pos is not None:
    print(lista_estaciones[pos])
else:
    print("La estacion no esta en la lista")