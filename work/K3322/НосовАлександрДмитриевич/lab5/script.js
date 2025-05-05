function showWheelAlert() {
    alert("Болейте за Омский Авангард!!!");
}

function changeTitleColor(event) {
    event.preventDefault();
    document.getElementById("ava-title").classList.toggle("clicked");
}

function changeImage(event) {
    event.preventDefault();
    let img = document.getElementById("ava-image");
    img.src = (img.src.includes("ava_white.jpg")) ? "ava_black.jpg" : "ava_white.jpg";
}

document.getElementById("order-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let name = document.getElementById("name").value;
    let phone = document.getElementById("phone").value;
    let email = document.getElementById("email").value;
    let model = document.getElementById("jur-model").value;

    if (name && phone && email && model) {
        document.getElementById("order-form").style.display = "none";
        document.getElementById("success-message").classList.remove("hidden");
    } else {
        alert("Пожалуйста, заполните все обязательные поля.");
    }
});