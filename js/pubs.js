// Publication cards, shared by index.html (selected publications) and
// publications.html (full list). Both pages fetch data/publications.json;
// this file only turns one record into HTML, so the two lists always match.

// Return the badge text and colors for a publication status.
function statusLabel(s) {
  const map = {
    'published':  { text: 'Published',  color: '#16a34a', bg: '#f0fdf4' },
    'in press':   { text: 'In Press',   color: '#2563eb', bg: '#eff6ff' },
    'submitted':  { text: 'Submitted',  color: '#d97706', bg: '#fffbeb' },
    'accepted':   { text: 'Accepted',   color: '#7c3aed', bg: '#f5f3ff' },
    'preprint':   { text: 'Preprint',   color: '#d97706', bg: '#fffbeb' },
  };
  return map[s] || { text: s, color: '#64748b', bg: '#f1f5f9' };
}

// Return the HTML card for one publication. If `number` is given, the title starts with "number. ".
function pubCardHtml(p, number) {
  const link = p.url
    ? `<a href="${p.url}" target="_blank" class="pub-link">DOI ↗</a>`
    : '';
  const prefix = number ? `${number}. ` : '';
  // Published is the normal case, so only other statuses (e.g. Preprint) get a badge.
  let badge = '';
  if (p.status !== 'published') {
    const s = statusLabel(p.status);
    badge = `<span style="
          background:${s.bg}; color:${s.color};
          font-size:0.75rem; font-weight:600;
          padding:0.15rem 0.5rem; border-radius:4px;
        ">${s.text}</span>`;
  }
  return `
    <div class="pub-card" data-status="${p.status}">
      <div class="pub-title">${prefix}${p.title}</div>
      <div class="pub-authors">${p.authors}</div>
      <div class="pub-meta">
        <span class="pub-year-badge">${p.year}</span>
        <span><em>${p.journal}</em>${p.volume ? ', ' + p.volume : ''}</span>
        ${badge}
        ${link}
      </div>
    </div>`;
}
