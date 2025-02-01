if (!('BarcodeDetector' in window))
  document.getElementById("box").innerHTML = 'QR Code reader is not compatible';
else {
    const video = document.querySelector('#video')
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({
        video: {
          facingMode: "environment"
        },
        audio: false
      })
          .then(stream => video.srcObject = stream);
    }
    let barcodeDetector = new BarcodeDetector({ formats: ['qr_code'] });
    setInterval(() => {
      barcodeDetector.detect(video).then(codes => {
        if (codes.length === 0) return;
        if (!codes[0].rawValue.startsWith('https://menu.hereus.net/')) return;
        if (codes[0].rawValue.split('/').length !== 4) return;
        document.getElementById("box").innerHTML = 'Loading...';
        barcodeDetector = null;
        window.location.pathname = `/${codes[0].rawValue.split('/')[3]}`;
      }).catch(err => {});
    }, 1000);
}