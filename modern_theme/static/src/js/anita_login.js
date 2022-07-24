window.onload=function() { 
    
    var togglePassword = document.getElementById("toggle-password");
    if (togglePassword) {
        togglePassword.addEventListener('click', function() {
            var x = document.getElementById("password");
            if (x.type === "password") {
                x.type = "text";
            } else {
                x.type = "password";
            }
        });
    }

    $("#show_hide_password a").on('click', function (event) {
        event.preventDefault();
        if ($('#show_hide_password input').attr("type") == "text") {
            $('#show_hide_password input').attr('type', 'password');
            $('#show_hide_password i').addClass("fa-eye-slash");
            $('#show_hide_password i').removeClass("fa-eye");
        } else if ($('#show_hide_password input').attr("type") == "password") {
            $('#show_hide_password input').attr('type', 'text');
            $('#show_hide_password i').removeClass("fa-eye-slash");
            $('#show_hide_password i').addClass("fa-eye");
        }
    });

    // Background Image
	$('.background-image').each(function(){
		$(this).css('background-image', $(this).attr('data-background'));
	});

	// Opacity mask
	$('.opacity-mask').each(function(){
		$(this).css('background-color', $(this).attr('data-opacity-mask'));
	});
} 
