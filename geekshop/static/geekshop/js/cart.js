'use strict';

const cart = {
    cartWrapper: document.getElementById('cart-wrapper'),

    init() {
        this.cartWrapper.addEventListener('change', this.onInputChange.bind(this));
        this.cartWrapper.addEventListener('click', this.onClick.bind(this));
    },

    async onInputChange(event) {
        const newValue = event.target.value;
        const productId = event.target.dataset.pk;
        const data = await this.fetchData(`/cart/edit/${productId}/${newValue}`);
        this.render(data);
    },

    async onClick(event) {
        const target = event.target;
        if (target.classList.contains('qty-block__change')) {
            const qtyBlock = target.parentNode.children[1].children[0];
            const newValue = target.classList.contains('add-btn') ? +qtyBlock.value + 1 : +qtyBlock.value - 1;
            const productId = qtyBlock.dataset.pk;
            const data = await this.fetchData(`/cart/edit/${productId}/${newValue}`);
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
