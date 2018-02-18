---
title: "LRMI Concept Schemes"
date: 2018-01-12T18:19:06Z
draft: false
---

<table border="0">
<tr>
<td width="50">Creator:</td>
<td>LRMI Task Group (DC-Education Community)</td>
</tr>
<tr>
<td>Editors:</td>
<td>Phil Barker<br />Stuart Sutton</td>
</tr>
<tr>
<td>Document Status:</td>
<td>DCMI Community Specification</td>
</tr>
<tr>
<td>Description:</td>
<td>The LRMI concept schemes are small sets of concepts for use as values with the LRMI properties in learning resource description and Web markup. Since the properties for which these concepts are intended <u>also exists</u> as <a href="https://schema.org">Schema.org properties</a>, the concepts in this concept scheme can be used with a level of certainty in Web markup. The concepts in the vocabularies have been declared in RDF using the W3C's <a href="https://www.w3.org/2004/02/skos/">Simple Knowledge Organization System</a>.</td>
</tr>
</table>

<p><small>Licensed under a <a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International License</a>.</small></p>

<p><a id="toc" name="toc"></a></p>

<h2 id="table-of-contents">Table of Contents</h2>

<a href="#intro">1. Introduction &amp; Definitions</a><br />
<a href="#namespace">2. Namespaces</a><br/>
<a href="#concept-scheme">3. Concept Schemes</a><br />
&nbsp;&nbsp;&nbsp;<a href="#alignment-type">3.1. Alignment Type</a><br/>
&nbsp;&nbsp;&nbsp;<a href="#educational-audience-role">3.2. Educational Audience Role</a><br/>
&nbsp;&nbsp;&nbsp;<a href="#educational-use">3.3. Educational Use</a><br/>
&nbsp;&nbsp;&nbsp;<a href="#interactivity-type">3.4. Interactivity Type</a><br/>
		


<p><a id="terms" name="terms"></a></p>

<h2 id="index-of-terms-in-the-lrmi-terms-namespace">Alphabetical Index of Concepts</h2>

<ul>
<li><a href="#active">active</a></li>
<li><a href="#administrator">administrator</a></li>
<li><a href="#assesses">assesses</a></li>
<li><a href="#assessment">assessment</a></li>
<li><a href="#complexity-level">complexity level</a></li>
<li><a href="#educational-level">educational level</a></li>
<li><a href="#educational-subject">educational subject</a></li>
<li><a href="#expositive">expositive</a></li>
<li><a href="#general-public">general public</a></li>
<li><a href="#instruction">instruction</a></li>
<li><a href="#mentor">mentor</a></li>
<li><a href="#mixed">mixed</a></li>
<li><a href="#parent">parent</a></li>
<li><a href="#peer-tutor">peer tutor</a></li>
<li><a href="#prerequisite">prerequisite</a></li>
<li><a href="#professional">professional</a></li>
<li><a href="#professional-support">professional support</a></li>
<li><a href="#reading-level">reading level</a></li>
<li><a href="#student">student</a></li>
<li><a href="#teacher">teacher</a></li>
<li><a href="#teaches">teaches</a></li>
</ul>

<p><a id="intro" name="intro"></a></p>

<h2 id="1-introduction-amp-definitions">1. Introduction &amp; Definitions</h2>

<p>This document is an up-to-date specification of the LRMI concept schemes maintained by the Dublin Core Metadata Initiative.</p>

