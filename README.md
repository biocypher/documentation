# BioCypher Docs

This repository contains the integrated documentation for the BioCypher
ecosystem.

## Setup

This repository uses mkdocs-material with GitHub submodules for the BioCypher
and BioChatter documentation.

To clone the repository, use the following command:

```bash
git clone --recurse-submodules https://github.com/biocypher/documentation.git
```

If already cloned, run this to update the submodules:

```bash
git submodule update --init --recursive
```

## Local Development

```bash
poetry install
poetry run mkdocs serve
```
