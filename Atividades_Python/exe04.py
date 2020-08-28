height = float(input("Digite sua altura: "))
Weight = float(input("Digite seu peso: "))

imc = Weight / height ** 2

if imc <= 18.5:
    print("Seu imc é {:.1f} você está abaixo do peso! ".format(imc))
elif imc >= 25:
    print("Seu imc é {:.1f} você está acima do peso! ".format(imc))
if imc > 18.5 and imc <= 25:
    print("Seu imc é {:.1f} você esta com peso normal! ".format(imc))