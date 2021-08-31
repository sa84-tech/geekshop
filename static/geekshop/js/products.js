'use strict';

const products = {
    link_container: document.querySelector('.featured_menu_links'),

    init() {
        this.link_container.addEventListener('click', this.onClick.bind(this));
    },

    onClick(event) {

        if (event.target.classList.contains('popular_products-link')) {
            this.toggleBlock('.popular_products', '.new_products');
        }
        else if (event.target.classList.contains('new_products-link')) {
        console.log(event.target)
            this.toggleBlock('.new_products', '.popular_products');
        }
    },

    toggleBlock(showBlock, hideBlock) {
        document.querySelector(showBlock).classList.remove('d-none');
        document.querySelector(`${showBlock}-link`).classList.add('active');
        document.querySelector(hideBlock).classList.add('d-none');
        document.querySelector(`${hideBlock}-link`).classList.remove('active');
    }
}

products.init();
