# Workshop "Establishing a knowledge graph community in biomedical science"

This workshop took place in June 2026 in Heidelberg. Another workshop is planned for February 2026, again in Heidelberg. Stay tuned for announcements about this event! 

We had a great time welcoming participants from bioinformatics and related disciplines, but also beyond! 

 The BioCypher Workshop was a week-long event held in Heidelberg from the 15th to the 19th of June, organized by the Scientific Software Center together with the BioCypher team and supported by the DFG and the International Society for Information Fusion. Its purpose was to teach researchers how to turn messy, heterogeneous biomedical data into semantic knowledge graphs using BioCypher, and to foster a community around reusable, well-documented data adapters, with each day combining a morning of plenary talks with three hands-on afternoon sessions that were frequently split into novice and advanced tracks. Monday laid the foundations by introducing knowledge graphs, nodes, edges and triples, ontologies such as OWL, RDFS and Biolink, project-specific schemas, reasoning, provenance through strict mode, and Neo4j querying with Cypher, while also previewing the three ways of using BioCypher through code, low-code OntoWeaver, and AI assistance. Tuesday moved into building the first working adapter in Python, with a novice track using prepared protein-interaction data and an advanced track using real DrugCentral drug-target data, followed by sessions on the BioCypher MCP and a hands-on OntoWeaver tutorial given by Johann Dreo. Wednesday focused on harmonizing biomedical data through structured MLCroissant metadata to make datasets and adapters discoverable, portable, interoperable and reproducible, and it also covered adapter registries and AI-supported open-source software development, whereas Thursday extended a single adapter into multiple adapters and a heterogeneous knowledge graph, showing where BioCypher hands off to OntoWeaver's fusion module for identifier mapping, duplicate resolution and evidence aggregation, alongside sessions on BioChatter and Biotope, before Friday closed the week with highlights, feedback and guidance on contributing to BioCypher. 
 
 The overarching message of the week was that knowledge graphs become valuable because entities are connected through typed, interpretable relationships that can be queried along biologically meaningful paths, that schemas combined with strict provenance and a shared ontology like Biolink keep projects clean and reusable from the outset, and that BioCypher does not try to build one universal biology graph but instead frames each researcher's own question while preserving provenance and mapping onto standard ontologies, with OntoWeaver and Croissant handling fusion and metadata around it.


<div>
<img src="/assets/img/biocypher-workshop-group-picture.jpg" alt="Group picture of the participants, BioCypher user workshop 2026" width="800">
</div>
The group picture of the BioCypher workshop participants, on the rooftop terrace of the Mathematikon.

## Background

Many modern biomedical methods benefit from the availability of prior knowledge, for example about genes, proteins, or diseases. Knowledge graphs, i.e., representations of prior knowledge in machine-readable graph form, have become the quasi-standard for storing, manipulating, and sharing biomedical prior knowledge. To meet the needs of broad user communities in generating knowledge graphs, we have developed BioCypher, a modular framework for the creation of knowledge graphs based on ontologies, targeting single cell and spatial omics, microbiomics, metabolomics, and various multi-omics modelling and machine learning methods.

