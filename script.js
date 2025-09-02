const guestForm = document.getElementById('guestForm'); 
const guestList = document.getElementById('guestList'); 
  
guestForm.addEventListener('submit', function (e) { 
    e.preventDefault(); 
  
    const name = document.getElementById('name').value; 
    const message = document.getElementById('message').value; 
    const date = document.getElementById('date').value; 
    const thought = document.getElementById('thought').value; 
  
    const guestCard = document.createElement('div'); 
    guestCard.classList.add('guest-card'); 
    guestCard.innerHTML = ` 
                <h2>${name}</h2> 
                <p><strong>message:</strong> ${message}</p> 
                <p><strong>date:</strong> ${date}</p> 
                <p><strong>thought:</strong> ${thought}</p>`; 
  
    guestList.appendChild(guestCard); 
  
    guestForm.reset(); 
});
