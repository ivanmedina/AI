from lib.restricciones import R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11

RDn=7
RSn=4
K=1000

def verificarR1(input,X):
    verificado=True
    for c in range(0,len(input['cursos'])):
        if not R1(input,X, c):
            verificado=False
            break
    return 1 if verificado else 0

def verificarR2(input,X):
    verificado=True
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for p in range(0,len(input['profesores'])):
                if not R2(X,d,e,p):
                    verificado=False
                    break
            if not verificado: break
        if not verificado: break
    return 1 if verificado else 0

def verificarR3(X):
    verificado=True
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                if not R3(X,d,e,s):
                    verificado=False
                    break
            if not verificado: break
        if not verificado: break
    return 1 if verificado else 0

def verificarR4(input,Y):
    verificado=True
    for c in range(0,len(Y)):
        for p in range(0,len(Y[c])):
            if not R4(input,Y,c,p):
                verificado=False
        if not verificado: break
    return 1 if verificado else 0

def verificarR5(input,Y):
    verificado=True
    for p in range(0,len(input['profesores'])):
        if not R5(input,Y,p):
            verificado=False
            break
    return 1 if verificado else 0

def verificarR6(input,X):
    verificado=True
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for p in range(0,len(input['profesores'])):
                if not R6(input,X,d,e,p):
                    verificado=False
            if not verificado: break
        if not verificado: break
    return 1 if verificado else 0

def verificarR7(input,X):
    verificado=True
    for d in range(0,len(X)):
        for c in range(0,len(input['cursos'])):
            for p in range(0,len(input['profesores'])):
                if not R7(input,X,d,c,p):
                    verificado=False
                    break
            if not verificado: break
        if not verificado: break
    return 1 if verificado else 0

def verificarR8(V):
    verificado=0
    for c in range(0,len(V)):
        if not R8(V,c):
            verificado=verificado+(1/len(V))
    return verificado

def verificarR9(input,X,U,W):
    verificado=0
    for c in range(0,len(input['cursos'])):
        if not R9(X,U,W,c):
           verificado=verificado+(1/len(input['cursos']))
    return verificado 

def verificarR10(input,W):
    verificado=0
    # suma=0
    for d in range(0, len(W)-1):
        for c in range(0,len(W[d])):
            if not R10(W,d,c):
                verificado=verificado+(1/((len(input['dias'])-1)*(len(input['cursos']))))
                # break
        # if not verificado: break
    return verificado

def RDCheck(input,parametros):
    if RD(input,parametros)==RDn:
        return 1
    return 0

def RD(input,parametros):
    suma=0
    suma+=verificarR1(input,parametros['X'])
    suma+=verificarR2(input,parametros['X'])
    suma+=verificarR3(parametros['X'])
    suma+=verificarR4(input,parametros['Y'])
    suma+=verificarR5(input,parametros['Y'])
    suma+=verificarR6(input,parametros['X'])
    suma+=verificarR7(input,parametros['X'])
    return suma

def RS(input,parametros,Zanterior,Znueva):
    suma=0
    suma+=verificarR8(parametros['V'])
    suma+=verificarR9(input,parametros['X'],parametros['U'],parametros['W'])
    suma+=verificarR10(input,parametros['V'])
    suma+= 100 if R11(Zanterior,Znueva) else 0
    return suma

def fobjetivo(input,parametros,Zanterior,Znueva):
    return (RD(input,parametros)*K)+RS(input,parametros,Zanterior,Znueva)

def fitness(Z):
    return 1/(1-Z)