In this workshop, we will learn about knowledge representations, knowledge graphs, ontologies, and data structures, and put this knowledge to practical use with BioCypher. The workshop will also contain a module on [information fusion](https://ontoweaver.readthedocs.io/en/latest/sections/information_fusion.html), leveraging [OntoWeaver](https://ontoweaver.readthedocs.io/en/latest/) to combine data from different sources and joining this information into one single graph.
Further, we will learn how to utilize generative AI to upscale to more complex projects.

## Workshop Aim
    
Learn how to create knowledge graphs from your data and import them into a graph database for further studies.

## Research Topics

<div class="grid cards" markdown>

- :material-graph-outline: **Knowledge graphs**
- :material-dna: **Biomedical science**  
- :material-file-tree: **Ontologies**
- :material-brain: **Knowledge extraction**
- :material-source-merge: **Information fusion**
- :material-chat-processing-outline: **Agentic automation**

</div>


## Workshop program

=== "Monday"
    <table class="workshop-program-table" style="border-collapse:separate; border-spacing:0; border:1px solid var(--md-primary-fg-color); border-radius:0.6rem; overflow:hidden;">
        <thead>
            <tr>
                <th>Time</th>
                <th>Session</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>09:15-10:45</td>
                <td>Sebastian Lobentanzer (Helmholtz Munich), "The BioCypher ecosystem: Democratizing knowledge graphs"</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td></td>
                <td>Steffen Vogler (Bayer AG, Berlin), "Knowledge management with BioCroissant and agentic automation"</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>11:00-12:30</td>
                <td>hands-on session: "Knowledge graphs and BioCypher"</td>
            </tr>
            <tr>
                <td colspan="2">lunch break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>13:30-15:00</td>
                <td>hands-on session: "Knowledge graphs and BioCypher"</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>15:15-16:45</td>
                <td>hands-on session: "Knowledge graphs and BioCypher"</td>
            </tr>
        </tbody>
    </table>

=== "Tuesday"
    <table class="workshop-program-table" style="border-collapse:separate; border-spacing:0; border:1px solid var(--md-primary-fg-color); border-radius:0.6rem; overflow:hidden;">
        <thead>
            <tr>
                <th>Time</th>
                <th>Session</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>09:15-10:45</td>
                <td>Jan Baumbach (University of Hamburg, online), "Network Medicine GPT - A knowledge-graph based transformer for drug repurposing and disease module mining"</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td></td>
                <td>Johann Dreo (Institut Pasteur, Paris), "Explainable AI against Cancer - OntoWeaver's driving use-case"</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>11:00-12:30</td>
                <td>hands-on session: "Hands-on OntoWeaver" (Johann Dreo)</td>
            </tr>
            <tr>
                <td colspan="2">lunch break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>13:30-15:00</td>
                <td>hands-on session: "Adapters in BioCypher"</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>15:15-16:45</td>
                <td>hands-on session: "BioCypher MCP"</td>
            </tr>
        </tbody>
    </table>

=== "Wednesday"
    <table class="workshop-program-table" style="border-collapse:separate; border-spacing:0; border:1px solid var(--md-primary-fg-color); border-radius:0.6rem; overflow:hidden;">
        <thead>
            <tr>
                <th>Time</th>
                <th>Session</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>09:15-10:45</td>
                <td>Carl Herrmann (Heidelberg University), "Strategies for building domain specific knowledge for single-cell genomics"</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td></td>
                <td>Judith Wodke (University Medicine Greifswald), "MeDaX-KG: The bioMedical Data eXploration Knowledge Graph"</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td></td>
                <td>Alberto Santos Delgado (Technical University of Denmark, Copenhagen), "Unlocking Disease Mechanisms via Microbial Graph Analysis"</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>11:00-12:30</td>
                <td>hands-on session: "AI-supported open-source software development"</td>
            </tr>
            <tr>
                <td colspan="2">lunch break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>13:30-15:00</td>
                <td>hands-on session: "Harmonizing biomedical data"</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>15:15-16:45</td>
                <td>hands-on session: "Harmonizing biomedical data"</td>
            </tr>
        </tbody>
    </table>

=== "Thursday"
    <table class="workshop-program-table" style="border-collapse:separate; border-spacing:0; border:1px solid var(--md-primary-fg-color); border-radius:0.6rem; overflow:hidden;">
        <thead>
            <tr>
                <th>Time</th>
                <th>Session</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>09:15-10:45</td>
                <td>Tunca Dogan (Hacettepe University, Ankara), "Knowledge Graphs as AI-Ready Substrates: Integrating Heterogeneous Biomedical Data for Scalable Discovery and Reasoning"</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td></td>
                <td>Claire Laudy (ISIF & Institut Pasteur, Paris), "What is high-level information fusion, and why is it important?"</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>11:00-12:30</td>
                <td>hands-on session: "OntoWeaver's fusion module (Johann Dreo)"</td>
            </tr>
            <tr>
                <td colspan="2">lunch break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>13:30-15:00</td>
                <td>hands-on session: "Building Adapters in BioCypher"</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>15:15-16:45</td>
                <td>hands-on session: "BioChatter, Biotope and more (Sebastian Lobentanzer)"</td>
            </tr>
        </tbody>
    </table>

=== "Friday"
    <table class="workshop-program-table" style="border-collapse:separate; border-spacing:0; border:1px solid var(--md-primary-fg-color); border-radius:0.6rem; overflow:hidden;">
        <thead>
            <tr>
                <th>Time</th>
                <th>Session</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>09:15-10:45</td>
                <td>Workshop Highlights</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td></td>
                <td>Contributing to BioCypher on GitHub</td>
            </tr>
            <tr>
                <td colspan="2">coffee break</td>
            </tr>
            <tr style="background-color:var(--md-primary-fg-color); color:var(--md-primary-bg-color);">
                <td>11:00-12:30</td>
                <td>Achievements, feedback and workshop closing</td>
            </tr>
        </tbody>
    </table>

## Workshop speakers

- Jan Baumbach, University of Hamburg, Germany 
- Alberto Santos Delgado, Technical University of Denmark, Copenhagen, Denmark  
- Tunca Dogan, Hacettepe University, Ankara, Turkey 
- Johann Dreo, Institut Pasteur, Paris, France
- Carl Herrmann, Heidelberg University, Heidelberg, Germany
- Claire Laudy, ISIF & Institut Pasteur, Paris, France 
- Sebastian Lobentanzer, Helmholtz Munich, Germany 
- Steffen Vogler, Bayer AG, Berlin, Germany
- Judith Wodke, University Medicine Greifswald, Germany 

## Prerequisites

!!! warning "Requirements"
    Familiarity with ontologies and/or knowledge graphs and/or Python is helpful. You need to bring a laptop with a working Python installation and an IDE such as VSCode.

## Financial support

This workshop would not be possible without funding through the German Science Foundation DFG through project number 528753569. We gratefully acknowledge sponsorship from the [International Society for Information Fusion (ISIF)](https://isif.org/).

<div>
<img src="/assets/img/dfg_logo_schriftzug_blau_foerderung_de.png" alt="Funding through DFG" width="400">

<img src="/assets/img/ISIF-logo.png" alt="Sponsored by ISIF" width="400">
</div>