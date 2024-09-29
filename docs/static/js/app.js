async function fetch_markdown(url, table_elem, col_count) {
    try {
        const response = await fetch(url);
        const markdown = await response.text();
        const lines = markdown.trim().split('\n');

        if (lines.length > 3) {
            lines.splice(-3, 3); //remove last three (last modified)
        }


        const rows = lines.filter(line => !line.includes('---')); // separator
        const headers = rows[0].split('|').map(header => header.trim()).filter(Boolean); // headers
        const dataRows = rows.slice(1).map(row => {
        const cells = row.split('|').map(cell => cell.trim());
        const nthAfter = cells.slice(1, col_count);
        const fourthColumn = cells.slice(col_count).join(' | ').replace(/\s*\|\s*$/, ''); 
        return [...nthAfter, fourthColumn]; 
        });

        let htmlTable = `<table><thead><tr>`;   // thead
        headers.forEach(header => {
            htmlTable += `<th>${header}</th>`;
        });
        htmlTable += `</tr></thead><tbody>`;
        
        dataRows.forEach(row => {
            htmlTable += `<tr>`;
            row.forEach((cell, index) => {
                if(index===0) {
                    htmlTable += `<td><a href='${cell}#n${row[1]}'>${cell}</a></td>` //url with anchor to page number
                } else {
                    htmlTable += `<td>${cell}</td>`
                }
            })
            htmlTable += `</tr>`;
        });
        
        htmlTable += `</tbody></table>`;
        document.getElementById(table_elem).innerHTML = htmlTable;
    } catch (error) {
        console.error('Error fetching or converting Markdown:', error);
    }
}

fetch_markdown('https://raw.githubusercontent.com/tbwcjw/profanekernel/refs/heads/main/results/PROFANITY.md', 'profanity-table', 4);
fetch_markdown('https://raw.githubusercontent.com/tbwcjw/profanekernel/refs/heads/main/results/COUNT.md', 'count-table', 2);