document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

$(window).scroll(function(){
    if ($(this).scrollTop() > 1) {
       $('#navbar').addClass('scrolling');
    } else {
       $('#navbar').removeClass('scrolling');
    }
});