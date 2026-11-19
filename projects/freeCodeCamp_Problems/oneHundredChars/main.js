function main(char) {
    while (char.length < 100) {
        char += char;
    }
    return char.slice(0,100);
}

const submitButton = document.getElementById('submitChar');
submitButton.addEventListener('click', () => {
    const charString = document.getElementById("char").value;
    const output = main(charString)
    const outputContainer = document.querySelector(".outputContainer");
    outputContainer.textContent = output;
});