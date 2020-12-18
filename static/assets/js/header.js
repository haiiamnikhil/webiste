// function openNav() {
//     let nav = document.getElementById('mobile-nav');
//     let navclass = $('.sidemenu-opened');
//     if(navclass.length > 0) {
//         $('#mobile-nav').removeClass('sidemenu-opened');
//         document.getElementById("mobile-nav").style.width = "0px";
//     }
//     else{
//         $('#mobile-nav').addClass('sidemenu-opened');
//         document.getElementById("mobile-nav").style.width = "250px";
//     }
//   }

//   $(document).ready(function(){
//       $('.dropdown-toggle').hover(function(){
//         $(this).dropdown();
//       })
//   });

//   


// Header Sticky
function stickyFunction() {
	var header = document.getElementById("site-header");
	var sticky = header.offsetHeight;
	if (window.pageYOffset > 0) {
		header.classList.add("fixed");
	} else {
		header.classList.remove("fixed");
	}
}

 
$(document).ready(function(){
	var w_width = $( window ).width();
	
	/*Menu toggle Button*/
	$('.nav-button').click(function() {
		$('body').toggleClass('show_menu');
		$('.nav-wrap ul.top_nav').slideToggle();
	});

	/*Append down-arrow Span*/
	$('ul.top_nav > li:has(ul)').addClass('has-submenu').append('<span class="down-arrow"></span>');
    $('li.has-submenu ul > li:has(ul)').addClass('has-submenu').append('<span class="down-arrow"></span>');



    $("ul.top_nav li span.down-arrow").on("click",function(e){
        
		if($(this).parents(".has-submenu").hasClass("submenu-active") && (!($(this).parent().hasClass("submenu-active")) ) ){ 
			$(this).parent().siblings().removeClass("submenu-active");
			$(this).parent().addClass("submenu-active");
			$(this).parent().siblings(".has-submenu").children(".sub-nav").slideUp(400);
            $(this).siblings(".sub-nav").slideDown(400); 
            $(this).toggleClass("down");
		}	
		else if($(this).parents(".has-submenu").hasClass("submenu-active") && $(this).parent().hasClass("submenu-active")){
			$(this).parent().removeClass("submenu-active");
			$(this).siblings(".sub-nav").slideUp(400); 
		} 
		else{
			$(".has-submenu > .title").parent().removeClass("submenu-active");
			$(this).parent().addClass("submenu-active");
			$(".has-submenu > .sub-nav").slideUp(400);
			$(this).siblings(".sub-nav").slideDown(400);
		}
	});
	

})

$(window).resize( function(){
	var w_width = $( window ).width();
	if(w_width > 919){
		$('.nav-wrap ul.top_nav').show();			
		$('.nav-wrap ul.top_nav ul').removeAttr("style");;			
	}

});

