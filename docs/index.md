---
title: Biomedical knowledge graphs
template: home.html
hide:
  - navigation
  - toc
  - title
---

<div class="tx-home-body" markdown="0">

<section class="tx-section tx-section--intro" id="why">
  <div class="tx-section__header">
    <p class="tx-kicker">Why the BioCypher ecosystem</p>
    <h2>One workflow, from raw data to grounded answers</h2>
    <p>Each step uses your project's context to stay focused and semantically grounded.</p>
  </div>

  <div class="tx-feature-grid">
    <article class="tx-feature-card">
      <div class="tx-feature-card__head">
        <span class="tx-feature-card__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 3v11"/>
            <path d="M7.5 10 12 14.5 16.5 10"/>
            <path d="M5 19h14"/>
          </svg>
        </span>
        <h3>Gather</h3>
      </div>
      <p>Pull in data from any source. Extract structured entities from text and messy files, annotated with portable metadata.</p>
      <div class="tx-feature-card__tools" role="list" aria-label="Components">
        <a role="listitem" href="Biotope/">Biotope</a>
        <a role="listitem" href="https://github.com/mlcommons/BioCroissant/" target="_blank" rel="noopener noreferrer">BioCroissant</a>
      </div>
    </article>
    <article class="tx-feature-card">
      <div class="tx-feature-card__head">
        <span class="tx-feature-card__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="6" cy="7" r="2.2"/>
            <circle cx="18" cy="7" r="2.2"/>
            <circle cx="12" cy="17" r="2.2"/>
            <path d="M8.2 7h7.6"/>
            <path d="M7.1 8.9 10.9 15.1"/>
            <path d="M16.9 8.9 13.1 15.1"/>
          </svg>
        </span>
        <h3>Build</h3>
      </div>
      <p>Construct ontology-aligned knowledge graphs with reusable adapters, and export the same build to different formats and environments.</p>
      <div class="tx-feature-card__tools" role="list" aria-label="Components">
        <a role="listitem" href="BioCypher/">BioCypher</a>
      </div>
    </article>
    <article class="tx-feature-card">
      <div class="tx-feature-card__head">
        <span class="tx-feature-card__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 14a2 2 0 0 1-2 2H8l-4 4V5a2 2 0 0 1 2-2h13a2 2 0 0 1 2 2z"/>
            <circle cx="8.5" cy="9.5" r="0.6" fill="currentColor" stroke="none"/>
            <circle cx="12.5" cy="9.5" r="0.6" fill="currentColor" stroke="none"/>
            <circle cx="16.5" cy="9.5" r="0.6" fill="currentColor" stroke="none"/>
          </svg>
        </span>
        <h3>Reason</h3>
      </div>
      <p>Query and chat with your graph. Connect it to LLMs and shared context resources for grounded, agentic analysis.</p>
      <div class="tx-feature-card__tools" role="list" aria-label="Components">
        <a role="listitem" href="BioChatter/">BioChatter</a>
        <a role="listitem" href="https://biocontext.ai" target="_blank" rel="noopener noreferrer">BioContext</a>
      </div>
    </article>
  </div>

  <div class="tx-about-links">
    <a href="about/">Read more about the ecosystem.</a>
  </div>
</section>

