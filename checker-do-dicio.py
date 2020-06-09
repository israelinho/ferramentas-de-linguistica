"""
Script feito pro pessoal de linguística do MPEG

Israel Marcon, 2020.

Contato: marconisrael290@gmail.com
"""

import glob, openpyxl

#listando os áudios e fotos
audios = []
wav = glob.glob("audio/*.wav")
for i in wav:
	audios.append(i.replace('audio/', ''))

fotos = []
jpg = glob.glob("foto/*.jpg") #alterar aqui caso esteja usando png ou outro formato de imagem
for i in jpg:
	fotos.append(i.replace('foto/',''))	

#listando coisas do xlsx
ximg = [] #imagens do xlsx
xaud = [] #áudios do xlsx

xlsx = openpyxl.load_workbook('dicionario.xlsx')
sheet = xlsx.active

for i in sheet['B']: #coluna das imagens
	if i.value is not None:
		ximg.append(i.value)
for i in sheet['C']: #coluna dos áudios
	if i.value is not None:
		xaud.append(i.value)

#checando
missing = [] #lista de arquivos que faltam
for i in ximg:
	if i not in fotos:
		missing.append(i)
for i in xaud:
	if i not in audios:
		missing.append(i)

#escrevendo o resultado num arquivo
with open('missing.txt','w') as arquivo:
	arquivo.write('\n'.join(missing))
	arquivo.close()

print('prontinho')
