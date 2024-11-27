const digits = ['2', '6', '7', '8'];
const length = maxDigits;
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

const generateCombinations = (digits, length) => {
    if (length === 0) return [''];
    const smallerCombinations = generateCombinations(digits, length - 1);
    return digits.flatMap(d => smallerCombinations.map(sc => d + sc));
};

(async () => {
    for (const combination of generateCombinations(digits, length)) {
        try {
            const response = await fetch('https://hhc24-frostykeypad.holidayhackchallenge.com/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ answer: combination })
            });
            console.log(`Tried: ${combination}, Status: ${response.status}`);
            if (response.status === 200) return console.log(`Success: ${combination}`);
        } catch (error) {
            console.error(`Error trying combination ${combination}:`, error);
        }
        await sleep(100);
    }
})();
