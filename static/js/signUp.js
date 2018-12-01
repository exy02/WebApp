$(document).ready(function(){

	$("#btnSignUp").click(function(){

		$.ajax({
			type: "POST",
			url: "/signUp",
			data: $("form").serialize(),
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		})

		.done(function(data){
			if (data.message) {
				$("#successAlert").text(data.message).show();
				$("#errorAlert").hide();
			}
			else if (data.error) {
				$("#errorAlert").text(data.error).show();
				$("#successAlert").hide();
			}
		});

	});
	
});
