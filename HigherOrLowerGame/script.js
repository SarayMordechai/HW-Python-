let number = Math.floor(Math.random() * 100) + 1;
let feedback = document.getElementById("feedback");
let attempts = 0;
let maxAttempts = 10;
let timer;
let timeRemaining = 30;
let playAgainButton = document.getElementById("play-again");

function setDifficulty() {
    let level = parseInt(document.getElementById("level").value);
    document.getElementById("range").textContent = level;
    document.getElementById("guess").max = level;
    resetGame();
}

function resetGame() {
    number = Math.floor(Math.random() * parseInt(document.getElementById("level").value)) + 1;
    attempts = 0;
    timeRemaining = 30;
    feedback.textContent = "";
    clearInterval(timer);
    timer = setInterval(updateTimer, 1000);
}

function updateTimer() {
    timeRemaining--;
    document.getElementById("time").textContent = timeRemaining;
    if (timeRemaining <= 0) {
        clearInterval(timer);
        feedback.textContent = "Time's up! The correct number was " + number + ".";
    }
}

function checkGuess() {
    if (timeRemaining > 0) {
        let guess = parseInt(document.getElementById("guess").value);
        attempts++;

        if (attempts <= maxAttempts) {
            if (guess < number) {
                feedback.textContent = "Higher! Attempt " + attempts + " of " + maxAttempts + ".";
            } else if (guess > number) {
                feedback.textContent = "Lower! Attempt " + attempts + " of " + maxAttempts + ".";
            } else {
                clearInterval(timer);
                feedback.textContent = "You got it! The number was " + number + ". It took you " + attempts + " attempts.";
            }
        } else {
            clearInterval(timer);
            feedback.textContent = "Game over! You didn't guess the number within " + maxAttempts + " attempts. The correct number was " + number + ".";
        }
    }
}
function updateTimer() {
    timeRemaining--;
    document.getElementById("time").textContent = timeRemaining;
    if (timeRemaining <= 0) {
        clearInterval(timer);
        feedback.textContent = "Time's up! The correct number was " + number + ".";
        playAgainButton.style.display = "inline-block"; // Show the play again button
    }
}

function resetGame() {
    number = Math.floor(Math.random() * parseInt(document.getElementById("level").value)) + 1;
    attempts = 0;
    timeRemaining = 30;
    feedback.textContent = "";
    clearInterval(timer);
    timer = setInterval(updateTimer, 1000);
    playAgainButton.style.display = "none"; // Hide the play again button
}