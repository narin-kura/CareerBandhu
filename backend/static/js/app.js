const API = '';
let skills = [], ratingVal = 0, currentId = null, currentMode = 'career';
let allCareers = [], selectedCareerId = null, checkedSkills = new Set();
let region = 'IN';
let currentCareerData = null;
let activeCollar = 'all';
let careerQuery = '';

const COLLAR_META = [
  { key:'white', icon:'⚪', label:'White-collar' , tip:'Office & knowledge work',      clr:'#475569', bg:'#f1f5f9' },
  { key:'blue',  icon:'🔵', label:'Blue-collar'  , tip:'Physical & skilled trades',    clr:'#1d4ed8', bg:'#eff6ff' },
  { key:'pink',  icon:'🩷', label:'Pink-collar'  , tip:'Service & care roles',         clr:'#db2777', bg:'#fdf2f8' },
  { key:'gray',  icon:'🔘', label:'Gray-collar'  , tip:'Technical blend',              clr:'#4b5563', bg:'#f9fafb' },
  { key:'gold',  icon:'🟡', label:'Gold-collar'  , tip:'Elite & highly specialised',   clr:'#b45309', bg:'#fffbeb' },
  { key:'new',   icon:'🆕', label:'New-collar'   , tip:'Skills-based tech',            clr:'#6d28d9', bg:'#f5f3ff' },
  { key:'green', icon:'🟢', label:'Green-collar' , tip:'Environment & nature',         clr:'#15803d', bg:'#f0fdf4' },
  { key:'red',   icon:'🔴', label:'Red-collar'   , tip:'Government & public sector',   clr:'#b91c1c', bg:'#fef2f2' },
  { key:'brown', icon:'🟤', label:'Brown-collar' , tip:'Agriculture & military',       clr:'#92400e', bg:'#fefce8' },
  { key:'no',    icon:'🎨', label:'No-collar'    , tip:'Passion & arts',               clr:'#c2410c', bg:'#fff7ed' },
  { key:'open',  icon:'💻', label:'Open-collar'  , tip:'Remote & freelance',           clr:'#0e7490', bg:'#ecfeff' },
];

const COLLAR_DESC = {
  white: 'Office-based, knowledge-intensive roles — managers, analysts, lawyers, accountants, HR professionals. Usually desk jobs in air-conditioned offices.',
  blue:  'Physical or manual skilled labour — electricians, plumbers, welders, drivers, construction workers. Often require trade apprenticeships or ITI training.',
  pink:  'Service and people-facing roles — nurses, teachers, receptionists, beauticians, hospitality staff. Centred on care and interpersonal skills.',
  gray:  'A technical blend of physical and knowledge work — technicians, engineers on the floor, quality controllers. Bridge between blue and white collar.',
  gold:  'Highly specialised, elite professionals — top surgeons, IFS officers, senior scientists, BCBAs. Typically require advanced degrees and years of experience.',
  new:   'Skills-based tech roles where certificates or portfolios beat traditional degrees — web developers, data analysts, animators, UI/UX designers.',
  green: 'Careers focused on environment, sustainability, and nature — horticulturists, solar technicians, environmental scientists, conservationists.',
  red:   'Government and public-sector employees — civil servants, IAS/IPS officers, government doctors, public school teachers. Driven by PSC/UPSC exams.',
  brown: 'Agriculture, forestry, and military — farmers, army/navy/air force personnel, forest officers. Outdoor and field-heavy work.',
  no:    'Passion-driven creative careers without a fixed institution — artists, musicians, actors, sculptors, street performers. Portfolio is everything.',
  open:  'Remote, freelance, or location-independent roles — translators, podcasters, freelance designers, digital consultants. Work from anywhere.',
};

