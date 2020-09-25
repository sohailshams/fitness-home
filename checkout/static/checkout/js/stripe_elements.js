/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Got stripe PublicKey & clientSecret from template
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// Created variable using stripe public key
var stripe = Stripe(stripePublicKey);
// Created instance of stripe elements
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Ubunto", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#e84610',
        iconColor: '#e84610'
    }
};
// Created card elements
var card = elements.create('card', {style: style});
// Mounted card element to checkout.html div
card.mount('#card-element');

// Handling realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorMessage = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="far fa-window-close"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorMessage).html(html);
    } else {
        errorDiv.textContent = '';
    }
});
