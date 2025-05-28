window.addEventListener('DOMContentLoaded', () => {
  // Create and insert canvas into the DOM
  const canvas = document.createElement('canvas');
  canvas.id = 'flowCanvas';
  document.body.prepend(canvas);

  const ctx = canvas.getContext('2d');

  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  let t = 0;

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();

    const targetY = window.innerWidth <= 600 ? 180 : canvas.height / 2;

    for (let x = 0; x < canvas.width; x += 10) {
      const noise = (Math.random() - 0.5) * 2;
      const verticalShift = Math.sin(t * 5); // drift
      const y = targetY + Math.sin(x * 0.008 + t) * 40 + noise + verticalShift;

      ctx.lineTo(x, y);
    }

    ctx.strokeStyle = 'rgba(150,150,150,0.2)';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    t += 0.01;
    requestAnimationFrame(animate);
  }

  animate();
});
