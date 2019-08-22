class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Medico(Pessoa):
    def __init__(self, nome, crm, especialidade):
        super().__init__(nome)
        self.crm = crm
        self.especialidade = especialidade

        print('Nome: ' + nome + ',', 'CRM: ' + crm + ',', 'Especialidade: ' + especialidade)

class Paciente(Pessoa):
    def __init__(self, nome, rg, endereco, convenio, sintomas):
        super().__init__(nome)
        self.rg = rg
        self.endereco = endereco
        self.convenio = convenio
        self.sintomas = sintomas


        print('Nome: ' + nome + ',','RG: ' + rg +',', 'Endereço: ' + endereco + ',', 'Convenio: ' + convenio + ',','Sintomas: ' + sintomas)


paciente_1 = Paciente('Danilo', '43.434.353-3', 'Rua joao', 'AMil', 'catapora')
medico_1 = Medico('DR. Juninho', '4343533', 'Clinico')