<p>A subset of attributes from the following table are used in defining the concept schemes and their associated concepts. These attributes are drawn from the <em>Simple Knowledge Organization System</em> (SKOS) and other namespaces identified in Section 2.</p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Alternative Label:</td>
    <td>An alternative lexical label for a concept. Acronyms, abbreviations, spelling variants, and irregular plural/singular forms may be included among the alternative labels for a concept. Mis-spelled terms are normally included as hidden labels (see hiddenLabel).</td>
  </tr>
  <tr>
    <td align="right">Broader Concept:</td>
    <td>Relates a concept to a concept that is more general in meaning. Broader concepts are typically rendered as parents in a concept hierarchy (tree). By convention, skos:broader is only used to assert an immediate (i.e. direct) hierarchical link between two conceptual resources.</td>
  </tr>
  <tr>
    <td align="right">Date Created:</td>
    <td>Date of creation of the resource.</td>
  </tr>
  <tr>
    <td align="right">Date Modified:</td>
    <td>Date on which the resource was changed.</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>A statement or formal explanation of the meaning of a concept.</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>An account of the resource.</td>
  </tr>
  <tr>
    <td align="right">Has Top Concept:</td>
    <td>Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to these hierarchies.</td>
  </tr>
  <tr>
    <td align="right">Hidden Label:</td>
    <td>A lexical label for a resource that should be hidden when generating visual displays of the resource, but should still be accessible to free text search operations.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td>Relates a resource (for example a concept) to a concept scheme in which it is included. A concept may be a member of more than one concept scheme.</td>
  </tr>
  <tr>
    <td align="right">License:</td>
    <td>A legal document giving official permission to do something with the resource.</td>
  </tr>
  <tr>
    <td align="right">Narrower Concept:</td>
    <td>Relates a concept to a concept that is more specific in meaning. By convention, skos:narrower is only used to assert an immediate (i.e. direct) hierarchical link between two conceptual resources. Narrower concepts are typically rendered as children in a concept hierarchy (tree).</td>
  </tr>
  <tr>
    <td align="right">Preferred Label:</td>
    <td>Relates a concept to a concept that is more specific in meaning. By convention, skos:narrower is only used to assert an immediate (i.e. direct) hierarchical link between two conceptual resources. Narrower concepts are typically rendered as children in a concept hierarchy (tree).</td>
  </tr>
  <tr>
    <td align="right">Scope Note:</td>
    <td>A note that helps to clarify the meaning and/or the use of a concept.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>A related resource from which the described resource is derived. The described resource may be derived from the related resource in whole or in part.</td>
  </tr>
  <tr>
    <td align="right">Title:</td>
    <td>A name given to the resource.</td>
  </tr>
  <tr>
    <td align="right">Top Concept Of:</td>
    <td>Relates a concept to the concept scheme that it is a top level concept of.</td>
  </tr>
</table>

<p><a id="namespace" name="intro"></a></p>

<h2 id="2-namespaces">2. Namespaces</h2>

<p>In the following definitions of the <em>Alignment Type Concept Scheme</em> and it's component concepts, the namespaces in the table below are referenced:</p>

<table cellpadding="5" width="85%">
  <tr>
    <th width="150" align="right">Namespace Prefix</th>
    <th align="left">Namespace</th>
  </tr>
  <tr>
    <td width="150" align="right">dc</td>
    <td>http://purl.org/dc/elements/1.1/</td>
  </tr>
  <tr>
    <td align="right">dct</td>
    <td>http://purl.org/dc/terms/</td>
  </tr>
  <tr>
    <td align="right">rdf</td>
    <td>http://www.w3.org/2000/01/rdf-schema#</td>
  </tr>
  <tr>
    <td align="right">skos</td>
    <td>http://www.w3.org/2008/05/skos#</td>
  </tr>
</table>

<p><a id="concept-schemes" name="concept-schemes"></a></p>

<h2 id="3-concept-scheme">3. Concept Schemes</h2>


<p><a id="alignment-type" name="alignment-type"></a></p>

<h3 id="3.1-concept-scheme">3.1. Alignment Type</h3>

<table cellpadding="5" width="85%">
 <tr>
   <td align="right">URI:</td>
   <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/">http://purl.org/dcx/lrmi-vocabs/alignmentType/</td>
 </tr>
<tr>
  <td align="right">Type:</td>
  <td><a href="http://www.w3.org/2008/05/skos#ConceptScheme">skos:ConceptScheme</a></td>
</tr>  
  <tr>
    <td width="150" align="right">Title:</td>
    <td>LRMI Alignment Type Vocabulary</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>A concept scheme that defines the types of relationships between a learning resource and a node in an educational framework.</td>
  </tr>
  <tr>
    <td align="right">Creator:</td>
    <td>LRMI Task Group (DCMI)</td>
  </tr>
  <tr>
    <td align="right">Date Created:</td>
    <td>2017-03-01</td>
  </tr>
  <tr>
    <td align="right">Date Modified:</td>
    <td>2017-12-20</td>
  </tr>
  <tr>
    <td align="right">License:</td>
    <td><a href="<http://creativecommons.org/licenses/by/4.0/>">http://creativecommons.org/licenses/by/4.0/</a></td>
  </tr>
