// static/script.js
fetch('/users')
  .then(response => response.json())
  .then(data => {
    const table = document.getElementById('data-table');
    for (const [key, value] of Object.entries(data)) {
      const row = table.insertRow();
      const cell1 = row.insertCell();
      const cell2 = row.insertCell();
      cell1.textContent = key;
      cell2.textContent = value;
    }
  })
  .catch(error => console.error('Error fetching user data:', error));