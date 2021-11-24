/*버튼 누르면 색깔바꾸기*/
var menuLinks = document.querySelectorAll('.tag_btn');

function clickMenuHandler(){
    var activeMenu = document.querySelector('.menu-active');  /* querySelector 자체가 dom을 다 뒤져야 되므로 이것도 비효율적이라고 할 수 ㅇ..dom에 의존적 */
    if (activeMenu){
        activeMenu.classList.remove('menu-active');
    }
    this.classList.add('menu-active');
}

for (var i = 0; i < menuLinks.length; i++){
    menuLinks[i].addEventListener('click', clickMenuHandler);
}



/*버튼 초기화*/
$(document).ready(function(){
    //btn_reset 을 클릭했을때의 함수
    $("#reset").click(function () {
        $("#button_table").each( function () {
            this.reset();
        });
    });
});


