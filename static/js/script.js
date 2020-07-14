const symbolOfLike = document.querySelector('.news-card-likes')
const symbolOfDislike = document.querySelector('.news-card-dislikes')


/*
	Function changes color and count of dislikes
	Mark can be like of dislike.
	If user click on like => clickedMark is like, nonClickedMark is dislike
	If user click on dislike => clickedMark is dislike, nonClickedMark is like
*/
function changeMark(clickedMark, nonClickedMark){	
	if (clickedMark.style.color == 'red'){
		clickedMark.style.color = 'gray';
		// childNodes[3] is a count of clicked Mark
		clickedMark.childNodes[3].innerHTML--; 
	}
	else{
		clickedMark.style.color = 'red';
		clickedMark.childNodes[3].innerHTML++;
		if (nonClickedMark.style.color == 'red'){
			nonClickedMark.style.color = 'gray';
			nonClickedMark.childNodes[3].innerHTML--;
		}
	}
}

symbolOfLike.onclick = function() {
	changeMark(symbolOfLike, symbolOfDislike);
}

symbolOfDislike.onclick = function() {
	changeMark(symbolOfDislike, symbolOfLike)
}