function openCollarGuide() {
  const list = document.getElementById('collar-guide-list');
  list.innerHTML = COLLAR_META.map(m => `
    <div class="cg-row">
      <div class="cg-ico">${m.icon}</div>
      <div class="cg-body">
        <div class="cg-name">${m.label}</div>
        <div class="cg-tip">${COLLAR_DESC[m.key] || m.tip}</div>
      </div>
    </div>`).join('');
  document.getElementById('collar-modal').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeCollarGuide(e) {
  if (e && e.target !== document.getElementById('collar-modal')) return;
  document.getElementById('collar-modal').classList.remove('open');
  document.body.style.overflow = '';
}

function dismissBanner() {
  document.getElementById('welcome-banner').classList.add('hidden');
  try { localStorage.setItem('cb_welcomed', '1'); } catch(_) {}
}
function initWelcomeBanner() {
  try { if (localStorage.getItem('cb_welcomed')) { dismissBanner(); } } catch(_) {}
}

const POPULAR_SKILLS = {
  IN: ['Cooking','Driving','Sewing & Stitching','Teaching','Electrical Wiring',
       'Customer Service','Communication','Sales','MS Excel','Accounting',
       'Photography','Hair Styling','Welding Techniques','Patient Care','Crop Knowledge',
       'Physical Fitness','General Knowledge','Python','Leadership','Mathematics'],
  US: ['Programming','Python','Communication','Customer Service','MS Excel',
       'Patient Care','Driving','Electrical Wiring','Project Management','Data Analysis',
       'Welding Techniques','Marketing Strategy','Accounting','Leadership','Problem Solving',
       'Teaching','Physical Fitness','SQL','Mechanical Aptitude','Creativity'],
};

const CAREER_PICKS = {
  IN: ['Air Traffic Controller','Indian Army Officer','Chartered Accountant (CA)',
       'Space Scientist / Aerospace Engineer (ISRO)','Electrician','Nurse / Nursing Professional',
       'Civil Servant — IAS / IPS / IFS','Merchant Navy Officer (Deck / Marine Engineer)','Chef / Cook','Investment Banker'],
  US: ['Software Engineer','Registered Nurse (RN)','Commercial Airline Pilot','Investment Banker',
       'Electrician','Data Scientist','Police Officer','HVAC Technician','Accountant / CPA','Actuary'],
};

const CAT_ICONS = {
  'Technology':'💻','Data & Analytics':'📊','Business & Management':'💼',
  'Finance':'💰','Marketing & Sales':'📣','Design & Creative':'🎨',
  'Human Resources':'👥','Education & Training':'📚','Healthcare':'🏥',
  'Trades & Construction':'🔧','Food & Hospitality':'🍳','Beauty & Wellness':'💆',
  'Fashion & Apparel':'👗','Transport & Logistics':'🚚','Agriculture & Farming':'🌾',
  'Arts & Performance':'🎭','Government & Public Service':'🏛️',
  'Retail & Commerce':'🛍️','Social Work & Community':'🤝','Media & Journalism':'📰',
  'Aviation & Airport':'✈️','Defence & Armed Forces':'🎖️','Maritime & Shipping':'⚓',
  'Science & Research':'🔬',
  'Mythology & Culture':'📜','Film & Entertainment':'🎬','Animation Industry':'🎞️',
  'Mental Health & Therapy':'🧠','Entrepreneurship & MSME':'🏭',
  'Arts & Crafts':'🎨','Language & Diplomacy':'🌐','Trading & Commodities':'📈',
  'Medical Supplies & Distribution':'🏥','Manufacturing & Production':'⚙️',
  'Supply Chain & Logistics':'🚚','Media & Broadcasting':'📺',
  'Everyday Work & Trades':'🔨',
  'Legal & Justice':'⚖️','Real Estate & Property':'🏠','Insurance & Actuarial':'🛡️',
  'Sports & Athletics':'🏆','Music Industry':'🎵','Gaming & Esports':'🎮',
  'Aerospace & Space':'🚀','Automotive & EV':'🚗','Veterinary & Animal Care':'🐾',
  'Forensic & Investigation':'🔍','Architecture & Urban Planning':'🏗️',
  'Energy & Utilities':'⚡','Food Science & Nutrition':'🥗',
  'Publishing & Writing':'📝','Photography & Visual Media':'📷',
  'Spiritual & Religious':'🙏','Gemology & Jewelry':'💎',
  'Biotechnology & Pharma R&D':'🧬','NGO & Development':'🌱',
  'Library & Information Science':'📖'
};

async function init() {
  try {
    await get('/api/health', 15000);
    setDot('g'); setLbl('Live');
  } catch { setDot('r'); setLbl('Offline'); }
  await loadCareers();
  renderSugs(); renderChips();
}

async function loadCareers() {
  try {
    const c = await get(`/api/careers?region=${region}`);
    allCareers = c.careers || [];
    document.getElementById('stat-c').textContent = allCareers.length + '+';
    activeCollar = 'all';
    renderCollarFilter(); renderCareerSugs(); renderCareerDropdown(''); renderMoreFields();
    initWelcomeBanner();
  } catch {}
}

function quickExplore(category) {
  switchMode('career');
  document.getElementById('career-search').value = category;
  filterCareers();
  document.querySelector('.sidebar').scrollIntoView({behavior:'smooth', block:'start'});
}

const HF_INITIAL = ['Technology','Healthcare','Government & Public Service','Design & Creative','Science & Research','Business & Management','Education & Training','Trades & Construction'];
function renderMoreFields() {
  const more = document.getElementById('hf-more');
  if (!more || !allCareers.length) return;
  const cats = [...new Set(allCareers.map(c => c.category))].filter(c => !HF_INITIAL.includes(c)).sort();
  more.innerHTML = cats.map(c => `<button class="field-pill" onclick="quickExplore('${esc(c)}')">${CAT_ICONS[c]||'📌'} ${c}</button>`).join('');
}
function toggleMoreFields() {
  const more = document.getElementById('hf-more');
  const btn = document.getElementById('hf-toggle');
  const open = more.classList.toggle('open');
  btn.textContent = open ? 'Show fewer fields ▴' : 'Show more fields ▾';
}

async function switchRegion(r) {
  if (r === region) return;
  region = r;
  document.getElementById('rg-IN').className = r==='IN'?'on':'';
  document.getElementById('rg-US').className = r==='US'?'on':'';
  // reset selections that no longer apply
  selectedCareerId = null;
  document.getElementById('career-search').value = '';
  careerQuery = '';
  document.getElementById('selected-box').style.display = 'none';
  await loadCareers();
  renderSugs();
  switchMode(currentMode); // reset results pane to a clean empty state
}

function setDot(c) { document.getElementById('api-dot').className = `dot ${c}`; }
function setLbl(t) { document.getElementById('api-lbl').textContent = t; }
async function fetchJSON(path, opts, timeoutMs = 35000) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), timeoutMs);
  try {
    const r = await fetch(API+path, {...opts, signal: ctrl.signal});
    if (!r.ok) throw Error(r.status);
    return await r.json();
  } catch (e) {
    if (e.name === 'AbortError') throw Error('timeout');
    throw e;
  } finally {
    clearTimeout(timer);
  }
}
async function get(path, timeoutMs) { return fetchJSON(path, undefined, timeoutMs); }
async function post(path, body) { return fetchJSON(path, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}); }
function describeError(e) {
  if (e && e.message === 'timeout') return 'The server is waking up from sleep (free hosting tier) — this can take up to a minute. Please try again.';
  return `Something went wrong${e && e.message ? ` (${e.message})` : ''}. Please try again.`;
}

