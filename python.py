import random

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

    return random.choice(palavras).lower()

def jogar_forca():
    palavra = escolher_palavra()
    letras_acertadas = ["_"] * len(palavra)
    letras_erradas = []
    tentativas_maximas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while True:
        print("\nPalavra: " + " ".join(letras_acertadas))
        print("Erros: " + ", ".join(letras_erradas))
        print(f"Tentativas restantes: {tentativas_maximas - len(letras_erradas)}")
        
        if "_" not in letras_acertadas:
            print("\nParabéns! Você venceu!")
            break
            
        if len(letras_erradas) >= tentativas_maximas:
            print(f"\nGame Over! A palavra era: {palavra}")
            break
            
        tentativa = input("Digite uma letra: ").lower()
        
        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_acertadas[i] = tentativa
        else:
            if tentativa not in letras_erradas:
                letras_erradas.append(tentativa)

if __name__ == "__main__":
    jogar_forca()