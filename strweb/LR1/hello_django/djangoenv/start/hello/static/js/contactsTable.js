{/* <div class="filter-container">
    <input type="text" id="filterInput" placeholder="Поиск сотрудников...">
    <button id="filterButton">Найти</button>
</div>
<table id="contactsTable" class="contacts-table">
    <thead>
        <tr>
            <th>Выбрать</th>
            <th>Фото</th>
            <th data-column="name">ФИО</th>
            <th data-column="age">Возраст</th>
            <th data-column="phone_number">Телефон</th>
            <th data-column="specialization">Специализация</th>
            <th data-column="order_count">Выполненные заказы</th>
        </tr>
    </thead>
    <tbody>
        <!-- Данные добавляются с помощью JavaScript -->
    </tbody>
</table>
<div class="pagination-controls">
    <button id="prevPage">Назад</button>
    <span id="pageIndicator">Страница 1</span>
    <button id="nextPage">Вперед</button>
</div>
<div id="contactDetails" class="contact-details"></div> */}

class ContactsTable { 
    constructor() {
        this.apiUrl = "http://127.0.0.1:8000/api/contacts/"; // URL для API
        this.tableElement = document.getElementById("contactsTable").querySelector("tbody");
        this.contacts = [];
        this.filteredContacts = [];
        this.currentPage = 1;
        this.rowsPerPage = 3; // Количество контактов на одной странице
        this.sortOrder = {}; // Для отслеживания порядка сортировки
        this.loadContacts(); // Загружаем данные с сервера

        document.getElementById("filterButton").addEventListener("click", () => this.applyFilter());
        document.getElementById("nextPage").addEventListener("click", () => this.nextPage());
        document.getElementById("prevPage").addEventListener("click", () => this.previousPage());
        document.getElementById("rewardButton").addEventListener("click", () => this.rewardSelected());

        document.querySelectorAll("th[data-column]").forEach(th => {
            th.addEventListener("click", () => {
                this.sortByColumn(th.getAttribute("data-column"));
                this.updateSortIndicators(); 
            });
        });
    }

    updateSortIndicators() {
        document.querySelectorAll("#contactsTable th[data-column]").forEach((header) => {
          const indicator = header.querySelector(".sort-indicator");
          const column = header.dataset.column;
          if (column === currentSort.column) {
            indicator.textContent = currentSort.direction === "asc" ? " ▲" : " ▼";
          } else {
            indicator.textContent = "";
          }
        });
      }

    // Загружаем данные с API
    async loadContacts() {
        this.showPreloader();
        try {
            // Убедитесь, что путь к API совпадает с Django
            const url = `http://127.0.0.1:8000/api/contacts/?page=${this.currentPage}&page_size=${this.rowsPerPage}`;
            const data = await fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP Error: ${response.status} ${response.statusText}`);
                }
                return response.json(); // Parse the response as JSON
            })
            .then(json => {
                console.log("Fetched Data:", json); // Log the JSON data
                return json; // Return the parsed JSON
            })
            .catch(error => {
                console.error("Error fetching data:", error);
                return null; // Handle the error, returning null or any default value
            });
            console.log(data.data)

            // Обновляем состояние таблицы
            this.contacts = data.data;
            this.totalPages = data.total_pages;
            this.currentPage = data.current_page;
            this.renderTable();
        } catch (error) {
            console.error("Error fetching contacts:", error);
        } finally {
            this.hidePreloader();
        }
    }
    

    // Рендер таблицы
    renderTable() {
        this.tableElement.innerHTML = ""; // Очищаем таблицу
        const pageContacts = this.contacts; // Отображаем контакты для текущей страницы

        pageContacts.forEach(contact => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td><input type="checkbox" class="select-contact" data-name="${contact.name}"></td>
                <td><img src="${contact.img_url || 'https://cdn-icons-png.flaticon.com/512/219/219983.png'}" width="50" height="50"></td>
                <td>${contact.name}</td>
                <td>${contact.age}</td>
                <td>${contact.phone_number}</td>
                <td>${contact.specialization}</td>
                <td>${contact.order_count}</td>
            `;
            row.addEventListener("click", () => this.showDetails(contact)); // При клике показываем детали
            this.tableElement.appendChild(row); // Добавляем строку в таблицу
        });

