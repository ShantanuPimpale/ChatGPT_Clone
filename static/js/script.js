// Example POST method implementation:
async function postData(url = "", data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: "POST", 
      headers: {
        "Content-Type": "application/json",
        
      },referrerPolicy: "no-referrer", 
      body: JSON.stringify(data), 
    });
    return response.json(); 
  }


document.addEventListener("DOMContentLoaded", () => {
    const sendButton = document.getElementById("sendButton");
    sendButton.addEventListener("click", async () => {
        let questionInput = document.getElementById("questionInput").value;
        document.getElementById("questionInput").value = "";
        document.querySelector(".right2").style.display = "block";
        document.querySelector(".right1").style.display = "none";


        question1.innerHTML = questionInput;
        question2.innerHTML = questionInput;

        let result = await postData("/api",{"question":questionInput})
        solution.innerHTML = result.result;
    });
});


