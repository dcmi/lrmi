---
title: "Concept Schemes"
date: 2018-01-08T18:19:06Z
draft: false
---

# LRMI Concept Schemes

![](/images/LRMI_400w.png)

# LRMI Concept Schemes

![](/images/Specifications_logo.png)

<img src="/images/DCMI_logo_cropped.jpg" style="max-width: 25px; margin-right: 5px;" name="DCMI Logo"/>DCMI Home&nbsp;&nbsp;&nbsp; <img src="/images/DCMI_logo_cropped.jpg" style="max-width: 25px; margin-right: 5px;" name="DCMI Logo"/>[LRMI 1.1](/dcx/lrmi-terms/1.1/)&nbsp;&nbsp;&nbsp; <img src="/images/DCMI_logo_cropped.jpg" style="max-width: 25px; margin-right: 5px;" name="DCMI Logo"/>[Return to Community Specifications TOC](/documents/#communityspecifications)

<dl class="frontmatter">
<dt><strong>Title:</strong></dt>
<dd>LRMI Concept Schemes</dd>
<dt><strong>Creator:</strong></dt>
<dd>LRMI Task Group (DC-Education Community)</dd>
<dt><strong>Editors</strong></dt>
<dd>Phil Barker<br>Stuart Sutton</dd>
<dt><strong>Identifier:</strong></dt>
<dd><a href="@@@">@@@</a></dd>
<dt><strong>Current Version:</strong></dt>
<dd><a href="@@@">@@@</a></dd>
<dt><strong>Previous Version:</strong></dt>
<dd>--</dd>
<dt><strong>Date Issued:</strong></dt>
<dd>2018-01-15</dd>
<dt><strong>Document Status:</strong></dt>
<dd>Community Specification</dd>
<dt><strong>Description:</strong></dt>
<dd>The LRMI concept schemes are small sets of concepts for use as values with the LRMI properties in learning resource description and Web markup. Since the properties for which these concepts are intended <u>also exists</u> as <a href="https://schema.org">Schema.org properties</a>, the concepts in this concept scheme can be used with a level of certainty in Web markup. The concepts in the vocabularies have been declared in RDF using the W3C's <a href="https://www.w3.org/2004/02/skos/"><em>Simple Knowledge Organization System</em></a> (SKOS).</dd>
<dt>
<strong>Serializations:</strong> </dt>
<dd>RDF Turtle: <a href="@@@" target="_blank">@@@</a>
</dd>
<dd>JSONLD: <a href="@@@" target="_blank">@@@</a>
</dd>
<dt><strong>Further Development:</strong></dt>
<dd>Refinement of, and additions to, these SKOS concept schemes are managed through the DCMI/LRMI Github (<a href="https://github.com/dcmi/lrmi/blob/master/lrmi_vocabs/a">https://github.com/dcmi/lrmi/blob/master/lrmi_vocabs/</a>)</dd>
</dl>

<small>Licensed under a <a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International License</a>.</small>

## Table of Contents
1. [Introduction & Definitions](#introduction_and_defintitions)
2. [Namespaces](#namespaces)  
3. [Concept Schemes](#concept_schemes)
	* [Alignment Type](#alignment_type)  
  * [Educational Audience Role](#educational_audience_role)  
  * [Educational Use](#educational_use)  
  * [Interactivity Type](#interactivity_type)

## Alphabetical Index of Concepts

- [active](#active)
- [administrator](#administrator)
- [assesses](#assesses)
- [assessment](#assessment)
- [complexity level](#complexity_level)
- [educational level](#education_level)
- [educational subject](#educational_subject)
- [expositive](#expositive)
- [general public](#general_public)
- [instruction](#instruction)
- [mentor](#mentor)
- [mixed](#mixed)
- [parent](#parent)
- [peer tutor](#peer_tutor)
- [prerequisite](#prerequisite)
- [professional](#professional)
- [professional support](#professional_support)
- [reading level](#reading_level)
- [student](#student)
- [teacher](#teacher)
- [teaches](teaches)

<a name="introduction_and_defintitions"></a>
## 1. Introduction & Definitions

This document is an up-to-date specification of the LRMI concept schemes maintained by the Dublin Core Metadata Initiative.

A subset of attributes from the following table are used in defining the concept schemes and their associated concepts. These attributes are drawn from the _Simple Knowledge Organization System_ (SKOS) and other namespaces identified in Section 2.

| :Attribute: | :Description: |
| --- | --- |
| Alternative Label: | An alternative lexical label for a concept. Acronyms, abbreviations, spelling variants, and irregular plural/singular forms may be included among the alternative labels for a concept. Mis-spelled terms are normally included as hidden labels (see hiddenLabel). |
| Broader Concept: | Relates a concept to a concept that is more general in meaning. Broader concepts are typically rendered as parents in a concept hierarchy (tree). By convention, skos:broader is only used to assert an immediate (i.e. direct) hierarchical link between two conceptual resources. |
| Date Created: | Date of creation of the resource. |
| Date Modified: | Date on which the resource was changed. |
| Definition: | A statement or formal explanation of the meaning of a concept. |
| Description: | An account of the resource. |
| Has Top Concept: | Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to these hierarchies. |
| Hidden Label: | A lexical label for a resource that should be hidden when generating visual displays of the resource, but should still be accessible to free text search operations. |
| In Scheme: | Relates a resource (for example a concept) to a concept scheme in which it is included. A concept may be a member of more than one concept scheme. |
| License: | A legal document giving official permission to do something with the resource. |
| Narrower Concept: | Relates a concept to a concept that is more specific in meaning. By convention, skos:narrower is only used to assert an immediate (i.e. direct) hierarchical link between two conceptual resources. Narrower concepts are typically rendered as children in a concept hierarchy (tree). |
| Preferred Label: | Relates a concept to a concept that is more specific in meaning. By convention, skos:narrower is only used to assert an immediate (i.e. direct) hierarchical link between two conceptual resources. Narrower concepts are typically rendered as children in a concept hierarchy (tree). |
| Scope Note: | A note that helps to clarify the meaning and/or the use of a concept. |
| Source: | A related resource from which the described resource is derived. The described resource may be derived from the related resource in whole or in part. |
| Title: | A name given to the resource. |
| Top Concept Of: | Relates a concept to the concept scheme that it is a top level concept of. |

<a name="namespaces"></a>
## 2. Namespaces

In the following definitions of the _Alignment Type Concept Scheme_ and it's component concepts, the namespaces in the table below are referenced:

| Namespace Prefix | Namespace |
| --- | --- |
| dc | http://purl.org/dc/elements/1.1/ |
| dct | http://purl.org/dc/terms/ |
| rdf | http://www.w3.org/2000/01/rdf-schema# |
| skos | http://www.w3.org/2008/05/skos# |

<a name="concept_schemes"></a>
## 3. Concept Schemes

<a name="alignment_type"></a>
### 3.1. Alignment Type

| --- | --- |
| URI: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/](http://purl.org/dcx/lrmi-vocabs/alignmentType/) |
| Type: | [skos:ConceptScheme](http://www.w3.org/2008/05/skos#ConceptScheme) |
| Title: | LRMI Alignment Type Vocabulary |
| Description: | A concept scheme that defines the types of relationships between a learning resource and a node in an educational framework. |
| Creator: | LRMI Task Group (DCMI) |
| Date Created: | 2017-03-01 |
| Date Modified: | 2017-12-20 |
| License: | http://creativecommons.org/licenses/by/4.0/ |

<a name="assesses"></a>
#### **Assesses**

| URI: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/assesses](http://purl.org/dcx/lrmi-vocabs/alignmentType/assesses) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | assesses |
| Definition: | The learning resource being described may be used to assess the competency being referenced. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#Assesses. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/](http://purl.org/dcx/lrmi-vocabs/alignmentType/) |

<a name="complexity_level"></a>
**Complexity Level**

| URI: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/complexityLevel](http://purl.org/dcx/lrmi-vocabs/alignmentType/assesses) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | complexity level |
| Definition: | The point in the framework being referenced defines a level or range that measures the difficulty or challenge presented by the learning resource being described. |
| Scope Note: | Example frameworks include, but are not limited to, Bloom's Taxonomy, Norman Webb's Depth of Knowledge (DOK), Biggs' SOLO taxonomy, Lexile and Quantile frameworks by MetaMetrics. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/](http://purl.org/dcx/lrmi-vocabs/alignmentType/) |

<a name="educational_level"></a>
**Educational Level**

| URI: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/educationalLevel](http://purl.org/dcx/lrmi-vocabs/alignmentType/educationalLevel) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | educational level |
| Definition: | The point in the framework being referenced defines a level or stage within an education system for which the resource being described is intended or useful. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#EducationalLevel. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/](http://purl.org/dcx/lrmi-vocabs/alignmentType/) |

<a name="educational_subject"></a>
**Educational Subject**

| URI: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/educationalSubject](http://purl.org/dcx/lrmi-vocabs/alignmentType/educationalSubject) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | educational subject |
| Definition: | The point in the framework being referenced defines the subject context of the learning resource being described. |
| Scope Note: | The educational subject identifies the educational context of the resource being described such as "math", "science", "physics", "algebra", and "English language arts". To identify the particular topic(s), or aboutness, of the resource being described--e.g., "Pythagorean theorem", "Abraham Lincoln", "Ayers Rock"--use the schema.org/about property. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#EducationalSubject. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/](http://purl.org/dcx/lrmi-vocabs/alignmentType/) |

<a name="prerequisite"></a>
**Prerequisite**

| URI: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/prerequisite](http://purl.org/dcx/lrmi-vocabs/alignmentType/prerequisite) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | prerequisite |
| Definition: | The competency being referenced is a learning prerequisite to the effective outcome of the learning resource being described. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000715. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/](http://purl.org/dcx/lrmi-vocabs/alignmentType/) |

<a name="reading_level"></a>
**Reading Level**

| URI: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/readingLevel](http://purl.org/dcx/lrmi-vocabs/alignmentType/readingLevel) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | reading level |
| Definition: | The point in the framework being referenced defines a level or range of reading ability expected for a person using the learning resource being described. |
| Scope Note: | Example frameworks include, but are not limited to, Lexile Framework by MetaMetrics, ATOS by Renaissance Learning, Degrees of Reading Power (DRP) by Questar Assessment, Flesch-Kincaid (public domain), Reading Maturity by Pearson Education, SourceRater by Educational Testing Service, Easability Indicator by Coh-Metrix, and the Oxford Reading Tree levels from Oxford University Press. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#ReadingLevel. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/](http://purl.org/dcx/lrmi-vocabs/alignmentType/) |

<a name="teaches"></a>
**Teaches**

| URI: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/teaches](http://purl.org/dcx/lrmi-vocabs/alignmentType/teaches) |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | teaches |
| --- | --- |
| Definition: | The learning resource being described may be used to teach the competency being referenced. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#Teaches. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/alignmentType/](http://purl.org/dcx/lrmi-vocabs/alignmentType/) |

<a name="educational_audience_role"></a>
### 3.2. Educational Audience Role

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |
| Type: | [skos:ConceptScheme](http://www.w3.org/2008/05/skos#ConceptScheme) |
| Title: | LRMI Educational Audience Role Vocabulary |
| Description: | A concept scheme that defines the primary or intended roles of the audience (beneficiary) of the resource being described. |
| Creator: | LRMI Task Group (DCMI) |
| Date Created: | 2017-03-01 |
| Date Modified: | 2017-12-20 |
| License: | http://creativecommons.org/licenses/by/4.0/ |

<a name="administrator"></a>
**Administrator**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/administrator](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/administrator) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | administrator |
| Definition: | A trainer or educator with administrative authority and responsibility. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |

<a name="general_public"></a>
**General Public**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/generalPublic](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/generalPublic) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | general public |
| Definition: | The public at large. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |

<a name="mentor"></a>
**Mentor**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/mentor](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/mentor) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | mentor |
| Definition: | Someone who advises, trains, supports, and/or guides. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |

<a name="parent"></a>
**Parent**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/parent](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/parent) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | parent |
| Definition: | A father, mother, or legal guardian. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |

<a name="peer_tutor"></a>
**Peer Tutor**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/peerTutor](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/peerTutor) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | peer tutor |
| Definition: | The peer learner serving as tutor of another learner. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |

<a name="professional"></a>
**Professional**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/professional](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/professional) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | professional |
| Definition: | Someone already practicing a profession; an industry partner, or professional development trainer. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |

<a name="student"></a>
**Student**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/student](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/student) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | student |
| Definition: | The learner or trainee. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |

<a name="teacher"></a>
**Teacher**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/teacher](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/teacher) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | teacher |
| Definition: | A person who has been trained to implement educational methods and practices. |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/](http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/) |

<a name="educational_use"></a>
### 3.3. Educational Use

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalUse/](http://purl.org/dcx/lrmi-vocabs/educationalUse/) |
| Type: | [skos:ConceptScheme](http://www.w3.org/2008/05/skos#ConceptScheme) |
| Title: | LRMI Educational Use Vocabulary |
| Description: | A concept scheme that enumerates the educational uses of a learning resource. |
| Creator: | LRMI Task Group (DCMI) |
| Date Created: | 2017-03-01 |
| Date Modified: | 2017-12-20 |
| License: | http://creativecommons.org/licenses/by/4.0/ |

<a name="assessment"></a>
**Assessment**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalUse/assessment](http://purl.org/dcx/lrmi-vocabs/educationalUse/assessment) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | assessment |
| Definition: | Primary purpose of the resource is to evaluate learning, before, during, or after instruction occurs. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/001002#Assessment |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalUse/](http://purl.org/dcx/lrmi-vocabs/educationalUse/) |

<a name="instruction"></a>
**Instruction**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalUse/instruction](http://purl.org/dcx/lrmi-vocabs/educationalUse/instruction) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | instruction |
| Definition: | Primary purpose of the resource is to support the instructional process, student learning, or to provide information about the curriculum. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/001002#CurriculumInstruction |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalUse/](http://purl.org/dcx/lrmi-vocabs/educationalUse/) |

<a name="professional_support"></a>
**Professional Support**

| URI: | [http://purl.org/dcx/lrmi-vocabs/educationalUse/professionalSupport](http://purl.org/dcx/lrmi-vocabs/educationalUse/professionalSupport) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | professional support |
| Definition: | Primary purpose of the resource is to provide instruction for a teacher or other education professional including professional development. |
| Source: | Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/001002#ProfessionalDevelopment |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/educationalUse/](http://purl.org/dcx/lrmi-vocabs/educationalUse/) |

<a name="interactivity_type"></a>
### 3.4. Interactivity Type

| URI: | [http://purl.org/dcx/lrmi-vocabs/interactivityType/](http://purl.org/dcx/lrmi-vocabs/educationalUse/) |
| Type: | [skos:ConceptScheme](http://www.w3.org/2008/05/skos#ConceptScheme) |
| Title: | LRMI Interactivity Type Vocabulary |
| Description: | A concept scheme that defines the predominate interact mode of the learning resource being described. |
| Creator: | LRMI Task Group (DCMI) |
| Source: | Based on the IEEE Learning Object Metadata standard (IEEE/LOM - IEEE 1484.12.1-202) |
| Date Created: | 2017-03-01 |
| Date Modified: | 2017-12-20 |
| License: | http://creativecommons.org/licenses/by/4.0/ |

<a name="active"></a>
**Active**

| URI: | [http://purl.org/dcx/lrmi-vocabs/interactivityType/active](http://purl.org/dcx/lrmi-vocabs/interactivityType/active) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | active |
| Definition: | A concept scheme that defines the predominate interact mode of the learning resource being described. |
| Source: | Based on the IEEE Learning Object Metadata standard (IEEE/LOM - IEEE 1484.12.1-202). |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/interactivity type/](http://purl.org/dcx/lrmi-vocabs/interactivityType/) |

<a name="expositive"></a>
**Expositive**

| URI: | [http://purl.org/dcx/lrmi-vocabs/interactivityType/expositive](http://purl.org/dcx/lrmi-vocabs/interactivityType/expositive) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | expositive |
| Definition: | Use of a subject-matter expert to explain a concept or give clear and concise information in a purposeful way to the passive learner. |
| Source: | Based on the IEEE Learning Object Metadata standard (IEEE 1484.12.1-202 (LOMv1.0)). |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/interactivityType/](http://purl.org/dcx/lrmi-vocabs/interactivityType/) |

<a name="mixed"></a>
**Mixed**

| URI: | [http://purl.org/dcx/lrmi-vocabs/interactivityType/mixed](http://purl.org/dcx/lrmi-vocabs/interactivityType/mixed) |
| --- | --- |
| Type: | [skos:Concept](http://www.w3.org/2008/05/skos#Concept) |
| Preferred Label: | mixed |
| Definition: | Instructional interactions comprised of a mix of active learning and expositive approaches. |
| Source: | Based on IEEE Learning Object Metadata standard (IEEE 1484.12.1-202 (LOMv1.0)). |
| In Scheme: | [http://purl.org/dcx/lrmi-vocabs/interactivityType/](http://purl.org/dcx/lrmi-vocabs/educationalUse/) |

&nbsp;

* * *

