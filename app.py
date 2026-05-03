from colorama import init, Fore, Style

init()

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 0:
        return Fore.RED
    elif nivel == 1:
        return Fore.YELLOW
    elif nivel == 2:
        return Fore.GREEN
    elif nivel == 3:
        return Fore.CYAN
    elif nivel == 4:
        return Fore.BLUE

for i in range(len(niveis)):
    cor = definir_cor(i)
    print(cor + f"Nível {i+1} - {niveis[i]}")

print(Style.RESET_ALL)
