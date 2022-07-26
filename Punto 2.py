productos = {
    'prod1' : {
        'id' : 1, 
        'referencia' : 'BRAGA',
        'genero' : 'F',
        'precio' : 60_000
    },
    'prod2' : {
        'id' : 2,
        'referencia' : 'PANTALÓN',
        'genero' : 'M',
        'precio' : 70_000
    },
    'prod3' : {
        'id' : 3,
        'referencia' : 'JOGGER',
        'genero' : 'F',
        'precio' : 70_000
    }
}
aux = []
for i in range(len(productos)):
    aux += [productos['prod%s'%(i+1)]['precio']]
print(productos), print(f'La suma de los productos es de ${sum(aux)}')
