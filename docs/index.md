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
    <p class="tx-kicker">Why BioCypher</p>
    <h2>A practical way to build biomedical knowledge graphs.</h2>
  </div>

  <div class="tx-feature-grid">
    <article class="tx-feature-card">
      <span class="tx-feature-card__icon" aria-hidden="true">⌬</span>
      <h3>Ontology-aligned</h3>
      <p>Map incoming data to biomedical ontologies so graph labels and relationships stay understandable.</p>
    </article>
    <article class="tx-feature-card">
      <span class="tx-feature-card__icon" aria-hidden="true">⇄</span>
      <h3>Adapter-based</h3>
      <p>Reuse data adapters where they exist, and write small project adapters where they do not.</p>
    </article>
    <article class="tx-feature-card">
      <span class="tx-feature-card__icon" aria-hidden="true">↗</span>
      <h3>Flexible output</h3>
      <p>Write the same graph build to Neo4j, RDF/OWL, SQL, NetworkX, ArangoDB, or tables.</p>
    </article>
  </div>
</section>

<section class="tx-section tx-section--evidence" id="evidence">
  <div class="tx-section__header">
    <p class="tx-kicker">Papers</p>
    <h2>Papers and projects using BioCypher.</h2>
    <p>
      BioCypher sits behind citable software, deployed research graphs, and
      AI-facing biomedical data services.
    </p>
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
    <h3>Used in scientific knowledge-graph projects.</h3>
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
    <a href="https://blog.opentargets.org/official-open-targets-mcp/" target="_blank" rel="noopener noreferrer">
      <div class="tx-usecase-grid__logo" aria-hidden="true">
        <img src="assets/img/projects_logos/opentargets_mcp.png" alt="" width="1300" height="418" loading="lazy" decoding="async">
      </div>
      <span>Target discovery · Open Targets</span>
      <h3>Open Targets MCP</h3>
      <p>The official Open Targets MCP makes Platform data available to AI tools for target identification and prioritisation.</p>
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
    <h2>Ways to join.</h2>
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
      <a href="https://biocypher.zulipchat.com/#narrow/channel/371264-general/topic/General.20Questions/with/396284706" target="_blank" rel="noopener noreferrer">Ask a question →</a>
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
    <h2>Recent work.</h2>
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

    <div class="tx-activity-stream" aria-label="BioCypher ecosystem activity timeline">
      <div class="tx-activity-group">
        <h3>2026</h3>
        <a class="tx-activity-row" href="community/2026-workshop/">
          <time>Jun 2026</time>
          <span>
            <strong>Biomedical KG community workshop</strong>
            User workshop focused on shared practices.
          </span>
        </a>
        <a class="tx-activity-row" href="https://www.biorxiv.org/content/10.1101/2025.04.09.647963v1" target="_blank" rel="noopener noreferrer">
          <time>Jun 2026</time>
          <span>
            <strong>TomTom knowledge graph</strong>
            Integrated tomato KG accepted in New Phytologist; preprint available.
          </span>
        </a>
        <a class="tx-activity-row" href="https://iggytop.readthedocs.io/en/latest/" target="_blank" rel="noopener noreferrer">
          <time>May 2026</time>
          <span>
            <strong>IggyTop release</strong>
            Immune receptor signalling knowledge graph released.
          </span>
        </a>
        <a class="tx-activity-row" href="https://aac.slolab.ai" target="_blank" rel="noopener noreferrer">
          <time>Feb 2026</time>
          <span>
            <strong>Agentic Automation Canvas</strong>
            Double-feature preprint on agentic automation and expectation gaps.
          </span>
        </a>
      </div>

      <div class="tx-activity-group">
        <h3>Late 2025</h3>
        <a class="tx-activity-row" href="https://github.com/BioCypher/sys-bio-kgs" target="_blank" rel="noopener noreferrer">
          <time>Dec 2025</time>
          <span>
            <strong>Systems biology model loading</strong>
            ELIXIR BioHackathon Germany contributions to BioCypher and BioChatter.
          </span>
        </a>
        <a class="tx-activity-row" href="https://www.nature.com/articles/s41587-025-02900-9" target="_blank" rel="noopener noreferrer">
          <time>Nov 2025</time>
          <span>
            <strong>BioContext in Nature Biotechnology</strong>
            BioContext paper published and the registry launched at biocontext.ai.
          </span>
        </a>
        <a class="tx-activity-row" href="https://github.com/edamontology/edammcp" target="_blank" rel="noopener noreferrer">
          <time>Nov 2025</time>
          <span>
            <strong>EDAM Ontology MCP server</strong>
            ELIXIR BioHackathon Europe contributions to biomedical MCP infrastructure.
          </span>
        </a>
        <a class="tx-activity-row" href="https://www.nature.com/articles/s41746-025-01996-2" target="_blank" rel="noopener noreferrer">
          <time>Oct 2025</time>
          <span>
            <strong>Medical benchmarking study</strong>
            Published in npj Digital Medicine.
          </span>
        </a>
      </div>
    </div>
  </div>
</section>

</div>
