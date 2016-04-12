(function($){
    $(function(){

      $('.button-collapse').sideNav();
      $('.parallax').parallax();

    });

    $("#signInButton").click(function() {
        $.ajax({
            url: '/signInPage',
            type: 'GET',
            success: function(response) {
                console.log(response);
                console.log("Made it back to success")
            }
        });
    });
    // end of document ready
})(jQuery); // end of jQuery name space