import random
from time import sleep
numero = random.randint(0,5)
print('Adivinhe um número de 0 a 5.')
usuario = int(input('Digite seu número:'))
print('PROCESSANDO...')
sleep(2)
if usuario == numero:
    print('Você venceu')
else:
    print('Você perdeu! Eu pensei no número {} e não no número {}.'.format(numero,usuario))
print('FIM')