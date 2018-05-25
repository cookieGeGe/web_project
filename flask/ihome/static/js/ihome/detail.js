function hrefBack(e) {
    e.preventDefault()
    window.location.href = '/house/newhouse/';
}

function decodeQuery() {
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function (result, item) {
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function () {
    $(".book-house").show();
    var house_id = location.href.split('=')[1]
    $.ajax({
        url: '/house/details/',
        type: 'GET',
        dataType: 'json',
        data: {'id': house_id},
        success: function (data) {
            var detail_tem = template('tempsc', {mhouse: data.house});
            $('.container').append(detail_tem);

            if(data.is_self){
                $('.book-house').hide();
            }
            $('.book-house').attr('href','/house/book/?id=' + house_id);
            var mySwiper = new Swiper('.swiper-container', {
                loop: true,
                autoplay: 2000,
                autoplayDisableOnInteraction: false,
                pagination: '.swiper-pagination',
                paginationType: 'fraction'
            })
        }
    })


})