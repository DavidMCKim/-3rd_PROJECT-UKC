
  $(document).ready(function(){

    var btn = $(".tag_btn02")
    $('.tag_btn02').click(funcion() {
      var value = $('.tag_btn').val()
      $.ajax({
            type: "GET",
            url: "{% url home_1 %}",
            data: {'infos':infos}, // serializes the form's elements.
            datatype: 'Json',
            success: function(data)  // 서버로 ajax 요청 후 실행된 결과값을 반환 후 발생되는 이벤트
            {
               var list = $('#list').val(data);
               alert(list);
            }
          });
    });

  });