</table>

<p><a name="assesses"><strong>Assesses</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/assesses">http://purl.org/dcx/lrmi-vocabs/alignmentType/assesses</a></td>
  </tr>
  <tr>
    <td align="right">Type:</td>
    <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
  </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>assesses</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The learning resource being described may be used to assess the competency being referenced.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#Assesses.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/">http://purl.org/dcx/lrmi-vocabs/alignmentType/</a></td>
  </tr>
</table>

<p><a name="complexity-level"><strong>Complexity Level</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/assesses">http://purl.org/dcx/lrmi-vocabs/alignmentType/complexityLevel</a></td>
  </tr> 
  <tr>
    <td align="right">Type:</td>
    <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
  </tr>   
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>complexity level</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The point in the framework being referenced defines a level or range that measures the difficulty or challenge presented by the learning resource being described.</td>
  </tr>
  <tr>
    <td align="right">Scope Note:</td>
    <td>Example frameworks include, but are not limited to, Bloom's Taxonomy, Norman Webb's Depth of Knowledge (DOK), Biggs' SOLO taxonomy, Lexile and Quantile frameworks by MetaMetrics.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/">http://purl.org/dcx/lrmi-vocabs/alignmentType/</a></td>
  </tr>
</table>

<p><a name="educational-level"><strong>Educational Level</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/educationalLevel">http://purl.org/dcx/lrmi-vocabs/alignmentType/educationalLevel</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr>  
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>educational level</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The point in the framework being referenced defines a level or stage within an education system for which the resource being described is intended or useful.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#EducationalLevel.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/">http://purl.org/dcx/lrmi-vocabs/alignmentType/</a></td>
  </tr>
</table>

<p><a name="educational-subject"><strong>Educational Subject</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/educationalSubject">http://purl.org/dcx/lrmi-vocabs/alignmentType/educationalSubject</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr>  
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>educational subject</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The point in the framework being referenced defines the subject context of the learning resource being described.</td>
  </tr>
  <tr>
    <td align="right">Scope Note:</td>
    <td>The educational subject identifies the educational context of the resource being described such as "math", "science", "physics", "algebra", and "English language arts". To identify the particular topic(s), or aboutness, of the resource being described--e.g., "Pythagorean theorem", "Abraham Lincoln", "Ayers Rock"--use the schema.org/about property.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#EducationalSubject.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/">http://purl.org/dcx/lrmi-vocabs/alignmentType/</a></td>
  </tr>
</table>

<p><a name="prerequisite"><strong>Prerequisite</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/prerequisite">http://purl.org/dcx/lrmi-vocabs/alignmentType/prerequisite</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr>  
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>prerequisite</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The competency being referenced is a learning prerequisite to the effective outcome of the learning resource being described.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000715.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/">http://purl.org/dcx/lrmi-vocabs/alignmentType/</a></td>
  </tr>
</table>

<p><a name="reading-level"><strong>Reading Level</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/readingLevel">http://purl.org/dcx/lrmi-vocabs/alignmentType/readingLevel</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr>  
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>reading level</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The point in the framework being referenced defines a level or range of reading ability expected for a person using the learning resource being described.</td>
  </tr>
  <tr>
    <td align="right">Scope Note:</td>
    <td>Example frameworks include, but are not limited to, Lexile Framework by MetaMetrics, ATOS by Renaissance Learning, Degrees of Reading Power (DRP) by Questar Assessment, Flesch-Kincaid (public domain), Reading Maturity by Pearson Education, SourceRater by Educational Testing Service, Easability Indicator by Coh-Metrix, and the Oxford Reading Tree levels from Oxford University Press.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#ReadingLevel.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/">http://purl.org/dcx/lrmi-vocabs/alignmentType/</a></td>
  </tr>
</table>

<p><a name="teaches"><strong>Teaches</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/teaches">http://purl.org/dcx/lrmi-vocabs/alignmentType/teaches</a></td>
  </tr> 
  <tr>
    <td align="right">Type:</td>
    <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
  </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>teaches</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The learning resource being described may be used to teach the competency being referenced.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/000869#Teaches.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/alignmentType/">http://purl.org/dcx/lrmi-vocabs/alignmentType/</a></td>
  </tr>
</table>

<p><a id="educational-audience-role" name="educational-audience-role"></a></p>

