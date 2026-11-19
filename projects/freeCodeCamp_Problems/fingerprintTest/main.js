function checkLowerCase(fingerprint1, fingerprint2) {
    // check to make sure all characters are letters and lower case
    return fingerprint1 === fingerprint1.toLowerCase() && fingerprint2 === fingerprint2.toLowerCase();
}

function checkLength(fingerprint1, fingerprint2) {
    // Check to see that lengths are correct
    return fingerprint1.length === fingerprint2.length;
}

function main(fingerprint1, fingerprint2) {
    if (!checkLowerCase(fingerprint1, fingerprint2)) {
        return false; // Not all characters are lowercase letters
    }
    if (!checkLength(fingerprint1, fingerprint2)) {
        return false; // Lengths are not equal
    }

    let matchCount = 0;
    for (let i = 0; i < fingerprint1.length; i++) {
        if (fingerprint1[i] === fingerprint2[i]) {
            matchCount++;
        }
    }

    const matchRate = matchCount / fingerprint1.length;
    return matchRate >= 0.9; // Return true if match rate is 90% or higher
}

const checkMatchButton = document.getElementById('checkMatchButton');
checkMatchButton.addEventListener('click', () => {
    const fingerprintA = document.getElementById('fingerprintA').value;
    const fingerprintB = document.getElementById('fingerprintB').value;

    const isMatch = main(fingerprintA, fingerprintB);
    const outputContainer = document.querySelector('.outputContainer');
    outputContainer.textContent = (isMatch ? 'Fingerprints match!' : 'Fingerprints do not match.');
});