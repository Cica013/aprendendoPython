"""
Documentação:
https://pythonhosted.org/PyPDF2/
Para mais exemplos de uso:
http://www.blog.pythonlibrary.org/2018/06/07/as-intro-to-pypdf2/

pip instal pypdf2 # virtualenv
pipenv install pypdf2 # pipenv
"""

import PyPDF2
import os

# Juntas PDFs
caminho_dos_pdfs = 'pdf'

novo_pdf = PyPDF2.manipula_pdf.leitor()
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(fr'{caminho_dos_pdfs}\novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)


# Separa PDFs
with open(r'pdf\novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.manipula_pdf.leitor(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.manipula_pdf.escritor()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(fr'novos_pdfs\{num_paginas}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)


