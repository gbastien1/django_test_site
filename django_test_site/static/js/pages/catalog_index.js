(function($, undefined) {
	
	'use strict';
	
	var changeSelectedItem = function() {
		var t = $(this);
		if (!t.hasClass('selected')) {
			var id = t.attr('data-id');
			
			$('.category-item.selected').removeClass('selected');
			t.addClass('selected');
			
			$('.category-description.selected').removeClass('selected');
			$('.category-description').filter('[data-id=' + id + ']').addClass('selected');
		}
	};
	
	var init = function () {
		$('.category-item').on('click', changeSelectedItem);
	};
	
	$(window).ready(function () {
		init();
	});
	
})(jQuery);
