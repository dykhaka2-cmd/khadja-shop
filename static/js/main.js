// Khadja Rassoul Shop — main.js

document.addEventListener('DOMContentLoaded', function () {

  // Auto-fermeture des messages après 4s
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      alert.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      alert.style.opacity = '0';
      alert.style.transform = 'translateY(-10px)';
      setTimeout(() => alert.remove(), 600);
    }, 4000);
  });

  // Smooth scroll pour les ancres
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Marquer le lien actif dans la navbar
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.style.color = '#d4a843';
      link.style.borderBottomColor = '#d4a843';
    }
  });

  // Animation au scroll pour les cards produits
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }
      });
    },
    { threshold: 0.1 }
  );

  document.querySelectorAll('.product-card, .category-card, .garantie-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(card);
  });

});

// Menu mobile toggle
function toggleMenu() {
  const nav = document.getElementById('navLinks');
  nav.classList.toggle('open');
}
