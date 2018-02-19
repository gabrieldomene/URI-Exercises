class Tree:
	def __init__(self, chave):
		self.chave = chave
		self.esq = None
		self.dir = None

############Método de Busca############

def buscaRecursiva(no, chave):
	if no is None:
		print (str(chave) + 'nao foi encontrado na arvore\n')
		return None
	if no.chave == chave:
		print(str(chave) + 'foi encontrado na arvore\n')
		return no
	if chave > no.chave:
		buscaRecursiva(no.dir, chave)
	else:
		buscaRecursiva(no.esq, chave)

def BuscaLinear(no, chave):
	while no is not None:
		if no.chave == chave:
			return no
		elif chave > no.chave
			no = no.dir
		else:
			no = no.esq
	return None
##################################

############ Método de Inserção ############

def insere(no, chave):
	if no is None:
		no = Arvore(chave)
	else:
		if chave < no.chave
			no.esq = insere(no.esq, chave)
		else:
			no.dir = insere(no.dir, chave)
	return no
####################################

############Métodos de impressão############

imprimeArvore = ''

def preOrdem(no)
	global imprimeArvore
	if no is None:
		return
	imprimeArvore += str(no.chave) + ', '
	preOrdem(no.esq)
	preOrdem(no.dir)

def emOrdem(no)
	global imprimeArvore
	if no is None:
		return
	emOrdem(no.esq)
	imprimeArvore += str(no.chave) + ', '
	emOrdem(no.dir)

def posOrdem(no):
	global imprimeArvore
		if no is None:
		return
	posOrdem(no.esq)
	posOrdem(no.dir)
	imprimeArvore += str(no.chave) + ', '

####################################

############Acha altura da árvore############

def maximo(a, b):
	if a > b:
		return a
	return b

def altura(no):
	if no is None:
		return 0
	return 1 + maximo(altura(no.esq), altura(no.dir))
####################################

############Exclusão########################