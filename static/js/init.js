(function($){
    $(function(){

      $('.button-collapse').sideNav();
      $('.parallax').parallax();

    });

    $("#btnSignUp").click(function() {
        var emailval = $('input#emailInput').val();
        var pwdval = $('input#pwdInput').val();
        console.log(emailval);
        console.log(pwdval);
        if (emailval !== "") {
            $.ajax({
                url: '/signUpButton',
                type: 'POST',
                data: {
                    email: emailval,
                    password: pwdval
                },
                success: function(response) {
                    console.log(response);
                }
            });
        } else {
            alert("Insert a email!");
        }
    });
    // end of document ready
})(jQuery); // end of jQuery name space