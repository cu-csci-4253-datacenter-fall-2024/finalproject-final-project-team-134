document.addEventListener("DOMContentLoaded", function () {
  const workshopsSection = document.getElementById("workshops-section");
  const workshopsList = document.getElementById("workshops-list");
  const loadWorkshopsBtn = document.getElementById("load-workshops-btn");


  loadWorkshopsBtn.addEventListener("click", function () {
 
    workshopsSection.style.display = "block";
    workshopsList.innerHTML = "<p>Loading workshops...</p>";

    
    fetch("http://localhost:5001/workshops/")
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
      
        workshopsList.innerHTML = "";
        if (data.length === 0) {
          workshopsList.innerHTML = "<p>No workshops available at the moment.</p>";
          return;
        }

        data.forEach(workshop => {
          const workshopCard = document.createElement("div");
          workshopCard.className = "workshop-card";
          workshopCard.innerHTML = `
            <h3>${workshop.title}</h3>
            <p><strong>Location:</strong> ${workshop.location}</p>
            <p><strong>Price:</strong> $${workshop.price}</p>
          `;
          workshopsList.appendChild(workshopCard);
        });
      })
      .catch(error => {
        console.error("Error fetching workshops:", error);
        workshopsList.innerHTML = "<p>Error loading workshops. Please try again later.</p>";
      });
  });
});

