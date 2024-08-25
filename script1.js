let currentIndex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
const totalImages = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8];

function showImage(sliderId, index) {
    const images = document.querySelectorAll(`#bike${sliderId} .bike-image`);
    images.forEach((img, i) => {
        img.classList.toggle('active', i === index);
    });
}

function prevImage(sliderId) {
    currentIndex[sliderId - 1] = (currentIndex[sliderId - 1] - 1 + totalImages[sliderId - 1]) % totalImages[sliderId - 1];
    showImage(sliderId, currentIndex[sliderId - 1]);
}

function nextImage(sliderId) {
    currentIndex[sliderId - 1] = (currentIndex[sliderId - 1] + 1) % totalImages[sliderId - 1];
    showImage(sliderId, currentIndex[sliderId - 1]);
}

// Initialize sliders
document.addEventListener('DOMContentLoaded', () => {
    showImage(1, 0);
    showImage(2, 0);
    showImage(3, 0);
    showImage(4, 0);
    showImage(5, 0);
    showImage(6, 0);
    showImage(7, 0);
    showImage(8, 0);
    showImage(9, 0);
    showImage(10, 0);
    showImage(11, 0);
    showImage(12, 0);
    showImage(13, 0);
    showImage(14, 0);
    showImage(15, 0);
    showImage(16, 0); 
});

// Get the button
let backToTopBtn = document.getElementById("backToTop");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        backToTopBtn.style.display = "block";
    } else {
        backToTopBtn.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
backToTopBtn.onclick = function() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
};
