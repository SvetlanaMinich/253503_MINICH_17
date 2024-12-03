function closeForm() {
    document.getElementById("addContactModal").style.display = "none";
  }
function openForm() {
    document.getElementById("addContactModal").style.display = "block";
  }


class ContactForm {
    constructor() {
        this.addContactButton = document.getElementById("addContact");
        this.addContactButton.disabled = true;

        this.modal = document.getElementById("addContactModal");
        this.form = document.getElementById("addContactForm");

        this.imgUrlInput = document.getElementById("img_url");
        this.isImgUrl = false;

        this.phoneInput = document.getElementById("phone_number");
        this.isPhone = false;

        this.inputs = Array.from(this.form.querySelectorAll("input[required]"));
        this.inputStatus = {};

        // Инициализация начальных значений для inputStatus
        this.inputs.forEach(input => {
            this.inputStatus[input.name] = false; // Все поля изначально пустые
            input.addEventListener("input", () => this.handleInputChange(input)); // Обработчик изменения
        });

        this.imgUrlError = document.getElementById("imgUrlError");
        this.phoneError = document.getElementById("phoneError");

        this.urlRegex = /^(https?:\/\/).+\.(png|jpeg|jpg)$/i;
        this.phoneRegex = /^(\+375)[\s-]?(\(\d{2}\)|\d{2})[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$/;

        this.initializeEvents();
    }

    handleInputChange(input) {
        // Проверяем, заполнено ли поле
        this.inputStatus[input.name] = input.value.trim() !== "";

        // Проверяем валидность URL и телефона
        if (input === this.imgUrlInput) {
            this.validateUrl();
        }
        if (input === this.phoneInput) {
            this.validatePhone();
        }

        // Проверяем, все ли поля заполнены
        const allFieldsFilled = Object.values(this.inputStatus).every(status => status);

        // Активируем или отключаем кнопку
        this.addContactButton.disabled = !allFieldsFilled;
    }

    validateUrl() {
        this.isImgUrl = this.urlRegex.test(this.imgUrlInput.value);
        if (!this.isImgUrl) {
            this.imgUrlError.textContent = "Неверный формат URL. Пример: http://site.ru/index.php";
            this.imgUrlInput.invalid = true;
        } else {
            this.imgUrlError.textContent = "";
            this.imgUrlInput.valid = true;
        }
    }

    validatePhone() {
        this.isPhone = this.phoneRegex.test(this.phoneInput.value);
        if (!this.isPhone) {
            this.phoneError.textContent = "Неверный формат телефона. Пример: +375 (29) 111-22-33";
        } else {
            this.phoneError.textContent = "";
        }
    }

    toggleModal() {
        this.modal.classList.toggle("hidden");
    }

    fieldsFilled() {
        if (this.isDate && this.isEmail && this.isImgUrl && this.isName && this.isPhone) {
            this.addContactButton.disabled = false;
        }
    }

    async handleFormSubmit(event) {
        event.preventDefault(); // Предотвращаем перезагрузку страницы

        const newContact = {
            name: this.form.name.value,
            img_url: this.form.img_url.value,
            age: this.form.date_of_birth.value,
            phone_number: this.form.phone_number.value,
            specialization: 'Замена запчастей',
            order_count: 0, // Укажите значение по умолчанию
        };

        try {
            const csrfToken = this.getCSRFToken();
            const response = await fetch("http://127.0.0.1:8000/api/contacts/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify(newContact),
            });

            if (!response.ok) {
                const errorData = await response.json();
                console.error(`HTTP Error: ${response.status}`, errorData);
                alert(`Ошибка при добавлении контакта: ${errorData.message}`);
                return;
            }

            const result = await response.json();
            if (result.success) {
                alert("Контакт успешно добавлен!");
                this.toggleModal();
                this.form.reset();
            } else {
                alert("Ошибка при добавлении контакта: " + result.message);
            }
        } catch (error) {
            console.error("Ошибка:", error);
            alert("Произошла ошибка при добавлении контакта.");
        }
    }

    // Функция получения CSRF токена
    getCSRFToken() {
        const cookieValue = document.cookie.match(/(^|;\s*)csrftoken=([^;]*)/);
        return cookieValue ? cookieValue[2] : "";
    }
    
    initializeEvents() {
        this.form.addEventListener("submit", (event) => this.handleFormSubmit(event));
    }
}

// Инициализация
document.addEventListener("DOMContentLoaded", () => {
    new ContactForm();
});
