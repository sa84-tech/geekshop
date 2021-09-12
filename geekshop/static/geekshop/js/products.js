'use strict';

const products = {
    linkBlock: document.querySelector('.featured_menu_links'),
    mainBlock: document.querySelector('.main_wrapper'),

    init() {
        this.linkBlock.addEventListener('click', this.onLinkBlockClick.bind(this));
        this.mainBlock.addEventListener('click', this.onMainBlockClick.bind(this));
    },

    onLinkBlockClick(event) {

        if (event.target.classList.contains('popular_products-link')) {
            this.toggleBlock('.popular_products', '.new_products');
        }
        else if (event.target.classList.contains('new_products-link')) {
            this.toggleBlock('.new_products', '.popular_products');
        }
    },

    onMainBlockClick(event) {
        console.log("🚀 ~ file: products.js ~ line 23 ~ onMainBlockClick ~ event", event)

    },

    toggleBlock(showBlock, hideBlock) {
        document.querySelector(showBlock).classList.remove('d-none');
        document.querySelector(`${showBlock}-link`).classList.add('active');
        document.querySelector(hideBlock).classList.add('d-none');
        document.querySelector(`${hideBlock}-link`).classList.remove('active');
    },

    clearBlock() {
        while (this.mainBlock.firstChild) {
            this.mainBlock.firstChild.remove();
        }
    },

    renderHTML(html_string, wrapper = 'mainBlock') {
        this.clearBlock();
        this[wrapper].insertAdjacentHTML('beforeend', html_string);
    },

    renderErrorAlert(error) {
        const html_string = `<div class="alert alert-danger" role="alert">
                Ошибка: status ${error.status}. ${error.statusText}
            </div>`;
        this.renderHTML(html_string);
    },

    async fetchData(url, options = null) {
        const response = await fetch(url, options);
        if (response.ok) {
            const json = await response.json();
            return json;
        }
        else {
            this.renderErrorAlert(response);
            return { error: true, objects: [] };
        }
    },
}

products.init();
