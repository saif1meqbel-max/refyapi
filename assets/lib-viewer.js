(function () {
  const grid = document.getElementById('libGrid');
  const viewer = document.getElementById('libViewer');
  if (!grid || !viewer) return;

  const slides = Array.from(grid.querySelectorAll('.lib-card'));
  const img = viewer.querySelector('.lib-viewer-img');
  const titleEl = viewer.querySelector('.lib-viewer-title');
  const counterEl = viewer.querySelector('.lib-viewer-counter');
  const prevBtn = viewer.querySelector('.lib-nav-prev');
  const nextBtn = viewer.querySelector('.lib-nav-next');
  const zoomInBtn = viewer.querySelector('.lib-zoom-in');
  const zoomOutBtn = viewer.querySelector('.lib-zoom-out');
  const zoomResetBtn = viewer.querySelector('.lib-zoom-reset');
  const fullscreenBtn = viewer.querySelector('.lib-fullscreen');
  const filterBtns = document.querySelectorAll('.lib-filter');
  const stage = viewer.querySelector('.lib-viewer-stage');

  let index = 0;
  let zoom = 1;
  let filtered = slides;

  function visibleSlides() {
    return filtered.filter(s => !s.hidden);
  }

  function setZoom(z) {
    zoom = Math.min(3, Math.max(1, z));
    img.style.transform = `scale(${zoom})`;
    if (zoomResetBtn) zoomResetBtn.disabled = zoom === 1;
  }

  function show(i) {
    const list = visibleSlides();
    if (!list.length) return;
    index = ((i % list.length) + list.length) % list.length;
    const slide = list[index];
    const src = slide.dataset.src;
    const alt = slide.querySelector('img')?.alt || '';

    img.src = src;
    img.alt = alt;
    titleEl.innerHTML = slide.querySelector('.lib-card-title')?.innerHTML || '';
    counterEl.textContent = `${index + 1} / ${list.length}`;
    setZoom(1);

    slides.forEach(s => s.classList.toggle('active', s === slide));
    slide.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
  }

  function applyFilter(cat, startIdx) {
    filtered = slides.filter(s => cat === 'all' || s.dataset.category === cat);
    slides.forEach(s => {
      s.hidden = cat !== 'all' && s.dataset.category !== cat;
    });
    filterBtns.forEach(b => b.classList.toggle('on', b.dataset.filter === cat));
    show(startIdx !== undefined ? startIdx : 0);
  }

  filterBtns.forEach(b => {
    b.addEventListener('click', () => applyFilter(b.dataset.filter));
  });

  slides.forEach(slide => {
    slide.addEventListener('click', () => {
      const list = visibleSlides();
      const idx = list.indexOf(slide);
      if (idx >= 0) show(idx);
    });
  });

  prevBtn.addEventListener('click', () => show(index - 1));
  nextBtn.addEventListener('click', () => show(index + 1));

  if (zoomInBtn) zoomInBtn.addEventListener('click', () => setZoom(zoom + 0.25));
  if (zoomOutBtn) zoomOutBtn.addEventListener('click', () => setZoom(zoom - 0.25));
  if (zoomResetBtn) zoomResetBtn.addEventListener('click', () => setZoom(1));

  if (fullscreenBtn && stage.requestFullscreen) {
    fullscreenBtn.addEventListener('click', () => {
      if (document.fullscreenElement) document.exitFullscreen();
      else stage.requestFullscreen();
    });
  }

  document.addEventListener('keydown', e => {
    if (!viewer.contains(document.activeElement) && document.activeElement?.tagName === 'INPUT') return;
    if (e.key === 'ArrowLeft') { e.preventDefault(); show(index - 1); }
    if (e.key === 'ArrowRight') { e.preventDefault(); show(index + 1); }
    if (e.key === 'Escape' && document.fullscreenElement) document.exitFullscreen();
  });

  let touchX = 0;
  stage.addEventListener('touchstart', e => { touchX = e.changedTouches[0].clientX; }, { passive: true });
  stage.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - touchX;
    if (Math.abs(dx) > 50) show(dx > 0 ? index - 1 : index + 1);
  }, { passive: true });

  const hash = location.hash.replace('#', '');
  const startSlide = hash ? slides.find(s => s.id === hash) : null;
  const startIdx = startSlide ? visibleSlides().indexOf(startSlide) : 0;
  applyFilter('all', startIdx >= 0 ? startIdx : 0);
})();
