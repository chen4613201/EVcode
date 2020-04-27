function SendEmail() {
		User_Email = $('#input_email').val();
		$.ajax({
			url:"/send_email",
			data:{
				'user_email':User_Email
			},
			timeout:9000,
			type:"POST",
			async:true,
			success:function(result) {
				if(result=='1'){
					$("#Send_Status").html("Succeed");
					$("#Send_Status").css("color","green")
					$("#veriCodeError").hide()
				}else{
					$("#Send_Status").html("Failed");
					$("#Send_Status").css("color","red")
					$("#veriCodeError").show()
					confirm("Send Failed,try again.")
				}
			},
			error:function(e){
				confirm("Send Failed,Please contact system administrator.")
            }
		});
}
