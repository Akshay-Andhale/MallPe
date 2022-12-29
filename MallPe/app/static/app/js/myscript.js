$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

// $('.plus-cart').click(function(){
    
//     let id = $(this).attr("pid").toString();
//     let elm = this.parentNode.children[2];
//     console.log(id)
//     $.ajax({
//         type:"GET",
//         url:"/pluscart",
//         data:{
//             prod_id:id
//         },
//     success:function(data)
//     {
//         elm.innerText = data.quantity
//         document.getElementById('amt').innerText = data.amt
//         document.getElementById('finalamt').innerText = data.finalamt
//     } 
//     })
// })


// $('.minus-cart').click(function(){
    
//     let id = $(this).attr("pid").toString();
//     let elm = this.parentNode.children[2];
//     console.log(id)
//     $.ajax({
//         type:"GET",
//         url:"/minuscart",
//         data:{
//             prod_id:id
//         },
//     success:function(data)
//     {
//         elm.innerText = data.quantity
//         document.getElementById('amt').innerText = data.amt
//         document.getElementById('finalamt').innerText = data.finalamt
//     } 
//     })
// })


// $('.remove-cart').click(function(){
    
//     let id = $(this).attr("pid").toString();
//     console.log(id)
//     $.ajax({
//         type:"GET",
//         url:"/removecart",
//         data:{
//             prod_id:id
//         },
//     success:function(data)
//     {
//         console.log("Delete")
//         document.getElementById('amt').innerText = data.amt
//         document.getElementById('finalamt').innerText = data.finalamt
//         elm.parentNode.parentNode.parentNode.parentNode.remove()
//     } 
//     })
// })
