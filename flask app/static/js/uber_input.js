$(function(){
	$('#btn').click(function(){
		
		$.ajax({
			url: '/',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				// document.location = '/graph'
				console.log("response",response);
				
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
