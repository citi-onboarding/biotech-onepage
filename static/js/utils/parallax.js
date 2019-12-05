const bannerBackgrounds = document.querySelectorAll('.banner-content img');

console.log(bannerBackgrounds);

window.addEventListener('scroll', e => {
    let scrolled = window.pageYOffset;

    bannerBackgrounds.forEach(banner => {
        // banner.style.top = -(scrolled * 0.00001) + 'px';
        banner.style.width = `${100 + 0.01*scrolled}%`;
    });
});