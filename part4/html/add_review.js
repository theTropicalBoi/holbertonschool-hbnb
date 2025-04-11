// Fonction pour lire un cookie
function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) return value;
    }
    return null;
}

// Fonction pour extraire l’ID du lieu depuis l’URL
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

// Vérifie l'authentification
function checkAuthentication() {
    const token = getCookie('token');
    if (!token) {
        // Rediriger vers index si non connecté
        window.location.href = 'index.html';
    }
    return token;
}

// Soumet un avis via l’API
async function submitReview(token, placeId, reviewText, rating) {
    try {
        const response = await fetch('http://127.0.0.1:3000/api/v1/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                comment: reviewText,
                rating: parseInt(rating),
                place_id: placeId
            })
        });

        if (response.ok) {
            alert('Avis envoyé avec succès !');
            document.getElementById('review-form').reset();
        } else {
            const error = await response.json();
            alert('Erreur : ' + (error.error || 'Impossible d’envoyer l’avis.'));
        }
    } catch (error) {
        console.error('Erreur réseau :', error);
        alert('Erreur de connexion au serveur.');
    }
}

// Lancement au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    const reviewForm = document.getElementById('review-form');
    const token = checkAuthentication();
    const placeId = getPlaceIdFromURL();

    if (reviewForm) {
        reviewForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const reviewText = reviewForm.comment.value.trim();
            const rating = reviewForm.rating.value;
            if (!reviewText || !rating) {
                alert("Veuillez remplir tous les champs.");
                return;
            }
            submitReview(token, placeId, reviewText, rating);
        });
    }
});
