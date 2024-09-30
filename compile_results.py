import csv
from datetime import datetime
import matplotlib.pyplot as plt

def keyword_count_pie(csvf, output):
    keywords = []
    counts = []

    with open(csvf, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keywords.append(row['keyword'])
            counts.append(int(row['count']))

        total_count = sum(counts)
        filtered_keywords = []
        filtered_counts = []

        for i in range(len(counts)):
            percentage = (counts[i] / total_count) * 100
            if percentage >= 1:
                filtered_keywords.append(keywords[i])
                filtered_counts.append(counts[i])

        
        plt.figure(figsize=(8, 8))
        plt.pie(filtered_counts, labels=filtered_keywords, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 16})
        plt.axis('equal')
        plt.savefig(output)

def csv_to_md_table(csvf):
    with open(csvf, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        headers = rows[0]
        markdown = "| " + " | ".join(headers) + "|\n"                   #header
        markdown += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'  #separator

        for row in rows[1:]:
            markdown += "| " + " | ".join(row) + ' |\n'                 #row
    
    markdown += f"\n\nLast updated: {datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")}"
    return markdown

def write_to_readme(csvf, output):
    md = csv_to_md_table(csvf)
    with open(output, 'w') as f:
        f.write(md)
        f.close()

def append_to_readme(str, output):
    with open(output, 'a') as f:
        f.write(f"\n{str}")
        f.close()

def write_to_runlog(input, file):
    with open(file, 'a', newline='', encoding='utf-8') as csvf:
        csv_writer = csv.writer(csvf)
        csv_writer.writerow(input)