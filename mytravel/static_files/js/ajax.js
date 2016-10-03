$(function(){
	$('$search').keyup(function(){
		$.ajax({
			type: 'POST',
			url: "/songs/search",
			data: {
				'search_text':$('#search').val(),
				'crsfmiddlewaretoken': $("input[name=crsfmiddlewaretoken]").val()
			},
			success:searchSuccess,
			dataType:'html'
		});
			});
});
		
