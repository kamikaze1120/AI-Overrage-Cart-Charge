document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const overageFee = parseFloat(document.getElementById('overage').value);
    
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];
    
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const data = new Uint8Array(e.target.result);
            const workbook = XLSX.read(data, {type: 'array'});
            const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
            const jsonData = XLSX.utils.sheet_to_json(firstSheet);
            
            const results = jsonData.map(row => {
                const bagsCount = row.BagsCount;
                const recordID = row.RecordID;
                const fee = bagsCount > 5 ? (bagsCount - 5) * overageFee : 0;
                return { RecordID: recordID, OverloadedBags: bagsCount, FeeAssigned: fee };
            });

            document.getElementById('result').innerText = JSON.stringify(results, null, 2);
        };
        reader.readAsArrayBuffer(file);
    }
});
