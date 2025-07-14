from datetime import datetime
import enum

class pagamento (enum.Enum):
    em_aberto = 0
    parcial = 1
    pago = 2

class Boleto:
    def __init__(self, cd_barras, dt_emissao, dt_vencimento, vl_boleto, vl_pago):
        self.set_cd_barras(cd_barras)
        self.set_dt_emissao(dt_emissao)
        self.set_dt_vencimento(dt_vencimento)
        self.__dt_pagamento = None
        self.set_vl_boleto(vl_boleto)
        self.set_vl_pago (vl_pago)
        self.__situacao = pagamento.em_aberto

    def set_cd_barras(self, cd_barras):
        if cd_barras == "": raise ValueError ("Código de barras inválido")
        self.__cd_barras = cd_barras 
    def get_cd_barras(self):
        return self.__cd_barras
    
    def set_dt_emissao(self, dt_emissao):
        if dt_emissao > datetime.now(): raise ValueError ("Data de emissão inválida")
        self.__dt_emissao = dt_emissao
    def get_dt_emissao(self):
        return self.__dt_emissao
    
    def set_dt_vencimento(self, dt_vencimento):
        if dt_vencimento < datetime.now(): raise ValueError ("Data de vencimento inválida")
        self.__dt_vencimento = dt_vencimento
    def get_dt_vencimento(self):
        return self.__dt_vencimento
    
    def set_vl_boleto(self, vl_boleto):
        if vl_boleto < 0 :raise ValueError ("Valor inválido")
        self.__vl_boleto = vl_boleto
    def get_vl_boleto(self):
        return self.__vl_boleto
    
    def set_vl_pago(self, vl_pago):
        if vl_pago < 0 : raise ValueError("Valor inválido")
        self.__vl_pago = vl_pago
    def get_vl_pago(self):
        return self.__vl_pago
    
    def pagar (self, vl_pago):
        self.__dt_pagamento = datetime.now()
        if vl_pago <= 0: raise ValueError ("Valor inválido")
        if vl_pago == self.__vl_boleto:
            self.__situacao = pagamento.pago
            self.__vl_pago = self.__vl_boleto
        if vl_pago < self.__vl_boleto:
            self.__situacao = pagamento.parcial
            self.__vl_pago = vl_pago

    def __str__(self):
        return f"Código de barras: {self.__cd_barras} | Data de emissão: {self.__dt_emissao} | Data de vencimento: {self.__dt_vencimento} | Data do pagamento: {self.__dt_pagamento} | Valor do boleto: {self.__vl_boleto}\nValor pago: {self.__vl_pago} | Situação do boleto: {self.__situacao.name}"

class BoletoUI:

    @classmethod
    def menu(cls):
        menu = int((input("1 - Calcular boleto | 2 - Fim: ")))
        return menu
    
    @classmethod
    def main(cls):
        op = 0
        while op != 2:
            op = BoletoUI.menu()
            if op == 1: BoletoUI.inserir()
            else: print("Fim")
    
    @classmethod
    def inserir(cls):
        cd_barras = input("informe o código de barras: ")
        vl_boleto = float(input("informe o valor do boleto: "))
        dt_emissao = datetime.strptime(input("informe a data de emissão do boleto: "), "%d/%m/%Y")
        dt_vencimento = datetime.strptime(input("informe a data de vencimento do boleto: "), "%d/%m/%Y")
        vl_pago = int(input("Informe o valor pago: "))

        x = Boleto(cd_barras, dt_emissao, dt_vencimento, vl_boleto, vl_pago)
        x.pagar(vl_pago)
        print(x)
        print(x.pagar)

BoletoUI.main()