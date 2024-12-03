class Slider 
{
    constructor(container, intervalInput, options = {})
    {
        this.container = container;
        this.slides = Array.from(container.querySelectorAll('.slide'));
        this.intervalInput = intervalInput;
        this.currentSlide = 0;
        
        this.interval = options.auto ? 5000 : parseInt(this.intervalInput.value, 10);
        this.loop = options.loop ?? true;
        this.auto = options.auto ?? true;
        this.stopMouseHover = options.stopMouseHover ?? true;
        this.navs = options.navs ?? true;
        this.pags = options.pags ?? true;

        this.initControls();
        if (this.auto) this.startSlider();

         // Set event listener for changes in interval input
        this.intervalInput.addEventListener('input', () => {
            clearInterval(this.slideInterval); // Stop the current interval
            this.interval = parseInt(this.intervalInput.value, 10) || 5000; // Update the interval value
            this.startSlider(); // Restart the slider with new interval
        });
    }

    initControls() {
        if (this.navs) 
        {
            document.getElementById('prevSlide').addEventListener('click', () => this.prevSlide());
            document.getElementById('nextSlide').addEventListener('click', () => this.nextSlide());
        } 
        else 
        {
            document.querySelectorAll('.nav-btn').forEach(btn => btn.style.display = 'none');
        }

        if (this.pags)
        {
            this.paginationDots = Array.from(document.querySelectorAll('.pagination-dot'));
            this.paginationDots.forEach(dot => {
                dot.addEventListener('click', (e) => this.goToSlide(parseInt(e.target.dataset.index, 10)));
        });
        }
    }

    startSlider()
    {
        this.showSlide(this.currentSlide);
        this.slideInterval = setInterval(() => this.nextSlide(), this.interval); 

        if (this.stopMouseHover) {
            this.container.addEventListener('mouseover', () => clearInterval(this.slideInterval));
            this.container.addEventListener('mouseout', () => this.startSlider());
        }
    }

    showSlide(curInd)
    {
        this.slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === curInd);
        });

        document.getElementById('caption').textContent = this.slides[curInd].dataset.caption;
        document.getElementById('slideNumber').textContent = `${curInd + 1} / ${this.slides.length}`;
        
        // Update pagination dots
        this.paginationDots.forEach((dot, i) => {
            dot.classList.toggle('active', i === curInd);
        });
    }

    nextSlide()
    {
        if (this.currentSlide < this.slides.length - 1) {
            this.currentSlide++;
        } else if (this.loop) {
            this.currentSlide = 0;
        } else {
            clearInterval(this.slideInterval);
            return;
        }
        this.showSlide(this.currentSlide);
    }

    prevSlide() {
        if (this.currentSlide > 0) {
            this.currentSlide--;
        } else if (this.loop) {
            this.currentSlide = this.slides.length - 1;
        }
        this.showSlide(this.currentSlide);
    }

    goToSlide(index) {
        clearInterval(this.slideInterval);
        this.currentSlide = index;
        this.showSlide(this.currentSlide);
        if (this.auto) this.startSlider();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const banner = document.querySelector('.banner');
    const intervalInput = document.getElementById('intervalInput');
    new Slider(banner, intervalInput, {
        loop: true,
        navs: true,
        pags: true,
        auto: true,
        stopMouseHover: true
    });
});