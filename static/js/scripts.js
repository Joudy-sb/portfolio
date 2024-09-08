var phrases = ["Machine Learning Engineer", "Softwar Engineer", "Frontend Developer", "Mobile App Developer"];
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
          labels: ['Time Management', 'Critical Thinking', 'Emotional Intelligence', 'Resiliense',  'Communication'],
          datasets: [{
              label: 'Soft Skills',
              data: [20, 25, 30, 15, 10], // Example data, change to your actual percentages
              backgroundColor: [
                  '#a9c4d8',
                  '#809aad',
                  '#587284',
                  '#324c5d',
                  '#0d2a39'
              ],
              borderColor: [
                '#111', // Border color for 'Communication'
                '#111', // Border color for 'Teamwork'
                '#111', // Border color for 'Problem-solving'
                '#111', // Border color for 'Time Management'
                '#111'  // Border color for 'Adaptability'
            ],
            borderWidth: 1 // Set border width
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
                    boxHeight:10,
                }
              },
              tooltip: {
                  enabled: true
              }
          }
      }
  });
});

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

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}
