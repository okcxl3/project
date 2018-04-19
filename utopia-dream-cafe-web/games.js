//mobile menu//
var menu_icon = $("#menu_icon")[0];
var menu = $("#mobile_menu")[0];
var clicked = false;
var sitewrapper = document.getElementById("sitewrapper");

$("#menu_icon").click(function(){
	if (clicked){
		menu_icon.style.transform = "rotate(0)";
		clicked=false;
		$("#mobile_menu").animate({width:"0vw"},500);
		$("#firstlayer_background")[0].style.webkitFilter="brightness(0.75) grayscale(0.5) contrast(1.1)";
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