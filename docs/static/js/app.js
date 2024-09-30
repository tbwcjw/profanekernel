async function fetch_markdown(url, table_elem, col_count, link = false, page_size = 24) {
    try {
        const response = await fetch(url);
        const markdown = await response.text();
        const lines = markdown.trim().split('\n');

        let lastModifiedDate = '';
        if (lines.length > 3) {
            lastModifiedDate = lines[lines.length - 1];
            lines.splice(-3, 3);
        }

        const rows = lines.filter(line => !line.includes('---'));
        const headers = rows[0].split('|').map(header => header.trim()).filter(Boolean);
        let dataRows = rows.slice(1).map(row => {
            const cells = row.split('|').map(cell => cell.trim());
            const nthAfter = cells.slice(1, col_count);
            const fourthColumn = cells.slice(col_count).join(' | ').replace(/\s*\|\s*$/, '');
            return [...nthAfter, fourthColumn];
        });

        let currentPage = 1;
        let filteredRows = dataRows;

        function renderTable(rows, page) {
            const start = (page - 1) * page_size;
            const paginatedRows = rows.slice(start, start + page_size);

            let htmlTable = '';

            if (paginatedRows < 1) {
                htmlTable += `<div class="card mb-3 mt-3">
                <div class="card-header" style="text-align: left;">No results</div></div>`;
            }
            paginatedRows.forEach(row => {
                const linkCell = row[0];
                const lineNumber = row[1];
                const keyword = row[2];
                const code = row[3];

                htmlTable += `<div class="card mb-3 mt-3">
                    <div class="card-header" style="text-align: left;">`;

                if (link) {
                    htmlTable += `File: <a href='${linkCell}#n${lineNumber}'>${linkCell}</a>`;
                } else {
                    htmlTable += `${linkCell}`;
                }

                htmlTable += `</div>
                    <a href='${linkCell}#n${lineNumber}' style='text-decoration: none;'>
                        <div class="card-body">
                            <div class="code-box">
                                <code><div class="line-num">${lineNumber}.</div>${code}</code>
                            </div>
                            <footer class="text-muted small">Keyword: <i>"${keyword}"</i></footer>
                        </div>
                    </a>
                </div>`;
            });

            document.getElementById(table_elem).innerHTML = htmlTable;
            document.getElementById('last-modified').innerHTML = lastModifiedDate;
            renderPaginationControls(rows.length, page);
        }

        function renderPaginationControls(totalRows, currentPage) {
            const totalPages = Math.ceil(totalRows / page_size);
            let paginationHtml = '';

            for (let i = 1; i <= totalPages; i++) {
                paginationHtml += `<button type="button" class="page-btn btn ${i === currentPage ? 'btn-primary' : 'btn-outline-secondary'} btn-sm m-1" data-page="${i}">${i}</button>`;
            }

            document.getElementById('pagination-controls').innerHTML = paginationHtml;

            document.querySelectorAll('.page-btn').forEach(button => {
                button.addEventListener('click', (event) => {
                    const selectedPage = parseInt(event.target.getAttribute('data-page'));
                    currentPage = selectedPage;
                    renderTable(filteredRows, currentPage);
                });
            });
        }


        function searchTable(keyword) {
            if (keyword) {
                filteredRows = dataRows.filter(row => row[2].toLowerCase().includes(keyword.toLowerCase()));
            } else {
                filteredRows = dataRows;
            }
            currentPage = 1;
            renderTable(filteredRows, currentPage);
        }

        document.getElementById('search-btn').addEventListener('click', () => {
            const keyword = document.getElementById('search-input').value.trim();
            searchTable(keyword);
        });
        document.getElementById('clear-btn').addEventListener('click', () => {
            const keyword = "";
            document.getElementById('search-input').value = "";
            searchTable(keyword);
        });

        renderTable(dataRows, currentPage);
    } catch (error) {
        console.error('Error fetching or converting Markdown:', error);
    }
}

async function fetch_counts(url, table_elem) {
    const response = await fetch(url);
    const markdown = await response.text();
    const lines = markdown.trim().split('\n');
    let totalExpletives = 0;
    let lastModifiedDate = '';
    if (lines.length > 3) {
        lastModifiedDate = lines[lines.length - 1];
        lines.splice(-3, 3);
    }

    const rows = lines.filter(line => !line.includes('---'));
    const headers = rows[0].split('|').map(header => header.trim()).filter(Boolean);
    const dataRows = rows.slice(1).map(row => {
        const cells = row.split('|').map(cell => cell.trim());
        return cells;
    });

    let htmlTable = '';
    const keywordCounts = {};
    dataRows.forEach(cells => {
        const keyword = cells[1];
        const amount = parseInt(cells[2]);

        if (keywordCounts[keyword]) {            //aggregate keyword counts
            keywordCounts[keyword] += amount;
        } else {
            keywordCounts[keyword] = amount;
        }

        totalExpletives += parseInt(amount);
        htmlTable += ` <b>${amount}</b> ${keyword}'s `;
    });
    htmlTable.replace(/,\s*$/, "");
    totalExpletives = `In our last search, we found ${totalExpletives} expletives.`;
    document.getElementById('expletive-count').innerHTML = totalExpletives;
    document.getElementById(table_elem).innerHTML = htmlTable.trim();
}
fetch_markdown('https://raw.githubusercontent.com/tbwcjw/profanekernel/refs/heads/main/results/PROFANITY.md', 'profanity-table', 4, true);
fetch_counts('https://raw.githubusercontent.com/tbwcjw/profanekernel/refs/heads/main/results/COUNT.md', 'keyword-stats', 2, false);