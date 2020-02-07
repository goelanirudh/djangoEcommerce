$('#trackerForm').submit(function(event){

    $('#updateItem').empty();

    var formData={
        'order_id':$('input[name=order_id]').val(),
        'email':$('input[name=email]').val(),
        'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
    };


    $.ajax({
        type:'POST',
        url:'/shop/tracker/',
        data:formData,
        encode:true,
    })
    .done(function(data){
        // console.log(data);
        data=JSON.parse(data)
        updates=data[0];
        // console.log(updates);
        if(updates.length>0 & updates!={}){

        for(i=0;i<updates.length;i++){
            text=updates[i]['text'];
            time=updates[i]['time'];

            mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                    ${text}
                    <span class="badge badge-primary badge-pill">${time}</span>
                </li>`
            $('#updateItem').append(mystr);
        }
    }else{
            mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                    Please enter correct order Id or email
                </li>`
            $('#updateItem').append(mystr);
    }
// fill in the order details
cart=JSON.parse(data[1])
// console.log(cart)
        for (var item in cart) {
            let name = cart[item][1]
            let qty = cart[item][0]

            mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                    ${name}
                    <span class="badge badge-primary badge-pill">${qty}</span>
                </li>`
            $('#detailItem').append(mystr);
        }


    });

    event.preventDefault();
});