function switchMode(m) {
  currentCareerData = null;
  currentMode = m;
  document.getElementById('tab-skills').className = m==='skills'?'on':'';
  document.getElementById('tab-career').className = m==='career'?'on career':'';
  document.getElementById('panel-skills').style.display = m==='skills'?'':'none';
  document.getElementById('panel-career').style.display = m==='career'?'':'none';
  document.getElementById('search-pane').style.display = '';
  document.getElementById('detail').style.display = 'none';
  if (m === 'career') renderCollarFilter();
  setResults(`<div class="empty"><div class="emo">${m==='skills'?'🎯':'🔍'}</div><h3>${m==='skills'?'Match me to careers':'Explore any career'}</h3><p>${m==='skills'?'Add your skills and tap <strong>Find matching careers</strong>.':'Search or pick a career and tap <strong>Show skills needed</strong>.'}</p></div>`);
}

/* skills mode */
function addSkill(name) {
  const n = name.trim();
  if (!n || skills.some(s=>s.toLowerCase()===n.toLowerCase())) return;
  skills.push(n); renderChips();
}
function addFromInput() { const el=document.getElementById('skill-in'); addSkill(el.value); el.value=''; el.focus(); }
function removeSkill(name) { skills=skills.filter(s=>s!==name); renderChips(); }
function renderChips() {
  const el = document.getElementById('chips');
  el.innerHTML = skills.length
    ? skills.map(s=>`<span class="chip">${s}<x onclick="removeSkill('${esc(s)}')">×</x></span>`).join('')
    : '<span class="hint">No skills added yet</span>';
}
function renderSugs() {
  document.getElementById('sugs').innerHTML = (POPULAR_SKILLS[region]||POPULAR_SKILLS.IN).map(s=>`<span class="sug" onclick="addSkill('${esc(s)}')">${s}</span>`).join('');
}
document.getElementById('skill-in').addEventListener('keydown',e=>{ if(e.key==='Enter') addFromInput(); });

