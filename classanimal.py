class Animal:
    def __init__(self, nome, tipo, raca):
        self.nome = nome
        self.tipo = tipo 
        self.raca = raca

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo
        
    def get_raca(self):
        return self.raca

    def set_raca(self, raca):
        self.raca = raca

#objeto
animal = Animal("Bolinha", "Cachorro", "SRD")
print(animal.__dict__)
animal.nome = str(input("Informe o nome do animal: "))
animal.tipo = str(input("Informe o tipo do animal: "))
animal.raca = str(input("Informe a raca do animal: "))
print(animal.nome)
print(animal.tipo)
print(animal.raca)