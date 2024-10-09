# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media 

def verificar_media(media):
    if media >=7:
        return "aprovado"
    else:
        return "reprovado"
    
nota1 = float(input("digite a nota "))
nota2 = float(input("digite a nota "))
nota3 = float(input("digite a nota "))

resultado_media = calcular_media(nota1, nota2, nota3)
analise_da_media = verificar_media(resultado_media)

print(f'sua media é {resultado_media}')
print(f'voce está {analise_da_media}')