function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    $('.popup_con').fadeIn('fast');
    $('.popup_con').fadeOut('fast');
    $.get('/house/get_info/', function (data) {
        if (data.code == '200') {
            for (var i = 0; i < data.areas_list.length; i++) {
                $('#area-id').append('<option value="' + data.areas_list[i].id +
                    '">' + data.areas_list[i].name + '</option>')
            };
            s = '';
            for (var i = 0; i < data.facility_list.length; i++) {
                s += '<li><div class="checkbox"><label>'
                s += '<input type="checkbox" name="facility" value="' +
                    data.facility_list[i].id + '">' + data.facility_list[i].name
                s += '</label></div></li>'
            };
            $('.house-facility-list').append(s);
        }
    })


})

// <li><div class="checkbox"><label>
//               <input type="checkbox" name="facility" value="1">无线网络
//          </label></div></li>


$('#form-house-info').submit(function (e) {
    e.preventDefault()
    $('.error-msg').hide()
    $(this).ajaxSubmit({
        url:'/house/newhouse/',
        type:'POST',
        dataType:'json',
        success:function (data) {
            if (data.code=='200'){

                $('#form-house-info').hide()
                $('#form-house-image').show()
                $('#house-id').attr('value', data.houseid)
            } else {
                $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>请将全部信息填写完整后再提交')
                $('.error-msg').show()
            }
        },
        error:function (data) {
            alert('添加房源信息失败')
        }
    })
})



$('#form-house-image').submit(function (e) {
    e.preventDefault()
    $(this).ajaxSubmit({
        url:'/house/newhouse/',
        type:'PUT',
        dataType:'json',
        success:function (data) {
            if (data.code=='200'){
                s = '<img src="'+ data.imgurl +'">'
                $('.house-image-cons').append(s)
            }
        },
        error:function (data) {
            alert('上传头像失败')
        }
    });
    return false;
})

