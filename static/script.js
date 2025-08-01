const background = document.querySelector('.background');

document.addEventListener('mousemove', (e) => {
  const x = (e.clientX / window.innerWidth) * 100;
  const y = (e.clientY / window.innerHeight) * 100;

  background.style.background = `radial-gradient(circle at ${x}% ${y}%, #1565c0, #001f3f)`;
});
