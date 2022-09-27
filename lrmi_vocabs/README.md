# LRMI Concept Schemes (value lists)

Small sets of concepts for use to provide controlled value lists for LRMI properties. May include draft terms that are unstable.

* The latest [stable, normative versions](https://www.dublincore.org/specifications/lrmi/concept_schemes/) are on the DCMI website
* See [current issues](https://github.com/dcmi/lrmi/issues?q=is%3Aissue+is%3Aopen+label%3AConcept_schemes) relating to LRMI Concept schemes.

The LRMI concept schemes are small sets of concepts for use as values with the LRMI properties in learning resource description and Web markup. Since the properties for which these concepts are intended also exists as Schema.org properties, the concepts in this concept scheme can be used with a level of certainty in Web markup. The concepts in the vocabularies have been declared in RDF using the W3C's Simple Knowledge Organization System.

## Current concept schemes

* [alignmentType](alignmentType/)
* [educationalAudienceRole](educationalAudienceRole/)
* [educationalUse](educationalUse/)
* [interactivityType](interactivityType)
* [learningResourceType](learningResourceType)

With all LRMI concept schemes, the intention is to provide a small number of broad, top-level concepts. Users who need to classify against more specific concepts are encouraged to declare these concepts using SKOS and to map them to the appropriate LRMI concept using skos:broadMatch. 
