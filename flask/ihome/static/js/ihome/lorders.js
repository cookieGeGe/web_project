//模态框居中的控制
function centerModals() {
    $('.modal').each(function (i) {   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top - 30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);

    $.get('/order/cus_orders/', function (data) {
        var orders_temp = template('lorders', {orders: data.lorders})
        $('.orders-list').append(orders_temp)
        $(".order-accept").on("click", function () {
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-accept").attr("order-id", orderId);
        });
        $(".order-reject").on("click", function () {
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-reject").attr("order-id", orderId);
        });


    });
    $(".modal-accept").click(function (e) {
        var id = $(this).attr('order-id')
        $.ajax({
            url: '/order/lorder/' + id + '/',
            type: 'PATCH',
            dataType: 'json',
            data: {'id': id, 'status': 'WAIT_PAYMENT'},
            success: function (data) {
                if (data.code == '200') {
                    $("body").attr('class','');
                    $('#accept-modal').attr({'style': 'display:none', 'class': 'modal fade'});
                    $('.modal-backdrop').hide()
                    $('#btn_' + id).hide()
                    $('#span_order_' + id).html('待支付')
                }
            }
        })
    });



    $(".modal-reject").click(function (e) {
        var id = $(this).attr('order-id')
        $.ajax({
            url: '/order/lorder/' + id + '/',
            type: 'PATCH',
            dataType: 'json',
            data: {'id': id, 'status': 'REJECTED', 'rejected': $('#reject-reason').val()},
            success: function (data) {
                if (data.code == '200') {
                    $("body").attr('class','');
                    $('#reject-modal').attr({'style': 'display:none', 'class': 'modal fade'});
                    $('.modal-backdrop').hide()
                    // $('#reject-modal').modal('hide')
                    $('#btn_' + id).hide()
                    $('#span_order_' + id).html('已拒绝')
                }
            }
        })
    });


});