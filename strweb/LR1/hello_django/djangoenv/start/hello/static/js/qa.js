{/* <label>
    <input type="checkbox" id="toggleSettings" /> Изменить внешний вид
</label>
<!-- Элементы для изменения стиля -->
<div id="styleSettings" style="display: none;">
    <div>
        <label for="fontSize">Размер шрифта:</label>
        <select id="fontSize">
            <option value="14px">14px</option>
            <option value="16px">16px</option>
            <option value="18px">18px</option>
            <option value="20px">20px</option>
        </select>
    </div>
    <div>
        <label for="textColor">Цвет текста:</label>
        <input type="color" id="textColor" value="#000000" />
    </div>
    <div>
        <label for="bgColor">Цвет фона:</label>
        <input type="color" id="bgColor" value="#ffffff" />
    </div>
</div> */}

class PageStyler {
    constructor() {
        // Получаем ссылки на элементы страницы
        this.toggleSettings = document.getElementById('toggleSettings');
        this.styleSettings = document.getElementById('styleSettings');
        this.fontSizeSelect = document.getElementById('fontSize');
        this.textColorInput = document.getElementById('textColor');
        this.bgColorInput = document.getElementById('bgColor');

        // Инициализируем обработчики событий
        this.initEventListeners();
    }

    // Метод для инициализации обработчиков событий
    initEventListeners() {
        // Обработчик изменения флажка, показывающего блок настроек
        this.toggleSettings.addEventListener('change', this.toggleStyleSettings.bind(this));

        // Обработчики для изменения стилей
        this.fontSizeSelect.addEventListener('change', this.changeFontSize.bind(this));
        this.textColorInput.addEventListener('input', this.changeTextColor.bind(this));
        this.bgColorInput.addEventListener('input', this.changeBgColor.bind(this));
    }

    // Метод для переключения видимости блока с настройками
    toggleStyleSettings() {
        this.styleSettings.style.display = this.toggleSettings.checked ? 'block' : 'none';
    }

    // Метод для изменения размера шрифта
    changeFontSize() {
        document.body.style.fontSize = this.fontSizeSelect.value;
    }

    // Метод для изменения цвета текста
    changeTextColor() {
        document.body.style.color = this.textColorInput.value;
    }

    // Метод для изменения цвета фона
    changeBgColor() {
        document.body.style.backgroundColor = this.bgColorInput.value;
    }
}

// Создаем экземпляр класса PageStyler при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    new PageStyler();
});
