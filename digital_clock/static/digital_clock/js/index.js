let section = document.querySelector("section"),
    icons = document.querySelector(".icons");

icons.onclick = () =>{
    section.classList.toggle("dark");
}

// creating a function and calling it in every seconds

setInterval(() =>{
    let date = new Date(),
    hour = date.getHours(),
    minute = date.getMinutes(),
    seconds = date.getSeconds();

    let d;
    d = hour < 12 ? "AM" : "PM"; // if hour is smaller than 12 its value will be AM else its value will be PM
    hour = hour > 12 ? hour - 12 : hour;// if hour value is greater than 12, 12 will subtract( by doing this we will get value till 12 )
    hour = hour == 0 ? hour = 12 : hour;// if hour value is 0 than it value will be 12

    // adding 0 to all the value if they will less than 10
    hour = hour < 10 ? "0" + hour: hour;
    minute = minute < 10 ? "0" + minute: minute;
    seconds = seconds < 10 ? "0" + seconds: seconds;

    document.querySelector("span.hour_num").innerText = hour;
    document.querySelector("span.min_num").innerText = minute;
    document.querySelector("span.sec_num").innerText = seconds;
    document.querySelector("span.am_pm").innerText = d;
}, 1000); // 1000 miliseconds = 1s