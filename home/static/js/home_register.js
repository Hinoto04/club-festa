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
            var idcheckp = document.getElementById('idcheck');
            if(response.data == 'exist') {
                idcheckp.innerHTML = "사용할 수 없는 아이디입니다.";
                return;
            } else {
                console.log('yes');
                idcheckp.innerHTML = "사용할 수 있는 아이디입니다.";
                return;
            }
        },
        error:function(xhr, error) {
            alert("통신 오류입니다.");
            return;
        }
    });
}