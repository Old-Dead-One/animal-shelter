"use strict";

document.addEventListener("DOMContentLoaded", async (e) => {
  const baseurl = "http://localhost:8000";

  const response = await fetch(`${baseurl}/shelters`);
  const shelters = await response.json();

  const contentElement = document.getElementById("shelters");

  for (let i = 0; i < shelters.length; i++){
    const shelterElement = createShelterElement(shelters[i])
    contentElement.appendChild(shelterElement);
  }

  const shelterElement = createShelterElement();
  contentElement.appendChild(shelterElement);
});

function createShelterElement(shelter) {
  const section = document.createElement("section");
  section.className = "shelter-card";

  section.innerHTML = `
    <h3>${shelter.name}</h3>
    <p>${shelter.address}</p>
    <p>Dogs ${shelter.animals.dogs}</p>
    <p>Cats ${shelter.animals.cats}</p>`;

  return section;
}