/* career mode */
function renderCareerSugs() {
  const picks = CAREER_PICKS[region] || CAREER_PICKS.IN;
  document.getElementById('career-sugs').innerHTML = picks.map(t => {
    const c = allCareers.find(c=>c.title===t);
    return c ? `<span class="sug nv" onclick="selectCareer('${c.id}','${esc(c.title)}')">${t}</span>` : '';
  }).filter(Boolean).join('');
}
function renderCollarFilter(q = '') {
  const ql = q.toLowerCase();
  const pool = ql
    ? allCareers.filter(c => c.title.toLowerCase().includes(ql) || c.category.toLowerCase().includes(ql))
    : allCareers;
  const counts = {};
  for (const c of pool) counts[c.collar] = (counts[c.collar]||0) + 1;
  const total = pool.length;
  const isAll = activeCollar === 'all';
  const activeMeta = COLLAR_META.find(m => m.key === activeCollar);

  const trigger = document.getElementById('collar-trigger');
  if (trigger) {
    const trgIcon = isAll ? '🌐' : (activeMeta ? activeMeta.icon : '🌐');
    trigger.style.setProperty('--c-clr', isAll ? '#4338ca' : (activeMeta ? activeMeta.clr : '#4338ca'));
    trigger.style.setProperty('--c-bg', isAll ? '#eef2ff' : (activeMeta ? activeMeta.bg : '#eef2ff'));
    trigger.innerHTML = `
      <span class="c-ico-wrap"><span class="c-ico">${trgIcon}</span></span>
      <span class="c-body">
        <span class="c-lbl">${isAll ? 'All career paths' : activeMeta.label.replace('-collar',' careers')}</span>
        <span class="c-tip">${isAll ? 'Browse the full catalogue' : activeMeta.tip}</span>
      </span>
      <span class="c-cnt">${isAll ? total : (counts[activeCollar] || 0)}</span>
      <span class="collar-chev">▾</span>
    `;
  }

  let html = `<button class="collar-btn collar-all${isAll?' active':''}" data-collar="all"
    style="--c-clr:#4338ca;--c-bg:#eef2ff" onclick="setCollar('all')">
    <span class="c-ico-wrap"><span class="c-ico">🌐</span></span>
    <span class="c-body">
      <span class="c-lbl">All career paths</span>
      <span class="c-tip">Browse the full catalogue</span>
    </span>
    <span class="c-cnt">${total}</span>
  </button>`;

  for (const m of COLLAR_META) {
    const cnt = counts[m.key] || 0;
    if (!ql && !cnt) continue;
    const active = activeCollar === m.key;
    const dimmed = ql && cnt === 0;
    html += `<button class="collar-btn${active?' active':''}${dimmed?' dimmed':''}" data-collar="${m.key}"
      style="--c-clr:${m.clr};--c-bg:${m.bg}" onclick="setCollar('${m.key}')" title="${m.tip}">
      <span class="c-ico-wrap"><span class="c-ico">${m.icon}</span></span>
      <span class="c-body">
        <span class="c-lbl">${m.label.replace('-collar',' careers')}</span>
        <span class="c-tip">${m.tip}</span>
      </span>
      <span class="c-cnt">${cnt}</span>
    </button>`;
  }
  const el = document.getElementById('collar-dropdown');
  if (el) el.innerHTML = html;
}
function toggleCollarDrop(e) {
  e.stopPropagation();
  const dd = document.getElementById('collar-dropdown');
  const open = dd.classList.toggle('open');
  document.getElementById('collar-trigger').setAttribute('aria-expanded', open ? 'true' : 'false');
}
function closeCollarDrop() {
  document.getElementById('collar-dropdown').classList.remove('open');
  document.getElementById('collar-trigger').setAttribute('aria-expanded', 'false');
}
document.addEventListener('click', e => { if (!e.target.closest('.collar-combo')) closeCollarDrop(); });
function setCollar(key) {
  activeCollar = key;
  renderCollarFilter(careerQuery);
  renderCareerDropdown(careerQuery);
  closeCollarDrop();
  if (key === 'all') {
    setResults(`<div class="empty"><div class="emo">🔍</div><h3>Explore any career</h3><p>Pick a collar type above, search, or choose from popular paths.</p></div>`);
  } else {
    showCollarCareers(key);
  }
}

