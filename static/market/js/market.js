$(function () {
    $('.market').width(innerWidth)

    var typeIndex=$.cookie('typeIndex')
    if (typeIndex) {
        $('.type-slider .type-item').eq(typeIndex).addClass("active")
    }else {
        $('.type-slider .type-item').eq(0).addClass("active")

    }

    $('.type-slider .type-item').click(function () {

        // $(this).addClass('active')

        $.cookie('typeIndex',$(this).index(),{expires:3,path:'/'})
    })
})