class ContaBancaria:

 def __init__(self, numero_conta, saldo=0, limite_saldo=float('inf')):
  self.numero_conta = numero_conta
  self.__saldo = saldo
  self.transacoes = []
 
 def depositar(self, valor):
  self.__saldo += valor
  self.registrar_transacao("Depósito", valor)
 
 def sacar(self, valor):
 
  if self.__saldo >= valor:
   self.__saldo -= valor
   self.registrar_transacao("Saque", valor)
  else:
  
   print("Saldo insuficiente.")
  
   def consultar_saldo(self):
    print("Saldo:", self.saldo)
    
    # getter para acessa saldo
    def get_saldo (self):
     return self.__saldo

    # setter para acessa saldo
    def set_saldo (self, valor):
      if valor >= 0:
       self.__saldo = valor
      else:
           print("voce nao pode ser pobre")
 
  def registrar_transacao(self, tipo, valor):
     self.transacoes.append({"Tipo": tipo, "Valor": valor})

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, limite_cheque_especial=0):
        super().__init__(numero_conta)
        self.limite_cheque_especial = limite_cheque_especial
    def emitir_cheque(self, valor):
    
        if self.__saldo + self.limite_cheque_especial >= valor:
            self.__saldo -= valor
            self.registrar_transacao("Emissão de Cheque", valor)
    
        else:
            print("Limite de cheque especial excedido.")

class ContaPoupanca(ContaBancaria):
    
    def calcular_juros_mensal(self, taxa_juros):
        juros = self.__saldo * (taxa_juros / 100)
        self.__saldo += juros
        self.registrar_transacao("Juros Mensais", juros)

class ContaInvestimento(ContaBancaria):
    
    def __init__(self, numero_conta):
        super().__init__(numero_conta)
        self.investimentos = []
 
    def realizar_investimento(self, produto, valor):
# Lógica para realizar o investimento
        self.registrar_transacao("Investimento", valor) 

    