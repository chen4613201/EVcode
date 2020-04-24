function SendEmail() {
		User_Email = $('#input_email').val();
		$.ajax({
			url:"/send_email",
			data:{
				'user_email':User_Email
			},
			type:"POST",
			async:false,
			success:function(result) {
				console.log(result);
				str = result;
			},
			error:function(e){
                console.log(e.status);
                console.log(e.responseText);
            }
		});
}