function showCollarCareers(collarKey) {
  const meta = COLLAR_META.find(m => m.key === collarKey);
  if (!meta) return;
  const careers = allCareers.filter(c => c.collar === collarKey);
  if (!careers.length) {
    setResults(`<div class="empty"><div class="emo">${meta.icon}</div><h3>No ${meta.label}-collar careers in this region yet</h3></div>`);
    return;
  }
  const byCat = {};
  for (const c of careers) (byCat[c.category] = byCat[c.category] || []).push(c);
  let html = `
    <div class="collar-header" style="background:linear-gradient(135deg,${meta.clr}dd,${meta.clr}99)">
      <div class="collar-hero-icon">${meta.icon}</div>
      <div>
        <div class="collar-title">${meta.label} careers</div>
        <div class="collar-subtitle">${meta.tip} &nbsp;·&nbsp; ${careers.length} careers — tap any to explore</div>
      </div>
    </div>`;
  for (const [cat, cs] of Object.entries(byCat)) {
    html += `<div class="collar-section">
      <div class="collar-cat-label">${CAT_ICONS[cat]||'📌'} ${cat}</div>
      ${cs.map(c=>`<div class="card" onclick="selectAndExplore('${c.id}','${esc(c.title)}')">
        <div class="card-body">
          <div class="card-top">
            <div class="cc-icon" style="--ic-clr:${meta.clr};--ic-bg:${meta.bg}">${CAT_ICONS[c.category]||meta.icon}</div>
            <div class="cc-info">
              <div class="cc-eyebrow">${cat}</div>
              <div class="card-title">${c.title}</div>
            </div>
          </div>
          <div class="cc-pills" style="margin-top:13px">
            ${c.growth_outlook?`<span class="stat-pill">📈 ${c.growth_outlook}</span>`:''}
            <span class="stat-pill">${c.region==='US'?'🇺🇸 USA':'🇮🇳 India'}</span>
          </div>
        </div>
        <div class="card-foot"><div class="meta"><span>${meta.icon} ${meta.label.replace('-collar',' career')}</span></div><span class="view">Explore career →</span></div>
      </div>`).join('')}
    </div>`;
  }
  setResults(html);
}

async function selectAndExplore(id, title) {
  selectCareer(id, title);
  await exploreCareer();
}

function renderCareerDropdown(q) {
  const drop = document.getElementById('dropdown');
  let pool = allCareers;
  if (activeCollar !== 'all') pool = pool.filter(c => c.collar === activeCollar);
  const filtered = q ? pool.filter(c=>c.title.toLowerCase().includes(q.toLowerCase())||c.category.toLowerCase().includes(q.toLowerCase())) : pool;
  if(!filtered.length) { drop.innerHTML='<div class="dd-empty">No careers found</div>'; return; }
  const byCat = {};
  for (const c of filtered) (byCat[c.category]=byCat[c.category]||[]).push(c);
  drop.innerHTML = Object.entries(byCat).map(([cat, cs]) =>
    `<div class="dd-cat">${CAT_ICONS[cat]||'📌'} ${cat}</div>
     ${cs.map(c=>`<div class="dd-item" onclick="selectCareer('${c.id}','${esc(c.title)}')">${CAT_ICONS[c.category]||'📌'} ${c.title}</div>`).join('')}`).join('');
}
function filterCareers() {
  const q = document.getElementById('career-search').value;
  careerQuery = q;
  renderCollarFilter(q);
  renderCareerDropdown(q);
  document.getElementById('dropdown').classList.add('open');
}
function openDrop() { document.getElementById('dropdown').classList.add('open'); renderCareerDropdown(''); }
document.addEventListener('click', e => { if(!e.target.closest('.combo')) document.getElementById('dropdown').classList.remove('open'); });
function selectCareer(id, title) {
  selectedCareerId = id;
  document.getElementById('career-search').value = title;
  careerQuery = '';
  document.getElementById('dropdown').classList.remove('open');
  document.getElementById('selected-box').style.display = '';
  document.getElementById('selected-name').textContent = title;
  renderCollarFilter();
  renderCareerDropdown('');
}

/* actions */
async function findCareers() {
  if (!skills.length) { alert('Please add at least one skill first.'); return; }
  const btn = document.getElementById('find-btn');
  btn.disabled = true; btn.textContent = 'Searching…';
  setResults('<div class="status"><div class="spinner"></div><p>Matching your skills…</p></div>');
  try { const d = await post('/api/recommend', {skills, region}); renderResults(d.recommendations||[]); }
  catch(e) { setResults(`<div class="empty"><div class="emo">⚠️</div><h3>${describeError(e)}</h3><button class="full-cta" onclick="findCareers()">Try again</button></div>`); }
  btn.disabled=false; btn.textContent='Find matching careers';
}
async function exploreCareer() {
  if (!selectedCareerId) { alert('Please select a career first.'); return; }
  const btn = document.getElementById('career-btn');
  btn.disabled=true; btn.textContent='Loading…';
  setResults('<div class="status"><div class="spinner"></div><p>Loading career details…</p></div>');
  checkedSkills.clear();
  currentCareerData = null;
  try {
    const [cv, gv] = await Promise.all([ get(`/api/career/${selectedCareerId}`), post(`/api/career/${selectedCareerId}/gap`, {skills: []}) ]);
    renderCareerSkillView(cv, gv);
  } catch(e) {
    setResults(`<div class="empty"><div class="emo">⚠️</div><h3>${describeError(e)}</h3><button class="full-cta" onclick="exploreCareer()">Try again</button></div>`);
  } finally {
    btn.disabled=false; btn.textContent='Show skills needed';
  }
}

