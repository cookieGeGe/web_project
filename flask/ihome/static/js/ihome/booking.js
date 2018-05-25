function hrefBack() {
    history.go(-1);
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function decodeQuery() {
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function (result, item) {
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

function showErrorMsg() {
    $('.popup_con').fadeIn('fast', function () {
        setTimeout(function () {
            $('.popup_con').fadeOut('fast', function () {
            });
        }, 1000)
    });
}

$(document).ready(function () {
    $(".input-daterange").datepicker({
        format: "yyyy-mm-dd",
        startDate: "today",
        language: "zh-CN",
        autoclose: true
    });
    $(".input-daterange").on("changeDate", function () {
        var startDate = $("#start-date").val();
        var endDate = $("#end-date").val();

        if (startDate && endDate && startDate > endDate) {
            showErrorMsg();
        } else {
            var sd = new Date(startDate);
            var ed = new Date(endDate);
            days = (ed - sd) / (1000 * 3600 * 24) + 1;
            var price = $(".house-text>p>span").html();
            var amount = days * parseFloat(price);
            $(".order-amount>span").html(amount.toFixed(2) + "(共" + days + "晚)");
        }
    });
})

$(document).ready(function () {
    var path = location.href.split('=')[1];
    $.get('/house/books/' + path + '/', function (data) {
        if (data.code == '200') {
            var temp_book = template('temph', {mhouse:data.house});
            $('.house-info').append(temp_book);
        };

    });
})

$('.submit-btn').click(function () {
    var id = location.href.split('=')[1]
    var start_time = $('#start-date').val()
    var end_time = $('#end-date').val()
    $.ajax({
        url:'/order/',
        dataType:'json',
        type:'POST',
        data:{'id':id,'start_date':start_time,'end_date':end_time},
        success:function (data) {
            if (data.code=='200'){
                location.href='/order/myorder/'
            }
        }
    })



})