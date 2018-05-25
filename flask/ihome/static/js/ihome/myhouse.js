$(document).ready(function () {
    // $(".auth-warn").show();

    $.get('/house/auth/', function (data) {
        if (data.code == '200') {
            $('.auth-warn').hide();
            $('.new-house').show();
        } else {
            $('.auth-warn').show();
            $('.new-house').hide();
        }
    });
    $.get('/house/auth_house/', function (data) {
        if (data.code) {
            s = '';
            for (var i = 0; i < data.house_list.length; i++) {
                s += '<li>';
                s += '<a href="/house/detail/?id=' + data.house_list[i].id + '">';
                s += '<div class="house-title">';
                s += '<h3>房屋ID:' + data.house_list[i].id + ' —— ' + data.house_list[i].title + '</h3>';
                s += '</div><div class="house-content">';
                s += '<img src="' + data.house_list[i].image + '">';
                s += '<div class="house-text"><ul>';
                s += '<li>位于：' + data.house_list[i].area + '</li>';
                s += '<li>价格：￥' + data.house_list[i].price + '/晚</li>';
                s += '<li>发布时间：' + data.house_list[i].create_time + '</li>';
                s += '</ul></div></div></a></li>';
            };
            $('#houses-list').append(s);
        }

    })
})


//
//
//
//
//
//
//
//
//
//