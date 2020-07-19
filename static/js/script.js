const symbolOfLikeSet = document.querySelectorAll('.news-card-likes')
const symbolOfDislikeSet = document.querySelectorAll('.news-card-dislikes')


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

for (let i = 0; i < symbolOfLikeSet.length; i++){
	symbolOfLikeSet[i].onclick = function() {
		changeMark(symbolOfLikeSet[i], symbolOfDislikeSet[i]);
	}
}

for (let i = 0; i < symbolOfDislikeSet.length; i++){
	symbolOfDislikeSet[i].onclick = function() {
		changeMark(symbolOfDislikeSet[i], symbolOfLikeSet[i])
	}
}