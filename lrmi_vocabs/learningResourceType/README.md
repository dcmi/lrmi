# LRMI Learning Resource Type Concept Scheme
**Status:** Incomplete draft.

**creator:** [LRMI Task Group (DCMI)](https://www.dublincore.org/groups/lrmi-task-group/)

**license:** http://creativecommons.org/licenses/by/4.0/

A top-level concept scheme that enumerates different types of Learning Resource, designed to supplement existing more generic resource type schemes and which can support local extensions.

## Explanatory Notes

By  learning resource we mean a persistent resource that has one or more physical or digital representation, and that explicitly involves, specifies or entails a learning activity or learning experience.  Since a learning resource is persistent it cannot be an event (though it can be a record of an event); in schema.org a separate class, [`EducationEvent`](https://schema.org/EducationEvent), exists to cover these. In LRMI learning resources are creative works, that is the LRMI [definition](https://www.dublincore.org/specifications/lrmi/lrmi_terms/2020-11-12/#LearningResource) of the learning resource class states that it is a subclass of schema.org [`CreativeWork`](https://schema.org/CreativeWork) (this does not preclude the use of LRMI terms with other vocabularies, such as Dublin Core). It follows that, for LRMI, learning resources cannot be, for example, a person. A learning activity or experience is one that has characteristics that may improve or measure a person's knowledge, skills or abilities. A learning resource may reference other supporting materials, creative works, tools, etc. that do not themselves meet the definition of learning resource.

Things that do not fall under this definition of learning resource that are relevant to learning should be classified using other appropriate concept schemes, for example the Library of Congress [Genre/Form Terms](https://id.loc.gov/authorities/genreForms.html).

### What is a Learning Resource Type?

By type we mean a category for what kind of learning resource is being described. The vocabulary concepts are intended for use with the LRMI `learningResourceType` property and similar properties in other schemas. Examples of learning resource type include 'textbook', 'lesson plan', 'lecture recording'.

The LRMI Resource Type Concept Scheme is not intended to indicate the encoding format, mime-type, material, educational use and other characteristics of a learning resource.  Other vocabulary schemes exist for these other categorizations, for example, IANA [mime types](http://www.iana.org/assignments/media-types/media-types.xhtml) for encoding format, RDA [carrier type](http://www.loc.gov/standards/valuelist/rdacarrier.html) for material, and the LRMI [Concept Scheme for Educational Use](https://www.dublincore.org/specifications/lrmi/concept_schemes/#educational-use).

### About this Concept Scheme
This is not intended to be a complete list. The aim is that it should be possible to classify any learning resource using one or more concept from this scheme. That is probably not yet the case and so the list is open for further additions, see below.

This is not a detailed list. While there is a tendency to want to classify learning resources more precisely, several efforts to do so in a wide range of contexts have exposed the ambiguity of such classifications. Providing a more detailed set of concepts increases ambiguity even as it seems to increase specificity. The aim is that although the concepts here are broad, they will be useful; however, for specialized uses it may be necessary for other concept schemes to refine or subdivide these concepts. A `skos:broadMatch` relationship may be declared to express a relationship from such a concept to one in this LRMI Resource Type concept scheme. For example a service specializing in textbooks may wish to create classification concepts that are narrower than the TextBook concept defined here in order to classify more specific types of text book. We hope they will define a `skos:broadMatch` relationship between their concepts and ours, and that they will find it useful to publish descriptions that include reference to our broader concept defined here if it is more widely understood.

No hierarchy is hard-wired into the concept names or identifiers. Relationships between concepts, which may include the concepts being broader and narrower than each other, will be specified using SKOS, but we would not create a concept with the sole purpose of gathering a group of concepts under one heading. This maximises compatibility with other vocabularies (a rabbit is a rabbit regardless of whether it is classified in a hierarchy under pets, food or mammals). It also avoids the sometimes awkward or arbitrary results of having to place everything in a hierarchy.

The concept identifiers and definitions defined here are normative; labels and scope notes are not normative.

### Suggesting new concepts
It is not the aim to provide a comprehensive list of every possible category of learning resource, the aim is to provide a limited number of broad categories such that the type of any learning resource can be specified.

If there is a broad type of learning resource that you think is not covered and which meets the definitions provided in notes above, please open an issue using the [new learning resource type](https://github.com/dcmi/lrmi/issues/new?assignees=philbarker&labels=enhancement%2C+LearningResourceTypes&template=new-learning-resource-type.md&title=%5BNew+learning+resource+type%5D) template.
(Alternatively you may contact the Dublin Core Metadata Initiative LRMI Task Group at lrmi-contact@dublincore.net)
