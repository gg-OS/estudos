def somaimposto(taxaimposto, custo):
    t = taxaimposto / 100
    return t * custo


taxa = float(input('Insira o valor da taxa (em %): '))
cust = float(input('Insira o valor do item: '))

print(f'O valor a ser pago em imposto é de: R$ {somaimposto(taxa, cust):.2f}')
