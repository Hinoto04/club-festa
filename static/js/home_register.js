$("input#username").change(function() {
    console.log('changed');
});

function check() {
    $.ajax({
        url:'/checkid?username='+$("#username").val(),
        type:'get',
        dataType:'json',
        success:function(response) {
            if(response.result != 'success') {
                console.error(response.data);
                return;
            }
            if(response.data == 'exist') {
                alert("존재하는 아이디입니다.");
                return;
            } else {
                alert("사용 가능한 아이디입니다.");
                return;
            }
        },
        error:function(xhr, error) {
            alert("통신 오류입니다.");
            return;
        }
    });
}