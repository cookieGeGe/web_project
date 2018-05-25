function subshop(goodid) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app/subcart/',
        type: 'POST',
        data: {'goodid': goodid},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            $('#num_' + goodid).html(msg.c_num)
            // alert(goodid)
        },
        error: function (msg) {
            alert('请求失败')
        }
    })
}

function addshop(goods_id) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    // alert(csrf)
    // alert(goods_id)
    $.ajax({
        url: '/app/addcart/',
        type: 'POST',
        headers: {'X-CSRFToken': csrf},
        data: {'goodsid': goods_id},
        dataType: 'json',
        success: function (msg) {
            $('#num_' + goods_id).html(msg.c_num)
        },
        error: function (msg) {
            alert('请求错误')
        }
    })
}

function subselect(cartid) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app/subselect/',
        type: 'POST',
        data: {'cartid': cartid},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            $('#num_' + cartid).html(msg.c_num)
        },
        error: function (msg) {
            alert('请求失败')
        }
    })
}

function addselect(cartid) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app/addselect/',
        type: 'POST',
        data: {'cartid': cartid},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            $('#num_' + cartid).html(msg.c_num)
        },
        error: function (msg) {
            alert('请求失败')
        }
    })
}


function changestatus(cartid) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app/changestatus/',
        type: 'POST',
        data: {'cartid': cartid},
        headers: {'X-CSRFToken': csrf},
        dataType: 'json',
        success: function change(msg) {
            if (msg.is_delete) {
                s = '<span onclick="changestatus(' + cartid + ')">X</span>'
            } else {
                s = '<span onclick="changestatus(' + cartid + ')">√</span>'
            }
            $('#span_' + cartid).html(s)
        },
        // alert('请求成功')
        error: function (msg) {
            alert('请求失败')
        }
    })
}

function changeall(istrue) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app/changeall/',
        type: 'POST',
        dataType: 'json',
        data: {'istrue': istrue},
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            location.reload()

        },
        error: function (msg) {
            alert('请求错误')
        }
    })
}

function orderpay(orderid) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    // alert(orderid)
    $.ajax({
        url: '/app/pay/'+orderid+'/',
        type: 'POST',
        dataType: 'json',
        data: {'orderid': orderid},
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            window.location.href = msg.urls
        },
        error: function (msg) {
            alert('请求错误')
        }
    })
}

function confirm_rec(order_id) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    // alert(orderid)
    $.ajax({
        url: '/app/confirm_rec/',
        type: 'POST',
        dataType: 'json',
        data: {'orderid': order_id},
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            location.reload()
        },
        error: function (msg) {
            alert('请求错误')
        }
    })
}