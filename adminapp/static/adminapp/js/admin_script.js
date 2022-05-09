'use strict';

const settings = {
    menuBlockClass: '.nav_list',
    mainBlockClass: '.main_wrapper',
    toggleButton: '#header_toggler',
    headerBlock: '#header',
    bodyBlock: '#body_block',
    navBlock: '#nav_block',
};

const users = {
    users: null,
    url_read: 'users/read/',
    url_create: 'users/create/',
    url_update: 'users/update/',
    url_delete: 'users/delete/',

    setObjectsList(userData) {
        this.users = userData;
    },

    _getUserListItemHTML(users) {
        return users.reduce(
            (prev, object) =>
                prev +
                ` <tr  class=${object.is_active ? '' : 'text-secondary'} 
            style="--bs-text-opacity: .5;"
        >
            <td>
                ${object.username}
            </td>
            <td>${object.first_name}</td>
            <td>${object.last_name}</td>
            <td>${object.email}</td>
            <td class="text-center">
                ${
                    object.is_staff
                        ? '<i class="fa fa-check-circle"></i>'
                        : '<i class="fa fa-times-circle"></i>'
                }
            </td>
            <td class="text-center">
                ${
                    object.is_active
                        ? '<i class="fa fa-check-circle"></i>'
                        : '<i class="fa fa-times-circle"></i>'
                }
            </td>
            <td class="text-center">
                <button 
                    type="button" 
                    class="btn btn-outline-secondary btn__update"
                    data-key="${object.id}"
                >
                    редактировать
                </button>
            </td>
            <td class="text-center">

                <button type="button" class="btn btn-outline-secondary btn__remove" data-key="${
                    object.id
                }">
                    ${object.is_active ? 'удалить' : 'восстановить'}
                </button>

            </td>
        </tr>
            `,
            ''
        );
    },

    getObjectsListHTML() {
        const listItems = this._getUserListItemHTML(this.users);

        return `<main>
            <div class="container-fluid">
                <h1 class="mt-4">Пользователи</h1>
                <div class="card mb-4">
                    <div class="card-header">
                        <i class="fas fa-table mr-1"></i>
                        Пользователи
                    </div>
                    <div class="card-body">
                        <div class="table-responsive">
                            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                                <thead>
                                    <tr>
                                        <th>Имя пользователя</th>
                                        <th>Имя</th>
                                        <th>Фамилия</th>
                                        <th>Адрес эл. почты</th>
                                        <th>Персонал сайта</th>
                                        <th>Активный</th>
                                        <th></th>
                                        <th></th>
                                    </tr>
                                </thead>
                                <tfoot>
                                    <tr>
                                        <th>Имя пользователя</th>
                                        <th>Имя</th>
                                        <th>Фамилия</th>
                                        <th>Адрес эл. почты</th>
                                        <th>Персонал сайта</th>
                                        <th>Активный</th>
                                        <th></th>
                                        <th></th>
                                    </tr>
                                </tfoot>
                                <tbody id="table_body">
                                ${listItems}
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="card-footer">
                        <button class="btn btn-primary btn__create">Создать пользователя</button>
                    </div>
                </div>
            </div>
        </main>`;
    },
};

