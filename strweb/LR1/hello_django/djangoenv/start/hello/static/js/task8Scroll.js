// Получаем элементы изображений
const carImage = document.getElementById("car");
const tool1Image = document.getElementById("tool1");
const tool2Image = document.getElementById("tool2");

// Проверяем, что элементы найдены
if (carImage && tool1Image && tool2Image) {
    // Функция для вычисления угла поворота
    function rotateOnScroll() {
        const scrollPosition = window.scrollY; // Текущая позиция прокрутки
        const rotationSpeed = 0.2; // Скорость вращения

        // Вычисляем угол поворота в зависимости от прокрутки
        const rotation = scrollPosition * rotationSpeed;

        // Применяем вращение к изображениям
        carImage.style.transform = `rotate(${rotation}deg)`;
        tool1Image.style.transform = `rotate(-${rotation}deg)`;
        tool2Image.style.transform = `rotate(${rotation}deg)`;
    }

    // Добавляем обработчик события для скроллинга
    window.addEventListener("scroll", rotateOnScroll);
} else {
    console.error("Одно или несколько изображений не найдены.");
}
