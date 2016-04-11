$(document).ready(function() {
	var handPhoneLeft;
	var handPhoneTop;
	var x;
	var y;
	$('header .overlay, header .container').mousemove(function(event) {
		x = event.clientX;
		y = event.clientY;


		handPhoneLeft = x/16 - 45;

		handPhoneTop = y/16 - 50;


		$('.hand-phone').css('left', -handPhoneLeft + 'px');
		$('.hand-phone').css('top', -handPhoneTop + 'px');
	});

	$(window).scroll(function() {
		if ( $(window).scrollTop() > $('.advantages').offset().top - window.innerHeight + 300 ) {
			$('.three-in-one, .adv-item.diary, .adv-item.psychologist, .adv-item-big.trainer , .vertical-line, .horizontal-line').addClass('animation');
		}

		if ( $(window).scrollTop() > $('.fourth-screen').offset().top - window.innerHeight + 600 ) {
			$('.screen, .diary-category').addClass('show');
		}

		if ( $(window).scrollTop() > $('.sixth-screen').offset().top - window.innerHeight + 600 ) {
			$('.sixth-screen .app-category-thumb, .trainer-category').addClass('show');
		}

		if ( $(window).scrollTop() > $('.eighth-screen').offset().top - window.innerHeight + 600 ) {
			$('.eighth-screen .app-category-thumb, .psych-category').addClass('show');
		}

	});

	$('.scroll-to').click(function(event) {
		var scrollTo = $(this).attr('data-scroll');
		console.log(scrollTo);
		$('html, body').animate({	scrollTop : $(scrollTo).offset().top }, 500);
		return false;
	});

	$('.modal-open').click(function(event) {
		event.preventDefault();
		var modalWindow = $(this).attr('data-modal');
		$('.modal-overlay').addClass('show');
		$(modalWindow).addClass('show');
	});

	$('.modal-close').click(function(event) {
		event.preventDefault();
		$(this).parent('.modal').removeClass('show');
		$('.modal-overlay').removeClass('show');
	});
});