from logic import And, Not, Implication, Or, Symbol, model_check, Biconditional

# Symbols
# "Rain"
# "Hagrid"
# "Dumbledore"

R=Symbol("Rain")
H= Symbol('Hagrid')
D= Symbol("Dumbledore")

# knowledge
knowledge = And(Implication(Not(R),H),(
                And(Implication(H, Not(D)), Implication(D, Not(H)))),
                D)

# L: llovio
# H: harry visita a hagrid
# D: harry visita a dumbledore

# Si no llovió, Harry visitó a Hagrid hoy
# not L → H

# Harry visitó a Hagrid o a Dumbledore hoy, pero no a ambos
# (H → not D) v (D → not H)

# Harry visitó a Dumbledore hoy
# D 

print(f"Rain: {model_check(knowledge, R)}")
print(f"Hagrid: {model_check(knowledge, H)}")
print(f"Dumbledore: {model_check(knowledge, D)}")
print(knowledge.formula())

# Examples

## 1. Si estudio o hago tareas, entonces paso el curso, pero si no estudio, no paso.
"""
((E v T) → C) ^ (not E → not C)
Dado que: estudio

- ¿paso el curso? → True
- ¿no paso el curso? → False
"""
Estudio=Symbol("Estudio")
Tarea=Symbol("Tarea")
Curso=Symbol("Curso")
knowledge2=And(Implication(Or(Estudio,Tarea),Curso),
                  Implication(Not(Estudio),Not(Curso)))

knowledge2.add(Estudio)
print(f"Estudio: {model_check(knowledge2, Estudio)}")
print(f"Hace tarea: {model_check(knowledge2, Tarea)}")
print(f"Paso curso: {model_check(knowledge2, Curso)}")

## 2. Si estudio, entonces si hago tareas paso el curso.
""""
E → (T → C)
Dado que: estudio, hago tareas

- ¿paso el curso? → True
"""
knowledge3=And(Implication(Estudio,Implication(Tarea,Curso)))
knowledge3.add(Estudio)
knowledge3.add(Tarea)
print(f"Estudio: {model_check(knowledge3, Estudio)}")
print(f"Hace tarea: {model_check(knowledge3, Tarea)}")
print(f"Paso curso: {model_check(knowledge3, Curso)}")



## 3. Voy al cine si y solo si termino la tarea y no estoy cansado.
"""
C<->(T ^ not C)
Dado que: termino la tarea, no estoy cansado

- ¿voy al cine? → True
- ¿no voy al cine? → False
"""
Cine=Symbol("Cine")
TerminoT=Symbol("TerminoT")
Cansado=Symbol("Cansado")

knowledge4=And(Biconditional(Cine,And(TerminoT,Not(Cansado))))
knowledge4.add(TerminoT)
knowledge4.add(Not(Cansado))

print(f"Voy al cine: {model_check(knowledge4, Cine)}")
print(f"Termino tarea: {model_check(knowledge4, TerminoT)}")
print(f"Esta cansado: {model_check(knowledge4, Cansado)}")



## 4. Si el sistema responde y no hay timeout, entonces la transacción se procesa; de lo contrario, falla.
"""
((S ^ not T) → P) ^ not ((S ^ not T) → P)
Dado que: el sistema responde, no hay timeout

- ¿la transacción se procesa? → True
- ¿la transacción falla? → False
"""
SistemaR= Symbol("SistemaR")
TimeOut= Symbol("TimeOut")
ProcesaT= Symbol("ProcesaT")

knowledge5=And(Implication(And(SistemaR, Not(TimeOut)),ProcesaT),Not(Implication(And(SistemaR, Not(TimeOut)),ProcesaT)))
knowledge5.add(ProcesaT)

"""
---

## 5. No es cierto que si estudio entonces paso.
not(E → P)
- ¿estudio? → True
- ¿no paso? → True
"""
