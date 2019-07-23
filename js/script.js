const today=document.querySelector('.st-bg-today');


function onClick(event){
	event.preventDefault();
	console.log('Hello');
}


today.addEventListener('click',onClick);