<section class="tx-section tx-section--evidence" id="evidence">
  <div class="tx-section__header">
    <p class="tx-kicker">Ecosystem publications</p>
    <h2>Core publications from the BioCypher ecosystem</h2>
  </div>

  <ul class="tx-publication-list" aria-label="Academic publications">
    <li>
      <a href="https://www.nature.com/articles/s41587-023-01848-y" target="_blank" rel="noopener noreferrer">
        <span>Nature Biotechnology · 2023</span>
        <span class="tx-publication-list__title">
          <strong>BioCypher</strong>
          <small>Modular biomedical knowledge graph construction</small>
        </span>
      </a>
    </li>
    <li>
      <a href="https://www.nature.com/articles/s41587-024-02534-3" target="_blank" rel="noopener noreferrer">
        <span>Nature Biotechnology · 2025</span>
        <span class="tx-publication-list__title">
          <strong>BioChatter</strong>
          <small>Conversational AI for biomedical knowledge resources</small>
        </span>
      </a>
    </li>
    <li>
      <a href="https://www.nature.com/articles/s41587-025-02900-9" target="_blank" rel="noopener noreferrer">
        <span>Nature Biotechnology · 2025</span>
        <span class="tx-publication-list__title">
          <strong>BioContext</strong>
          <small>Context resources for biomedical AI systems</small>
        </span>
      </a>
    </li>
  </ul>

  <div class="tx-section__header tx-section__header--compact">
    <p class="tx-kicker">Deployed use cases</p>
    <h3>BioCypher in scientific knowledge-graph projects.</h3>
  </div>

  <div class="tx-usecase-grid">
    <a href="https://github.com/IGVF-DACC/igvf-catalog" target="_blank" rel="noopener noreferrer">
      <div class="tx-usecase-grid__logo" aria-hidden="true">
        <img src="assets/img/projects_logos/igvf.webp" alt="" width="602" height="206" loading="lazy" decoding="async">
      </div>
      <span>Regulatory genomics · Stanford / ENCODE</span>
      <h3>IGVF Catalog / ENCODE</h3>
      <p>BioCypher helps the IGVF team shape genomic variation data into a Biolink-inspired graph with a user-facing API.</p>
    </a>
    <a href="https://doi.org/10.1111/nph.71382" target="_blank" rel="noopener noreferrer">
      <div class="tx-usecase-grid__logo tx-usecase-grid__logo--wordmark" aria-hidden="true">TomTom</div>
      <span>Plant biology · RWTH Aachen</span>
      <h3>TomTom knowledge graph</h3>
      <p>TomTom uses BioCypher to integrate tomato multi-omics data for gene and protein function discovery.</p>
    </a>
    <a href="https://github.com/biocypher/metalinks" target="_blank" rel="noopener noreferrer">
      <div class="tx-usecase-grid__logo" aria-hidden="true">
        <img src="assets/img/projects_logos/metalinks_db_logo_3x4.png" alt="" width="1460" height="1022" loading="lazy" decoding="async">
      </div>
      <span>Metabolism · Heidelberg</span>
      <h3>Metalinks</h3>
      <p>BioCypher reduced the first structured knowledge-graph build from about 2.5 months of scripts to roughly two weeks.</p>
    </a>
  </div>
</section>

<section class="tx-section tx-section--involved" id="ecosystem">
  <div class="tx-section__header">
    <p class="tx-kicker">Community</p>
    <h2>Ways to join</h2>
    <p>Use the tools, cite the papers, ask questions, or contribute code and docs.</p>
  </div>

  <div class="tx-involved-grid">
    <article class="tx-involved-card">
      <h3>Contribute on GitHub</h3>
      <p>Report issues, improve adapters, add documentation, or review open pull requests.</p>
      <a href="https://github.com/biocypher">Open GitHub →</a>
    </article>
    <article class="tx-involved-card">
      <h3>Discuss on Zulip</h3>
      <p>Ask questions, coordinate ideas, and meet the people building BioCypher.</p>
      <a href="https://biocypher.zulipchat.com/#narrow/channel/371279-announcements/topic/Releases/with/598596369" target="_blank" rel="noopener noreferrer">Announcements →</a>
      <a href="https://biocypher.zulipchat.com/#narrow/channel/371278-help" target="_blank" rel="noopener noreferrer">Ask a question →</a>
    </article>
    <article class="tx-involved-card">
      <h3>Start from tutorials</h3>
      <p>Build a graph manually with BioCypher or install Biotope's agent skills.</p>
      <a href="BioCypher/learn/quickstart/">Manual tutorial →</a>
      <a href="Biotope/plugin/">Agent setup →</a>
    </article>
  </div>
</section>

<section class="tx-section tx-section--activity" id="activity">
  <div class="tx-section__header">
    <p class="tx-kicker">Activity</p>
    <h2>Recent work</h2>
    <p>Workshops, BioHackathons, releases, papers, and related tools from the BioCypher community.</p>
  </div>

  <div class="tx-activity-layout">
    <a class="tx-activity-feature" href="community/2026-workshop/">
      <img src="assets/img/biocypher-workshop-group-picture.jpg" alt="BioCypher workshop participants">
      <div>
        <span>June 2026 · Workshop</span>
        <h3>Building the biomedical KG community</h3>
        <p>User workshop on shared knowledge-graph practice in biomedical science.</p>
      </div>
    </a>

    <!-- recent-work-from-timeline -->
  </div>
</section>

</div>
