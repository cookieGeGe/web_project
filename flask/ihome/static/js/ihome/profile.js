function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function () {
        setTimeout(function () {
            $('.popup_con').fadeOut('fast', function () {
            });
        }, 1000)
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


// $('#form-avatar').submit(function () {
//     var fileobj = $('#avatar').files[0]
//     var formdata = new FormData()
//     formdata.append('file', fileobj)
//     // alert(fileobj)
//     $.ajax({
//         url: '/user/profile/',
//         type: 'POST',
//         data: fromdata,
//         dataType: 'file',
//         contentType: false,
//         // processData: false,
//         success: function (data) {
//             // alert(data.img_url)
//             if (data.code = 200) {
//                 $('#user-avatar').attr('src', data.img_url)
//             }
//         },
//         error: function (data) {
//             alert(data.msg)
//         }
//
//     })
// })

// 也可以用function(e)

// e.preventDefault()阻止默认行为



$('#form-avatar').submit(function () {

    $(this).ajaxSubmit({
        url:'/user/profile/',
        type:'PUT',
        dataType:'json',
        success:function (data) {
            if (data.code=='200'){
                $('#user-avatar').attr('src', data.img_url)
            }
        },
        error:function (data) {
            alert('上传头像失败')
        }
    });
    return false;
})




$('#form-name').submit(function (e) {
    e.preventDefault()
    $('.error-msg').hide()
    var name = $('#user-name').val()
    $.ajax({
        url: '/user/profile/name/',
        type: 'POST',
        dataType: 'json',
        data: {'name': name},
        success: function (data) {
            if (data.code == '200') {
                showSuccessMsg()
            }else{
                $('.error-msg').html('<i class="fa fa-exclamation-circle">用户名已存在，请重新设置</i>')
                $('.error-msg').show()
            };
        },
        error: function (data) {
            alert(data.msg)
        }
    })
})