<h3 id="3.2-educational-audience-role">3.2. Educational Audience Role</h3>

<table cellpadding="5" width="85%">
 <tr>
   <td align="right">URI:</td>
   <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</td>
 </tr>
<tr>
  <td align="right">Type:</td>
  <td><a href="http://www.w3.org/2008/05/skos#ConceptScheme">skos:ConceptScheme</a></td>
</tr>  
  <tr>
    <td width="150" align="right">Title:</td>
    <td>LRMI Educational Audience Role Vocabulary</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>A concept scheme that defines the primary or intended roles of the audience (beneficiary) of the resource being described.</td>
  </tr>
  <tr>
    <td align="right">Creator:</td>
    <td>LRMI Task Group (DCMI)</td>
  </tr>
  <tr>
    <td align="right">Date Created:</td>
    <td>2017-03-01</td>
  </tr>
  <tr>
    <td align="right">Date Modified:</td>
    <td>2017-12-20</td>
  </tr>
  <tr>
    <td align="right">License:</td>
    <td><a href="<http://creativecommons.org/licenses/by/4.0/>">http://creativecommons.org/licenses/by/4.0/</a></td>
  </tr>
</table>

<p><a name="administrator"><strong>Administrator</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/administrator">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/administrator</a></td>
  </tr> 
  <tr>
    <td align="right">Type:</td>
    <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
  </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>administrator</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>A trainer or educator with administrative authority and responsibility.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</a></td>
  </tr>
</table>

<p><a name="general-public"><strong>General Public</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/generalPublic">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/generalPublic</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>general public</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The public at large.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</a></td>
  </tr>
</table>

<p><a name="mentor"><strong>Mentor</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/mentor">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/mentor</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>mentor</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>Someone who advises, trains, supports, and/or guides.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</a></td>
  </tr>
</table>

<p><a name="parent"><strong>Parent</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/parent">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/parent</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>parent</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>A father, mother, or legal guardian.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</a></td>
  </tr>
</table>

<p><a name="peer-tutor"><strong>Peer Tutor</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/peerTutor">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/peerTutor</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>peer tutor</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The peer learner serving as tutor of another learner.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</a></td>
  </tr>
</table>

<p><a name="professional"><strong>Professional</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/professional">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/professional</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>professional</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>Someone already practicing a profession; an industry partner, or professional development trainer.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</a></td>
  </tr>
</table>

<p><a name="student"><strong>Student</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/student">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/student</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>student</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The learner or trainee.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</a></td>
  </tr>
</table>

<p><a name="teacher"><strong>Teacher</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/teacher">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/teacher</a></td>
  </tr> 
  <tr>
    <td align="right">Type:</td>
    <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
  </tr>
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>teacher</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>A person who has been trained to implement educational methods and practices.</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/">http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/</a></td>
  </tr>
</table>

<p><a id="educational-use" name="educational-use"></a></p>

<h3 id="3.3-educational-use">3.3. Educational Use</h3>

<table cellpadding="5" width="85%">
 <tr>
   <td align="right">URI:</td>
   <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/">http://purl.org/dcx/lrmi-vocabs/educationalUse/</td>
 </tr> 
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#ConceptScheme">skos:ConceptScheme</a></td>
 </tr>
  <tr>
    <td width="150" align="right">Title:</td>
    <td>LRMI Educational Use Vocabulary</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>A concept scheme that enumerates the educational uses of a learning resource.</td>
  </tr>
  <tr>
    <td align="right">Creator:</td>
    <td>LRMI Task Group (DCMI)</td>
  </tr>
  <tr>
    <td align="right">Date Created:</td>
    <td>2017-03-01</td>
  </tr>
  <tr>
    <td align="right">Date Modified:</td>
    <td>2017-12-20</td>
  </tr>
  <tr>
    <td align="right">License:</td>
    <td><a href="<http://creativecommons.org/licenses/by/4.0/>">http://creativecommons.org/licenses/by/4.0/</a></td>
  </tr>
</table>

<p><a name="assessment"><strong>Assessment</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/assessment">http://purl.org/dcx/lrmi-vocabs/educationalUse/assessment</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>assessment</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>Primary purpose of the resource is to evaluate learning, before, during, or after instruction occurs.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/001002#Assessment</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/">http://purl.org/dcx/lrmi-vocabs/educationalUse/</a></td>
  </tr>
