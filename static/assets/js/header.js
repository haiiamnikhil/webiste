function openNav() {
    let nav = document.getElementById('mobile-nav');
    let navclass = $('.sidemenu-opened');
    if(navclass.length > 0) {
        $('#mobile-nav').removeClass('sidemenu-opened');
        document.getElementById("mobile-nav").style.width = "0px";
    }
    else{
        $('#mobile-nav').addClass('sidemenu-opened');
        document.getElementById("mobile-nav").style.width = "250px";
    }
  }

  $(document).ready(function(){
      $('.dropdown-toggle').hover(function(){
        $(this).dropdown();
      })
  });