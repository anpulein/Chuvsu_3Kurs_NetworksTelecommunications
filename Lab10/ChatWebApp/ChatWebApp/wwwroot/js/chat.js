class Message {
    constructor(username, text, when, type, file) {
        this.userName = username;
        this.text = text;
        this.when = when;
        this.typeMessage = type;
        this.file = file;
    }
}

class Files {
    constructor(id, name) {
        this.id = id
        this.name = name;
    }
}

// userName is declared in razor page.
const username = userName;
const textInput = document.getElementById('messageText');
const whenInput = document.getElementById('when');
const chat = document.getElementById('chat-content');
const messagesQueue = [];

let messageType = "";

document.getElementById('submitButton').addEventListener('click', () => {
    var currentdate = new Date();
    when.innerHTML =
        (currentdate.getMonth() + 1) + "/"
        + currentdate.getDate() + "/"
        + currentdate.getFullYear() + " "
        + currentdate.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
    
    messageType = "FILE"
});

document.getElementById('submitButtonForFile').addEventListener('click', () => {
    var currentdate = new Date();
    when.innerHTML =
        (currentdate.getMonth() + 1) + "/"
        + currentdate.getDate() + "/"
        + currentdate.getFullYear() + " "
        + currentdate.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })

    messageType = "MESSAGE";
});

function clearInputField() {
    messagesQueue.push(textInput.value);
    textInput.value = "";
}

function sendMessage(fileId, type) {
    let text = messagesQueue.shift() || "";
    if (text.trim() === "" && type !== "FILE") return;
    
    let when = new Date();
    if (type === "FILE") {
        let messageFile = document.getElementById("file-upload").files[0];
        let file = new Files(fileId, messageFile.name)
        
        let enumFile = type === "FILE" ? 1 : 0;
        
        let message = new Message(username, text, when, enumFile, file);
        sendMessageToHub(message);
    } else {
        let message = new Message(username, text, when);
        sendMessageToHub(message);
    }
}

// function sendMessageForFile() {
//     let when = new Date();
//     let file = document.getElementById("file-upload").files[0];
//     let message = new Message(username, " ", when, type, file);
//     sendMessageToHubFile(message);
// }

function addMessageToChat(message) {
    let isCurrentUserMessage = message.userName === username;

    let container = document.createElement('div');
    container.className = isCurrentUserMessage ? "media media-chat media-chat-reverse" : "media media-chat media-chat-answer";
    
    var containerMessage = document.createElement('div');
    containerMessage.className = "media-body";

    let sender = document.createElement('div');
    sender.className = "name";
    sender.innerHTML = message.userName;
    

    let when = document.createElement('p');
    when.className = "meta";
    let whenTime = document.createElement('time')
    var currentdate = new Date();
    whenTime.innerHTML = 
        (currentdate.getMonth() + 1) + "/"
        + currentdate.getDate() + "/"
        + currentdate.getFullYear() + " "
        + currentdate.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
    when.appendChild(whenTime)

    containerMessage.appendChild(sender);

    if (message.typeMessage === 1) {

        var containerFile = document.createElement('a');
        var fileId = message.file.id;
        containerFile.href = "/Home/Download?fileName=" + encodeURIComponent(fileId);
        
        let image = document.createElement('i');
        image.className = "fa fa-file";
        image.setAttribute("aria-hidden", "true");

        let filename = document.createElement('p');
        filename.innerHTML = message.file.name;

        containerFile.appendChild(image)
        containerFile.appendChild(filename);
        
        containerMessage.appendChild(containerFile);
    } else {
        let text = document.createElement('p');
        text.innerHTML = message.text;

        containerMessage.appendChild(text);
    }
    containerMessage.appendChild(when);
    container.appendChild(containerMessage)
    chat.appendChild(container);
}
