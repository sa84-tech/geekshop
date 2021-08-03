cart = {
    wrapper: document.getElementById('cart-wrapper'),
    init() {
        this.wrapper.addEventListener('change', this.onInputChange.bind(this));
    },

    onInputChange(event) {
        console.log('EVENT:', event);
        newValue = event.target.value;
        productId = event.target.dataset.pk;
        this.updateData(`/cart/edit/${productId}/${newValue}`);
    },

    async updateData(url=null, options=null) {
        const response = await fetch(url);
        console.log(response)
    }
};

cart.init();