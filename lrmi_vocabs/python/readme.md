A script to turn the ttl (Turtle, terse triple language) definition files of the LRMI vocabularies into the md (markdown) tables used on the website.

## Installation
Clone from here, create a virtual environment, pip install dependencies (readchar and rdflib).

## Usage
Assuming the current directory is one of the lrmi_vocabs directories:

`(venv) $ ../python/ttl2md.py input.ttl [output.md]`

If no output filename is provided the markdown text will be displayed, otherwise it is saved to file.

## Assumptions / Limitations
Produces a markdown fragment that can be copied and pasted into the file that runs the DCMI website. Doesn't display properly as markdown on its own.

Based on how we currently describe LRMI vocaburaries this program assumes:

* Vocabularies are defined as skos:Concepts in a skos:ConceptScheme
* There is only one skos:ConceptScheme per file
* Concept Schemes are described with:
  *   dc.title / dcterms:title
  *   dc.description / dcterms:description
  *   dc.creator / dcterms.creator
  *   dcterms.dateSubmitted
  *   dcterms.created
  *   dcterms.modified
  *   dc.source / dcterms.source
  *   dcterms.license
  *   adms.status
* Concepts are declared and skos:inScheme <theConceptScheme>
* Concepts are defined with:
  *   skos.prefLabel
  *   skos.definition
  *   dc.source / dcterms.source
  *   skos.scopeNote
  *   skos.relatedMatch
  *   skos.exactMatch
  *   skos.closeMatch
  *   skos.narrowMatch
  *   skos.broadMatch
  *   vs.term_status

It is straightforward to add new properties to process, and would be pretty straightforward to overcome some of the other limitations.

## known issues
If the value of a property looks like a URL but is actually treated as a string, rdflib complains, but the output is nevertheless OK.
