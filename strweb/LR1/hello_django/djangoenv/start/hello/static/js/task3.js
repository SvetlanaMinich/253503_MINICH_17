// Функция для вычисления факториала
function factorial(n) {
    return n === 0 ? 1 : n * factorial(n - 1);
}

// Разложение косинуса в ряд Тейлора
function taylorCos(x, terms) {
    let result = 0;
    for (let n = 0; n < terms; n++) {
        result += Math.pow(-1, n) * Math.pow(x, 2 * n) / factorial(2 * n);
    }
    return result;
}

// Создаем данные для графика
const xValues = []; // Значения x
const taylorValues = []; // Значения разложения
const mathValues = []; // Значения Math.cos

const terms = 3; // Количество членов ряда
const step = 0.1; // Шаг по x

for (let x = -Math.PI; x <= Math.PI; x += step) {
    xValues.push(x.toFixed(2)); // Округляем до двух знаков
    taylorValues.push(taylorCos(x, terms));
    mathValues.push(Math.cos(x));
}

const ctx = document.getElementById("myChart").getContext("2d");
const chart = new Chart(ctx, {
    type: "line", // Тип графика
    data: {
        labels: xValues,
        datasets: [
            {
                label: `Ряд Тейлора (n=${terms})`,
                data: taylorValues,
                borderColor: "blue",
                fill: false,
                tension: 0.1, // Плавность линии
            },
            {
                label: "Math.cos(x)",
                data: mathValues,
                borderColor: "red",
                fill: false,
                tension: 0.1,
            },
        ],
    },
    options: {
        animation: {
            duration: 2000, // Длительность анимации в миллисекундах
        },    
        responsive: true,
        plugins: {
            legend: {
                display: true, // Включаем легенду
            },
            tooltip: {
                enabled: true,
            },
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: "x",
                },
            },
            y: {
                title: {
                    display: true,
                    text: "F(x)",
                },
            },
        },
    },
});

document.getElementById("saveChart").addEventListener("click", function () {
    const link = document.createElement("a");
    link.href = chart.toBase64Image();
    link.download = "chart.png";
    link.click();
});
