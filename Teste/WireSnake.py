import subprocess

def criar_rede_falsa(nome_rede, canal, interface):
    """Cria um ponto de acesso Wi-Fi falso usando airbase-ng."""
    try:
        comando = ["airbase-ng", "-e", nome_rede, "-c", str(canal), interface]
        processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        saida, erro = processo.communicate()

        if processo.returncode == 0:
            print("Ponto de acesso falso criado com sucesso!")
            print(saida.decode())
        else:
            print(f"Erro ao criar ponto de acesso falso: {erro.decode()}")
    except FileNotFoundError:
        print("airbase-ng não encontrado. Certifique-se de que o Aircrack-ng esteja instalado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
criar_rede_falsa("Rede Falsa", 6, "wlan0mon")

# para parar o processo, pode se usar o comando
# airbase-ng --stop wlan0mon