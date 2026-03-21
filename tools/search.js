/**
 * GitGalaxy Search Controller
 * v1.0
 * Location: js/tools/search.js
 * Responsibilities:
 * - Indexing: Flattens hierarchical system data into a searchable list.
 * - Input: Handles typing and keyboard navigation (Up/Down/Enter).
 * - UI: Renders the "Glassmorphism" dropdown results.
 */

class SearchController {
    constructor(inputId, containerId) {
        this.input = document.getElementById(inputId);
        this.container = document.getElementById(containerId); // Parent of input
        this.index = [];
        this.results = [];
        this.selectedIndex = -1;
        
        // Create Dropdown DOM if it doesn't exist
        if (!document.getElementById('search-dropdown')) {
            this.dropdown = document.createElement('div');
            this.dropdown.id = 'search-dropdown';
            this.dropdown.className = 'search-dropdown';
            this.container.appendChild(this.dropdown);
        } else {
            this.dropdown = document.getElementById('search-dropdown');
        }

        this.bindEvents();
    }

    /**
     * Ingests data from ANY source (Mock or Real)
     * @param {Array} systemData - Array of file objects { name, type, metrics... }
     */
    setIndex(systemData) {
        this.index = systemData.map(item => ({
            name: item.name,
            type: item.type || (item.name.includes('.') ? 'file' : 'dir'),
            metrics: item.metrics,
            // Pre-compute lowercase for performance
            searchStr: item.name.toLowerCase() 
        }));
        console.log(`Search: Indexed ${this.index.length} entities.`);
        this.clear();
    }

    bindEvents() {
        if (!this.input) return;

        this.input.addEventListener('input', (e) => this.onInput(e.target.value));
        
        this.input.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowDown') {
                e.preventDefault();
                this.nav(1);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                this.nav(-1);
            } else if (e.key === 'Enter') {
                e.preventDefault();
                this.executeSelection();
            } else if (e.key === 'Escape') {
                this.clear();
                this.input.blur();
            }
        });

        // Close on click outside
        document.addEventListener('click', (e) => {
            if (!this.container.contains(e.target)) this.clear();
        });
    }

    onInput(query) {
        if (query.length < 2) {
            this.clear();
            return;
        }

        const q = query.toLowerCase();
        
        // Filter logic: Name match OR Extension match
        // Limit to top 8 results for UI cleanliness
        this.results = this.index
            .filter(item => item.searchStr.includes(q))
            .sort((a, b) => {
                // Priority sorting: Starts with > Includes
                const startA = a.searchStr.startsWith(q);
                const startB = b.searchStr.startsWith(q);
                if (startA && !startB) return -1;
                if (!startA && startB) return 1;
                return 0;
            })
            .slice(0, 8);

        this.render();
    }

    render() {
        this.dropdown.innerHTML = '';
        this.selectedIndex = -1;

        if (this.results.length === 0) {
            this.dropdown.style.display = 'none';
            return;
        }

        this.dropdown.style.display = 'block';

        this.results.forEach((item, i) => {
            const el = document.createElement('div');
            el.className = 'search-result';
            
            // Icon Logic
            const icon = item.type === 'dir' ? '📁' : '📄';
            
            // Metric Hint (e.g., [1500 LOC])
            const meta = item.metrics ? `<span class="meta">${item.metrics.loc} LOC</span>` : '';

            el.innerHTML = `
                <div class="result-left">
                    <span class="icon">${icon}</span>
                    <span class="name">${this.highlightMatch(item.name)}</span>
                </div>
                ${meta}
            `;
            
            el.addEventListener('click', () => {
                this.selectedIndex = i;
                this.executeSelection();
            });

            this.dropdown.appendChild(el);
        });
    }

    highlightMatch(text) {
        const q = this.input.value.toLowerCase();
        const start = text.toLowerCase().indexOf(q);
        if (start === -1) return text;
        const end = start + q.length;
        return text.substring(0, start) + 
               `<span class="highlight">${text.substring(start, end)}</span>` + 
               text.substring(end);
    }

    nav(dir) {
        if (!this.results.length) return;
        this.selectedIndex += dir;
        
        // Wrap around
        if (this.selectedIndex < 0) this.selectedIndex = this.results.length - 1;
        if (this.selectedIndex >= this.results.length) this.selectedIndex = 0;

        this.updateHighlight();
    }

    updateHighlight() {
        const items = this.dropdown.querySelectorAll('.search-result');
        items.forEach((el, i) => {
            if (i === this.selectedIndex) el.classList.add('active');
            else el.classList.remove('active');
        });
    }

    executeSelection() {
        if (this.selectedIndex === -1 && this.results.length > 0) {
            this.selectedIndex = 0; // Default to top result
        }

        if (this.selectedIndex >= 0 && this.results[this.selectedIndex]) {
            const target = this.results[this.selectedIndex];
            
            // Dispatch Event to Main App
            const event = new CustomEvent('galaxy-navigate', { 
                detail: { targetName: target.name } 
            });
            window.dispatchEvent(event);

            this.input.value = target.name;
            this.clear();
        }
    }

    clear() {
        this.results = [];
        this.dropdown.innerHTML = '';
        this.dropdown.style.display = 'none';
        this.selectedIndex = -1;
    }
}

// Export
window.SearchController = SearchController;