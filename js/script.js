let today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();
let selectYear = document.getElementById("year");
let selectMonth = document.getElementById("month");

let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

let monthAndYear = document.getElementById("monthAndYear");
showCalendar(currentMonth, currentYear);


function next() {
    currentYear = (currentMonth === 11) ? currentYear + 1 : currentYear;
    currentMonth = (currentMonth + 1) % 12;
    showCalendar(currentMonth, currentYear);
}

function previous() {
    currentYear = (currentMonth === 0) ? currentYear - 1 : currentYear;
    currentMonth = (currentMonth === 0) ? 11 : currentMonth - 1;
    showCalendar(currentMonth, currentYear);
}

function jump() {
    currentYear = parseInt(selectYear.value);
    currentMonth = parseInt(selectMonth.value);
    showCalendar(currentMonth, currentYear);
}




function showCalendar(month, year) {

    let firstDay = (new Date(year, month)).getDay();
    let daysInMonth = 32 - new Date(year, month, 32).getDate();

    let tbl = document.getElementById("calendar-body"); // body of the calendar

    // clearing all previous cells
    //tbl.innerHTML = "";

    // filing data about month and in the page via DOM.
    monthAndYear.innerHTML = months[month] + " " + year;
    selectYear.value = year;
    selectMonth.value = month;

    // creating all cells
    let date = 1;
    

    for (let i = 0; i < 6; i++) {
        // creates a table row
        let row = document.createElement("tr");

        //creating individual cells, filing them up with data.
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                let cell = document.createElement("td");
                
                let cellText = document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
                cell.setAttribute('id',`${year} ${month} ${date}`);
            }
            else if (date > daysInMonth) {
                break;
            }

            else {
                let cell = document.createElement("td");
                let cellText = document.createTextNode(date);
                cell.setAttribute('id',`${year} ${months[month]} ${date}`);

                if (date === today.getDate() && year === today.getFullYear() && month === today.getMonth()) {
                   // cell.classList.add("bg-info");
                } // color today's date
                cell.appendChild(cellText);
                

                
                row.appendChild(cell);
                date++;
                cell.addEventListener('click',onClick);
            }


        }

        tbl.appendChild(row); // appending each row into calendar body.
    }

}


function whenSubmit(event){
    event.preventDefault();
}

function onClick(event){
    const cells=document.querySelectorAll('td');
    const eventsAdd=document.querySelector('.add');
    const ongoing=document.querySelector('.ongoing ul');
      //eventsAdd.classList.remove('hidden');
    //for(let i=0;i<cells.length;i++){
      //  cells[i].classList.remove('bg-info');
    //}
  
    let id=event.target.id;
    
    document.querySelector('#id').value=id
    hidden_form=document.querySelector('#hidden-form');
    hidden_form.addEventListener('submit',whenSubmit);
    hidden_form.submit();

    event.target.classList.add('bg-info');
   


}
const form=document.querySelector('.add form');


function onSubmit(event){
    event.preventDefault();
    const activeCell=document.querySelector('.bg-info');
    //const time=document.querySelector('#time').value;
    //const info=document.querySelector('#info').value;
    let id=activeCell.id;
    document.querySelector('#date').value = id;
    form.submit();
    //$.post('/calendar',{'date':id,'info':info,'time':time});
    document.querySelector('#time').value="";
    document.querySelector('#info').value="";
    
}

/*$(document).ready(function(){
$("#daily_button").click(insertDaily);

    function insertDaily(){
        let daily = $('input[name="goal"]:checked');
        $("#goal-id").append(`<p>${daily}</p>`);
        $("#daily_button").hide();
        $("#dgoal").hide();

        }
});*/
function goalOnSubmit(event){
    const goal=document.querySelector('#dgoal').value;
    const p=document.querySelector('#goal-text');
    p.textContent=goal;


}
const goalForm=document.querySelector('.goal-form');
goalForm.addEventListener('submit',goalOnSubmit);


form.addEventListener('submit',onSubmit);