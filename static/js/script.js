document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling
    document.querySelectorAll('.nav-links a, .cta-button').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            window.scrollTo({
                top: targetElement.offsetTop - 70,
                behavior: 'smooth'
            });
        });
    });

    // Particle animation for hero section
    const canvas = document.getElementById('particle-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const particleCount = 100;

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 3 + 1;
            this.speedX = Math.random() * 1 - 0.5;
            this.speedY = Math.random() * 1 - 0.5;
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            if (this.size > 0.2) this.size -= 0.01;
            if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
            if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
        }

        draw() {
            ctx.fillStyle = 'rgba(20, 184, 166, 0.5)';
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function initParticles() {
        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }
    }

    function animateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(particle => {
            particle.update();
            particle.draw();
            if (particle.size <= 0.2) {
                particles.splice(particles.indexOf(particle), 1);
                particles.push(new Particle());
            }
        });
        requestAnimationFrame(animateParticles);
    }

    initParticles();
    animateParticles();

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });

    // Form validation with real-time feedback
    const form = document.getElementById('contact-form');
    const inputs = form.querySelectorAll('input, textarea');

    inputs.forEach(input => {
        input.addEventListener('input', () => {
            const errorElement = document.getElementById(`${input.name}-error`);
            if (input.name === 'email' && input.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value)) {
                errorElement.textContent = 'Please enter a valid email address.';
            } else if (input.value.trim() === '') {
                errorElement.textContent = `${input.placeholder} is required.`;
            } else {
                errorElement.textContent = '';
            }
        });
    });

    form.addEventListener('submit', (e) => {
        let hasError = false;
        inputs.forEach(input => {
            const errorElement = document.getElementById(`${input.name}-error`);
            if (input.value.trim() === '') {
                errorElement.textContent = `${input.placeholder} is required.`;
                hasError = true;
            } else if (input.name === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value)) {
                errorElement.textContent = 'Please enter a valid email address.';
                hasError = true;
            }
        });

        if (hasError) {
            e.preventDefault();
            alert('Please fix the errors in the form.');
        }
    });

    // Scroll-triggered animations
    const sections = document.querySelectorAll('.section');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.2 });

    sections.forEach(section => {
        observer.observe(section);
    });
});

// Background animation
const hero = document.querySelector('.hero');
if (!hero) {
    console.error('Hero element not found!');
} else {
    const images = [
        '/media/background2.jpg',
        '/media/background3.jpg',
        
    ];
    let currentIndex = 0;

    function changeBackground() {
        console.log('Changing to:', images[currentIndex]); // Debug log
        hero.style.transition = 'opacity 1s ease';
        hero.style.opacity = 0;
        setTimeout(() => {
            hero.style.backgroundImage = `url("${images[currentIndex]}")`;
            hero.style.backgroundSize = 'cover';
            hero.style.backgroundPosition = 'center';
            hero.style.opacity = 1;
            currentIndex = (currentIndex + 1) % images.length;
            console.log('Applied:', hero.style.backgroundImage);
        }, 5000);
    }

    setInterval(changeBackground, 5000);
    changeBackground(); // Initial load
}