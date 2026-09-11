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

  const ZOOM_MIN = 1;
  const ZOOM_MAX = 5;
  const ZOOM_STEP = 0.35;

  let index = 0;
  let zoom = 1;
  let baseZoom = 1;
  let filtered = slides;

  function visibleSlides() {
    return filtered.filter(s => !s.hidden);
  }

  function applyTransform() {
    img.style.transform = `scale(${zoom})`;
    if (zoomResetBtn) zoomResetBtn.disabled = Math.abs(zoom - baseZoom) < 0.01;
  }

  function setZoom(z, { isBase } = {}) {
    zoom = Math.min(ZOOM_MAX, Math.max(ZOOM_MIN, z));
    if (isBase) baseZoom = zoom;
    applyTransform();
  }

  function fitToStage() {
    if (!img.naturalWidth) return;
    const pad = 48;
    const maxW = Math.min(stage.clientWidth - pad, 1200);
    const maxH = Math.min(stage.clientHeight - pad, 700);
    const fit = Math.min(maxW / img.naturalWidth, maxH / img.naturalHeight, 1);
    setZoom(Math.max(fit, ZOOM_MIN), { isBase: true });
  }

  function show(i) {
    const list = visibleSlides();
    if (!list.length) return;
    index = ((i % list.length) + list.length) % list.length;
    const slide = list[index];
    const src = slide.dataset.src;
    const alt = slide.querySelector('img')?.alt || '';

    img.onload = fitToStage;
    img.src = src;
    img.alt = alt;
    if (img.complete) fitToStage();
    titleEl.innerHTML = slide.querySelector('.lib-card-title')?.innerHTML || '';
    counterEl.textContent = `${index + 1} / ${list.length}`;

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

  if (zoomInBtn) zoomInBtn.addEventListener('click', () => setZoom(zoom + ZOOM_STEP));
  if (zoomOutBtn) zoomOutBtn.addEventListener('click', () => setZoom(zoom - ZOOM_STEP));
  if (zoomResetBtn) zoomResetBtn.addEventListener('click', () => setZoom(baseZoom, { isBase: true }));

  img.addEventListener('dblclick', () => {
    if (zoom > baseZoom + 0.05) setZoom(baseZoom, { isBase: true });
    else setZoom(Math.min(2.5, ZOOM_MAX));
  });

  stage.addEventListener('wheel', e => {
    if (!e.ctrlKey && !e.metaKey) return;
    e.preventDefault();
    setZoom(zoom + (e.deltaY < 0 ? ZOOM_STEP : -ZOOM_STEP));
  }, { passive: false });

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
    if (e.key === '+' || e.key === '=') { e.preventDefault(); setZoom(zoom + ZOOM_STEP); }
    if (e.key === '-') { e.preventDefault(); setZoom(zoom - ZOOM_STEP); }
    if (e.key === '0') { e.preventDefault(); setZoom(baseZoom, { isBase: true }); }
    if (e.key === 'Escape' && document.fullscreenElement) document.exitFullscreen();
  });

  let touchX = 0;
  stage.addEventListener('touchstart', e => { touchX = e.changedTouches[0].clientX; }, { passive: true });
  stage.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - touchX;
    if (Math.abs(dx) > 50) show(dx > 0 ? index - 1 : index + 1);
  }, { passive: true });

  window.addEventListener('resize', () => {
    if (img.src) fitToStage();
  });

  const hash = location.hash.replace('#', '');
  const startSlide = hash ? slides.find(s => s.id === hash) : null;
  const startIdx = startSlide ? visibleSlides().indexOf(startSlide) : 0;
  applyFilter('all', startIdx >= 0 ? startIdx : 0);
})();
