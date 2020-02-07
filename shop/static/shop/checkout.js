if (localStorage.getItem('cart') == null) {
    var cart = {}
}
else {
    cart = JSON.parse(localStorage.getItem('cart'))
}
console.log(cart)
var sum=0;
var totalPrice=0;
if($.isEmptyObject(cart)){
    mystr = `<p>Your cart is empty, add some item to your cart</p>`
    $('#item').append(mystr);
}
for(var item in cart){
    let name=cart[item][1]
    let qty=cart[item][0]
    let price=cart[item][2]
    sum=sum+qty;
    totalPrice=totalPrice+qty*price;

    mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                    ${name}
                    <span class="badge badge-primary badge-pill">${qty}</span>
                </li>`
    $('#item').append(mystr);
}

document.getElementById('cart').innerHTML=sum
document.getElementById('totalPrice').innerHTML=totalPrice


function clearCart() {
    cart = JSON.parse(localStorage.getItem('cart'));
    for (var item in cart) {
        document.getElementById('div' + item).innerHTML = '<button id="' + item + '"class="btn btn-primary cart">Add To Cart</button>'
    }
    localStorage.clear()
    cart = {}
    updateCart(cart);
}

$('#item_json').val(JSON.stringify(cart))
