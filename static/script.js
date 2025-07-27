document.addEventListener("DOMContentLoaded", function(){
  const textElement = document.getElementById("text");

  const message = "Welcome to my portfolio! Explore to know more about me and my works.";

  let index = 0;

  function type(){
    if (index < message.length){
      textElement.textContent += message.charAt(index);
      index++;

      setTimeout(type, 100); //Adjust the speed here (in milliseconds)
    }
  }

  type();
})

document.addEventListener("DOMContentLoaded", function(){
  const textElement_1 = document.getElementById("text_1");

  const message_1 = "Hi, I'm Abel Ogbonna, a Python Developer with a passion for AI and Machine Learning. I have experience in Python, JavaScript, CSS, HTML, SQL and Machine Learning.";

  let index_1 = 0;

  function type_1(){
    if (index_1 < message_1.length){
      textElement_1.textContent += message_1.charAt(index_1);
      index_1++;

      setTimeout(type_1, 100); //Adjust the speed here (in milliseconds)
    }
  }

  type_1();
});

// Slideshow functionality
let currentSlideIndex = 0;
let slides = [];

document.addEventListener('DOMContentLoaded', function() {
  // Initialize slideshow
  slides = document.querySelectorAll('.project-slide');
  updateSlideCounter();
  updateIndicators();
  updateNavigationButtons();
});

function changeSlide(direction) {
  const totalSlides = slides.length;
  
  // Hide current slide
  slides[currentSlideIndex].style.display = 'none';
  
  // Calculate new slide index
  currentSlideIndex += direction;
  
  // Handle wrap-around
  if (currentSlideIndex >= totalSlides) {
    currentSlideIndex = 0;
  } else if (currentSlideIndex < 0) {
    currentSlideIndex = totalSlides - 1;
  }
  
  // Show new slide with fade animation
  slides[currentSlideIndex].style.display = 'block';
  slides[currentSlideIndex].classList.add('fade');
  
  // Remove fade class after animation
  setTimeout(() => {
    slides[currentSlideIndex].classList.remove('fade');
  }, 500);
  
  updateSlideCounter();
  updateIndicators();
  updateNavigationButtons();
}

function currentSlide(slideIndex) {
  if (slideIndex < 1 || slideIndex > slides.length) return;
  
  // Hide current slide
  slides[currentSlideIndex].style.display = 'none';
  
  // Update current slide index (convert from 1-based to 0-based)
  currentSlideIndex = slideIndex - 1;
  
  // Show new slide with fade animation
  slides[currentSlideIndex].style.display = 'block';
  slides[currentSlideIndex].classList.add('fade');
  
  // Remove fade class after animation
  setTimeout(() => {
    slides[currentSlideIndex].classList.remove('fade');
  }, 500);
  
  updateSlideCounter();
  updateIndicators();
  updateNavigationButtons();
}

function updateSlideCounter() {
  const currentSlideElement = document.getElementById('current-slide');
  const totalSlidesElement = document.getElementById('total-slides');
  
  if (currentSlideElement && totalSlidesElement) {
    currentSlideElement.textContent = currentSlideIndex + 1;
    totalSlidesElement.textContent = slides.length;
  }
}

function updateIndicators() {
  const indicators = document.querySelectorAll('.indicator');
  
  indicators.forEach((indicator, index) => {
    if (index === currentSlideIndex) {
      indicator.classList.add('active');
    } else {
      indicator.classList.remove('active');
    }
  });
}

function updateNavigationButtons() {
  const prevBtn = document.querySelector('.prev-btn');
  const nextBtn = document.querySelector('.next-btn');
  
  if (prevBtn && nextBtn) {
    // For circular navigation, buttons are always enabled
    prevBtn.disabled = false;
    nextBtn.disabled = false;
  }
}

// Project card sliding functionality with backend integration
function completeProject(button) {
  const projectCard = button.closest('.project-card');
  const projectSlide = button.closest('.project-slide');
  const projectId = projectSlide.getAttribute('data-project');
  const projectTitle = projectCard.querySelector('.project-header h4').textContent;
  
  // Disable button to prevent multiple clicks
  button.disabled = true;
  button.textContent = 'Processing...';
  
  // Make API call to backend
  fetch('/api/complete-project', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      project_id: projectId,
      project_title: projectTitle,
      timestamp: new Date().toISOString()
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      // Add sliding animation class
      projectCard.classList.add('sliding-out');
      
      // Update button state
      button.textContent = 'Completed';
      button.style.background = 'rgba(108, 117, 125, 0.5)';
      
      // Remove slide after animation completes
      setTimeout(() => {
        projectSlide.style.display = 'none';
        
        // Move to next slide if available
        if (slides.length > 1) {
          changeSlide(1);
        }
        
        // Show completion message with project title
        showProjectCompletionMessage(projectId, projectTitle);
      }, 800);
      
      console.log('Project completed successfully:', data.message);
    } else {
      // Re-enable button if there was an error
      button.disabled = false;
      button.textContent = 'Complete';
      console.error('Error completing project:', data.error);
    }
  })
  .catch(error => {
    // Re-enable button if there was an error
    button.disabled = false;
    button.textContent = 'Complete';
    console.error('Error completing project:', error);
  });
}

function showProjectCompletionMessage(projectId, projectTitle) {
  // Create a temporary completion message
  const message = document.createElement('div');
  message.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: rgba(40, 167, 69, 0.9);
    color: white;
    padding: 15px 25px;
    border-radius: 10px;
    font-weight: 600;
    z-index: 1000;
    animation: slideInRight 0.5s ease-out;
    max-width: 300px;
    word-wrap: break-word;
  `;
  message.textContent = `Project "${projectTitle}" completed!`;
  
  document.body.appendChild(message);
  
  // Remove message after 4 seconds
  setTimeout(() => {
    message.style.animation = 'slideOutRight 0.5s ease-in';
    setTimeout(() => {
      document.body.removeChild(message);
    }, 500);
  }, 4000);
}

// Add CSS animations for notification
const style = document.createElement('style');
style.textContent = `
  @keyframes slideInRight {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
  
  @keyframes slideOutRight {
    from {
      transform: translateX(0);
      opacity: 1;
    }
    to {
      transform: translateX(100%);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);

// Add hover effects for project cards
document.addEventListener('DOMContentLoaded', function() {
  const projectCards = document.querySelectorAll('.project-card');
  
  projectCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-8px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0) scale(1)';
    });
  });
});