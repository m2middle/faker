import re, csv,  chardet,  argparse

parser = argparse.ArgumentParser(description='Filtrer les utilisateurs dans un fichier CSV.')
parser.add_argument('input_file', type=str, help='Le fichier CSV d\'entrée')
parser.add_argument('output_file', type=str, help='Le fichier CSV de sortie')
args = parser.parse_args()

with open(args.input_file, 'rb') as f:
    encoding = chardet.detect(f.read())['encoding']

with open(args.input_file, mode='r', encoding=encoding) as infile:
    lines = infile.readlines()

with open(args.output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['version:v1.0'])
    writer.writerow(['Nom d\'utilisateur [userPrincipalName] Obligatoire'])
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    for line in lines:
        match = email_pattern.search(line)
        if match:
            writer.writerow([match.group()])

print(f"Users filtered and saved to {args.output_file}")