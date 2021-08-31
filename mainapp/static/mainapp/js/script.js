
const isScrolledIntoView = (elem) =>{
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
    var elemBottom = elemTop + $(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}

var av_animated = false;
$(document).ready(() =>{
    setTimeout(()=> av_animated=true, 2005);
    $('[data-toggle="tooltip"]').tooltip({placement : 'bottom' , delay : { "show": 500, "hide": 100 }, html : true});
    $('#Logout').tooltip({placement : 'bottom' , delay : { "show": 500, "hide": 100 }, html : true});
    $('.card-img-top').animate({"opacity" : "1.0"}, 2000);
    $('img.mx-auto')
        .animate({"opacity" : "1.0"}, 2000)
        .on({
            mouseenter : function(){
                if(av_animated){
                    $(this).stop(true, true).animate({opacity : "1.0", width : "41%"});
                }
            },

            mouseleave : function(){
                if(av_animated){
                    $(this).stop(true, true).animate({opacity : "0.95", width : "40%"});
                }
            }
        });
    $(window).on('wheel DOMMouseScroll', (event) => {
        var check = document.querySelector('br')
        if (event.originalEvent.wheelDelta >= 0) {
            /* Scroll up */
            if(!isScrolledIntoView(check)){
                $('nav').stop(true, false).animate({height : "show"});                 
            }
        }
        else {
            /* Scroll down */
            if(!isScrolledIntoView(check)){
                $('nav').stop(true, false).animate({height : "hide"});

            }
        }
    });
    $(".nav-link, .navbar-brand").click(function (){
        $('html, body').animate({
            scrollTop: $($(this).attr("href")).offset().top
        }, 1000);
    });

    $("#Logout").click(function (){
        $(this)
            .text("")
            .html('<span class="spinner-border"></span>');
    });

    $("td img").on({
        mouseenter : function(){
            $(this).stop(true, true).css({
                width: "9vh",
                "-webkit-animation" : "rotate_l 0.6s ease-in-out",
                "-moz-animation" : "rotate_l 0.6s ease-in-out",
                animation : "rotate_l 0.6s ease-in-out",
            });
        },

        mouseleave : function(){
            $(this).stop(true, true).css({
                "-webkit-animation" : "rotate_r 0.6s ease-in-out",
                "-moz-animation" : "rotate_r 0.6s ease-in-out",
                animation : "rotate_r 0.6s ease-in-out",
                width: "8vh"
            });
        }
    });      
});  
