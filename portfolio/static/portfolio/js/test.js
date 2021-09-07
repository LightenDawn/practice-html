
let nav = document.querySelector(".navigation");
window.addEventListener("scroll", () =>{
    if(document.documentElement.scrollTop > 20){
        nav.classList.add("sticky");
    }
    else{
        nav.classList.remove("sticky");
    }
});

// (() =>{
//     document.addEventListener("click", (event) =>{
//         const tar = event.target.closest("section.active"),
//         tar1 = event.target.closest("section"),
//         getSpan = event.target.classList.contains("span"&&"active"),
//         getSpanId = event.target.getAttribute("id");
//         //section activate
//         if(tar1.classList.contains("active") || getSpan){
//             null;
//         }
//         else{
//             document.querySelector("section.active").classList.remove("active");
//             tar1.classList.add("active");
//         }

//         function check(){
            
//         }
//     })
// })();

$('.row img').click(function(){
    console.log($(this).parents('.container').find('.span').val())
  })

(() =>{
    document.addEventListener("click", (event) =>{
        if(event.target.closest("section.active") || event.target.classList.contains("active")){
            // console.log(event.target.closest("section.active").classList.contains("span"))
        }
        else{
            document.querySelector(".section.active").classList.remove("active");
            event.target.closest("section").classList.add("active");
        }
    })
})();