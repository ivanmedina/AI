import random
from lib.funciones import *
from lib.reacciones import *
from lib.operadores import *
from timetabling.lib.funciones import MatricesX, rearmarX, Z

def remplazarIndividuo(poblacion, n , nm):
    for i in range(0,len(poblacion)):
        if poblacion[i].n == n:
            poblacion[i] == nm
    return poblacion

def mejorSolucion(poblacion,mejor):
    print('mejor PE antes> ',mejor.PE)
    for i in range( 0, len(poblacion) ):
        if float(poblacion[i].PE) < float(mejor.PE):
            print(float(poblacion[i].PE) +'<'+ float(mejor.PE))
            mejor = poblacion[i]
    print('mejor PE> ',mejor.PE)
    return mejor
        

def CRO( initialKE, KELossRate, colision, finicio, pinicio, fobjetivo, pobjetivo, pneighbor, alfa, beta, criterios ):
    poblacion = finicio( pinicio ) #inicializacion
    pobSize = len(poblacion)
    buffer = 0
    mejor = mejorSolucion(poblacion,poblacion[0])
    iteracion = 0
    # CRITERIOS DE ITERACION 
    while( pobSize < criterios['a'] and pobSize > criterios['b'] and iteracion < criterios['c'] ):
        t=random.uniform(0,1)
        if t > colision: # revisar si no es colision intermolecular
            m = random.choice(poblacion) # seleccionar molecula
            if m.hits - m.miniumhits > alfa:
                mds=descomposicion( m, float(buffer), halfOddEven, pneighbor, fobjetivo, pobjetivo, pobSize, initialKE )
                if mds[3]:
                    md1=mds[0] # molecula 1
                    md2=mds[1] # molecula 2
                    poblacion.remove( m )
                    poblacion.append( md1 ) # agregar molecula 1 a la poblacion
                    poblacion.append( md2 ) # agregar molecula 2 a la poblacion
                    buffer = float(mds[2])
            else:
                md=colision_inef_pared( m, buffer, randomRotate, pneighbor, fobjetivo, pobjetivo, KELossRate )
                if md[0].PE < md[0].minimumPE:
                    md[0].minimumPE = md[0].PE 
                    md[0].minimumhits = md[0].hits 
                    md[0].minimumw = md[0].w
                poblacion = remplazarIndividuo( poblacion, m.n, md[0] )
                buffer=float(md[1])
        elif len(poblacion) > 1:
            n1 = 0
            n2 = 0
            while(n1==n2):
                m1=random.choice(poblacion)  # seleccionar molecula 1
                m2=random.choice(poblacion)  # seleccionar molecula 2
                n1=m1.n
                n2=m2.n
            if m1.KE <= beta and m2.KE < beta:
                md=sintesis( m1, m2, halfExchange, pneighbor, fobjetivo, pobjetivo, pobSize, initialKE )
                if(md[1]): # si es una reaccion exitosa
                    poblacion.remove( m1 ) # remover molecula 1 de la poblacion
                    poblacion.remove( m2 ) # remover molecula 2 de la poblacion
                    poblacion.append( md[0] ) # agregar nueva molecula a la poblacion
            else:
                mds=colision_inef_intermol( m1, m2, randomRotate, pneighbor, fobjetivo, pobjetivo )
                md1=mds[0] # molecula 1
                md2=mds[1] # molecula 2
                if md1.PE < md1.minimumPE:
                    md1.minimumPE = md1.PE 
                    md1.minimumhits = md1.hits 
                    md1.minimumw = md1.w
                if md2.PE < md2.minimumPE:
                    md2.minimumPE = md2.PE 
                    md2.minimumhits = md2.hits 
                    md2.minimumw = md2.w 
                poblacion = remplazarIndividuo( poblacion, m1.n, md1)
                poblacion = remplazarIndividuo( poblacion, m2.n, md2)
        mejores=mejorSolucion(poblacion,mejor)
        pobSize= len(poblacion)
        iteracion = iteracion +1
    return mejor