function setResults(html) { document.getElementById('results-area').innerHTML = html; }
function col(s) { return s>=60?'var(--ok)':s>=30?'var(--wn)':'var(--bd-c)'; }
function rankClass(i) { return i===0?'g':i===1?'s':i===2?'b':'n'; }

function renderResults(list) {
  if(!list.length) { setResults('<div class="empty"><div class="emo">🤔</div><h3>No matches found</h3><p>Try adding more skills — trades, soft skills, or tools you know.</p></div>'); return; }
  const hdr = `<div class="results-head"><h3>Career matches for you</h3><span class="count">${list.length} found</span></div>`;
  const cards = list.map((r,i) => {
    const sc=r.score, c=col(sc), cr=r.career;
    const meta = COLLAR_META.find(m=>m.key===cr.collar) || {clr:'#4338CA', bg:'#EEF2FF', icon:'📌', label:'Career'};
    const haves=(r.matching_skills||[]).slice(0,3).map(s=>`<span class="tag have">${s.skill}</span>`).join('');
    const needs=(r.top_gaps||[]).slice(0,2).map(s=>`<span class="tag need">${s.skill}</span>`).join('');
    const sal = cr.salary_range ? formatSal(cr.salary_range) : '';
    return `<div class="card" onclick="openDetail('${cr.id}','skills')">
      <div class="card-body">
        <div class="card-top">
          <div class="cc-icon" style="--ic-clr:${meta.clr};--ic-bg:${meta.bg}">${CAT_ICONS[cr.category]||meta.icon}</div>
          <div class="cc-info">
            <div class="cc-eyebrow">${cr.category}</div>
            <div class="card-title">${cr.title}</div>
          </div>
          <div class="score"><div class="pct" style="color:${c}">${sc}%</div><div class="pl">Match</div></div>
        </div>
        ${cr.description?`<p class="cc-desc">${cr.description}</p>`:''}
        <div class="cc-pills">
          ${sal?`<span class="stat-pill">💰 ${sal}</span>`:''}
          <span class="stat-pill">📈 ${cr.growth_outlook||'Good'}</span>
          <span class="stat-pill">${meta.icon} ${meta.label.replace('-collar',' collar')}</span>
        </div>
        <div class="track"><div style="width:${sc}%;background:${c}"></div></div>
        <div class="tags">${haves}${needs}</div>
      </div>
      <div class="card-foot"><div class="meta"><span>📋 Tap for the full skill roadmap</span></div><span class="view">View gap →</span></div>
    </div>`;
  }).join('');
  setResults(hdr + cards);
}

function renderCareerSkillView(cv, gv) {
  currentCareerData = cv.career;
  const c = cv.career, g = gv;
  const byLv = {critical:[],important:[],helpful:[]};
  for (const gap of (g.gaps||[])) (byLv[gap.level]=byLv[gap.level]||[]).push(gap);
  const labels = {critical:'Critical skills', important:'Important skills', helpful:'Helpful skills'};

  const sections = ['critical','important','helpful'].map(lv => {
    const items = byLv[lv]||[]; if(!items.length) return '';
    return `<div class="group"><span class="level ${lv[0]}">${labels[lv]}</span>
      ${items.map(gap => {
        const res=(g.resources||{})[gap.skill]||[]; const r2=res.find(r=>r.free)||res[0];
        const link=r2?`<a class="res-link" href="${r2.url}" target="_blank" rel="noopener" onclick="event.stopPropagation()">${r2.platform}</a>`:'';
        return `<div class="skill-row tick" onclick="toggleSkillCheck(this,'${esc(gap.skill)}')">
          <input type="checkbox" onclick="event.stopPropagation();toggleSkillCheck(this.parentElement,'${esc(gap.skill)}')">
          <span class="sname">${gap.skill}</span>${link}
        </div>`;
      }).join('')}</div>`;
  }).join('');

  const sal = c.salary_range ? formatSal(c.salary_range) : '';
  const entry = (c.entry_paths||[]).map(p=>`<div class="entry">${p}</div>`).join('');
  const quals = (c.qualifications||[]).map(q=>`<div class="entry">${q}</div>`).join('');
  const total = (g.gaps||[]).length;

  const meta = COLLAR_META.find(m=>m.key===c.collar);
  setResults(`
    <div class="d-hero career">
      <div class="d-icon">${CAT_ICONS[c.category]||'📌'}</div>
      <div class="d-top">
        <div>
          <div class="d-title">${c.title}</div>
          <div class="d-cat">${c.category}${meta ? ` · ${meta.icon} ${meta.label}` : ''}</div>
        </div>
        <div class="d-score"><div class="n">${total}</div><div class="s">Skills mapped</div></div>
      </div>
      <p class="d-desc">${c.description}</p>
      <div class="d-pills">
        ${sal?`<span class="d-pill">💰 ${sal}</span>`:''}
        <span class="d-pill">📈 ${c.growth_outlook}</span>
        ${meta?`<span class="d-pill">${meta.icon} ${meta.tip}</span>`:''}
      </div>
    </div>

    ${quals?`<div class="box"><div class="box-title">📜 Prerequisites &amp; qualifications</div>${quals}</div>`:''}

    ${entry?`<div class="box"><div class="box-title">🎓 Pathways into this career</div>${entry}</div>`:''}

    <div class="box">
      <div class="box-title">📘 Curriculum — skills you'll need, tick what you already have</div>
      <div id="skill-checker">${sections}</div>
      <div class="live-box">
        <div class="k">Your live match score</div>
        <div class="live-track"><div id="live-fill"></div></div>
        <div class="live-text" id="live-text">0% — tick the skills you already have</div>
      </div>
    </div>

    <button class="full-cta" onclick="openDetail('${c.id}','career')">Run full gap analysis →</button>
  `);
  updateLiveScore(c);
}

