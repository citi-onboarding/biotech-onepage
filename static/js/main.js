// BANNER SLICK
$(document).ready(function () {
    console.log('Made with 💻 and 💚 by CITi');

    document.querySelector('.preloader').style.opacity = 0;
    setTimeout(() => {
        document.querySelector('.preloader').style.display = 'none';
    }, 200);

    $('#banner-carousel').slick({
        arrows: true,
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 10000,
        draggable: false,
    });

    $(".slick-next").empty();
    $(".slick-prev").empty();

    // Smooth scroll
    $(".categorias a").on('click', function(event) {

        if (this.hash !== "") {
            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
            scrollTop: $(hash).offset().top - 60
            }, 800, function(){

            window.location.hash = '';
            });
        }
    });
});

// NAVBAR
const nav = document.querySelector('nav');
const categorias = document.querySelector('.categorias');
const hamMenu = document.querySelector('#menu-barras');
const dropdown = document.querySelector('#dropdown');
const logo = document.querySelector('#logo-navbar');

let prevScrollpos = window.pageYOffset;

hamMenu.addEventListener('click', e => {
    if(dropdown.classList.contains('change')){
        dropdown.style.opacity = 0;
        setTimeout(() => {
            document.querySelector('#menu-barras').classList.toggle("change");
            dropdown.classList.toggle("change");
        }, 300);
    }
    else{
        document.querySelector('#menu-barras').classList.toggle("change");
        dropdown.classList.toggle("change");
        setTimeout(() => {
            dropdown.style.opacity = 1;
        }, 100);
    }

})

window.addEventListener('scroll', () => {
    let currentScrollPos = window.pageYOffset;

    if(currentScrollPos > 30){
        nav.style.backgroundColor = 'black';
        nav.style.height = '70px';
        logo.style.transform = 'scale(0.8)';
        dropdown.style.top = '0px';
    }
    else {
        nav.style.backgroundColor = 'transparent';
        nav.style.height = '100px';
        dropdown.style.top = '-30px';
        logo.style.transform = 'scale(1)';
    }        
});