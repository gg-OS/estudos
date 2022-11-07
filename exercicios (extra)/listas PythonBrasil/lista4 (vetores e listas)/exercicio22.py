c = 0
mouse = []

while True:
    id = input('Insira o problema do mouse: ')
    if id == '0':
        break
    else:
        mouse.append(id)
        c += 1
print('Situação\t\t\tQuantidade\tPercentual')
print(f'1 - necessita de esfera: {mouse.count("esfera")} - {(mouse.count("esfera") / len(mouse)) * 100:.0f}%')
print(f'2 - necessita de limpeza: {mouse.count("limpeza")} - {(mouse.count("limpeza") / len(mouse)) * 100:.0f}%')
print(f'3 - necessita de troca de cabo: {mouse.count("cabo")} - {(mouse.count("cabo") / len(mouse)) * 100:.0f}%')
print(f'4 - quebrado ou inutilizado: {mouse.count("quebrado")} - {(mouse.count("quebrado") / len(mouse)) * 100:.0f}%')