function toggleSkillCheck(el, skillName) {
  const cb = el.querySelector('input[type=checkbox]');
  const nowChecked = !checkedSkills.has(skillName);
  if(nowChecked) { checkedSkills.add(skillName); el.classList.add('checked'); if(cb) cb.checked=true; }
  else { checkedSkills.delete(skillName); el.classList.remove('checked'); if(cb) cb.checked=false; }
  if(currentCareerData) updateLiveScore(currentCareerData);
}
function updateLiveScore(c) {
  const req = c.required_skills||[]; const wts={critical:3,important:2,helpful:1};
  let total=0, earned=0;
  for(const s of req){ const w=wts[s.level]||1; total+=w; if(checkedSkills.has(s.skill)) earned+=w; }
  const pct = total>0 ? Math.round(earned/total*100) : 0;
  const fill=document.getElementById('live-fill'), txt=document.getElementById('live-text');
  const clr = pct>=60?'var(--ok)':pct>=30?'var(--wn)':'var(--bd-c)';
  if(fill){ fill.style.width=pct+'%'; fill.style.background=clr; }
  if(txt) txt.textContent = `${pct}% — ${pct>=60?'Great fit! 🎉':pct>=30?'Good start, keep learning 💪':'Tick the skills you already have 👇'}`;
}

function formatSal(sr) {
  if(sr.currency==='INR/month') return `₹${(sr.min/1000)|0}k–₹${(sr.max/1000)|0}k/mo`;
  return `$${(sr.min/1000)|0}k–$${(sr.max/1000)|0}k/yr`;
}

async function openDetail(id, fromMode) {
  currentId = id; ratingVal = 0;
  document.getElementById('search-pane').style.display = 'none';
  document.getElementById('detail').style.display = 'block';
  document.getElementById('detail-body').innerHTML = '<div class="status"><div class="spinner"></div><p>Running gap analysis…</p></div>';
  window.scrollTo({top:0,behavior:'smooth'});
  const mySkills = fromMode==='career' ? Array.from(checkedSkills) : skills;
  try {
    const [cv,gv] = await Promise.all([ get(`/api/career/${id}`), post(`/api/career/${id}/gap`,{skills:mySkills}) ]);
    renderDetail(cv, gv);
  } catch(e) { document.getElementById('detail-body').innerHTML=`<div class="empty"><div class="emo">⚠️</div><h3>${describeError(e)}</h3><button class="full-cta" onclick="openDetail('${id}','${fromMode}')">Try again</button></div>`; }
}

