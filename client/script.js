document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const results = await response.json();
    document.getElementById('result').innerText = JSON.stringify(results, null, 2);
});
