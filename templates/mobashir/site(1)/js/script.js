/* =====================================
	Prelaoder
=====================================*/

$(window).on('load', function () {
	$('#status').fadeOut();
	$('#preloader').fadeOut();
});

/* =====================================
	Navigation
=====================================*/

$(function () {
	showHideNav ();
	$(window).scroll(function () {
		showHideNav ();
	});
	function showHideNav () {
		if($(window).scrollTop() > 60) {
			$("nav").addClass("navbar-dark");
			$("#back-to-top").fadeIn();
		}
		else {
			$("nav").removeClass("navbar-dark");
			$("#back-to-top").fadeOut();
		}
	}
});

/* =====================================
	Smooth Scroll
=====================================*/

$(function () {
	$("a.smooth-scroll").click(function (event) {
		event.preventDefault();
		var section_id = $(this).attr("href");
		$("html, body").animate({
			scrollTop: $(section_id).offset().top - 64
		}, 1250, "easeInOutExpo");
	})
});

/* =====================================
	Load More Button
=====================================*/

$(function () {
	$(".box-hidden").slice(0, 6).show();
	$("#loadMore").on('click', function(e) {
		e.preventDefault();
		$(".box-hidden:hidden").slice(0, 3).slideDown();
		if ($(".box-hidden:hidden").length == 0) {
			$("#loadMore").fadeOut('slow');
		}
	});
});

/* =====================================
	Mobile Navigation
=====================================*/
$(function () {
	$("#mobile-nav-open-btn").click(function () {
		$("#mobile-nav").css("height", "100%");
	});
	$("#mobile-nav-close-btn, #mobile-nav a").click(function () {
		$("#mobile-nav").css("height", "0%");
	});
});


