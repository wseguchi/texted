$(document).ready(function() {

});

function pageScroll(id) {
	$("html, body").animate({
		scrollTop: $(id).offset().top
	}, 800);
}

function selectMode(value) {
	if (value == 'readability') {
		document.getElementById('inlineCheckbox').checked = false;
		document.getElementById('inlineCheckbox').setAttribute('value', 'readability');
		document.getElementById('main-input-selector-options-readability').classList.add('input-selector-active');
		document.getElementById('main-input-selector-options-similarity').classList.remove('input-selector-active');
		$("#main-input-selector-2").fadeIn().css("display", "flex");
		$("#main-input-selector-3").fadeIn().css("display", "flex");
		$("#main-input-textbox-2").fadeOut();
	} else if (value == 'similarity') {
		document.getElementById('inlineCheckbox').checked = true;
		document.getElementById('inlineCheckbox').setAttribute('value', 'similarity');
		document.getElementById('main-input-selector-options-readability').classList.remove('input-selector-active');
		document.getElementById('main-input-selector-options-similarity').classList.add('input-selector-active');
		$("#main-input-selector-2").fadeIn().css("display", "flex");
		$("#main-input-selector-3").fadeIn().css("display", "flex");
		$("#main-input-textbox-2").fadeIn();
	} else {
		alert('Sorry... something went wrong!');
	};

}

function changeMethodVisibility(option) {
	if (option == 'readability') {
		$('#method-text-readability').fadeIn();
		$("#method-text-similarity").hide();
		document.getElementById('method-title-readability').classList.remove('mt-inactive');
		document.getElementById('method-title-similarity').classList.add('mt-inactive');
		document.getElementById('method-title-span-readability').classList.add('ed');
		document.getElementById('method-title-span-similarity').classList.remove('ed');
	} else {
		$('#method-text-readability').hide();
		$("#method-text-similarity").fadeIn();
		document.getElementById('method-title-readability').classList.add('mt-inactive');
		document.getElementById('method-title-similarity').classList.remove('mt-inactive');
		document.getElementById('method-title-span-readability').classList.remove('ed');
		document.getElementById('method-title-span-similarity').classList.add('ed');
	}
}


function checkSubmitFunction() {
	// check if the box is empty
	var input01 = false;
	var input02 = false;

	// check mode (readability or similarity)
	if (document.getElementById('inlineCheckbox').value === "") {
		$("#warning-option").fadeIn();
		$("html, body").animate({
			scrollTop: $('#main-input-selector-1').offset().top
		}, 800);
	}

	// check text-area 01
	if (document.getElementById('text-input-form-01').value === "") {
		$("#warning-textbox-1").fadeIn();
		$("html, body").animate({
			scrollTop: $('#main-input-selector-2').offset().top
		}, 800);
		input01 = false;
	} else {
		input01 = true;
		$("#warning-textbox-1").fadeOut();
	}

	// check text-area 02
	if (document.getElementById('inlineCheckbox').checked) {
		if (document.getElementById('text-input-form-02').value === "") {
			$("#warning-textbox-2").fadeIn();
			$("html, body").animate({
				scrollTop: $('#main-input-selector-2').offset().top
			}, 800);
			input02 = false;
		} else {
			input02 = true;
			$("#warning-textbox-2").fadeOut();
		}
	} else {
		input02 = true;
	}

	if ((document.getElementById('inlineCheckbox').checked) && (document.getElementById('text-input-form-01').value === document.getElementById('text-input-form-02').value)) {
		$("#warning-identical-texts").fadeIn();
		$("html, body").animate({
			scrollTop: $('#main-input-selector-2').offset().top
		}, 800);
		input01 = false;
	} else {
		$("#warning-identical-texts").fadeOut();
	}

	if (input01 && input02) {
		return true;
	} else {
		return false;
	}
}