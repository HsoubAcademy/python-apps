from docx2pdf import convert
from pathlib import Path

docx_file = Path.home() / Path('Desktop', 'word files', 'academy_1.docx')
pdf_file = Path.home() / Path('Desktop', 'academy_1_converted.pdf')
multi_file = Path.home() / Path('Desktop', 'word files/')

convert(multi_file)
