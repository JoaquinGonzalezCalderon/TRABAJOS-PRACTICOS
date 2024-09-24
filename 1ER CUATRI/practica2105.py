#Metodos

def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento['nombre'], elemento['id'])
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(elemento['sublist']):
            print('    ', second_index, second_element)
    print() 

def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index) 
    
def by_name(item):
    return item['nombre']

def by_temp(item):
    return item['temp']

def by_hegiht(item):
    return item['altura']

def by_house(item):
    return item['casa_comic']+item['nombre']

entrenadores = [

    {'nombre' : 'Ash', 'torneos': 5, 'ganadas': 10, 'perdidas':50, 
     'pokemones': [{'pokemon': 'Pikachu', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'volador',
     'pokemon': 'Charizard', 'nivel': 55, 'tipo': 'fuego', 'subtipo': 'volador'}]
     },

    {'nombre': 'Misty', 'torneos': 3, 'ganadas': 8, 'perdidas': 30, 
     'pokemones': [{'pokemon': 'Starmie', 'nivel': 40, 'tipo': 'agua', 'subtipo': 'psíquico'}]
    },
    
    {'nombre': 'Brock', 'torneos': 2, 'ganadas': 5, 'perdidas': 25, 
     'pokemones': [{'pokemon': 'Geodude', 'nivel': 30, 'tipo': 'roca', 'subtipo': 'tierra'}]
     },

    {'nombre': 'Gary Oak', 'torneos': 4, 'ganadas': 7, 'perdidas': 40, 
     'pokemones': [{'pokemon': 'Arcanine', 'nivel': 55, 'tipo': 'fuego', 'subtipo': 'N/A'}]
     },

    {'nombre': 'Cynthia', 'torneos': 6, 'ganadas': 3, 'perdidas': 60, 
     'pokemones': [{'pokemon': 'Roserade', 'nivel': 65, 'tipo': 'planta', 'subtipo': 'veneno', 
     'pokemon': 'Charizard', 'nivel': 55, 'tipo': 'fuego', 'subtipo': 'volador'}]
     }
    
]

#a. obtener la cantidad de Pokémons de un determinado entrenador

# def cantidadpokemones(entrenadores, buscado):
#     for entrenador in entrenadores:
#         if entrenador['nombre'] == buscado:

for entrenador in entrenadores:
    pos = search(entrenadores, 'nombre', entrenador['nombre'])
    if pos is not None:
        entrenadores[pos]['sublist'].append(entrenador)
    else:
        print('El entrenador no esta en la lista')