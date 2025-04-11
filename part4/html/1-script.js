console.log("1-script.js")

// Attendre que le DOM soit complètement chargé
document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication(); // Vérifie si l'utilisateur est connecté

    // Ajoute un écouteur sur le filtre de prix
    const filterSelect = document.getElementById('price-filter');
    if (filterSelect) {
        filterSelect.addEventListener('change', handlePriceFilter);
    }
});

// Fonction pour récupérer un cookie spécifique (ici le token JWT)
function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) {
            return value;
        }
    }
    return null;
}

// Vérifie si l'utilisateur est connecté et affiche ou cache le bouton Connexion
function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        // Si aucun token, afficher le lien de connexion
        loginLink.style.display = 'block';
    } else {
        // Sinon, cacher le lien et afficher les lieux
        loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

let allPlaces = []; // Stocke toutes les données de lieux

// Récupère les lieux depuis l'API avec le token JWT
async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:3000/api/v1/places', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            allPlaces = data; // stocker les lieux pour le filtre
            displayPlaces(allPlaces);
        } else {
            alert("Erreur lors de la récupération des lieux.");
        }
    } catch (error) {
        console.error('Erreur réseau:', error);
    }
}

// Affiche dynamiquement les lieux dans le DOM
function displayPlaces(places) {
    const container = document.querySelector('main');

    // On commence par vider le contenu et réinsérer le filtre
    container.innerHTML = `
        <select id="price-filter">
            <option value="all">Tous</option>
            <option value="10">Max 10€</option>
            <option value="50">Max 50€</option>
            <option value="100">Max 100€</option>
        </select>
    `;

    // Affichage de chaque lieu dans une section
    places.forEach(place => {
        const section = document.createElement('section');
        section.classList.add('place-card');
        section.setAttribute('data-price', place.price); // utile pour le filtrage

        section.innerHTML = `
            <h3>${place.name}</h3>
            <p>Prix : ${place.price}€/nuit</p>
            <a href="place.html"><button class="details-button">Voir les détails</button></a>
        `;

        container.appendChild(section);
    });

    // Rebrancher l'écouteur du filtre après avoir réinséré l'élément
    const filterSelect = document.getElementById('price-filter');
    filterSelect.addEventListener('change', handlePriceFilter);
}

// Gère le filtrage client-side par prix
function handlePriceFilter(event) {
    const maxPrice = event.target.value;
    const cards = document.querySelectorAll('.place-card');

    cards.forEach(card => {
        const price = parseFloat(card.getAttribute('data-price'));
        if (maxPrice === 'all' || price <= parseFloat(maxPrice)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}
