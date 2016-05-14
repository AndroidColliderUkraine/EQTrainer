/*Menu-toggle*/
$(document).ready(function(){
	console.log('Test my sss');
	var page = $("#temp_page").val();

	$( ".temp_page_class").remove();
	if (page){
		$("#" + page).after('<i class="temp_page_class fa fa-check pull-right" aria-hidden="true"></i>');
	}

	console.log('Test my sss' + page);
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("active");
    });
});