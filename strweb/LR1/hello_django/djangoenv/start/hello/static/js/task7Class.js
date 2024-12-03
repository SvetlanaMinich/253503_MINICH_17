// Базовый класс
class Subscriber {
    constructor(lastName, address, newspapers, magazines) {
        this._lastName = lastName;
        this._address = address;
        this._newspapers = newspapers;
        this._magazines = magazines;
    }

    getName() {
        return this._lastName;
    }
    getAddress() {
        return this._address;
    }
    getNewspapersCount() {
        return this._newspapers;
    }
    getMagazinesCount() {
        return this._magazines;
    }

    setName(van) {
        this._lastName = val;
    }
    setAddress(val) {
        this._address = val;
    }
    setNewspapersCount(val) {
        this._newspapers = val;
    }
    setMagazinesCount(val) {
        this._magazines = val;
    }
}

// Класс-наследник
class PremiumSubscriber extends Subscriber {
    constructor(lastName, address, newspapers, magazines, pictures) {
        super(lastName, address, newspapers, magazines);
        this._pictures = pictures;
    }

    getPicturesCount() {
        return this._pictures;
    }
    setPicturesCount(val) {
        this._pictures = val;
    }

    static addSubscriber(subscriberList, subscriber) {
        subscriberList.push(subscriber);
    }

    static listSubscribers(subscriberList) {
        return subscriberList.map(subscriber => subscriber.getFullInfo()).join("\n");
    }

    static filterSubscribers(subscriberList) {
        return subscriberList.filter(
            sub => sub.getNewspapersCount() >= 3 && sub.getMagazinesCount() >= 2
        );
    }
}

const subscribers = [];

const subscriber1 = new Subscriber("Иванов", "ул. Ленина, 1", 4, 3);
const subscriber2 = new Subscriber("Петров", "ул. Мира, 2", 1, 1);
const subscriber3 = new Subscriber("Васильев", "ул. Ленина, 1", 7, 12);
const subscriber4 = new Subscriber("Быков", "ул. Мира, 2", 1, 13);
const subscriber5 = new Subscriber("Машеров", "ул. Ленина, 1", 4, 8);
const subscriber6 = new Subscriber("Петровский", "ул. Мира, 2", 5, 1);
const subscriber7 = new PremiumSubscriber("Сидоров", "ул. Свободы, 3", 5, 2, 14);

PremiumSubscriber.addSubscriber(subscribers, subscriber1);
PremiumSubscriber.addSubscriber(subscribers, subscriber2);
PremiumSubscriber.addSubscriber(subscribers, subscriber3);
PremiumSubscriber.addSubscriber(subscribers, subscriber4);
PremiumSubscriber.addSubscriber(subscribers, subscriber5);
PremiumSubscriber.addSubscriber(subscribers, subscriber6);
PremiumSubscriber.addSubscriber(subscribers, subscriber7);

// Отображаем подписчиков сразу после загрузки
window.onload = () => {
    displaySubscribers();
};

function addSubscriberFromForm() {
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const mag_count = document.getElementById('magazines').value;
    const news_count = document.getElementById('newspapers').value;
    const pic_cont = document.getElementById('pictures').value;
  
    const newSubs = new PremiumSubscriber(name, address, news_count, mag_count, pic_cont);
    PremiumSubscriber.addSubscriber(subscribers, newSubs);
  
    displaySubscribers();
  }
  
function displaySubscribers() {
    const outputDiv = document.getElementById('subscribers-output');
    outputDiv.innerHTML = '';
  
    subscribers.forEach(sub => {
      outputDiv.innerHTML += `
        <p>Имя: ${sub.getName()} - Адрес: ${sub.getAddress()}</p>
        <p>Журналы: ${sub.getMagazinesCount()} - Газеты: ${sub.getNewspapersCount()} - Картинки: ${sub.getPicturesCount()}</p>
      `;
    });
  }
  
function filterSubscribers() {
    const filteredSubscribers = PremiumSubscriber.filterSubscribers(subscribers);

    const filteredDiv = document.getElementById('filtered-subscribers-output');
    filteredDiv.innerHTML = '';

    if (filteredSubscribers.length === 0) {
        filteredDiv.innerHTML = 'Подписчиков, выписывающих более 3 газет и 2 журналов, не найдено.';
    } else {
        filteredSubscribers.forEach(sub => {
            filteredDiv.innerHTML += `<p>Адрес: ${sub.getAddress()}</p>`;
        });
    }
}