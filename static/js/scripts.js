var phrases = ["Machine Learner", "Softwar Engineer", "Data Scientist"];
var i = 0;
var j = 0;
var currentPhrase = phrases[0];
var isDeleting = false;
var speed = 100;

function typeWriter() {
  var displayText = currentPhrase.substring(0, i);
  document.getElementById("dynamic-part").innerHTML = displayText;

  if (isDeleting) {
    if (i > 0) {
      i--;
      setTimeout(typeWriter, speed / 2); // Speed up the deleting effect
    } else {
      isDeleting = false;
      j = (j + 1) % phrases.length;
      currentPhrase = phrases[j];
      setTimeout(typeWriter, speed);
    }
  } else {
    if (i < currentPhrase.length) {
      i++;
      setTimeout(typeWriter, speed);
    } else {
      isDeleting = true;
      setTimeout(typeWriter, speed * 2); // Pause before starting to delete
    }
  }
}

document.addEventListener('DOMContentLoaded', typeWriter);

// skills
document.addEventListener('DOMContentLoaded', () => {
  const progressBars = document.querySelectorAll('.progress');

  progressBars.forEach(bar => {
      const percentage = bar.getAttribute('data-percentage');
      bar.style.width = percentage + '%';
  });
});

//chart
document.addEventListener('DOMContentLoaded', () => {
  const progressBars = document.querySelectorAll('.progress');

  progressBars.forEach(bar => {
      const percentage = bar.getAttribute('data-percentage');
      bar.style.width = percentage + '%';
  });

  const ctx = document.getElementById('softSkillsChart').getContext('2d');
  const softSkillsChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['Communication', 'Teamwork', 'Problem-solving', 'Time Management', 'Adaptability'],
          datasets: [{
              label: 'Soft Skills',
              data: [20, 25, 30, 15, 10], // Example data, change to your actual percentages
              backgroundColor: [
                  '#FF6384',
                  '#36A2EB',
                  '#FFCE56',
                  '#4BC0C0',
                  '#9966FF'
              ]
          }]
      },
      options: {
          responsive: true,
          plugins: {
              legend: {
                  position: 'bottom',
                  labels: {
                    font: {
                        size: 10
                    },
                    boxWidth:10,
                    boxHeight:10
                }
              },
              tooltip: {
                  enabled: true
              }
          }
      }
  });
});

let currentIndex = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-item');
    if (index >= slides.length) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = slides.length - 1;
    } else {
        currentIndex = index;
    }
    const offset = -currentIndex * 100;
    document.querySelector('.carousel-inner').style.transform = `translateX(${offset}%)`;
}

function nextSlide() {
    showSlide(currentIndex + 1);
}

function prevSlide() {
    showSlide(currentIndex - 1);
}

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

// prevent link jump 
document.querySelectorAll('.sidenav a').forEach(link => {
  link.addEventListener('click', function(event) {
      event.preventDefault(); // Prevent default jump
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
          closeNav(); // Close nav after scrolling
      }
  });
});
