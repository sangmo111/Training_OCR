import os
import random
import pathlib
import subprocess

training_text_file = 'langdata/bod.training_text'

lines = []

with open(training_text_file, 'r') as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

output_directory = 'tesstrain/data/Noto_Serif_Tibetan-ground-truth'

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

random.shuffle(lines)

count = 100

lines = lines[:count]

line_count = 0
for line in lines:
    training_text_file_name = pathlib.Path(training_text_file).stem
    line_training_text = os.path.join(output_directory, f'{training_text_file_name}_{line_count}.gt.txt')
    with open(line_training_text, 'w') as output_file:
        output_file.writelines([line])

    file_base_name = f'bod_{line_count}'

    subprocess.run([
        'text2image',
        '--font=Noto Serif Tibetan',
        f'--text={line_training_text}',
        f'--outputbase={output_directory}/{file_base_name}',
        '--max_pages=1',
        '--strip_unrenderable_words',
        '--leading=32',
        '--xsize=3600',
        '--ysize=480',
        '--char_spacing=1.0',
        '--exposure=0',
        '--unicharset_file=langdata/bod.unicharset'
    ])

    line_count += 1