document.addEventListener("DOMContentLoaded", () => {
    const sendButton = document.getElementById("sendButton");
    sendButton.addEventListener("click", async () => {
        let questionInput = document.getElementById("questionInput").value;
        document.getElementById("questionInput").value = "";
        document.querySelector(".right2").style.display = "block";
        document.querySelector(".right1").style.display = "none";


        question1.innerHTML = questionInput;
        question2.innerHTML = questionInput;
    });
});
