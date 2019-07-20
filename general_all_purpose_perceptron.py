'''
general purpose perceptron algorithm that is able to take any number of inputs,
train on the data then end with a calculated weight vector
'''
import numpy as np

#please fill in the upcoming variables so the program works properly!
no_of_inputs = 3 # the number of inputs to the system
no_of_dimensions = 2
x1 = [-1, 0, 10] #in this case we have 3 points: (-1, 1); (0, -1); and (10, 1)
x2 = [1, -1, 1]
w = np.zeros(no_of_dimensions + 1)
for element in w:
    element = int(element)
# ...
# create lists for more dimensions, create more elements for teh list for more
# inputs (coordinates)
# also create the output list (has to have as many elements as no_of_inputs):
y = [1, -1, 1]
learning_rate = 1
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
    for i in range(0, no_of_inputs):
        inputx = [1, x1[i], x2[i]] #input vektor craftolása, y[i]-ben van a várt y
        if (w[0]*inputx[0] + w[1]*inputx[1] + w[2]*inputx[2]) > 0:
            fx = 1
        elif (w[0]*inputx[0] + w[1]*inputx[1] + w[2]*inputx[2]) == 0:
            fx = 0
        else:
            fx = -1
        if y[i] == 1 and fx == -1:
            e = 1
        else:
            e = y[i] - fx #hiba számítása
        # w értékeit egyenként felülírni
        print('Eredeti w = ', w)
        print('A b értéke: ', w[0]*inputx[0])
        print('A w a b első elem nélkül: ', w[1:])
        print('Craftolt x amit használunk épp bemenetként:', inputx)
        print('Az ismert kimenet y = ', y[i])
        print('Számított f(x), azaz a tipp f(x) = ', fx)
        if e == 0:
            cstr = 'NINCS HIBA!!!'
        else:
            cstr = ''
            w[0] = w[0] + e*learning_rate
            ecount += 1
        print('A hiba (y - f(x)): e = ', e, cstr)

        for j in range(1, no_of_inputs):
            w[j] = w[j] + e*inputx[j]*learning_rate
        print('w <- w + ', e, '*x = ', w)
        print('-----------------------------------')
    

print('Kész vagyunk! Az adott w vektor tartalmazza a beállított súlyokat.')
