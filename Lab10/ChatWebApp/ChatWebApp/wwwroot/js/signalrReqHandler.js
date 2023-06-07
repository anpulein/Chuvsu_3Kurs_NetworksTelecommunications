var connection = new signalR.HubConnectionBuilder()
    .withUrl('/Home/Index')
    .build();

connection.on('receiveMessage', addMessageToChat);

connection.start()
    .catch(error => {
        console.error(error.message);
    });

function sendMessageToHub(message) {
    connection.invoke('sendMessage', message);
}

// function sendMessageToHubFile(message) {
//     connection.invoke('sendMessageForFile', message)
//         .then(function() {
//             console.log('Сообщение успешно отправлено.');
//             addMessageToChat(message); // Вызываем метод addMessageToChat после успешной отправки сообщения
//         })
//         .catch(function(error) {
//             console.log('Произошла ошибка при отправке сообщения: ' + error);
//         });
// }