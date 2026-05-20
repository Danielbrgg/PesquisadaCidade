contador = 0
contadorMasculino = 0

salarioMasc = 0
rendafem = 0
rendatotal = 0

IdadeMaximaMasculina = 0
IdadeMinimaMasculina = 999

IdadeMaximaFeminino = 0
IdadeMinimaFeminino = 999

while True:
    idade = int(input("Qual a sua idade?: "))

    sexo = input("Qual o seu sexo? (m/f): ").lower()
    renda = float(input("Qual a sua renda? R$ "))

    contador += 1

    if renda >= 2000:
        rendatotal += 1

    if sexo == "m":
        salarioMasc += renda
        contadorMasculino += 1

        if idade > IdadeMaximaMasculina:
            IdadeMaximaMasculina = idade

        if idade < IdadeMinimaMasculina:
            IdadeMinimaMasculina = idade

    elif sexo == "f":

        if idade > IdadeMaximaFeminino:
            IdadeMaximaFeminino = idade

        if idade < IdadeMinimaFeminino:
            IdadeMinimaFeminino = idade

        if renda >= 1000 and renda <= 3000:
            rendafem += 1

    continuar = input("\nDeseja cadastrar outra pessoa? (s/n): ").lower()

    if continuar == "n":
        break

if contadorMasculino > 0:
    MediaSalarioMasc = salarioMasc / contadorMasculino
else:
    MediaSalarioMasc = 0

if contador > 0:
    PercentualTotal = (rendatotal / contador) * 100
else:
    PercentualTotal = 0

print(f"\nTotal de pessoas cadastradas: {contador}")

print(f"\nMédia de salário masculino: R$ {MediaSalarioMasc:.2f}")

print(f"\nMasculino:")
print(f"Maior idade: {IdadeMaximaMasculina} anos")
print(f"Menor idade: {IdadeMinimaMasculina} anos")

print(f"\nFeminino:")
print(f"Maior idade: {IdadeMaximaFeminino} anos")
print(f"Menor idade: {IdadeMinimaFeminino} anos")

print(f"\nQuantidade de mulheres com renda entre R$1000 e R$3000: {rendafem}")

print(f"Percentual de pessoas com renda maior ou igual a R$2000: {PercentualTotal:.2f}%")
