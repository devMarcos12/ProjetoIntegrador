
# name = input('Digite o nome do produto: ')
# cod = int(input('Digite o código do Produto: '))
CustoProduto = int(input('Qual o custo de produção (CP)? '))
CustoFixo = int(input('Qual o custo fixo(CF)? '))
ComissaoVendas = int(input('Qual a commissão de vendas (CV)? '))
Imposto = int(input('Qual o Imposto (sobre vendas)? '))
MargemLucro = int(input('Qual a Margem de lucro(CP)? '))
PrecoVenda = CustoProduto / (1-((CustoFixo+ComissaoVendas+Imposto+MargemLucro)/(100)))


print(f'{PrecoVenda:.3f}')

ReceitaBruta = PrecoVenda - CustoProduto
print(f'{ReceitaBruta:.3f}')  

PercentCf = 15 * PrecoVenda / 100
PercentCv = 5 * PrecoVenda / 100
PercentImp = 12 * PrecoVenda / 100

OutrosCustos = PercentCf + PercentCv + PercentImp
print(f'{OutrosCustos:.3f}')



rent = ReceitaBruta - OutrosCustos
print(f'{rent:.3f}')


print('Descrição / Valor / %')
print(f'Preço de Venda / {PrecoVenda} / 100%')
print(f'Custo de Aquisição / {CustoProduto} / {CustoProduto}')
print(f'Receita Bruta / {ReceitaBruta} / {ReceitaBruta}')
print(f'Custo Fixo / {PercentCf} / {CustoFixo}')
print(f'Comissão de Venda / {PercentCv} / {ComissaoVendas}')
print(f'Impostos / {PercentImp} / {Imposto}')
print(f'Outros Custos / {OutrosCustos} / ')
print(f'Rentabilidade / {rent} / ')





