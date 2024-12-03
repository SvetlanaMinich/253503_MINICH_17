class CountdownTimer {
    constructor(duration, elementId) {
        this.duration = duration; // countdown duration in milliseconds
        this.element = document.getElementById(elementId);
        this.startTime = this.getOrSetStartTime();
        this.updateCountdown(); // Initialize display
        this.startInterval();
    }

    // Retrieve or set the start time in local storage
    getOrSetStartTime() {
        let storedTime = localStorage.getItem('startTime');
        if (!storedTime) {
            storedTime = Date.now();
            localStorage.setItem('startTime', storedTime);
        }
        return parseInt(storedTime, 10);
    }

    updateCountdown() {
        const now = Date.now();
        const elapsedTime = now - this.startTime;
        const timeRemaining = this.duration - elapsedTime;

        if (timeRemaining <= 0) {
            this.element.textContent = "Время истекло!";
            this.clearCountdown();
            return;
        }

        const hours = 0;
        const minutes = Math.floor(timeRemaining / (1000 * 60));
        const seconds = Math.floor(timeRemaining / 1000 - minutes * 60);

        this.element.textContent = `Обратный отсчёт: ${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }

    startInterval() {
        this.intervalId = setInterval(() => this.updateCountdown(), 1000);
    }

    clearCountdown() {
        clearInterval(this.intervalId);
        localStorage.removeItem('startTime');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const countdownDuration = 60 * 60 * 1000;
    new CountdownTimer(countdownDuration, 'countdown');
});