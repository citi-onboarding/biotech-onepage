const bannerBackgrounds = document.querySelectorAll('.banner-content img');

window.addEventListener('scroll', e => {
    let scrolled = window.pageYOffset;

    bannerBackgrounds.forEach(banner => {
        banner.style.width = `${100 + 0.01*scrolled}%`;
    });
});