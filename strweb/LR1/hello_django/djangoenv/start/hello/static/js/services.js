class ServicesCatalog {
    constructor(services, itemsPerPage) {
        this.services = services; // Все услуги
        this.filteredServices = services; // Отфильтрованные услуги
        this.itemsPerPage = itemsPerPage; // Количество элементов на страницу
        this.currentPage = 1; // Текущая страница

        // DOM элементы
        this.servicesGrid = document.getElementById("servicesGrid");
        this.pagination = document.getElementById("pagination");
        this.filterForm = document.getElementById("filterForm");

        this.initialize();
    }

    initialize() {
        this.renderServices();
        this.renderPagination();
        this.addEventListeners();
    }

    // Отображение услуг на текущей странице
    renderServices() {
        this.servicesGrid.innerHTML = "";
        const start = (this.currentPage - 1) * this.itemsPerPage;
        const end = start + this.itemsPerPage;
        const paginatedServices = this.filteredServices.slice(start, end);

        if (paginatedServices.length === 0) {
            this.servicesGrid.innerHTML = "<p>Услуги не найдены.</p>";
            return;
        }

        paginatedServices.forEach(service => {
            const serviceCard = document.createElement("div");
            serviceCard.classList.add("service-item");
            serviceCard.innerHTML = `
                <h3><a href="/service_info_not/${service.id}">${service.name}</a></h3>
                <p>Цена: ${service.price} ₽</p>
                <p>Тип услуги: ${service.type}</p>
            `;
            this.servicesGrid.appendChild(serviceCard);
        });
    }

    // Отображение навигации по страницам
    renderPagination() {
        this.pagination.innerHTML = "";
        const totalPages = Math.ceil(this.filteredServices.length / this.itemsPerPage);

        for (let i = 1; i <= totalPages; i++) {
            const button = document.createElement("button");
            button.textContent = i;
            button.classList.toggle("disabled", i === this.currentPage);
            button.addEventListener("click", () => {
                this.currentPage = i;
                this.renderServices();
                this.renderPagination();
            });
            this.pagination.appendChild(button);
        }
    }

    // Фильтрация услуг по цене
    applyFilter(event) {
        event.preventDefault();
        const priceFrom = parseInt(document.getElementById("price_from").value, 10);
        const priceTo = parseInt(document.getElementById("price_to").value, 10);

        this.filteredServices = this.services.filter(service =>
            service.price >= priceFrom && service.price <= priceTo
        );

        this.currentPage = 1; // Сбрасываем на первую страницу после фильтрации
        this.renderServices();
        this.renderPagination();
    }

    // Добавление обработчиков событий
    addEventListeners() {
        this.filterForm.addEventListener("submit", (event) => this.applyFilter(event));
    }
}

// Создание экземпляра и инициализация каталога
document.addEventListener("DOMContentLoaded", () => {
    // Десериализация данных из JSON
    const parsedServices = services.map(service => ({
        id: service.pk,
        ...service.fields,
    }));
    new ServicesCatalog(parsedServices, 3); // 3 элемента на страницу
});
