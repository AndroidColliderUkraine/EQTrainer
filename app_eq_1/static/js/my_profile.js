/*Menu-toggle*/
$(document).ready(function(){
	var page = $("#temp_page").val();

	$( ".temp_page_class").remove();
	if (page){
		$("#" + page).after('<i class="temp_page_class fa fa-check pull-right" aria-hidden="true"></i>');
	}
	
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("active");
    });
});