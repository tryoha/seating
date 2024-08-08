"use strict"

let cntctsMenu = document.getElementById("popup-contacts");
let hotelsMenu = document.getElementById("popup-hotels");
let hotelsOverlay = document.getElementById("popup-overlay-hotels");
let cntctsOverlay = document.getElementById("popup-overlay");
let hamburger = document.getElementById("mobile-menu");
let mainMenu = document.getElementById("main-menu");


function displayContactsOverlay() {
    cntctsOverlay.classList.remove("closed");
    cntctsOverlay.classList.add("opened");
}


function hideContactsOverlay() {
    cntctsOverlay.classList.remove("opened");
    cntctsOverlay.classList.add("closed");
}

function openHotelOverlay() {
    hotelsOverlay.classList.remove('closed');
    hotelsOverlay.classList.add('opened');
}

function hideHotelsOverlay() {
  hotelsOverlay.classList.remove('opened');
  hotelsOverlay.classList.add('closed');
}

function openMobileMenu() {
    mainMenu.classList.remove('mobile-menu-hidden');
}

function closeMobileMenu() {
    mainMenu.classList.add('mobile-menu-hidden');
}

cntctsMenu.addEventListener("click", displayContactsOverlay);
cntctsOverlay.addEventListener("click", hideContactsOverlay);
hotelsMenu.addEventListener("click", openHotelOverlay);
hotelsOverlay.addEventListener("click", hideHotelsOverlay);
hamburger.addEventListener("click", openMobileMenu);
mainMenu.addEventListener("click", closeMobileMenu);

