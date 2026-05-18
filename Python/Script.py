contador = 0
contadorM = 0
salarioMasc = 0

IdadeMaximaMasculina = 0
IdadeMinimaMasculina = 999

IdadeMaximaFeminino = 0
IdadeMinimaFeminino = 999

while True:
    idade = int(input("Qual a sua idade? (digite 0 para parar o contador): "))

    if idade == 0:
        break

    sexo = input("Qual o seu sexo? m (masculino) f (feminino): ")
    renda = float(input("Qual a sua renda: R$ "))

    contador += 1

    if sexo == "m":
        salarioMasc += renda
        contadorM += 1

        if idade > IdadeMaximaMasculina:
            IdadeMaximaMasculina = idade

        if idade < IdadeMinimaMasculina:
            IdadeMinimaMasculina = idade

    if sexo == "f":

        if idade > IdadeMaximaFeminino:
            IdadeMaximaFeminino = idade

        if idade < IdadeMinimaFeminino:
            IdadeMinimaFeminino = idade

if contadorM > 0:
    MediaSalarioMasc = salarioMasc / contadorM
else:
    MediaSalarioMasc = 0

print(f"\nTotal de pessoas cadastradas: {contador}")

print(f"\nMédia de salário masculino: R$ {MediaSalarioMasc:.2f}")

print(f"\nMasculino:")
print(f"Maior idade: {IdadeMaximaMasculina} anos")
print(f"Menor idade: {IdadeMinimaMasculina} anos")

print(f"\nFeminino:")
print(f"Maior idade: {IdadeMaximaFeminino} anos")
print(f"Menor idade: {IdadeMinimaFeminino} anos")