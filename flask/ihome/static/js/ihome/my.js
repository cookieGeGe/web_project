function logout() {
    $.get("/user/logout/", function (data) {
        if (data.code == '200') {
            location.href = "/user/login/";
        }
    })
}

$(document).ready(function () {

    $.ajax({
        url: '/user/user_info/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // alert('a')
            if (data.code = 200) {
                $('#user-avatar').attr('src', data.user.avatar)
                $('#user-name').text(data.user.name)
                $('#user-mobile').text(data.user.phone)
            }
        },
        error:function (data) {
            alert(data.msg)
        }
    })


})