if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    // Set the language for recognition
    recognition.lang = 'en-US';
    recognition.interimResults = true;

    const startBtn = document.getElementById('start-btn');
    const speechOutput = document.getElementById('userInputMessage');

    recognition.onresult = function(event) {
        let transcript = '';
        for (let i = 0; i < event.results.length; i++) {
            transcript += event.results[i][0].transcript;
        }
        speechOutput.value = transcript;
    };

    recognition.onstart = function() {
        document.getElementById('sendBtn').disabled = true;
    };

    recognition.onend = function() {
        document.getElementById('start-btn').disabled = true;
        document.getElementById('sendBtn').disabled = false;
    };

    // Error handling
    recognition.onerror = function(event) {
        document.getElementById('sendBtn').disabled = true;
    };

    // Start the recognition when the button is clicked
    startBtn.addEventListener('click', function() {
        recognition.start();
    });

} else {
    alert("Speech recognition is not supported in this browser.");
}
