with open('series.csv', 'r', encoding='utf-8') as file:
    serie=str(input('Forneça a série: '))
    for line in file.readlines():
        lista = line.split(',')
        if lista[0] == serie:
            temporada = max(lista[1])
            if (max(lista[1]) == temporada:
                n_epi = max(lista[2])
                print(serie,'Temporadas: ',temporada,'Episodios: ',n_epi)
                         
        
