function SendEmail() {
		User_Email = $('#input_email').val();
		$.ajax({
			url:"/send_email",
			data:{
				'user_email':User_Email
			},
			type:"GET",
			async:false,
			success:function(result) {
				if(result=='1'){
					$("#Send_Status").html("Succeed");
					$("#Send_Status").css("color","green")
				}else{
					$("#Send_Status").html("Failed");
					$("#Send_Status").css("color","red")
					confirm("Send Failed,Please contact system administrator.")
				}

			},
			error:function(e){
				confirm("Send Failed,Please contact system administrator.")
            }
		});
}