        document.getElementById("pageIndicator").textContent = `Страница ${this.currentPage} из ${this.totalPages}`;
    }

    // renderTableSorted() {
    //     this.tableElement.innerHTML = ""; // Очищаем таблицу
    //     const pageContacts = this.filteredContacts; // Отображаем контакты для текущей страницы

    //     pageContacts.forEach(contact => {
    //         const row = document.createElement("tr");
    //         row.innerHTML = `
    //             <td><input type="checkbox" class="select-contact" data-name="${contact.name}"></td>
    //             <td><img src="${contact.img_url || 'https://cdn-icons-png.flaticon.com/512/219/219983.png'}" width="50" height="50"></td>
    //             <td>${contact.name}</td>
    //             <td>${contact.age}</td>
    //             <td>${contact.phone_number}</td>
    //             <td>${contact.specialization}</td>
    //             <td>${contact.order_count}</td>
    //         `;
    //         row.addEventListener("click", () => this.showDetails(contact)); // При клике показываем детали
    //         this.tableElement.appendChild(row); // Добавляем строку в таблицу
    //     });

    //     document.getElementById("pageIndicator").textContent = `Страница ${this.currentPage} из ${this.totalPages}`;
    // }

    sortByColumn(column) {
        const sortDirection = this.sortOrder[column] === "asc" ? "desc" : "asc";
        this.sortOrder[column] = sortDirection;
        const multiplier = sortDirection === "asc" ? 1 : -1;

        this.contacts.sort((a, b) => {
            if (a[column] > b[column]) return 1 * multiplier;
            if (a[column] < b[column]) return -1 * multiplier;
            return 0;
        });

        this.renderTable();
        document.querySelectorAll("th[data-column]").forEach(th => th.classList.remove("sorted-asc", "sorted-desc"));
        document.querySelector(`th[data-column="${column}"]`).classList.add(`sorted-${sortDirection}`);
    }

    rewardSelected() {
        const selectedContacts = Array.from(document.querySelectorAll(".select-contact:checked"))
            .map(checkbox => checkbox.getAttribute("data-name"));

        if (selectedContacts.length === 0) {
            alert("Выберите сотрудников для премирования.");
            return;
        }

        const rewardContainer = document.getElementById("rewardMessage");
        rewardContainer.innerHTML = ""; // Очистить контейнер перед добавлением новых данных

        selectedContacts.forEach(name => {
            const rewardItem = document.createElement("p");
            rewardItem.textContent = `Сотрудник ${name} премирован.`;
            rewardContainer.appendChild(rewardItem);
        });
    }

    showPreloader() {
        document.getElementById("preloader").classList.remove("hidden");
    }

    hidePreloader() {
        document.getElementById("preloader").classList.add("hidden");
    }

    // Применение фильтра
    applyFilter() {
        const filterText = document.getElementById("filterInput").value.toLowerCase(); // Текст фильтра
        this.filteredContacts = this.contacts.filter(contact =>
            contact.name.toLowerCase().includes(filterText) ||
            contact.phone_number.includes(filterText) ||
            contact.specialization.toLowerCase().includes(filterText)
        );
        this.currentPage = 1; // После фильтрации сбрасываем на первую страницу
        this.renderTable(); // Обновляем таблицу с отфильтрованными данными
    }

    // Переход на следующую страницу
    nextPage() {
        if (this.currentPage < this.totalPages) {
            this.currentPage++;
            this.loadContacts(); // Перезагружаем данные с нового номера страницы
        }
    }

    // Переход на предыдущую страницу
    previousPage() {
        if (this.currentPage > 1) {
            this.currentPage--;
            this.loadContacts(); // Перезагружаем данные с нового номера страницы
        }
    }

    // Показ деталей контакта
    showDetails(contact) {
        const detailsContainer = document.getElementById("contactDetails");
        detailsContainer.innerHTML = `
            <h3>Информация о сотруднике</h3>
            <p><strong>ФИО:</strong> ${contact.name}</p>
            <p><strong>Возраст:</strong> ${contact.age}</p>
            <p><strong>Телефон:</strong> ${contact.phone_number}</p>
            <p><strong>Специализация:</strong> ${contact.specialization}</p>
            <p><strong>Выполненные заказы:</strong> ${contact.order_count}</p>
        `;
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const contactsTable = new ContactsTable("/contacts_api/", "contactsTable");
});
