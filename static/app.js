function getUserInput() {
    var userInput = document.getElementById("user-input").value;
    appendToChat("User: " + userInput,"user");

    // Make a POST request to the server to get the bot's response
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'user_input=' + userInput,
    })
    .then(response => response.json())
    .then(data => {
        var botResponse = data.bot_response;
        appendToChat("Bot: " + botResponse,"bot");
    });
}

function appendToChat(message,who) {
    var chatBox = document.getElementById("chat-box");
    var newMessage = document.createElement("p");
    newMessage.setAttribute('class',who)
    newMessage.textContent = message;
    chatBox.appendChild(newMessage);
    document.getElementById("user-input").value = "";
}