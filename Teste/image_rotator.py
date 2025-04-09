# image_rotator.py
# image_rotator.py

from PIL import Image
import argparse

# iniciar o analisador
parser = argparse.ArgumentParser()

# adicionar os argumentos com os nomes correspondentes
# observe que agora usamos o parâmetro help
parser.add_argument('input_file', help='input file path')
parser.add_argument('output_file', help='output file path')
parser.add_argument('--angle', '-a', type=int, default=90, help='rotação em sentido anti-horário (graus)')
parser.add_argument('-i', '--info', action='store_true', help='exibir tamanho da imagem')

# analisar os argumentos
args = parser.parse_args()

# carregar uma imagem do argumento input_file
im = Image.open(args.input_file)

# exibir o tamanho da imagem apenas se o sinalizador info estiver definido como True
if args.info:
    print('dimensões da imagem de entrada:', im.size)

# girar
rotated = im.rotate(args.angle)

# salvar
rotated.save(args.output_file)