const categories = {
    categories: null,
    url_create: 'categories/create/',
    url_read: 'categories/read/',
    url_update: 'categories/update/',
    url_delete: 'categories/delete/',

    setObjectsList(categoriesData) {
        this.categories = categoriesData;
    },

    _getCategoryListItemHTML(categories) {
        return categories.reduce(
            (prev, object) =>
                prev +
                ` <tr  class=${object.is_active ? '' : 'text-secondary'} 
            style="--bs-text-opacity: .5;"
        >
            <td>
                ${object.name}
            </td>
            <td>${object.description}</td>
            <td class="text-center">
                <button 
                    type="button" 
                    class="btn btn-outline-secondary btn__products" 
                    data-key="${object.id}"
                >
                    товары категории
                </button>
            </td>
            <td class="text-center">
                <button 
                    type="button" 
                    class="btn btn-outline-secondary btn__update" 
                    data-key="${object.id}"
                >
                    редактировать
                </button>
            </td>
            <td class="text-center">

                <button type="button" class="btn btn-outline-secondary btn__remove" data-key="${
                    object.id
                }">
                    ${object.is_active ? 'удалить' : 'восстановить'}
                </button>

            </td>
        </tr>
            `,
            ''
        );
    },

    getObjectsListHTML() {
        const listItems = this._getCategoryListItemHTML(this.categories);

        return `<main>
            <div class="container-fluid">
                <h1 class="mt-4">Категории</h1>
                <div class="card mb-4">
                    <div class="card-header">
                        <i class="fas fa-table mr-1"></i>
                        Категории
                    </div>
                    <div class="card-body">
                        <div class="table-responsive">
                            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                                <thead>
                                    <tr>
                                        <th>Категория</th>
                                        <th>Описание</th>
                                        <th></th>
                                        <th></th>
                                        <th></th>
                                    </tr>
                                </thead>
                                <tfoot>
                                    <tr>
                                        <th>Категория</th>
                                        <th>Описание</th>
                                        <th></th>
                                        <th></th>
                                        <th></th>
                                    </tr>
                                </tfoot>
                                <tbody id="table_body">
                                    ${listItems}
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="card-footer">
                        <button class="btn btn-primary btn__create">Создать категорию</button>
                    </div>
                </div>
            </div>
        </main>`;
    },
};

const products = {
    products: null,
    url_create: 'products/create/category/',
    url_read: 'products/read/category/',
    url_read_details: 'products/read/',
    url_update: 'products/update/',
    url_delete: 'products/delete/',

    setObjectsList(productsData) {
        if (productsData) this.products = productsData;
    },

    _getProductsListItemHTML(products) {
        return products.reduce(
            (prev, object) =>
                prev +
                ` <tr  class=${object.is_active ? '' : 'text-secondary'} 
            style="--bs-text-opacity: .5;"
        >
            <td><img class="img-fluid" src="/media/${object.image}" alt="${
                    object.name
                }"></a></td>
            <td>${object.name}</td>
            <td>${object.short_desc}</td>
            <td>${object.price}</td>
            <td>${object.qtty}</td>
            <td class="text-center">
                <button type="button" class="btn btn-outline-secondary btn__details" data-key="${
                    object.id
                }">
                    подробнее
                </button>
            </td>
            <td class="text-center">
                <button 
                    type="button" 
                    class="btn btn-outline-secondary btn__update" 
                    data-key="${object.id}"
                >
                    редактировать
                </button>
            </td>
            <td class="text-center">
                <button type="button" class="btn btn-outline-secondary btn__remove" data-key="${
                    object.id
                }">
                    ${object.is_active ? 'удалить' : 'восстановить'}
                </button>

            </td>
        </tr>
            `,
            ''
        );
    },

    getObjectsListHTML() {
        const category = this.products.category;
        const listItems = this._getProductsListItemHTML(
            this.products.products_list
        );

        return `<main>
            <div class="container-fluid">
                <h1 class="mt-4">Продукты</h1>
                <div class="card mb-4">
                    <div class="card-header">
                        <i class="fas fa-table mr-1"></i>
                        ${category.name}
                    </div>
                    <div class="card-body">
                        <div class="table-responsive">
                            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                                <thead>
                                    <tr>
                                        <th>Изображение</th>
                                        <th>Наименование</th>
                                        <th>Краткое описание</th>
                                        <th>Цена</th>
                                        <th>Количество</th>
                                        <th>Подробнее</th>
                                        <th>Редактировать</th>
                                        <th>Удалить</th>
                                    </tr>
                                </thead>
                                <tfoot>
                                    <tr>
                                        <th>Изображение</th>
                                        <th>Наименование</th>
                                        <th>Краткое описание</th>
                                        <th>Цена</th>
                                        <th>Количество</th>
                                        <th>Подробнее</th>
                                        <th>Редактировать</th>
                                        <th>Удалить</th>
                                    </tr>
                                </tfoot>
                                <tbody id="table_body">
                                    ${listItems}
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="card-footer">
                        <button 
                            class="btn btn-primary btn__create" 
                            data-key="${category.id}"
                        >
                            Создать товар
                        </button>
                    </div>
                </div>
            </div>
        </main>`;
    },

    getObjectDetailsHTML(product_id) {
        const product = this.products.products_list.find(
            (item) => item.id == product_id
        );

        if (!product) return '<main><div>Товар не найден</div></main>';

        const descriptions = product.description
            .split(';')
            .map((s) => s.trim())
            .reduce((prev, curr) => prev + `<p>${curr}</p>`, '');

        return `<main>
                <div class="container-fluid">
                    <h1 class="mt-4">Товары</h1>
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-table mr-1"></i>
                            Информация о: ${product.name}
                        </div>
                        <div class="card-body">

                            <div class="details-products row mb-3">
                                <div class="col-md-6">
                                    <div class="slider-product">
                                        <img class="img-fluid" src="/media/${product.image}">
                                    </div>
                                
                                </div>
                                <div class="col-md-6">
                                    <h3 class="big-bold">${product.name}</h3>
                                    <p class="price">${product.price}<span>руб</span></p>
                                    <a href="#" class="red-button">
                                        заказать <i class="fa fa-chevron-right" aria-hidden="true"></i>
                                    </a>
                                    <div class="description-text">
                                        ${descriptions}
                                    </div>
                                </div>
                            </>

                        </div>
                        <div class="card-footer">
                            <button 
                                class="btn btn-outline-primary btn__back"
                                data-key="${product.category_id}" 
                            >
                                Назад
                            </button>
                        </div>
                    </div>
                </div>
            </main>`;
    },
};

