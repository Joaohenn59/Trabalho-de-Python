import random  # Importa o módulo 'random' para selecionar palavras aleatoriamente

# Função que escolhe uma palavra aleatória da lista
def escolher_palavra():
    palavras = [
        "python", "programacao", "desenvolvimento", "jogo", "computador",
        "algoritmo", "software", "hardware", "codigo", "interface",
        "banco", "dados", "internet", "rede", "servidor",
        "inteligencia", "artificial", "variavel", "função", "objeto",
        "classe", "estrutura", "sistema", "debug", "script",
        "modulo", "pacote", "compilador", "editor", "terminal",
        "linux", "windows", "macos", "cloud", "api",
        "framework", "biblioteca", "versao", "controle", "loop",
        "condicional", "while", "for", "if", "else"
    ]
    
    # Retorna uma palavra aleatória em letras minúsculas
    return random.choice(palavras).lower()

# Função principal do jogo da forca
def jogar_forca():
    palavra = escolher_palavra()  # Palavra a ser adivinhada
    letras_acertadas = ["_"] * len(palavra)  # Lista com "_" para cada letra da palavra
    letras_erradas = []  # Lista para armazenar letras erradas
    tentativas_maximas = 6  # Número máximo de tentativas permitidas
    
    print("Bem-vindo ao Jogo da Forca!")
    
    # Loop principal do jogo
    while True:
        # Mostra o estado atual da palavra e erros
        print("\nPalavra: " + " ".join(letras_acertadas))
        print("Erros: " + ", ".join(letras_erradas))
        print(f"Tentativas restantes: {tentativas_maximas - len(letras_erradas)}")
        
        # Verifica se o jogador venceu
        if "_" not in letras_acertadas:
            print("\nParabéns! Você venceu!")
            break
        
        # Verifica se o jogador perdeu
        if len(letras_erradas) >= tentativas_maximas:
            print(f"\nGame Over! A palavra era: {palavra}")
            break
        
        # Solicita uma letra ao jogador
        tentativa = input("Digite uma letra: ").lower()
        
        # Verifica se a letra está na palavra
        if tentativa in palavra:
            # Atualiza as letras acertadas
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_acertadas[i] = tentativa
        else:
            # Adiciona à letra na lista de erros se ainda não tiver sido tentada
            if tentativa not in letras_erradas:
                letras_erradas.append(tentativa)

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    jogar_forca()
