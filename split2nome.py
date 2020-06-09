"""
Script feito pro pessoal de linguística do MPEG

Israel Marcon, 2020.

Contato: marconisrael290@gmail.com
"""

import glob, os, sys, shutil
prefixo = sys.argv[1]

#criando listas com os nomes dos arquivos arquivos
txt = glob.glob('*.txt')
todos = glob.glob('*.wav') + txt

#copiando arquivos pra evitar perder dados etc
if not os.path.exists('renomeados'): os.makedirs('renomeados')
dest_dir = os.getcwd() + '/renomeados'
for i in todos:
	shutil.copy(i,dest_dir)

#definindo correção de ipa pra ortografia de arquivo
def ortografar(pal):
	substituidas = []
	for i in pal:
		i = i.replace('æ','a')
		i = i.replace('ʌ','a')
		i = i.replace('ʌ̃','a')
		i = i.replace('ã','a')
		i = i.replace('æ̃','a')
		i = i.replace('ɛ̃','e')
		i = i.replace('ẽ','e')
		i = i.replace('ẽ','e')
		i = i.replace('ɛ','e')
		i = i.replace('ĩ','i')
		i = i.replace('ĩ','i')
		i = i.replace('ɨ̃','y')
		i = i.replace('ɨ','y')
		i = i.replace('ɔ','o')
		i = i.replace('ɔ̃','o')
		i = i.replace('õ','o')
		i = i.replace('õ','o')
		i = i.replace('ũ','u')
		i = i.replace('ũ','u')
		i = i.replace('ʊ','u')
		i = i.replace('ʊ̃','u')
		i = i.replace('ɲ','n')
		i = i.replace('ʃ','s')
		i = i.replace('ɾ','r')
		i = i.replace('j̃','j')
		i = i.replace('ʔ','-')
		i = i.replace('\'','')
		i = i.replace(' ','-')
		if i is not '\n': substituidas.append(i)
	palavra_final = "".join(substituidas)
	return palavra_final

#renomeando
for i in txt:
	with open(i) as arquivo:
		for texto in arquivo:
			#criando lista só com os arquivos .wav
			wav = 'renomeados/' + i.replace('.txt', '.wav')
			#tirando os caracteres ipa
			orto = ortografar(texto)
			final = 'renomeados/' + prefixo + str(orto) + '.wav'
			index = 2 #(pra renomear cópias como 'arquivo2', 'arquivo3', etc)
			#checando se o arquivo é repetido
			while os.path.exists(final):
				final = 'renomeados/' + prefixo + str(orto) + str(index) + '.wav'
				index += 1
			os.rename(wav, final)
			#apagando os .txt
			for i in txt:
				rem = 'renomeados/' + i
				if os.path.exists(rem):
					os.remove(rem)			

#checagem final
check = glob.glob('renomeados/*')
if len(check) == len(txt):
	print('provavelmente deu certo :D')
else:
	print('acho que deu ruim D:')