</table>

<p><a name="instruction"><strong>Instruction</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/instruction">http://purl.org/dcx/lrmi-vocabs/educationalUse/instruction</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>instruction</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>Primary purpose of the resource is to support the instructional process, student learning, or to provide information about the curriculum.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/001002#CurriculumInstruction</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/">http://purl.org/dcx/lrmi-vocabs/educationalUse/</a></td>
  </tr>
</table>

<p><a name="professional-support"><strong>Professional Support</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/professionalSupport">http://purl.org/dcx/lrmi-vocabs/educationalUse/professionalSupport</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr> 
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>professional support</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>Primary purpose of the resource is to provide instruction for a teacher or other education professional including professional development.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on Common Education Data Standards (CEDS): https://ceds.ed.gov/element/001002#ProfessionalDevelopment</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/">http://purl.org/dcx/lrmi-vocabs/educationalUse/</a></td>
  </tr>
</table>

<p><a id="interactivity-type" name="interactivity-type"></a></p>

<h3 id="3.4-interactivity-type">3.4. Interactivity Type</h3>

<table cellpadding="5" width="85%">
 <tr>
   <td align="right">URI:</td>
   <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/">http://purl.org/dcx/lrmi-vocabs/interactivityType/</td>
 </tr>
<tr>
  <td align="right">Type:</td>
  <td><a href="http://www.w3.org/2008/05/skos#ConceptScheme">skos:ConceptScheme</a></td>
</tr>  
  <tr>
    <td width="150" align="right">Title:</td>
    <td>LRMI Interactivity Type Vocabulary</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>A concept scheme that defines the predominate interact mode of the learning resource being described.</td>
  </tr>
  <tr>
    <td align="right">Creator:</td>
    <td>LRMI Task Group (DCMI)</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on the IEEE Learning Object Metadata standard (IEEE/LOM - IEEE 1484.12.1-202)</td>
  </tr>
  <tr>
    <td align="right">Date Created:</td>
    <td>2017-03-01</td>
  </tr>
  <tr>
    <td align="right">Date Modified:</td>
    <td>2017-12-20</td>
  </tr>
  <tr>
    <td align="right">License:</td>
    <td><a href="<http://creativecommons.org/licenses/by/4.0/>">http://creativecommons.org/licenses/by/4.0/</a></td>
  </tr>
</table>

<p><a name="active"><strong>Active</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/interactivityType/active">http://purl.org/dcx/lrmi-vocabs/interactivityType/active</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr>  
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>active</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>A concept scheme that defines the predominate interact mode of the learning resource being described.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on the IEEE Learning Object Metadata standard (IEEE/LOM - IEEE 1484.12.1-202).</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/interactivityType/">http://purl.org/dcx/lrmi-vocabs/interactivity type/</a></td>
  </tr>
</table>

<p><a name="expositive"><strong>Expositive</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/interactivityType/expositive">http://purl.org/dcx/lrmi-vocabs/interactivityType/expositive</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr>  
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>expositive</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>Use of a subject-matter expert to explain a concept or give clear and concise information in a purposeful way to the passive learner.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on the IEEE Learning Object Metadata standard (IEEE 1484.12.1-202 (LOMv1.0)).</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/interactivityType/">http://purl.org/dcx/lrmi-vocabs/interactivityType/</a></td>
  </tr>
</table>

<p><a name="mixed"><strong>Mixed</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/interactivityType/mixed">http://purl.org/dcx/lrmi-vocabs/interactivityType/mixed</a></td>
  </tr>
 <tr>
   <td align="right">Type:</td>
   <td><a href="http://www.w3.org/2008/05/skos#Concept">skos:Concept</a></td>
 </tr>  
  <tr>
    <td width="150" align="right">Preferred Label:</td>
    <td>mixed</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>Instructional interactions comprised of a mix of active learning and expositive approaches.</td>
  </tr>
  <tr>
    <td align="right">Source:</td>
    <td>Based on IEEE Learning Object Metadata standard (IEEE 1484.12.1-202 (LOMv1.0)).</td>
  </tr>
  <tr>
    <td align="right">In Scheme:</td>
    <td><a href="http://purl.org/dcx/lrmi-vocabs/educationalUse/">http://purl.org/dcx/lrmi-vocabs/interactivityType/</a></td>
  </tr>
</table>

