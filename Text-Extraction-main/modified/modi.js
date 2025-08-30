function extractText() {
  const file = document.getElementById("imageInput").files[0];
  if (!file) {
      alert("Please upload an image first!");
      return;
  }

  const formData = new FormData();
  formData.append("image", file);

  fetch('/extract-text', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      if (data.text) {
          document.getElementById("output").innerText = data.text;
      } else {
          alert(data.error);
      }
  })
  .catch(err => {
      alert("Error extracting text: " + err);
  });
}
