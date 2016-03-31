$(document).ready(function(){
	var longitude = "";
	var latitude = "";
	$("#submit").click(function()
	{ 
	$.ajax({       
			console.log('ajax')
			url : "site/activite/"+ $('#commune').val(),       
			type : 'GET',       
			dataType : 'json',      
			success : function(data){
	        	$("ul").html("");
	        	$.each(data, function(index, element) {
	        		var tst = "<li>"+JSON.stringify(element[0])+"</li>";
		            $("ul").append(tst);
		        });

	   		 },
	   		 error: function() {
	   		 	alert("Erreur");
	   		 },
		});  
 	});

 	$("#submitCartes").click(function()
	{ 
	$.ajax({       
			url : "site/activite/"+ $('#commune').val()+"/"+$('#carte').val(),       
			type : 'GET',       
			dataType : 'json',      
			success : function(data){
	        	$("ul").html("");
	        	$.each(data, function(index, element) {
	        		longitude = JSON.stringify(element[0]);
	        		latitude = JSON.stringify(element[1]);
	        		var tst = "<li>"+JSON.stringify(element[0])+"</li>";
		            $("ul").append(tst);
		        });

	   		 },
	   		 error: function() {
	   		 	alert("Erreur");
	   		 },
		});  
 	});






})