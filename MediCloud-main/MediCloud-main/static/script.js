document.getElementById('addAppointment').addEventListener('click', function() {
    let doctor = document.getElementById('doctor').value;
    let date = document.getElementById('date').value;
    let appointment = `${doctor} - ${date}`;
    let li = document.createElement('li');
    li.textContent = appointment;
    document.getElementById('remindersUl').appendChild(li);
  });
  
  document.getElementById('addReminder').addEventListener('click', function() {
    let reminderDate = document.getElementById('reminderDate').value;
    let li = document.createElement('li');
    li.textContent = reminderDate;
    document.getElementById('remindersUl').appendChild(li);
  });
  

  