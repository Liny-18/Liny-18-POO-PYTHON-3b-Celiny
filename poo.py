class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(self.titulo, "-", self.genero)
class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print(f"Filme: {self.titulo} | Gênero: {self.genero} | Duração: {self.duracao} min")

class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print(f"Série: {self.titulo} | Gênero: {self.genero} | Temporadas: {self.temporadas}")

class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print(f"Doc: {self.titulo} | Gênero: {self.genero} | Tema: {self.tema}")



class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    # Sobrescrevendo o método exibir_info
    def exibir_info(self):
        print(f"Podcast: {self.titulo} | Gênero: {self.genero} | Episódios: {self.episodios}")



catalogo = [
    Filme("IT: A coisa", "Terror",135),
    Filme("Invocação do Mal", "Terror", 112),
    Serie("Monstros: A história de Lizzie Borden", "Suspense", 4),
    Serie("Round 6", "Suspense", 2),
    Documentario("Nosso Planeta", "Natureza", "Vida selvagem"),
    Documentario("A noite que mudou o pop","Musical",'Música anos 80'),
    Podcast("Colecionador de ossos", "Casos criminais", 450)
]

print("--- EXIBINDO O CATÁLOGO MISTO ---")
for item in catalogo:
    item.exibir_info()  # Aqui acontece o Polimorfismo!
