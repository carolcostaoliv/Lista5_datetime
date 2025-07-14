from datetime import datetime

class Paciente:
    def __init__ (self, nome, cpf, tel, dtn):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_tel(tel)
        self.set_dtn(dtn)

    def set_nome(self, nome):
        if nome == '': raise ValueError()
        self.__nome = nome
    def get_nome(self):
        return  self.__nome
    
    def set_cpf(self, cpf):
        if cpf == '': raise ValueError()
        self.__cpf = cpf
    def get_cpf(self):
        return self.__cpf
    
    def set_tel(self, tel):
        if tel =='': raise ValueError()
        self.__tel = tel
    def get_tel(self):
        return self.__tel
    
    def set_dtn(self, dtn):
        if dtn > datetime.now(): raise ValueError()
        self.__dtn = dtn
    def get_dtn(self):
        return self.__dtn
    
    def __str__(self):
        return f'Nome: {self.__nome} | Data de nascimento: {self.__dtn} | CPF: {self.__cpf} | Telefone {self.__tel}'

class PacienteUI:
    pacientes = []

    @classmethod
    def menu(cls):
        menu = int((input("1 - Listar dados | 2 - Fim: ")))
        return menu
    
    @classmethod
    def main(cls):
        op = 0
        while op != 2:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            else: print("Fim")
    
    @classmethod
    def inserir(cls):
        nome = input("Digite o seu nome: ")
        cpf = input("Digite o seu CPF: ")
        tel = input("Digite o seu telefone: ")
        dtn = datetime.strptime( input("Digite a sua data de nascimento: "), "%d/%m/%Y")

        p = Paciente(nome, cpf, tel, dtn)
        cls.pacientes.append(p)
        print(p)
        
PacienteUI.main()
