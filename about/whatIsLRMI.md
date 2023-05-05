# What is LRMI, in one page

LRMI[1], an effort that has been running since 2011, seeks to allow the creation of structured data about learning resources in order to facilitate resource discovery, selection, management, and other uses. The formal definition LRMI uses for a learning resource is given below, but the important points are that such a resource is reusable (and therefore persistent) and designed for educational purposes. LRMI metadata can also be used for educational events (though such events are not usually persistent unless recorded for later availability).

> **Learning Resource:**  a persistent resource that has one or more physical or digital representations, and that explicitly involves, specifies or entails a learning activity or learning experience.

Structured data provides machine-readable descriptions of these resources, which in turn helps people create services that use that data. A typical example of such a service is one that finds resources suitable for a given audience or learning need. LRMI conformant data can also be used in services that identify when resources should be updated, resources to be used in AI models, and many other types of services.

LRMI provides a lightweight data model and vocabulary that complements broadly applicable and widely used standards adding the ability to describe educational characteristics of resources. It is based on the concepts of Resource Description Framework (RDF), the semantic web, linked data, and knowledge graphs, as used by many major technology services.

The focus of the model is on relationships between things. In 2012, Google showed how important it was to deal in "things not strings". The text "Taj Mahal" doesn't tell you much unless you know whether you are dealing with a mausoleum in India, one of many restaurants, or a blues musician. The relationships between the thing being described and other things are what makes the description, for example:

* the relationship between a resource and an audience: this resource is meant for use by teachers; this resource is aimed at helping young children learn.
* the relationship between a resource and something that may be learned (such as a topic, a competence, learning objective): this resource will help you learn mathematics; this resource will assess your level of skill in spelling certain words.
* the relationship between a resource and some text: the resource has this name; this is a description of the resource.

LRMI on its own is not enough to describe a resource as it lacks many properties such as title and description that will always be required for a functional description. However, these properties are available in many other RDF vocabularies. As LRMI and these other vocabularies are based on the same RDF model, LRMI can be used with these other vocabularies to provide for richer, more precise descriptions of the teaching and learning characteristics of, and relationships among, a wide range of resources.

## Further information 
About LRMI: https://www.dublincore.org/about/lrmi/

LRMI Specifications: https://www.dublincore.org/specifications/lrmi/

LRMI Working Group: https://www.dublincore.org/groups/lrmi/

## Notes
1. LRMI™, if anyone asks, stands for Learning Resource Metadata Innovation. It is a Working Group of the Dublin Core Metadata Initiative, and a set of community standards produced by that Working Group.
2.  Amit Singhal (2012, May 16), "Introducing the Knowledge Graph: things, not strings" Google Blog, https://blog.google/products/search/introducing-knowledge-graph-things-not/
