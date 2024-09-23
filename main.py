nomePaciente = input("Nome do paciente: ")
idadePaciente = int(input("Idade do paciente: "))

if idadePaciente < 12:
    nomeAcompanhante = input("Nome do responsável/acompanhante: ")
    rgAcompanhante = input("RG do responsável/acompanhante: ")

sintomas = ['Dor', 'Febre', 'Vômito', 'Fratura', 'Ferimentos graves']
informacoesSintomas = {}
for sintoma in sintomas:
    resposta = input(f"{sintoma} (Sim/Não): ") == 'Sim'
    informacoesSintomas[sintoma] = resposta

if informacoesSintomas['Ferimentos graves']:
    grauUrgencia = 'Alta'
elif informacoesSintomas['Fratura'] or informacoesSintomas['Vômito']:
    grauUrgencia = 'Média'
elif informacoesSintomas['Febre'] or informacoesSintomas['Dor']:
    grauUrgencia = 'Baixa'
else:
    grauUrgencia = 'Baixa'

print("\n--- INFORMAÇÕES DO ATENDIMENTO ---")
print(f"NOME DO PACIENTE: {nomePaciente}")
print(f"IDADE DO PACIENTE: {idadePaciente}")

if idadePaciente < 12:
    print(f"NOME DO RESPONSÁVEL/ACOMPANHANTE: {nomeAcompanhante}")
    print(f"RG DO RESPONSÁVEL/ACOMPANHANTE: {rgAcompanhante}")
else:
    print("NÃO É NECESSÁRIO ACOMPANHANTE PARA PACIENTES COM 12 ANOS OU MAIS.")

sintomasExibicao = ', '.join([f"{sintoma}: {'SIM' if resposta else 'NÃO'}" for sintoma, resposta in informacoesSintomas.items()])
print(f"SINTOMAS - {sintomasExibicao}")

print(f"GRAU DE URGÊNCIA: {grauUrgencia}")



# for name,idade in zip (["Joao","maria","carla"],[40,20,30]):
#     print(f"{name} tem {idade} anos")


# # pessoa = {'nome': 'joao', 'idade': '45', 'função':'operador de maquina'}
# # for funcionario,dados in pessoa.items():
# #     print(funcionario,dados)


# # for numero in range(0,9):
# #     print(numero)
# # else:
# #     print("\n contagem concluida")