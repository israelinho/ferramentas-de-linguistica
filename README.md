# Ferramentas de Linguística
Scripts simples que eu fiz pra automatizar alguns processos na dicionarização nos moldes do Museu Paraense Emílio Goeldi. Se vc usar tipos de arquivos diferentes, nomes diferentes e essas coisas, meus scripts vêm cheios de # pra vc saber onde mudar.
Todos eu testei no meu python 3.5.2 então não garanto outras versões desculpa.

Meu e-mail pra contato é marconisrael290@gmail.com :)

## Os scripts
### split2nome.py
Feito pra rodar logo depois do elan2split, ele renomeia os áudios usando o texto que tá nos arquivos .txt

Como ele é feito pra língua Kanoé, a primeira coisa que vc tem que fazer pra rodar ele é checar se todos os caracteres IPA que vc usa tão naquela lista gigante no meio. Se não tiver, vc só coloca:

```python
i = i.replace('x','y') #x é o caractere IPA e y como ele vai precisa ficar corrigido, ex: ã vira a
```

Antes de rodar ele não esquece de tirar da pasta outros arquivos .txt e .wav que não sejam os do elan2split com aqueles nomes doidos (isso pode travar ou fazer o script demorar muito).

Rodar ele é simples, vc chama ele com o prefixo dos arquivos que vc tá usando (sem esquecer da hífen no final), por exemplo:

```bash
python3 split2nome KXO-20100718-DM-SK-FK-lbasica400-cores-
```

se der alguma coisa errada vc s apaga a pasta 'renomeados', faz o que precisar e tenta de novo.

### checker-do-dicio.py
É o checker final, pra verificar se os áudios e imagens do xlsx realmente tão nas pastas, e quais tão com problema. Ele vai gerar um arquivo chamado 'missing.txt' com a lista de áudios e imagens que tão faltando.

Não precisa de nada demais, vc só roda ele na pasta que tem o 'dicionario.xlsx' e as pastas 'foto' e 'audio'.

```bash
python3 checker-do-dicio.py
```
