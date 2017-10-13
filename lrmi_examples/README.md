# lrmi-examples
This repository contains examples of LRMI learning resource descriptions.

## Contents:
### LRexample01 
Example of description with many alignments to Common Core State Standards, in JSON LD, from Learning Registry provided by Jason Hoekstra.
* LRexample01a_md.html - same resource described in LRexample01.jsonld, but simplified and expressed in html with microdata.
* LRexample01a.json-ld - same description asLRexample01a_md.html but expressed in JSON-LD

### type+audience+level 
Simple example including educational resource types, an educational target audience, and an alignment to an educational level. Designed to illustrate that the target audience and educational level alignment do not necessarily relate to the same user.
* type+audience+level.html - plain HTML
* type+audience+level_md.html - same as type+audience+level.htm but with microdata in the HTML
* type+audience+level_rdfa.html - same as type+audience+level.htm but with RDFa in the HTML
* type+audience+level_jsonld.json - same resource as described in type+audience+level.htm but described in JSON-LD

Suggested for submission to schema.org as an example for learningResourceType, educationalAlignment, AlignmentObject, educationalFramework, alignmentType, targetName, targetUrl, audience, EducationalAudience, educationalRole

### alignmentsUK
Example of lesson plan for use of a video, showing curriculum alignment of the lesson plan to levels and topics in UK national curricula. Loosely based on http://www.bbc.co.uk/education/clips/z3sjtfr 
* alignmentsUK.html - plain HTML
* alignmentsUK_md.html - same as type+audience+level.htm but with microdata in the HTML
* alignmentsUK_rdfa.html - same as type+audience+level.htm but with RDFa in the HTML
* alignmentsUK_jsonld.json - same resource as described in type+audience+level.htm but described in JSON-LD

Suggested for submission to schema.org as an example for typicalAgeRange, timeRequired, educationalAlignment, AlignmentObject, educationalFramework, alignmentType, targetName, targetUrl

### sdo-lrmi-examples.txt
Fully prepped examples in schema.org examples text file format.

Note: validate with:
* https://developers.google.com/structured-data/testing-tool/
* https://webmaster.yandex.com/microtest.xml
* http://linter.structured-data.org/
