let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".sidebarBtn");

sidebarBtn.onclick = function() {
    if(sidebar.classList.contains("active")){
        sidebar.classList.remove("active");
    }
    else{
        sidebar.classList.add("active");
    }
}