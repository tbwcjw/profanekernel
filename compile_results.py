import csv
from datetime import datetime

def csv_to_md_table(csvf):
    with open(csvf, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        headers = rows[0]
        markdown = "| " + " | ".join(headers) + "|\n"                   #header
        markdown += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'  #separator

        for row in rows[1:]:
            markdown += "| " + " | ".join(row) + ' |\n'                 #row
    
    markdown += f"\n\nLast updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
    return markdown

def write_to_readme(csvf, output):
    md = csv_to_md_table(csvf)
    with open(output, 'w') as f:
        f.write(md)
        f.close()