const menuList = {
    _menuItems: [
        { name: 'Пользователи', icon: 'bx bx-user', page: 'users' },
        {
            name: 'Категории',
            icon: 'bx bx-message-square-detail',
            page: 'categories',
        },
    ],

    _getMenuItemHTML(item) {
        return `<a href="#" class="nav_link" data-page="${item.page}">
                <i class="nav_icon ${item.icon}"></i>
                <span class="nav_name">${item.name}</span>
            </a>`;
    },

    getMenuHTML() {
        return this._menuItems.reduce(
            (result, item) => result + this._getMenuItemHTML(item),
            ''
        );
    },
};

const admin = {
    menuBlock: null,
    mainBlock: null,
    toggleButton: null,
    headerBlock: null,
    bodyBlock: null,
    navBlock: null,
    url: '/admin_staff/api/',
    currentPage: '',

    users: null,
    categories: null,
    products: null,
    menuList: null,

    async init(
        {
            menuBlockClass,
            mainBlockClass,
            toggleButton,
            headerBlock,
            bodyBlock,
            navBlock,
        },
        users,
        categories,
        products,
        menuList
    ) {
        this.menuBlock = document.querySelector(menuBlockClass);
        this.mainBlock = document.querySelector(mainBlockClass);
        this.toggleButton = document.querySelector(toggleButton);
        this.headerBlock = document.querySelector(headerBlock);
        this.bodyBlock = document.querySelector(bodyBlock);
        this.navBlock = document.querySelector(navBlock);

        this.currentPage = 'users';

        this.users = users;
        this.categories = categories;
        this.products = products;
        this.menuList = menuList;

        this.displayMenuBlock();
        this.displayObjectsList();
        this.addEventHandlers();
    },

    displayMenuBlock() {
        const html_string = this.menuList.getMenuHTML();
        this.renderHTML(html_string, 'menuBlock');
    },

    async displayObjectsList(id = '') {
        const object = this[`${this.currentPage}`];
        const url = `${this.url}${object.url_read}${id}`;
        const response = await this.fetchData(url);
        console.log(response)
        if (!response.error) {
            object.setObjectsList(response.objects);
            this.renderHTML(object.getObjectsListHTML());
        }
    },

    displayObjectDetails(id) {
        const html_string =
            this[`${this.currentPage}`].getObjectDetailsHTML(id);
        this.renderHTML(html_string);
    },

    async displayCreateForm(id = null) {
        const object = this[`${this.currentPage}`];
        let url = `${this.url}${object.url_create}`;
        if (id) url += `${id}/`;
        const response = await this.fetchData(url);
        if (!response.error) this.renderHTML(response.result);
    },

    async displayUpdateForm(id) {
        const object = this[`${this.currentPage}`];
        const url = `${this.url}${object.url_update}${id}/`;
        const response = await this.fetchData(url);
        if (!response.error) this.renderHTML(response.result);
    },

    async removeListItem(target) {
        const object = this[`${this.currentPage}`];
        const response = await this.fetchData(
            `${this.url}${this.currentPage}/delete/${target.dataset?.key}/`
        );

        if (!response.error) {
            object.setObjectsList(response.objects);
            this.renderHTML(object.getObjectsListHTML());
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

    addEventHandlers() {
        this.menuBlock.addEventListener(
            'click',
            this.onMenuItemSelected.bind(this)
        );
        this.toggleButton.addEventListener('click', this.showNavbar.bind(this));
        this.mainBlock.addEventListener(
            'click',
            this.onMainBlockClick.bind(this)
        );
        this.mainBlock.addEventListener('submit', this.onFormSubmit.bind(this));
    },

    showNavbar() {
        this.navBlock.classList.toggle('show');
        this.toggleButton.classList.toggle('bx-x');
        this.bodyBlock.classList.toggle('body_block');
        this.headerBlock.classList.toggle('body_block');
    },

    onMenuItemSelected(event) {
        const link = event.target.closest('.nav_link');
        if (link) {
            document
                .querySelectorAll('.nav_link')
                .forEach((item) => item.classList.remove('active'));
            link.classList.add('active');

            this.currentPage = link.dataset.page;
            this.displayObjectsList();
        }
    },

    onMainBlockClicked(event) {
        const target = event.target;
        if (target.classList.contains('btn')) {
            if (target.classList.contains('btn__remove')) {
                this.removeListItem(target);
            } 
            else if (target.classList.contains('btn__products')) {
                const category_id = target.dataset.key;
                this.currentPage = 'products';
                this.displayObjectsList(category_id);
            } 
            else if (target.classList.contains('btn__details')) {
                const id = target.dataset.key;
                this.displayObjectDetails(id);
            } 
            else if (target.classList.contains('btn__back')) {
                this.displayObjectsList(target.dataset?.key);
            } 
            else if (target.classList.contains('btn__create')) {
                this.displayCreateForm(target.dataset?.key);
            } 
            else if (target.classList.contains('btn__update')) {
                const id = target.dataset.key;
                this.displayUpdateForm(id);
            }
        }
    },

    async onFormSubmit(event) {
        event.preventDefault();
        const object = this[`${this.currentPage}`];

        let url = event.target.dataset.is_create
            ? `${this.url}${object.url_create}`
            : `${this.url}${object.url_update}`;
        if (event.target.dataset?.key) url += `${event.target.dataset.key}/`;

        const formData = new FormData(event.target);

        const response = await this.fetchData(url, {
            method: 'POST',
            body: formData,
            credentials: 'same-origin',
        });

        if (!response.error) {
            if (response.is_valid && this.currentPage === 'products') {
                this.displayObjectsList(response.category);
            } else if (response.is_valid) {
                this.displayObjectsList();
            } else this.renderHTML(response.result);
        }
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

};

document.addEventListener('DOMContentLoaded', function (event) {
    admin.init(settings, users, categories, products, menuList);
});
