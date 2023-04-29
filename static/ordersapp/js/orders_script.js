'use strict';

document.addEventListener('DOMContentLoaded', function (event) {
    const order = {
        url: '/order/price/',
        orderWrapper: null,
        order_form: null,
        total_cost: null,
        total_qtty: null,
            
        init() {
            this. orderWrapper = document.getElementById('order-wrapper');
            this.order_form = document.querySelector('.order_form')
            this.total_cost = document.querySelector('.order_total_cost');
            this.total_qtty = document.querySelector('.order_total_qtty');
            this.orderWrapper.addEventListener('change', this.onInputChange.bind(this));
            this.updateStatistics()
        },

        updateStatistics() {
            const formElements = this.order_form.querySelectorAll('.formset_row');
            
            const statistics = [...formElements].reduce((result, curr, i) => {
                const qtty = parseInt(curr.querySelector(`#id_orderitems-${i}-qtty`)?.value);
                const price = parseFloat(curr.querySelector(`#orderitems-${i}-price`)?.innerText);
                if (qtty && price) {
                    result.total_qtty += qtty;
                    result.total_cost += qtty * price;
                }
                return result;
            }, {total_qtty: 0, total_cost: 0});

            this.renderStatistics(statistics);
        },

        renderStatistics(data={}) {
            if (this.total_cost) this.total_cost.innerText = data.total_cost;
            if (this.total_qtty) this.total_qtty.innerText = data.total_qtty;
        },

        renderPrice(row_id, price) {
            const formset_row = this.order_form.querySelectorAll('.formset_row')[row_id];
            const td3_element = formset_row.querySelector('.td3');
            td3_element.innerHTML = '';
            td3_element.insertAdjacentHTML('beforeend', `<span id="orderitems-${row_id}-price">${price}</span> руб`)
        },
    
        async onInputChange(event) {
            switch(event.target.type) {
                case 'number':
                    this.updateStatistics();
                    break;
                case 'select-one':
                    const product_id = event.target.selectedOptions[0].value;
                    const current_form_id = event.target.id.split('-')[1];
                    if (product_id) {
                        const response = await this.fetchData(this.url + product_id);
                        const price = parseFloat(response.result);

                        this.renderPrice(current_form_id, price);
                        this.updateStatistics();
                    }
                    break;
            }
        },
   
        async fetchData(url, options=null) {
            const response = await fetch(url, options);
            const json = await response.json();
            return json;
        },
    
    };
    
    order.init();
});