class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.filhos = filhos
        self.idade = idade
        self.nome = nome

    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    Gabriel = Homem(nome='Gabriel')
    Lucio = Homem(Gabriel, nome='Lucio')
    print(Pessoa.comprimentar(Gabriel))
    print(id(Gabriel))
    print(Gabriel.comprimentar())
    print(Gabriel.nome)
    print(Gabriel.idade)
    for filho in Gabriel.filhos:
        Gabriel.Sobrenome = 'Barcellos'
    del Gabriel.filhos
    Gabriel.olhos = 1
    del Gabriel.olhos
    print(Gabriel.__dict__)
    print(Lucio.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Lucio.olhos)
    print(Gabriel.olhos)
    print(id(Pessoa.olhos), id(Gabriel.olhos), id(Lucio.olhos))
    print(Pessoa.metodo_estatico, Gabriel.metodo_estatico)
    print(Pessoa.nome_e_atributos_de_class, Gabriel.nome_e_atributos_de_class)
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Gabriel, Pessoa))
    print(isinstance(Gabriel, Homem))