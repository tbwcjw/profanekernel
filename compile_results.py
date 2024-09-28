import csv

readme_file = "results/PROFANITY.md"
def csv_to_md_table(csvf):
    with open(csvf, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        headers = rows[0]
        markdown = "| " + " | ".join(headers) + "|\n"                   #header
        markdown += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'  #separator

        for row in rows[1:]:
            markdown += "| " + " | ".join(row) + ' |\n'                 #row
    
    return markdown

def write_to_readme(csvf):
    md = csv_to_md_table(csvf)
    with open(readme_file, 'w') as f:
        f.write(md)
        f.close()