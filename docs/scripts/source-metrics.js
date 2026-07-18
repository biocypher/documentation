/**
 * Keep the repository link and its metrics in sync with the active product.
 *
 * Material's source component stores one repository response under a global
 * session key. That makes its metrics stale after navigating between products
 * in this multi-repository documentation site, so metrics are loaded and
 * cached per repository here instead.
 */
(function () {
  var repositories = {
    biocypher: {
      name: "biocypher/biocypher",
      url: "https://github.com/biocypher/biocypher",
    },
    biochatter: {
      name: "biocypher/biochatter",
      url: "https://github.com/biocypher/biochatter",
    },
    biotope: {
      name: "biocypher/biotope",
      url: "https://github.com/biocypher/biotope",
    },
  };
  var requests = new Map();

  function repositoryForPath(pathname) {
    if (/(^|\/)BioChatter(\/|$)/.test(pathname)) {
      return repositories.biochatter;
    }
    if (/(^|\/)Biotope(\/|$)/.test(pathname)) {
      return repositories.biotope;
    }
    return repositories.biocypher;
  }

  function readCache(repository) {
    try {
      return JSON.parse(
        window.sessionStorage.getItem("__biocypher_source:" + repository.name)
      );
    } catch (_) {
      return null;
    }
  }

  function writeCache(repository, metrics) {
    try {
      window.sessionStorage.setItem(
        "__biocypher_source:" + repository.name,
        JSON.stringify(metrics)
      );
    } catch (_) {
      // Metrics still work when session storage is unavailable.
    }
  }

  function requestJson(url) {
    return window.fetch(url).then(function (response) {
      return response.ok ? response.json() : null;
    });
  }

  function loadMetrics(repository) {
    var cached = readCache(repository);
    if (cached) return Promise.resolve(cached);
    if (requests.has(repository.name)) return requests.get(repository.name);

    var apiUrl = "https://api.github.com/repos/" + repository.name;
    var request = Promise.all([
      requestJson(apiUrl),
      requestJson(apiUrl + "/releases/latest"),
    ])
      .then(function (responses) {
        var details = responses[0] || {};
        var release = responses[1] || {};
        var metrics = {
          version: release.tag_name || null,
          stars: Number.isFinite(details.stargazers_count)
            ? details.stargazers_count
            : null,
          forks: Number.isFinite(details.forks_count)
            ? details.forks_count
            : null,
        };
        writeCache(repository, metrics);
        return metrics;
      })
      .catch(function () {
        return null;
      })
      .finally(function () {
        requests.delete(repository.name);
      });

    requests.set(repository.name, request);
    return request;
  }

  function makeFact(type, value, label) {
    var fact = document.createElement("li");
    fact.className = "md-source__fact md-source__fact--" + type;
    fact.title = label;
    fact.setAttribute("aria-label", label + ": " + value);
    fact.textContent = value;
    return fact;
  }

  function renderMetrics(source, repository, metrics) {
    var name = source.querySelector(".md-source__repository");
    if (!name) return;

    name.replaceChildren(document.createTextNode(repository.name));
    name.classList.remove("md-source__repository--active");
    if (!metrics) return;

    var facts = document.createElement("ul");
    facts.className = "md-source__facts";
    if (metrics.version) {
      facts.append(makeFact("version", metrics.version, "Latest release"));
    }
    if (metrics.stars !== null) {
      facts.append(
        makeFact("stars", metrics.stars.toLocaleString(), "GitHub stars")
      );
    }
    if (metrics.forks !== null) {
      facts.append(
        makeFact("forks", metrics.forks.toLocaleString(), "GitHub forks")
      );
    }
    if (!facts.children.length) return;

    name.append(facts);
    name.classList.add("md-source__repository--active");
  }

  function updateSources() {
    var repository = repositoryForPath(window.location.pathname);
    var sources = document.querySelectorAll("[data-biocypher-source]");

    sources.forEach(function (source) {
      source.href = repository.url;
      source.title = repository.url;
      renderMetrics(source, repository, null);
    });

    loadMetrics(repository).then(function (metrics) {
      if (repositoryForPath(window.location.pathname) !== repository) return;
      sources.forEach(function (source) {
        renderMetrics(source, repository, metrics);
      });
    });
  }

  document$.subscribe(updateSources);
})();
