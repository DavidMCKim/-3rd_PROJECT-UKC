camping_image
$(document).ready(function(){
        $('.camping_image').each(function(index){
        $(this).hover(
            function(){
                $(this).animate({marginTop:'-30px'},'slow');
            },
            function(){
                $(this).animate({marginTop:'0px'},'slow')
            });
        });
    });
});

