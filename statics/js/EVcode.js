function SendEmail() {
		User_Email = $('#input_email').val();
		//console.log("User_Email"+User_Email);
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
		//$("#home").append(str);
}