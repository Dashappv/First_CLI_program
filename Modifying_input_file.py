import argparse

parser = argparse.ArgumentParser(description='argparse symbol modifications')
parser.add_argument('-i', '--input', help='original input file', required=True)
parser.add_argument('-o', '--output', help='modified output file', required=True)
parser.add_argument('--original_symbol', help='symbol to be replaced', required=True)
parser.add_argument('--replacement_symbol', help='symbol to replace the original symbol', required=True)
parser.add_argument('-u', '--upper', action='store_true', help=('will return all upper cases if flag is set'))

def modified_file(input_file, output_file, original_symbol, replacement_symbol, upper):
    with open(input_file, encoding='utf-8') as my_input_file:
        content = my_input_file.read()
        content = content.replace(original_symbol, replacement_symbol)
        if upper == True:
            content = content.upper()
    with open(output_file, 'w', encoding='utf-8') as my_output_file:
        my_output_file.write(content)

args = parser.parse_args()
modified_file(args.input, args.output, args.original_symbol, args.replacement_symbol, args.upper)