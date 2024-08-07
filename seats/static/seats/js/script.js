"use strict"

let cntctsMenu = document.getElementById("popup-contacts");
let hotelsMenu = document.getElementById("popup-hotels");
let hotelsOverlay = document.getElementById("popup-overlay-hotels");
let cntctsOverlay = document.getElementById("popup-overlay");


function displayContactsOverlay() {
    cntctsOverlay.classList.remove("closed");
    cntctsOverlay.classList.add("opened");
}


function hideContactsOverlay() {
  contactsOverlay.classList.remove("opened");
  contactsOverlay.classList.add("closed");
}

function openHotelOverlay() {
    hotelsOverlay.classList.remove('closed');
    hotelsOverlay.classList.add('opened');
}

function hideHotelsOverlay() {
  hotelsOverlay.classList.remove('opened');
  hotelsOverlay.classList.add('closed');
}

cntctsMenu.addEventListener("click", displayContactsOverlay);
cntctsOverlay.addEventListener("click", hideContactsOverlay);
hotelsMenu.addEventListener("click", openHotelOverlay);
hotelsOverlay.addEventListener("click", hideHotelsOverlay);
