document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const reviewForm = document.getElementById('review-form');

  /* Login Form */
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      await loginUser(email, password);
    });
  }

  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const reviewText = document.getElementById('review-text').value;
      const token = getCookie('token');
      const placeId = getPlaceIdFromURL();
      
      if (!token) {
        alert('Please login to submit a review');
        return;
      }
      
      await submitReview(token, placeId, reviewText);
    });
  }

  checkAuthentication();
  initializePriceFilter();
});


/* LOGIN SECTION: */
async function loginUser(email, password) {
  try {
    const response = await fetch('http://127.0.0.1:3000/api/v1/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });
    
    if (response.ok) {
      const data = await response.json();
      document.cookie = `token=${data.access_token}; path=/; secure; samesite=strict`;
      localStorage.setItem('user', JSON.stringify(data.user));
      window.location.href = 'index.html';
    } else {
      alert(`Login failed: ${response.statusText}`);
    }
  } catch (error) {
    console.error('Login error:', error);
    alert('Login failed: Network error or server unavailable');
  }
}


/* CHECK USER AUTHENTICATION SECTION: */
function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');
  const addReviewSection = document.getElementById('add-review');
  const placesList = document.getElementById('places-list');
  
  if (loginLink) {
    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
      console.log('User is logged in, with token: ', token);
      // Only fetch places if we're on the index page
      if (placesList) {
        fetchPlaces(token);
      }
    }
  } else {
    console.log('Login link element not found on this page');
  }

  if (addReviewSection) {
    if (!token) {
      addReviewSection.style.display = 'none';
    } else {
      addReviewSection.style.display = 'block';
      // Get place ID from URL and fetch place details
      const placeId = getPlaceIdFromURL();
      if (placeId) {
        fetchPlaceDetails(token, placeId);
      } else {
        console.error('No place ID found in URL');
      }
    }
  } else {
    console.log('Add review element not found on this page')
  }
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}


/* FETCH PLACES FROM THE API  */
async function fetchPlaces(token) {
  const url = new URL('http://127.0.0.1:3000/api/v1/places/');

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    mode: 'cors'
  });

  if (response.ok) {
    const places = await response.json();
    displayPlaces(places);
  } else {
    console.error('Failed to fetch places:', response.statusText);
  }
}


/* DISPLAY PLACES IN INDEX */
function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  if (!placesList) {
    console.error('Places list element not found');
    return;
  }
  placesList.innerHTML = '';

  places.forEach(place => {
    const placeElement = document.createElement('div');
    placeElement.className = 'place-card';
    placeElement.dataset.price = place.price;
    placeElement.dataset.id = place.id;
    
    placeElement.innerHTML = `
      <div class="content">
        <h3>${place.title}</h3>
        <p class="price">€${place.price} per night</p>
      </div>
    `;

    placeElement.addEventListener('click', () => {
      window.location.href = `place.html?id=${place.id}`;
    });

    placesList.appendChild(placeElement);
  });
}


/* PRICE FILTER DROPDOWN INIT */
function initializePriceFilter() {
  const priceFilter = document.getElementById('price-filter');
  if (!priceFilter) {
    console.error('Price filter element not found');
    return;
  }
  priceFilter.innerHTML = '';

  const options = [
    { value: 'all', text: 'All' },
    { value: '10', text: '€10' },
    { value: '50', text: '€50' },
    { value: '100', text: '€100' }
  ];
  
  options.forEach(option => {
    const optionElement = document.createElement('option');
    optionElement.value = option.value;
    optionElement.textContent = option.text;
    priceFilter.appendChild(optionElement);
  });
  
  priceFilter.addEventListener('change', filterPlacesByPrice);
}

/* FILTER PLACES BY PRICE LOGIC  */
function filterPlacesByPrice(event) {
  const selectedPrice = event.target.value;
  const placesList = document.getElementById('places-list');
  const placeCards = placesList.querySelectorAll('.place-card');
  
  placeCards.forEach(card => {
    const price = parseFloat(card.dataset.price);
    
    if (selectedPrice === 'all' || price <= parseFloat(selectedPrice)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}



/* FETCH PLACE ID FROM URL */
function getPlaceIdFromURL() {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get('id');
}

/* USE FETCH API TO GET THE PLACE DETAIL */
async function fetchPlaceDetails(token, placeId) {
  try {
    const response = await fetch(`http://127.0.0.1:3000/api/v1/places/${placeId}`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    displayPlaceDetails(data);
  } catch (error) {
    console.error('Error fetching place details:', error);
  }
}

/* DISPLAY THE PLACE DETAILS */
function displayPlaceDetails(place) {
  const placeDetailsSection = document.getElementById('place-details');
  
  console.log('Place object:', place);

  // Create reviews list HTML
  const reviewsHTML = place.reviews && place.reviews.length > 0
    ? `
      <div class="reviews">
        <h3>Reviews</h3>
        <ul>
          ${place.reviews.map(review => `
            <p>${review.text}</p>
          `).join('')}
        </ul>
      </div>
    `: '';

  placeDetailsSection.innerHTML = `
    <div class="place-details-container">
      <h1>${place.title}</h1>
      <h5 class="price">€${place.price} per night</h5>
      <br><br>
      <p class="description">${place.description}</p>
      ${reviewsHTML}
    </div>
  `;
}

async function submitReview(token, placeId, reviewText) {
  try {
    const response = await fetch(`http://127.0.0.1:3000/api/v1/reviews/`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 
        text: reviewText,
        place_id: placeId
      })
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Failed to submit review');
    }

    handleResponse(response);
  } catch (error) {
    console.error('Error submitting review:', error);
    alert('Failed to submit review: ' + error.message);
  }
}

function handleResponse(response) {
  if (response.ok) {
    alert('Review submitted successfully!');
    document.getElementById('review-text').value = '';
    const token = getCookie('token');
    const placeId = getPlaceIdFromURL();
    fetchPlaceDetails(token, placeId);
  } else {
    alert('Failed to submit review: ' + response.statusText);
  }
}