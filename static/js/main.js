// window.addEventListener('load', () => {
    
// });

// Banner Slick

// const bannerCarousel = document.querySelector('#banner-carousel');

// bannerCarousel.slick({
//     dots: true,
//     infinite: true,
//     speed: 500,
//     autoplay: true,
//     autoplaySpeed: 2000,
//     fade: true,
//     cssEase: 'linear'
// });

$(document).ready(function () {
    console.log('Made with code and love by CITi');

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
});