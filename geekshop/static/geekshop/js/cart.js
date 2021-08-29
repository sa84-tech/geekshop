'use strict';

const cart = {
    url: '/cart/edit',
    cartWrapper: document.getElementById('cart-wrapper'),

    init() {
        this.cartWrapper.addEventListener('change', this.onInputChange.bind(this));
        this.cartWrapper.addEventListener('click', this.onClick.bind(this));
    },

    async onInputChange(event) {
        const newValue = event.target.value;
        const productId = event.target.closest('.list-group-item').dataset.pk;

        const data = await this.fetchData(`${this.url}/${productId}/${newValue}`);
        this.render(data);
    },

    async onClick(event) {
        const target = event.target;

        if (target.classList.contains('qtty-block__change')) {
            const qttyBlock = target.parentNode.children[1].children[0];
            const newValue = target.classList.contains('add-btn') ? +qttyBlock.value + 1 : +qttyBlock.value - 1;
            const productId = target.closest('.list-group-item').dataset.pk;

            const data = await this.fetchData(`${this.url}/${productId}/${newValue}`);
            this.render(data);
        }
        else if (target.classList.contains('qtty-block__remove')) {
            const productId = target.closest('.list-group-item').dataset.pk;

            const data = await this.fetchData(`${this.url}/${productId}/0`);
            this.render(data);
        }
    },

    async fetchData(url, options=null) {
        const response = await fetch(url, options);
        return response.json();
    },

    render(data) {
        while (this.cartWrapper.firstChild) {
            this.cartWrapper.firstChild.remove();
        }
        this.cartWrapper.insertAdjacentHTML('beforeend', data.result);
        document.getElementById('badge_count').innerText = data.context.count;
        document.getElementById('badge_cost').innerHTML = `${data.context.total_cost} &#8381;`;
    },
};

cart.init();
