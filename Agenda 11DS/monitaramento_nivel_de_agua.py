
from colorama import Fore, Style, init

init(autoreset=True)

niveis = [
    "Muito baixo (CRÍTICO)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (ALERTA)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

print("=== MONITORAMENTO DO RESERVATÓRIO ===")
print("Escolha um nível de 1 a 5:")

nivel = int(input("Digite o nível atual: "))

if 1 <= nivel <= 5:
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    print(cor + mensagem + Style.RESET_ALL)
else:
    print("Nível inválido! Escolha de 1 a 5.")
