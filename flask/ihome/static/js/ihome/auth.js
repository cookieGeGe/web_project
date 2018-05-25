function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$('#form-auth').submit(function (e) {
    e.preventDefault()
    var name = $('#real-name').val()
    var card = $('#id-card').val()

    $.ajax({
        url:'/user/userauth/',
        type:'POST',
        dataType:'json',
        data:{'real-name':name,'id-card':card},
        success:function (data) {
            if (data.status.code=200){
                $('#real-name').val(data.real_name)
                $('#real-name').attr('disabled',"disabled")
                $('#id-card').val(data.card)
                $('#id-card').attr('disabled','disabled')
                $('.btn-success').hide()
                $('.error-msg').hide()
            }else{
                $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>'+ data.msg)
                $('.error-msg').show()
            }
        },
        error:function (data) {
            alert('修改用户信息失败')
        }
    })
})


$(document).ready(function () {
    $.ajax({
        url:'/user/realinfo/',
        type:'GET',
        dataType:'json',
        success:function (data) {
            if (data.status.code=200){
                $('#real-name').val(data.real_name)
                $('#real-name').attr('disabled',"disabled")
                $('#id-card').val(data.card)
                $('#id-card').attr('disabled',"disabled")
                $('.btn-success').hide()
            }
        },
        error:function (data) {
            // alert(data)
        }
    })
})