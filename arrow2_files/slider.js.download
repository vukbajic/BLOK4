// Title: tigra slider control
// Description: See the demo at url
// URL: http://www.softcomplex.com/products/tigra_slider_control/
// Version: 1.1 (commented source)
// Date: 08/28/2012
// Tech. Support: http://www.softcomplex.com/forum/
// Notes: This script is free. Visit official site for further details.
// Simplified by www.ResizeImage.net

function slider (a_init, a_tpl, a_update, div_parent ) {

	this.Enable = Enable;
	this.f_setValue  = f_sliderSetValue;
	this.f_getPos    = f_sliderGetPos;
	this.f_updateValue = a_update;
	
	// register in the global collection	
	if (!window.A_SLIDERS) window.A_SLIDERS = [];
	var n_id = this.n_id = window.A_SLIDERS.length;
	window.A_SLIDERS[n_id] = this;

	// save config parameters in the slider object
	var s_key;
	if (a_tpl)
		for (s_key in a_tpl)
			this[s_key] = a_tpl[s_key];
	for (s_key in a_init)
		this[s_key] = a_init[s_key];

	this.n_pix2value = this.n_pathLength / (this.n_maxValue - this.n_minValue);
	if (this.n_value == null)
		this.n_value = this.n_minValue;

	$get( div_parent ).innerHTML =	'<div style="position:relative; width:' + this.n_controlWidth + 'px;height:' + this.n_controlHeight + 'px;border:0;' +  '" id="sl' + n_id + 'base">' +	'<img src="' + this.s_imgControl + '"' + 'id="btmimg' + n_id + '"' + 
		  'width="' + this.n_controlWidth + '" height="' + this.n_controlHeight + '" border="0" style="position:absolute;left:0;">' +	'<img src="' + this.s_imgSlider + '" width="' + this.n_sliderWidth + '" height="' + this.n_sliderHeight + '" border="0" style="position:absolute;left:' + this.n_pathLeft + 'px;top:' + this.n_pathTop + 'px;z-index:' + this.n_zIndex + ';cursor:pointer;visibility:hidden;" name="sl' + n_id + 'slider" id="sl' + n_id + 'slider" onmousedown="return f_sliderMouseDown(' + n_id + ')" /></div>';
/*		
	$get( div_parent ).innerHTML =	'<div style="width:' + this.n_controlWidth + 'px;height:' + this.n_controlHeight + 'px;border:0; background-size:100%; background-image:url(' + this.s_imgControl + ')" id="sl' + n_id + 'base">' +
		'<img src="' + this.s_imgSlider + '" width="' + this.n_sliderWidth + '" height="' + this.n_sliderHeight + '" border="0" style="position:relative;left:' + this.n_pathLeft + 'px;top:' + this.n_pathTop + 'px;z-index:' + this.n_zIndex + ';cursor:pointer;visibility:hidden;" name="sl' + n_id + 'slider" id="sl' + n_id + 'slider" onmousedown="return f_sliderMouseDown(' + n_id + ')" /></div>';*/		
		
	this.e_base   = $get('sl' + n_id + 'base');
	this.e_slider = $get('sl' + n_id + 'slider');

	if (document.addEventListener) {
		this.e_slider.addEventListener("touchstart", function (e_event) { f_sliderMouseDown(n_id, e_event) },  false);
		document.addEventListener("touchmove", f_sliderMouseMove,  false);
		document.addEventListener("touchend", f_sliderMouseUp,  false);
	}
	
	// safely hook document/window events
	if (!window.f_savedMouseMove && document.onmousemove != f_sliderMouseMove) {
		window.f_savedMouseMove = document.onmousemove;
		document.onmousemove = f_sliderMouseMove;
	}
	if (!window.f_savedMouseUp && document.onmouseup != f_sliderMouseUp) {
		window.f_savedMouseUp = document.onmouseup;
		document.onmouseup = f_sliderMouseUp;
	}

	// preset to the value in the input box if available
	var e_input = $get(this.s_name);
	this.f_setValue(  e_input.value != '' ? e_input.value : null, 1);
	this.e_slider.style.visibility = 'visible';
}

function Enable( bEnable )
{
	this.b_Enable = bEnable;
	
	var strID 		= "sl" + this.n_id + "slider";
	var strBase 	= "sl" + this.n_id + "base";
	var strBtmImg = "btmimg" + this.n_id;
	
	if( this.b_Enable == 0 )	
	{
		$get( strID ).src = this.s_imgSliderDisable;
		$get( strID ).style.cursor = "auto";
		$get( strBtmImg ).src = this.s_imgControlDisable;
		
	///	$get( strBase ).style.backgroundImage = "url(" + this.s_imgControlDisable + ")";
	}
	else
	{
		$get( strID ).src = this.s_imgSlider;
		$get( strID ).style.cursor = "pointer";
		$get( strBtmImg ).src = this.s_imgControl;
		
	///	$get( strBase ).style.backgroundImage =  "url(" + this.s_imgControl + ")";
	}
}

