// Retrieve the container and slides
var container = document.querySelector('.container');
var slides = container.children;

// Initialize slide index
var currentSlide = 0;

// Function to show the current slide
function showSlide() {
    // Hide all slides
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }

    // Show the current slide
    slides[currentSlide].style.display = 'block';
}

// Function to navigate to the next slide
function nextSlide() {
    if (currentSlide < slides.length - 1) {
        currentSlide++;
        showSlide();
    }
}

// Call the showSlide function to display the initial slide
showSlide();

// Event listener for the keypress event to navigate to the next slide
document.addEventListener('keydown', function(event) {
    if (event.keyCode === 39 || event.keyCode === 32) { // Right arrow key or Spacebar
        nextSlide();
    }
});
