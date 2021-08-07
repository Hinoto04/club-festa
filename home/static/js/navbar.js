function setCookie(cname,cvalue,exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

window.onload = function() {
    console.log(getCookie('account'));
    var dropdown = document.getElementById('myPage');
    if (getCookie('account') == '3') {
        dropdown.innerHTML = '\
        <a class="dropdown-item" href="#">마이페이지</a>\
        <a class="dropdown-item" href="#">동아리 관리</a>\
        <a class="dropdown-item" href="#">행사 관리</a>';
    } else {
        dropdown.innerHTML = '<a class="dropdown-item" href="/login">로그인</a>'
    }
}