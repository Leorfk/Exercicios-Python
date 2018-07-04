cidade = str(input('Em qual cidade você nasceu ?')).strip().lower()
print(cidade[:5].upper() == 'SANTO')
if cidade in 'santo':
    print('Tem Santo')
else:
    print('Não tem santo')