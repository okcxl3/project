//mobile menu//
var menu_icon = $("#menu_icon")[0];
var menu = $("#mobile_menu")[0];
var clicked = false;

$("#menu_icon").click(function(){
	if (clicked){
		menu_icon.style.transform = "rotate(0)";
		clicked=false;
		$("#mobile_menu").animate({width:"0vw"},500);
		$("#firstlayer_background")[0].style.webkitFilter="brightness(0.55) grayscale(1) contrast(1.1)";
		$("body,html").css("overflow","visible");
	}
	else{
		menu_icon.style.transform = "rotate(90deg)";
		clicked=true;
		$("#mobile_menu").animate({width:"65vw"},500);
		$("#firstlayer_background")[0].style.webkitFilter="brightness(0.4) grayscale(0.7)";
		menu.style.zIndex="999";
		$("body,html").css("overflow","hidden");
	}
})

$(window).resize(function(){
	
	if(($(window).width()> 767) && clicked){
		$("#firstlayer_background")[0].style.webkitFilter="brightness(0.8) grayscale(0.2) contrast(1.1)";
	}
	
	else if(($(window).width()< 768) && clicked){
		$("#firstlayer_background")[0].style.webkitFilter="brightness(0.4) grayscale(0.7)";
	}

});

//mobile menu//

//ajax//
$("form").submit(function(event){
	event.preventDefault();
	var info = $(this).serialize();
	$(".error").remove();
	$("#firstname").css("border-color","rgb(204, 204, 204)");
	$("#lastname").css("border-color","rgb(204, 204, 204)");
	$("#formemail").css("border-color","rgb(204, 204, 204)");
	$("#formmessage").css("border-color","rgb(204, 204, 204)");
	$.post("contact_form.php",info,callback);
});

function callback(response){
	if(response == ""){
		$("#myform").html("<h4>Thank you</h4>");
	}
	else{
		response = JSON.parse(response);
		if(response.name_error != ""){
			$("#myname").before(response.name_error);
			$("#firstname").css("border-color","red");
			$("#lastname").css("border-color","red");
		}
		if(response.email_error != ""){
			$("#email").before(response.email_error);
			$("#formemail").css("border-color","red");
		}
		if(response.message_error != ""){
			$("#message").before(response.message_error);
			$("#formmessage").css("border-color","red");
		}
	}
}