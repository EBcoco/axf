$(function () {

    // console.log('home')
    $('.home').width(innerWidth)

    var topswiper = new Swiper('#top-swiper', {
        pagination: '.swiper-pagination',
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        loop: true,
        autoplay : 3000,
    });
    var mustbuySwiper = new Swiper('#mustbuySwiper', {
        pagination: '.swiper-pagination',
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 30,
        loop: true,
        autoplay : 3000,
    });
})