class Paciente:
    incremento = 0
    def __init__ (self, nome, ordem):
        self.nome = nome
        self.ordem = ordem
        
    def chegada (self, incremento):
        print (f" O paciente {self.nome} é o {self.ordem} na ordem de chegada. O próximo da fila é o paciente de número {self.ordem + incremento}. Por favor aguarde.")

teste1 = Paciente ("Antonio", 3)
teste1.chegada (1)

teste2 = Paciente ("Maria", 4)
teste2.chegada (1)

teste3 = Paciente ("Carlos", 5)
teste3.chegada (1)