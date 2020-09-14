class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributo_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

class homen(Pessoa):
    pass

if __name__ == '__main__':
    Dumaul = homen(nome='dumaul')
    luciano = homen(Dumaul, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'ramalho'
    print(luciano.sobrenome)
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(Dumaul.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(Dumaul.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(Dumaul.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classes(), luciano.nome_e_atributo_de_classes())
    pessoa=Pessoa('anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, homen))
    print(isinstance(Dumaul, Pessoa))
    print(isinstance(Dumaul, homen))