function f_sliderSetValue (n_value, bUpdateWH ) {
	if (n_value == null)
		n_value = this.n_value == null ? this.n_minValue : this.n_value;
	if (isNaN(n_value))
		return false;
	// round to closest multiple if step is specified
	if (this.n_step)
		n_value = Math.round((n_value - this.n_minValue) / this.n_step) * this.n_step + this.n_minValue;
	// smooth out the result
	if (n_value % 1)
		n_value = Math.round(n_value * 1e5) / 1e5;

	if (n_value < this.n_minValue)
		n_value = this.n_minValue;
	if (n_value > this.n_maxValue)
		n_value = this.n_maxValue;

	this.n_value = n_value;

	this.e_slider.style.left = (this.n_pathLeft + Math.round((n_value - this.n_minValue) * this.n_pix2value)) + 'px';


	this.f_updateValue( n_value, bUpdateWH );
}

// get absolute position of the element in the document
function f_sliderGetPos ( b_base) {
	var n_pos = 0,
		s_coord = 'Left';
	var o_elem = o_elem2 = b_base ? this.e_base : this.e_slider;
	
	while (o_elem) {
		n_pos += o_elem["offset" + s_coord];
		o_elem = o_elem.offsetParent;
	}
	o_elem = o_elem2;

	var n_offset;
	while (o_elem.tagName != "BODY") {
		n_offset = o_elem["scroll" + s_coord];
		if (n_offset)
			n_pos -= o_elem["scroll" + s_coord];
		o_elem = o_elem.parentNode;
	}
	return n_pos;
}

function f_sliderMouseDown (n_id, e_event) {

	var o_slider = A_SLIDERS[n_id];
	 
	if( o_slider.b_Enable == 0 )
		return false;

	window.n_activeSliderId = n_id;
	f_sliderSaveTouch(e_event);

	
	window.n_mouseOffset = window.n_mouseX - o_slider.n_sliderWidth  / 2 - o_slider.f_getPos(1) - parseInt(o_slider.e_slider.style.left);

	return false;
}

function f_sliderMouseUp (e_event, b_watching) {

	if (window.n_activeSliderId != null) {
		var o_slider = window.A_SLIDERS[window.n_activeSliderId];
		o_slider.f_setValue(o_slider.n_minValue + (	(parseInt(o_slider.e_slider.style.left) - o_slider.n_pathLeft)) / o_slider.n_pix2value, 1 );
		if (b_watching)	return;

		window.n_activeSliderId = null;
		window.n_mouseOffset = null;

	}
	if (window.f_savedMouseUp)
		return window.f_savedMouseUp(e_event);
}

function f_sliderMouseMove (e_event) {

	if (!e_event && window.event) e_event = window.event;

	// save mouse coordinates
	if (e_event) {
		window.n_mouseX = e_event.clientX + f_scrollLeft();
		window.n_mouseY = e_event.clientY + f_scrollTop();
	}

	// check if in drag mode
	if (window.n_activeSliderId != null) {

		f_sliderSaveTouch(e_event);
		var o_slider = window.A_SLIDERS[window.n_activeSliderId];

		var n_pxOffset;

			var n_sliderLeft = window.n_mouseX - o_slider.n_sliderWidth / 2 - o_slider.f_getPos(1) - window.n_mouseOffset;
			// limit the slider movement
			if (n_sliderLeft < o_slider.n_pathLeft)
				n_sliderLeft = o_slider.n_pathLeft;
			var n_pxMax = o_slider.n_pathLeft + o_slider.n_pathLength;
			if (n_sliderLeft > n_pxMax)
				n_sliderLeft = n_pxMax;

			o_slider.e_slider.style.left = n_sliderLeft + 'px';
			n_pxOffset = n_sliderLeft - o_slider.n_pathLeft;
		
			 f_sliderMouseUp(e_event, 1);

		return false;
	}
	
	if (window.f_savedMouseMove)
		return window.f_savedMouseMove(e_event);
}

function f_sliderSaveTouch (e_event) {
	if (!e_event || !e_event.touches) return;
	e_event.preventDefault();
	var e_touch = e_event.touches[0] || e_event.changedTouches[0];
	window.n_mouseX = e_touch.pageX;
	window.n_mouseY = e_touch.pageY;
}

// get the scroller positions of the page
function f_scrollLeft() {
	return f_filterResults (
		window.pageXOffset ? window.pageXOffset : 0,
		document.documentElement ? document.documentElement.scrollLeft : 0,
		document.body ? document.body.scrollLeft : 0
	);
}
function f_scrollTop() {
	return f_filterResults (
		window.pageYOffset ? window.pageYOffset : 0,
		document.documentElement ? document.documentElement.scrollTop : 0,
		document.body ? document.body.scrollTop : 0
	);
}
function f_filterResults(n_win, n_docel, n_body) {
	var n_result = n_win ? n_win : 0;
	if (n_docel && (!n_result || (n_result > n_docel)))
		n_result = n_docel;
	return n_body && (!n_result || (n_result > n_body)) ? n_body : n_result;
}