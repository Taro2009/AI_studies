'''
A program célja, hogy egy AND kaput tanuljon meg lemodellezni.
Erre a perceptron tanulóalgoritmust fogjuk használni.
Lépések:

megj.: b megy a súlyba, x bemenetbe meg megy a konstans 1

'''
    

w = [0, 0, 0] #súlyvektor, 0-ról indul az egész és majd a program
                    #állítgatja át a súlyokat a futása során, hogy jó legyen

#AND logiaki kapu be és kimenete [input1, input2, output] formájú vektorokban
x1 = [1, 1, 0, 0]
x2 = [1, 0, 1, 0]
y = [1, 0, 0, 0]
##############################################################################
# f(x) az = 1, ha w[0]*x1[0] + w[1]*x2[0] > 0 és 0 minden más esetben.
# e = y - f(x)
# Ha e = 0 akkor nem bántjuk a w-t.
# Ha e = -1, akkor w = w - x alapján módosul a w
# Ha e = 1, akkor w = w + x alapján módosul a w
fx = None
ecount = 1 #hibaszám az iterációban, arra hogy tudjuk mikor fejezzük be a
            #futást
while ecount != 0:
    ecount = 0
    for i in range(0, 4):
        inputx = [1, x1[i], x2[i]] #input vektor craftolása, y[i]-ben van a várt y
        if (w[0]*inputx[0] + w[1]*inputx[1] + w[2]*inputx[2]) > 0:
            fx = 1
        else:
            fx = 0
        e = y[i] - fx #hiba számítása
        # w értékeit egyenként felülírni
        print('Eredeti w = ', w)
        print('Craftolt x amit használunk épp bemenetként:', inputx)
        print('Az ismert kimenet y = ', y[i])
        print('Számított f(x), azaz a tipp f(x) = ', fx)
        if e == 0:
            cstr = 'NINCS HIBA!!!'
        else:
            cstr = ''
            ecount += 1
        print('A hiba (y - f(x)): e = ', e, cstr)

        for j in range(0, 3):
            w[j] = w[j] + e*inputx[j]
        print('w <- w + ', e, '*x = ', w)
        print('-----------------------------------')
    

print('Kész vagyunk! Az adott w vektor tartalmazza a beállított súlyokat, innentől képes az AND kapu szimulálására.')
