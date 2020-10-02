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
        errorMessage.textContent = '';
    }
});

// Handle form submition
// Source Stripe documentaion & Boutique ado project

var form = document.getElementById('order-payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#order-payment-form').fadeToggle(120);
    $('#loader-overlay').fadeToggle(120);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
    }).then(function(result) {
        if (result.error) {
            var errorMessage = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorMessage).html(html);
            $('#order-payment-form').fadeToggle(120);
            $('#loader-overlay').fadeToggle(120);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});