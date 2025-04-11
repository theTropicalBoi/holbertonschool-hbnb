console.log("place.js");

// Récupère un cookie par nom
function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) return value;
    }
    return null;
}

// Récupère l'ID du lieu depuis l'URL
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

// Vérifie l'authentification et lance l'affichage
function checkAuthentication() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');
    const placeId = getPlaceIdFromURL();

    if (!token) {
        addReviewSection.style.display = 'none';
    } else {
        addReviewSection.style.display = 'block';
    }

    fetchPlaceDetails(token, placeId);
}

// Récupère les infos d'un lieu
async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`http://3000/api/v1/places/${placeId}`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const place = await response.json();
            displayPlaceDetails(place);
        } else {
            alert("Erreur lors de la récupération des détails du lieu.");
        }
    } catch (err) {
        console.error("Erreur réseau :", err);
    }
}

// Affiche les infos dans le DOM
function displayPlaceDetails(place) {
    const section = document.getElementById('place-details');
    section.innerHTML = `
        <div class="place-info">
            <h2>${place.name}</h2>
            <p><strong>Hôte :</strong> ${place.owner_name}</p>
            <p><strong>Prix :</strong> ${place.price}€/nuit</p>
            <p><strong>Description :</strong> ${place.description}</p>
            <h4>Équipements :</h4>
            <ul>${place.amenities.map(a => `<li>${a}</li>`).join('')}</ul>
        </div>
        <h3>Avis</h3>
        ${place.reviews && place.reviews.length > 0 ? (
            place.reviews.map(review => `
                <div class="review-card">
                    <p><strong>${review.user_name} :</strong> ${review.comment}</p>
                    <p>Note : ${review.rating}/5</p>
                </div>
            `).join('')
        ) : '<p>Aucun avis pour ce lieu.</p>'}
    `;
}

// Lance au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();
});
