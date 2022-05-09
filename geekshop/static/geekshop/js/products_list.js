'use strict';

const products = {
    mainBlock: document.querySelector('.main_wrapper'),
    current_category: 0,

    init() {
        this.mainBlock.addEventListener('click', this.onMainBlockClick.bind(this));
        this.displyaProductList();
    },


    onMainBlockClick(event) {
        event.stopPropagation();
        if (event.target.classList.contains('menu_category')) {
            event.preventDefault();
            const category_id = event.target.href.split('/').reverse()[1];
            this.current_category = category_id;
            this.displyaProductList();
        }
        else if (event.target.classList.contains('nav_prev_page')) {
            event.preventDefault();
            const page = +document.querySelector('.current').textContent.trim().split(' ')[1];
            this.displyaProductList(page - 1);
        }
        else if (event.target.classList.contains('nav_next_page')) {
            event.preventDefault();
            const page = +document.querySelector('.current').textContent.trim().split(' ')[1];
            this.displyaProductList(page + 1);
        }
    },

    async displyaProductList(page = null) {
        let url = `/products/category/${this.current_category}/`;
        url += page ? `page/${page}/ajax/` : 'ajax/';
        const response = await this.fetchData(url);
        console.log("🚀 ~ file: products_list.js ~ line 32 ~ displyaProductList ~ url", url)
        // console.log("🚀 ~ file: products.js ~ line 37 ~ displyaProductList ~ response", response.result)
        if (!response.error) {
            this.renderHTML(response.result);
        }
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
            console.log("🚀 ~ file: products_list.js ~ line 53 ~ fetchData ~ response", response)
            const json = await response.json();
            return json;
        }
        else {
            this.renderErrorAlert(response);
            return { error: true, objects: [] };
        }
    },
}

document.addEventListener('DOMContentLoaded', function (event) {
    products.init();
});
