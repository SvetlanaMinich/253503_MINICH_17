// Базовый класс
function Subscriber(lastName, address, newspapers, magazines) {
    this._lastName = lastName;
    this._address = address;
    this._newspapers = newspapers;
    this._magazines = magazines;
}

// Методы базового класса
Subscriber.prototype.getName = function () {
    return this._lastName;
}
Subscriber.prototype.getAddress = function () {
    return this._address;
}
Subscriber.prototype.getNewspapersCount = function () {
    return this._newspapers;
}
Subscriber.prototype.getMagazinesCount = function () {
    return this._magazines;
}

Subscriber.prototype.setName = function (val) {
    this._lastName = val;
}
Subscriber.prototype.setAddress = function (val) {
    this._address = val;
}
Subscriber.prototype.setNewspapersCount = function (val) {
    this._newspapers = val;
}
Subscriber.prototype.setMagazinesCount = function (val) {
    this._magazines = val;
}

Subscriber.prototype.addSubscriber = function (subscriberList, subscriber) {
    subscriberList.push(subscriber);
};

Subscriber.prototype.listSubscribers = function (subscriberList) {
    return subscriberList.map(subscriber => subscriber.getFullInfo()).join("\n");
};

Subscriber.prototype.filterSubscribers = function (subscriberList) {
    return subscriberList.filter(
        sub => sub.newspapers >= 3 && sub.magazines >= 2
    );
};

// Класс-наследник
function PremiumSubscriber(lastName, address, newspapers, magazines, pictures) {
    Subscriber.call(this, lastName, address, newspapers, magazines);
    this._pictures = pictures;
}

// Наследование методов
PremiumSubscriber.prototype = Object.create(Subscriber.prototype);
PremiumSubscriber.prototype.constructor = PremiumSubscriber;

// Дополнительный метод для премиальных подписчиков
Subscriber.prototype.getPicturesCount = function () {
    return this._pictures;
}
Subscriber.prototype.setPicturesCount = function (val) {
    this._pictures = val;
}

// Пример использования
const subscribers = [];

const subscriber1 = new Subscriber("Иванов", "ул. Ленина, 1", 4, 3);
const subscriber2 = new Subscriber("Петров", "ул. Мира, 2", 1, 1);
const subscriber3 = new PremiumSubscriber("Сидоров", "ул. Свободы, 3", 5, 2, true);

subscriber1.addSubscriber(subscribers, subscriber1);
subscriber2.addSubscriber(subscribers, subscriber2);
subscriber3.addSubscriber(subscribers, subscriber3);

console.log("Все подписчики:");
console.log(subscriber1.listSubscribers(subscribers));

console.log("\nПодписчики с >= 3 газетами и >= 2 журналами:");
console.log(
    subscriber1
        .filterSubscribers(subscribers)
        .map(sub => sub.getFullInfo())
        .join("\n")
);
