#Ex001
print('Olá, Mundo!')
#Ex002
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
#Ex003
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} é {}.'.format(n1, n2, s))
#Ex004
a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}.'.format(type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está em maiúsculas? {}'.format(a.isupper()))
print('Está em minúsculas? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))

#Ex005
n = int(input('Digite um número: '))
print('O número antecessor de {} é {} e o sucessor é {}.'.format(n, (n-1), (n+1)))
#Ex006  
n = int(input('Digite um número: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
#Ex007
n1 = float(input('Digite a primeiro nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A média entre {} e {} é {:.1f}.'.format(n1, n2, ((n1+n2)/2)))
#Ex008
m = float(input('Digite uma distância em metros: '))
print('A distância de {} metros corresponde a:\n{:.0f} centímetros\n{:.0f} milímetros\n{:.3f} quilômetros\n{:.3f} decâmetros\n{:.3f} hectômetros'.format(m, (m*100), (m*1000), (m/1000), (m/10), (m/100)))
#Ex009
n = int(input('Digite um número para ver sua tabuada: '))
print('Tabuada de {}:\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(n, n, (n*1), n, (n*2), n, (n*3), n, (n*4), n, (n*5), n, (n*6), n, (n*7), n, (n*8), n, (n*9), n, (n*10)))
#Ex010
n = float(input('quanto dinheiro você tem na carteira? R$:'))
print('Com R${:.2f} você pode comprar U${:.2f}.'.format(n, (n/5.25)))
#Ex011
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
print('A área da parede é de {:.2f}m². Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(area, (area/2)))
#Ex012
p = float(input('Digite o preço do produto: R$'))
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(p, (p*0.95)))
#Ex013
s = float(input('Digite o salário do funcionário: R$'))
print('Um funcionário que ganhava R${:.2f}, com aumento de 15% passa a ganhar R${:.2f}.'.format(s, (s*1.15)))

