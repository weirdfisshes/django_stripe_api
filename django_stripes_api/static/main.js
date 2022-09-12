console.log("Sanity check!");

let url = new URL(window.location.href).href;
var pk = url.substring(url.lastIndexOf('item/') + 5);


fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  const stripe = Stripe(data.publicKey);
  document.querySelector("#submitBtn").addEventListener("click", () => {
    fetch("/buy/"+pk)
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});