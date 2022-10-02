def BINGO():
    print('\n\nWelcome to Quick BINGO\n===================\n')
    #CREAR LISTAS PARA LOS NUMEROS
    import random
    numbers = list()
    numbers2 = list()
    counter = 0
    counter2 = 0
    counter3 = 0
    listanumerosviejos = list()
    #SELECCIONANDO MODO DE JUEGO
    while True:
        partida = input('>>> You want to:\n1) Start a new game\n2) Resume a game\n3) Create Bingo cards\n\n>>> ')
        try:
            partida = int(partida)
        except:
            break
        if partida == 1:
            break
        if partida == 2:
            try:
                numerosviejos = input('Please write only the numbers that have already come out, followed by a comma *,*, without spaces and without repeating\n>>>')
            except:
                print('#ERROR \nPlease try again')
                continue
            x = numerosviejos.split(',')
            for number in x:
                try:
                    number = int(number)
                except:
                    number = 0

                listanumerosviejos.append(number)
            break
        #CREANDO CARTONES
        if partida ==3:
            cartones = input('How many cards do you want to create?\n>>>')
            try:
                cartones = int(cartones)
            except:
                print('Please indicate a valid number of cards\n ')
                continue
            for i in range(cartones):
                print('Card number:',counter3 + 1)
                #ASIGNANDO VALOR PSEUDORANDOM A CADA CARTON
                B = random.sample(range(1,16),5)
                I = random.sample(range(16,31),5)
                N = random.sample(range(31,46),4)
                G = random.sample(range(46,61),5)
                O = random.sample(range(61,76),5)
                print('O',sorted(O))
                print('G',sorted(G))
                print('N',sorted(N))
                print('I',sorted(I))
                print('B',sorted(B))
                counter3 = counter3 + 1
                print('\n')

        else:
            print('\n\nSelect a valid option\n\n')
            continue


    #AGREGANDO NUMEROS A LAS LISTAS
    while counter < 75:
        numbers.append(counter2 + 1)
        counter2 = counter2 + 1
        counter = counter + 1
    #AGREGANDO O QUITANDO NUMEROS EN CASO DE JUEGO PREVIO
    if sum(listanumerosviejos) > 0:
        for y in listanumerosviejos:
            try:
                numbers.remove(y)
                numbers2.append(y)
            except:
                continue

    print('\nLIST OF NUMBERS CREATED\n')

    while True:
        message = input('\n\nPress enter to see the next number\nType *done* to finish\n\n')
        if message == '':
            if sum(numbers) == 0:
                print('THANKS FOR PLAYING')
                exit()
            #GENERANDO NUMERO AL AZAR
            x = random.choice(numbers)
            #ASIGNANDOLE LETRA AL NUMERO
            if x <= 15:
                letra = 'B'
            elif x <= 30:
                letra = 'I'
            elif x <= 45:
                letra = 'N'
            elif x <= 60:
                letra = 'G'
            elif x <= 75:
                letra = 'O'
            print('\nTHE NUMBER IS:',letra,x)
            numbers2.append(x)
            numbers.remove(x)

            print('\nMARKED', numbers2)
        elif message == 'done':
            exit()

#PONIENDO EN MARCHA LA FUNCION
BINGO()