function renderDetail(cv, gv) {
  const c=cv.career, g=gv, sc=g.score;
  const byLv={critical:[],important:[],helpful:[]};
  for(const gap of (g.gaps||[])) (byLv[gap.level]=byLv[gap.level]||[]).push(gap);
  const labels = {critical:'Critical', important:'Important', helpful:'Helpful'};

  const gapHtml = ['critical','important','helpful'].map(lv=>{
    const items=byLv[lv]||[]; if(!items.length) return '';
    return `<div class="group"><span class="level ${lv[0]}">${labels[lv]}</span>
      ${items.map(gap=>{
        const res=(g.resources||{})[gap.skill]||[]; const r=res.find(r=>r.free)||res[0];
        return `<div class="skill-row"><span class="sname">${gap.skill}</span>${r?`<a class="res-link" href="${r.url}" target="_blank" rel="noopener">${r.platform}</a>`:''}</div>`;
      }).join('')}</div>`;
  }).join('');

  const haveHtml = (g.matching_skills||[]).length
    ? `<div class="box"><div class="box-title">✅ Skills you bring to the table</div><div class="have-chips">${(g.matching_skills||[]).map(s=>`<span class="have-chip">${s.skill}</span>`).join('')}</div></div>` : '';
  const fbs = cv.recent_feedback||[];
  const fbHtml = fbs.length ? `<div class="box"><div class="box-title">💬 Community feedback</div>
    ${fbs.map(f=>`<div class="fb"><div class="fb-top"><span class="fb-stars">${'★'.repeat(f.rating)}${'☆'.repeat(5-f.rating)}</span>${f.pursuing?'<span class="pursuing">Pursuing</span>':''}</div>${f.comment?`<p class="fb-comment">${f.comment}</p>`:''}</div>`).join('')}</div>` : '';
  const entryHtml = (c.entry_paths||[]).length ? `<div class="box"><div class="box-title">🎓 Pathways into this career</div>${(c.entry_paths||[]).map(p=>`<div class="entry">${p}</div>`).join('')}</div>` : '';
  const aiHtml = g.ai_advice ? `<div class="ai-box"><h3>🤖 AI coaching tips</h3><p>${g.ai_advice}</p></div>` : '';
  const sal = c.salary_range ? formatSal(c.salary_range) : '';
  const meta = COLLAR_META.find(m=>m.key===c.collar);

  document.getElementById('detail-body').innerHTML = `
    <div class="d-hero skills">
      <div class="d-icon">${CAT_ICONS[c.category]||'📌'}</div>
      <div class="d-top">
        <div>
          <div class="d-title">${c.title}</div>
          <div class="d-cat">${c.category}${meta ? ` · ${meta.icon} ${meta.label}` : ''}</div>
        </div>
        <div class="d-score"><div class="n">${sc}%</div><div class="s">Your match</div></div>
      </div>
      <div class="d-track"><div style="width:${sc}%"></div></div>
      <p class="d-desc">${c.description}</p>
      <div class="d-pills">
        ${sal?`<span class="d-pill">💰 ${sal}</span>`:''}
        <span class="d-pill">📈 ${c.growth_outlook}</span>
        ${cv.avg_rating?`<span class="d-pill">⭐ ${cv.avg_rating}/5 · ${cv.rating_count} reviews</span>`:''}
      </div>
    </div>
    ${haveHtml}
    ${(g.gaps||[]).length?`<div class="box"><div class="box-title">📘 Skill gaps to close</div>${gapHtml}</div>`:`<div class="box"><p style="color:var(--ok);font-weight:600">🎉 You have all required skills for this career!</p></div>`}
    ${entryHtml}
    ${aiHtml}
    <div class="box">
      <div class="box-title">⭐ Rate this career ${cv.avg_rating?`<span style="margin-left:auto;font-size:.74rem;color:var(--mut);font-weight:400">${cv.avg_rating}/5 · ${cv.rating_count} ratings</span>`:''}</div>
      <div class="stars">${[1,2,3,4,5].map(n=>`<span class="star" data-v="${n}" onclick="setRating(${n})">★</span>`).join('')}</div>
      <textarea class="rate-txt" id="rate-txt" placeholder="Share your experience (optional)…"></textarea>
      <label class="rate-check"><input type="checkbox" id="rate-pursuing"> I am currently pursuing this career</label>
      <div><button class="btn-submit" onclick="submitRating()">Submit rating</button></div>
      <div id="rate-msg"></div>
    </div>
    ${fbHtml}
  `;
}

function setRating(n) {
  ratingVal=n;
  document.querySelectorAll('.star').forEach(s=>s.className='star'+(parseInt(s.dataset.v)<=n?' on':''));
}
async function submitRating() {
  if(!ratingVal){alert('Please select a star rating.');return;}
  const btn=document.querySelector('.btn-submit'); btn.disabled=true;
  try {
    await post('/api/rate',{career_id:currentId,rating:ratingVal,comment:document.getElementById('rate-txt').value||null,pursuing:document.getElementById('rate-pursuing').checked,skills});
    document.getElementById('rate-msg').innerHTML='<div style="color:var(--ok);font-size:.85rem;font-weight:600;margin-top:10px">✓ Shukriya! Thanks for rating 🙏</div>';
  } catch(e) { btn.disabled=false; document.getElementById('rate-msg').innerHTML=`<span style="color:var(--bd-c);font-size:.82rem">Error: ${e.message}</span>`; }
}

function backToSearch() {
  document.getElementById('detail').style.display='none';
  document.getElementById('search-pane').style.display='';
  window.scrollTo({top:0,behavior:'smooth'});
}

function esc(s){ return (s||'').replace(/'/g,"\\'").replace(/\n/g,''); }
init();
