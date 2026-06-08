from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "📜 O Grimório do Python: Funções e Métodos", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", "", 12)

# Conteúdo resumido para o PDF
conteudo = """
1. FUNÇÕES EMBUTIDAS (Nativas)
- print(): Exibe mensagens na tela.
- input(): Recebe dados do usuário.
- len(): Conta o tamanho de listas ou textos.
- int() / str(): Convertem tipos de dados.
- str(): Converte para string.
- float(): Converte para número decimal.
- bool(): Converte para booleano (True/False).
- list(): Converte para lista.
- dict(): Converte para dicionário.
- tuple(): Converte para tupla.
- conjunto(): Converte para conjunto.
- range(): Gera uma sequência de números.
- type(): Mostra o tipo de dado.


2. MÉTODOS DE STRINGS (Textos)
- .strip(): Remove espaços inúteis.
- .lower() / .upper(): Muda para minúsculo/maiúsculo.
- .join(): Junta uma lista em uma string só.
- .upper(): Converte para maiúsculas.
- .replace(): Substitui partes do texto.
- .capitalize(): Deixa a primeira letra maiúscula.
- .split(): Divide uma string em partes.


3. MÉTODOS DE LISTAS
- .append(item): Adiciona no final da lista.
- .remove(item): Apaga um item específico.
- .pop(): Remove o último item e guarda na variável.
- .sort(): Ordena a lista.
- .insert(posição, item): Insere um item em uma posição específica.

4. MÉTODOS DE DICIONÁRIOS
- .keys(): Mostra as chaves.
- .values(): Mostra os valores guardados.
- del dicionario[chave]: Apaga um field.
- .items(): Mostra chaves e valores juntos.
- .get(chave, valor_padrao): Pega o valor de uma chave, ou retorna um valor padrão se a chave não existir.
- .update({chave: valor}): Atualiza o dicionário com novos pares chave-valor.
"""

for linha in conteudo.split('\n'):
    pdf.cell(0, 8, linha.encode('latin-1', 'replace').decode('latin-1'), 0, 1)

pdf.output("guia_python.pdf")
print("✅ PDF 'guia_python.pdf' gerado com sucesso na sua pasta!")