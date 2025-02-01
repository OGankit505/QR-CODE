document.getElementById("qrForm").addEventListener("submit", function (event) {
    event.preventDefault();

    let formData = new FormData(this);

    fetch("http://127.0.0.1:5000/generate_qr", {  // Ensure correct API URL
        method: "POST",
        body: formData
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to generate QR code");
            }
            return response.blob();
        })
        .then(blob => {
            let imgURL = URL.createObjectURL(blob);

            // Display QR Code
            let qrContainer = document.getElementById("qrCodeContainer");
            qrContainer.innerHTML = ""; // Clear old QR codes
            let imgElement = document.createElement("img");
            imgElement.src = imgURL;
            imgElement.alt = "QR Code";
            imgElement.style.maxWidth = "250px";
            qrContainer.appendChild(imgElement);

            // Enable Download Button
            let downloadBtn = document.getElementById("downloadBtn");
            downloadBtn.href = imgURL;
            downloadBtn.download = "qrcode.png";
            downloadBtn.style.display = "block";
        })
        .catch(error => console.error("Error:", error));
});