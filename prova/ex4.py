with open('series.csv', 'r', encoding='utf-8') as file:

    for line in file.readlines():
        lista = line.split(',')

        x=lista[0]
        if x == 'Breaking bad':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media1 = (imdb+netflix)/2
        if x == 'Black Mirror':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media2 = (imdb+netflix)/2
        if x == 'Friends':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media3 = (imdb+netflix)/2
        if x == 'The Big Bang Theory':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media4 = (imdb+netflix)/2
        
        
    dic1 = {'Breaking bad':media1,'Black Mirror':media2,'The Big Bang Theory':media3,'Friends':media4}
with open('series_novas.csv', 'r', encoding='utf-8') as file:

    for line in file.readlines():
        lista = line.split(',')

        x=lista[0]
        if x == 'Narcos':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media5 = (imdb+netflix)/2
        if x == 'Suits':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media6 = (imdb+netflix)/2
        if x == 'Designated Survivor':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media7 = (imdb+netflix)/2
        if x == 'Lucifer':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media8 = (imdb+netflix)/2
        if x == 'Fuller House':
            imbd = max(lista[5])
            netflix = max(lista[6])
            media9 = (imdb+netflix)/2
        
        
    dic2 = {'Narcos':media5,'Suits':media6,'Designated survivor':media7,'Lucifer':media8,'Fuller House': media9}


