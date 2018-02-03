---
title: "LRMI Metadata Terms (RDF)"
date: 2018-02-03T08:26:17Z
draft: false
---
    	

<p><img src="/images/LRMI_400w.png" width="300"></p>

<hr />

<table>
<tr><td width="150"><strong>Title</strong></td><td>LRMI Terms as RDF</td></tr>
<tr><td><strong>Creator</strong></td><td>LRMI Task Group (DC-Education Community)</td></tr>
<tr><td><strong>Editors</strong></td><td>Phil Barker<br />Stuart Sutton</td></tr>
<tr><td><strong>Description</strong></td><td>The LRMI specification is a collection of classes and properties for markup and description of educational resources. The specification builds on the extensive vocabulary provided by Schema.org and other standards. LRMI terms not included in schema.org may nevertheless be used to augment and enrich Schema.org markup.</td></tr>
<tr><td><strong>Identifier</strong></td><td>@@@</td></tr>
<tr><td><strong>Current Version</strong></td><td><a href="http://purl.org/dcx/lrmi_terms/">http://purl.org/dcx/lrmi_terms/</a></td></tr>
<tr><td><strong>Previous Version</strong></td><td>--</td></tr>
<tr><td><strong>Date Published</strong></td><td>2015-02-09</td></tr>
<tr><td><strong>Document Status</strong></td><td>DCMI Community Specification</td></tr>
</table>

<p><small>Licensed under a <a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International License</a>.</small></p>

<hr />

<p><a id="toc" name="toc"></a></p>

<h2 id="table-of-contents">Table of Contents</h2>

<p><a href="#terms">Index of Terms</a></p>

<ol>
<li><a href="#intro">Introduction &amp; Definitions</a></li>
<li><a href="#namespace">Namespace</a></li>
<li><a href="#classes">Classes</a></li>
<li><a href="#properties">Properties</a></li>
<li><a href="#version">Version Changes</a></li>
<li><a href="#turtle">Turtle Serialization</a></li>
<li><a href="#history">Schema History</a></li>
</ol>

<p><a id="terms" name="terms"></a></p>

<h2 id="index-of-terms-in-the-lrmi-terms-namespace">Index of Terms in the /lrmi-terms/ Namespace</h2>

<ul>
<li>Classes

<ul>
<li><a href="#AlignmentObject">AlignmentObject</a></li>
<li><a href="#EducationalAudience">EducationalAudience</a></li>
</ul></li>
<li>Properties

<ul>
<li><a href="#alignmentType">alignmentType</a></li>
<li><a href="#educationalAlignment">educationalAlignment</a></li>
<li><a href="#educationalFramework">educationalFramework</a></li>
<li><a href="#educationalRole">educationalRole</a></li>
<li><a href="#educationalUse">educationalUse</a></li>
<li><a href="#interactivityType">interactivityType</a></li>
<li><a href="#isBasedOnUrl">isBasedOnUrl</a></li>
<li><a href="#learningResourceType">learningResourceType</a></li>
<li><a href="#targetDescription">targetDescription</a></li>
<li><a href="#targetName">targetName</a></li>
<li><a href="#targetUrl">targetUrl</a></li>
<li><a href="#timeRequired">timeRequired</a></li>
<li><a href="#typicalAgeRange">typicalAgeRange</a></li>
<li><a href="#useRightsUrl">useRightsUrl</a></li>
</ul></li>
</ul>

<p><a id="intro" name="intro"></a></p>

<h2 id="1-introduction-amp-definitions">1. Introduction &amp; Definitions</h2>

<p>This document is an up-to-date draft specification in RDF of the LRMI 1.1 metadata terms maintained by the Dublin Core Metadata Initiative.</p>

<p>In the following term tables, each term is specified with the following minimal set of attributes:</p>

<table cellpadding="5" width="85%">
  <tr>
  	<td width="175" align="left"><strong>Name:</strong></td>
    <td>A token appended to the URI of the LRMI namespace to create the URI of the term.</td>
  </tr>
  <tr>
  	<td align="left"><strong>Label:</strong></td>
    <td>The human-readable label assigned to the term.</td>
  </tr>
  <tr>
  	<td align="left"><strong>URI:</strong></td>
    <td>The Uniform Resource Identifier used to uniquely identify a term.</td>
  </tr>
  <tr>
  	<td align="left"><strong>Definition:</strong></td>
    <td>A statement that represents the concept and essential nature of the term.</td>
  </tr>
  <tr>
  	<td align="left"><strong>Type of Term:</strong></td>
    <td>The type of term—class or property.</td>
  </tr>
  <tr>
  	<td align="left"><strong>Date Issued/Modified:</strong></td>
    <td>The date the term was created or modified.</td>
  </tr>
</table>

<p>&nbsp;</p>
<h4>Where applicable, the following attributes provide additional information about a term:</h4>
<p>&nbsp;</p>

<table cellpadding="5" width="85%">
	<td width="175" align="left"><strong>Description:</strong></td>
  <td>Additional information about the term or its application.</td>
  <tr>
  	<td align="left"><strong>Subproperty Of:</strong></td>
    <td>A property of which the described term is a subproperty.</td>
  </tr>
  <tr>
  	<td align="left"><strong>Equivalent Property:</strong></td>
    <td>A property to which the described term is equivalent (<a href="http://www.w3.org/TR/owl-ref/#equivalentProperty-def" target="_blank">owl:equivalentProperty</a>).</td>
  </tr>
  <tr>
  	<td align="left"><strong>Subclass Of:</strong></td>
    <td>A class of which the described term is a subclass.</td>
  </tr>
  <tr>
  	<td align="left"><strong>Equivalent Class:</strong></td>
    <td>A class to which the described term is equivalent (<a href="http://www.w3.org/TR/owl-ref/#equivalentClass-def" target="_blank">owl:equivalentClass</a>).</td>
  </tr>
  <tr>
  	<td align="left"><strong>Has Domain:</strong></td>
    <td>Any resource that has a given property is [inferred to be] an instance of one or more classes (<a href="http://www.w3.org/TR/rdf-schema/#ch_domain" target="_blank">rdfs:domain</a>).</td>
  </tr>
  <tr>
  	<td align="left"><strong>Has Range:</strong></td>
    <td>The values of a property are [inferred to be] instances of one or more classes. (<a href="http://www.w3.org/TR/rdf-schema/#ch_range" target="_blank">rdfs:range</a>)</td>
  </tr>
  <tr>
  	<td align="left"><strong>Domain Includes:</strong></td>
    <td>Relates a property to a class that is (one of) the type(s) the property is expected to be used on. (<a href="https://schema.org/domainIncludes" target="_blank">https://schema.org/domainIncludes</a>).</td>
  </tr>
  <tr>
  	<td align="left"><strong>Range Includes:</strong></td>
    <td>Relates a property to a class that constitutes (one of) the expected type(s) for values of the property. (<a href="https://schema.org/rangeIncludes" target="_blank">https://schema.org/rangeIncludes</a>).</td>
  </tr>
  <tr>
  	<td align="left"><strong>Usage Note:</strong></td>
    <td>A reference to a resource that provides information on how this resource is to be used. (<a href="http://purl.org/vocab/vann/usageNote" target="_blank">http://purl.org/vocab/vann/usageNote</a>).</td>
  </tr>
</table>

<p><a id="namespace" name="intro"></a></p>

<h2 id="2-namespaces">2. Namespaces</h2>

<p>The DCMI namespace for formal schemes and schemes of domain and practice communities is <tt><a href="http://purl.org/dcx/">http://purl.org/dcx/</a></tt>. Specific community specifications will be in directories appended to the base community namespace. Thus, the <tt><a href="http://dublincore.org/lrmi-terms/">http://dublincore.org/lrmi-terms/</a></tt> URI will always resolve to the latest RDF version of the LRMI terms—i.e., the LRMI properties and classes. The <a href="http://dublincore.org/lrmi-terms/1.1/">http://dublincore.org/lrmi-terms/1.1/</a> permanently points to the LRMI schema as transferred to DCMI for stewardship.</p>

<p>The names of the latest version of specific properties and classes in the RDF namespace are resolved by appending the term to the LRMI base URI—e.g., <tt><a href="http://dublincore.org/dcx/lrmi-terms/">http://dublincore.org/dcx/lrmi-terms/</a></tt>. Thus, the following term URI example using the /dcx/ DCMI community space:</p>

<blockquote>
<p><tt><a href="http://purl.org/dcx/lrmi-terms/AlignmentObject">http://purl.org/dcx/lrmi-terms/AlignmentObject</a></tt><br />
<tt><a href="http://purl.org/dcx/lrmi-terms/typicalAgeRange">http://purl.org/dcx/lrmi-terms/typicalAgeRange</a></tt></p>
</blockquote>

<p>Future controlled vocabularies for LRMI would follow the same namespace pattern. For example, should LRMI create a value vocabulary for use with the <tt>lrmi:alignmentType</tt> property, the vocabulary might be assigned the URI <tt><a href="http://purl.org/dcx/lrmiAlignType/">http://purl.org/dcx/lrmiAlignType/</a></tt> with individual concepts URI such as <tt><a href="http://purl.org/dcx/lrmiAlignType/teaches">http://purl.org/dcx/lrmiAlignType/teaches</a></tt>.</p>

<p>'</p>

<p><a id="classes" name="classes"></a></p>

<h2 id="3-classes">3. Classes</h2>

<p><a name="AlignmentObject"><strong>AlignmentObject</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>AlignmentObject</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Alignment Object</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/AlignmentObject">http://purl.org/dcx/lrmi-terms/AlignmentObject</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>An intangible item that describes an alignment between a learning resource and a node in an educational framework.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/2000/01/rdf-schema#Class">rdfs:Class</a></td>
  </tr>
  <tr>
    <td align="right">Subclass Of:</td>
    <td><a href="http://schema.org/Intangible">schema:Intangible</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Class:</td>
    <td><a href="http://schema.org/AlignmentObject">schema:AlignmentObject</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="EducationalAudience"><strong>EducationalAudience</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>EducationalAudience</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Educational Audience</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/EducationalAudience">http://purl.org/dcx/lrmi-terms/EducationalAudience</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>An individual or group for whom the learning resource was created or useful.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/2000/01/rdf-schema#Class">rdfs:Class</a></td>
  </tr>
  <tr>
    <td align="right">Subclass Of:</td>
    <td><a href="http://schema.org/Intangible">http://schema.org/Intangible</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Class:</td>
    <td><a href="http://schema.org/EducationalAudience">http://schema.org/EducationalAudience</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a id="properties" name="properties"></a></p>

<h2 id="4-properties">4. Properties</h2>

<p><a name="alignmentType"><strong>alignmentType</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name:</td>
    <td>alignmentType</td>
  </tr>
  <tr>
    <td align="right">Label:</td>
    <td>Alignment Type</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/alignmentType">http://purl.org/dcx/lrmi-terms/alignmentType</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>A category of alignment between the learning resource and the framework node.</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>Recommended values include: 'assesses', 'teaches', 'requires', 'textComplexity', 'readingLevel', 'educationalSubject', and 'educationLevel'.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td>
      <a href="http://purl.org/dcx/lrmi-terms/AlignmentObject">http://purl.org/dcx/lrmi-terms/AlignmentObject</a><br>
      <a href="http://schema.org/AlignmentObject">http://schema.org/AlignmentObject</a>
    </td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/alignmentType">http://schema.org/alignmentType</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="educationalAlignment"><strong>educationalAlignment</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name:</td>
    <td>educationalAlignment</td>
  </tr>
  <tr>
    <td align="right">Label:</td>
    <td>Educational Alignment</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/educationalAlignment">http://purl.org/dcx/lrmi-terms/educationalAlignment</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>An alignment to an established educational framework.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a property="rdf:type" href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td><a href="http://schema.org/CreativeWork">http://schema.org/CreativeWork</a></td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td>
      <a href="http://purl.org/dcx/lrmi-terms/AlignmentObject">http://purl.org/dcx/lrmi-terms/AlignmentObject</a><br>
      <a href="http://schema.org/AlignmentObject">http://schema.org/AlignmentObject</a>
    </td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/educationalAlignment">http://schema.org/educationalAlignment</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="educationalFramework"><strong>educationalFramework</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>educationalFramework</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Educational Framework</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/educationalFramework">http://purl.org/dcx/lrmi-terms/educationalFramework</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The framework to which the resource being described is aligned.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td>
      <a href="http://purl.org/dcx/lrmi-terms/AlignmentObject">http://purl.org/dcx/lrmi-terms/AlignmentObject</a><br>
      <a href="http://schema.org/AlignmentObject">http://schema.org/AlignmentObject</a>
    </td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/educationalFramework">http://schema.org/educationalFramework</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="educationalRole"><strong>educationalRole</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>educationalRole</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Educational Role</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/educationalRole">http://purl.org/dcx/lrmi-terms/educationalRole</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The role that describes the target audience of the content.</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>[The educational function assumed or part played by the group for whom the resource is intended.]</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td>
      <a href="http://purl.org/dcx/lrmi-terms/EducationalAudience">http://purl.org/dcx/lrmi-terms/EducationalAudience</a><br>
      <a href="http://schema.org/EducationalAudience">http://schema.org/EducationalAudience</a>
    </td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/educationalRole">http://schema.org/educationalRole</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="educationalUse"><strong>educationalUse</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>educationalUse</td>
  </tr>
  <tr>
    <td align="right">Label:</td>
    <td>Educational Use</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td axis="URI"><a href="http://purl.org/dcx/lrmi-terms/educationalUse">http://purl.org/dcx/lrmi-terms/educationalUse</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The purpose of a work in the context of education.</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>For example, 'assignment', 'group work'.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td><a href="http://schema.org/CreativeWork">http://schema.org/CreativeWork</a></td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/educationalUse">http://schema.org/educationalUse</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="interactivityType"><strong>interactivityType</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>interactivityType</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Interactivity Type</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/interactivityType">http://purl.org/dcx/lrmi-terms/interactivityType</a></td>
  </tr>
  <tr>
    <td align="right">Label:</td>
    <td>Interactivity Type</td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The predominant mode of learning supported by the learning resource.</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>Acceptable values are 'active', 'expositive', or 'mixed'.</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>Based on, and mappable from, IEEE LOM 5.1: Interactivity Type.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td><a href="http://schema.org/CreativeWork">http://schema.org/CreativeWork</a></td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/interactivityType">http://schema.org/interactivityType</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="isBasedOnUrl"><strong>isBasedOnUrl</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>isBasedOnUrl</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Is Based On URL</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/isBasedOnUrl">http://purl.org/dcx/lrmi-terms/isBasedOnUrl</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>A resource that was used in the creation of this resource.</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>This term can be repeated for multiple sources.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td><a href="http://schema.org/CreativeWork">http://schema.org/CreativeWork</a></td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2000/01/rdf-schema#Resource">http://www.w3.org/2000/01/rdf-schema#Resource</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/isBasedOnUrl">http://schema.org/isBasedOnUrl</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="learningResourceType"><strong>learningResourceType</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>learningResourceType</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Learning Resource Type</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/learningResourceType">http://purl.org/dcx/lrmi-terms/learningResourceType</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The predominant type or kind characterizing the learning resource.</td>
  </tr>
  <tr>
    <td align="right">Description:</td>
    <td>For example, 'presentation', 'handout'.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td><a href="http://schema.org/CreativeWork">http://schema.org/CreativeWork</a></td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/learningResourceType">http://schema.org/learningResourceType</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="targetDescription"><strong>targetDescription</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>targetDescription</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Target Description</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/targetDescription">http://purl.org/dcx/lrmi-terms/targetDescription</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The description of a node in an established educational framework.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td>
      <a href="http://purl.org/dcx/lrmi-terms/AlignmentObject">http://purl.org/dcx/lrmi-terms/AlignmentObject</a><br>
      <a href="http://schema.org/AlignmentObject">http://schema.org/AlignmentObject</a>
    </td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/targetDescription">http://schema.org/targetDescription</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="targetName"><strong>targetName</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>targetName</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Target Name</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/targetName">http://purl.org/dcx/lrmi-terms/targetName</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The name of a node in an established educational framework.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td>
      <a href="http://purl.org/dcx/lrmi-terms/AlignmentObject">http://purl.org/dcx/lrmi-terms/AlignmentObject</a><br>
      <a href="http://schema.org/AlignmentObject">http://schema.org/AlignmentObject</a>
    </td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/targetName">http://schema.org/targetName</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="targetUrl"><strong>targetUrl</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="right">Name</td>
    <td>targetURL</td>
  </tr>
  <tr>
    <td align="right">Label</td>
    <td>Target URL</td>
  </tr>
  <tr>
    <td align="right">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/targetUrl">http://purl.org/dcx/lrmi-terms/targetUrl</a></td>
  </tr>
  <tr>
    <td align="right">Definition:</td>
    <td>The URL of a node in an established educational framework.</td>
  </tr>
  <tr>
    <td align="right">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="right">Domain Includes:</td>
    <td>
      <a href="http://purl.org/dcx/lrmi-terms/AlignmentObject">http://purl.org/dcx/lrmi-terms/AlignmentObject</a><br>
      <a href="http://schema.org/AlignmentObject">http://schema.org/AlignmentObject</a>
    </td>
  </tr>
  <tr>
    <td align="right">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#anyURI">http://www.w3.org/2001/XMLSchema#anyURI</a></td>
  </tr>
  <tr>
    <td align="right">Equivalent Property:</td>
    <td><a href="http://schema.org/targetUrl">http://schema.org/targetUrl</a></td>
  </tr>
  <tr>
    <td align="right">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="right">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="timeRequired"><strong>timeRequired</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="left">Name</td>
    <td>timeRequired</td>
  </tr>
  <tr>
    <td align="left">Label</td>
    <td>Time Required</td>
  </tr>
  <tr>
    <td align="leftt">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/timeRequired">http://purl.org/dcx/lrmi-terms/timeRequired</a></td>
  </tr>
  <tr>
    <td align="left">Definition:</td>
    <td>Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience.</td>
  </tr>
  <tr>
    <td align="leftt">Description:</td>
    <td>Based on, and mappable from, IEEE LOM 5.9: Typical Learning Time.</td>
  </tr>
  <tr>
    <td align="left">Description:</td>
    <td>For example, 'PT30M' and 'PT1H25M'</td>
  </tr>
  <tr>
    <td align="left">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="left">Domain Includes:</td>
    <td><a href="http://schema.org/CreativeWork">http://schema.org/CreativeWork</a></td>
  </tr>
  <tr>
    <td align="left">Range Includes:</td>
    <td><a href="http://schema.org/Duration">http://schema.org/Duration</a></td>
  </tr>
  <tr>
    <td align="left">Equivalent Property:</td>
    <td><a href="http://schema.org/timeRequired">http://schema.org/timeRequired</a></td>
  </tr>
  <tr>
    <td align="left">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="left">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="typicalAgeRange"><strong>typicalAgeRange</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="leftt">Name</td>
    <td>typicalAgeRange</td>
  </tr>
  <tr>
    <td align="left">Label</td>
    <td>Typical Age Range</td>
  </tr>
  <tr>
    <td align="left">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/typicalAgeRange">http://purl.org/dcx/lrmi-terms/typicalAgeRange</a></td>
  </tr>
  <tr>
    <td align="left">Definition:</td>
    <td>The typical range of ages the content's intended end user.</td>
  </tr>
  <tr>
    <td align="left">Description:</td>
    <td axis="Description" property="dct:description">For example, '7-9', '18+'.</td>
  </tr>
  <tr>
    <td align="left">Description:</td>
    <td>Based on, and mappable from, IEEE LOM 5.7: Typical Age Range.</td>
  </tr>
  <tr>
    <td align="left">Type of Term:</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="left">Domain Includes:</td>
    <td><a href="http://schema.org/CreativeWork">http://schema.org/CreativeWork</a></td>
  </tr>
  <tr>
    <td align="leftt">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#string">http://www.w3.org/2001/XMLSchema#string</a></td>
  </tr>
  <tr>
    <td align="left">Equivalent Property:</td>
    <td><a href="http://schema.org/typicalAgeRange">http://schema.org/typicalAgeRange</a></td>
  </tr>
  <tr>
    <td align="left">Is Defined By:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/">http://purl.org/dcx/lrmi-terms/</a></td>
  </tr>
  <tr>
    <td align="left">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a name="useRightsUrl"><strong>useRightsUrl</strong></a></p>

<table cellpadding="5" width="85%">
  <tr>
    <td width="150" align="left">Name</td>
    <td>useRightsURL</td>
  </tr>
  <tr>
    <td align="left">Label</td>
    <td>Use Rights URL</td>
  </tr>
  <tr>
    <td align="left">URI:</td>
    <td><a href="http://purl.org/dcx/lrmi-terms/useRightsUrl">http://purl.org/dcx/lrmi-terms/useRightsUrl</a></td>
  </tr>
  <tr>
    <td align="left">Definition:</td>
    <td>The URL where the owner specifies permissions for using the resource.</td>
  </tr>
  <tr>
    <td align="left">Description:</td>
    <td>For example: 'http://creativecommons.org/licenses/by/3.0/, &amp; 'http://publisher.com/content-use-description'.</td>
  </tr>
  <tr>
    <td align="left">Type of Term:</td>
    <td axis="Type-of-Term"><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a></td>
  </tr>
  <tr>
    <td align="left">Subproperty Of:</td>
    <td><a href="http://schema.org/license">http://schema.org/license</a></td>
  </tr>
  <tr>
    <td align="left">Domain Includes:</td>
    <td><a href="http://schema.org/CreativeWork">http://schema.org/CreativeWork</a></td>
  </tr>
  <tr>
    <td align="left">Range Includes:</td>
    <td><a href="http://www.w3.org/2001/XMLSchema#anyURI">http://www.w3.org/2001/XMLSchema#anyURI</a></td>
  </tr>
  <tr>
    <td align="left">Date Issued:</td>
    <td>2015-01-12</td>
  </tr>
</table>

<p><a id="version" name="version"></a></p>

<h2 id="5-version-changes">5. Version Changes</h2>

<p>This version declares the LRMI 1.1 specification as an RDF schema. As such, it maintains the core property and class intentions of version 1.1 while:</p>

<ul>
<li><p>Assigning URI to all LRMI 1.1 properties &amp; classes in the <tt>/dcx/lrmi-terms/</tt> namespace;</p></li>

<li><p>Assigning, where appropriate, domains &amp; ranges as well as schema.org domainIncludes &amp; rangeIncludes where support for inferencing is not intended;</p></li>

<li><p>Declaring, where appropriate, property/class relationships to LOM elements and DCMI classes/properties where appropriate;</p></li>

<li><p>Declaring <tt><a href="http://www.w3.org/TR/owl-ref/#equivalentClass-def" target="_blank">owl:equivalentClass</a></tt> and <tt><a href="http://www.w3.org/TR/owl-ref/#equivalentProperty-def" target="_blank">owl:equivalentProperty</a></tt> relations to schema.org properties &amp; classes;</p></li>

<li><p>Addition of a missing definition for <tt>lrmi:EducationalAudience</tt>; and</p></li>

<li><p>Moving examples of property values from the property definitions to informative/explanatory description for the property.</p></li>
</ul>

<p><a id="turtle" name="turtle"></a></p>

<h2 id="6-turtle-serialization">6. Turtle Serialization</h2>

<pre>
@prefix dcterms: &lt;http://purl.org/dc/terms/&gt; .
@prefix owl: &lt;http://www.w3.org/2002/07/owl#&gt; .
@prefix rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; .
@prefix rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; .
@prefix schema: &lt;http://schema.org/&gt; .
@prefix xml: &lt;http://www.w3.org/XML/1998/namespace&gt; .
@prefix xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt; .

# LRMI RDF SCHEMA DESCRIPTION

&lt;http://purl.org/dcx/lrmi-terms/&gt; dcterms:creator "LRMI Task Group"@en ;
    dcterms:description "The LRMI specification is a collection of classes and properties for markup and description of educational resources. The specification builds on the extensive vocabulary provided by Schema.org and other standards."@en ;
    dcterms:identifier &lt;http://dublincore.org/dcx/lrmi-terms/&gt; ;
    dcterms:isVersionOf &lt;http://purl.org/dcx/lrmi-terms/1.1/&gt; ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    dcterms:license &lt;https://creativecommons.org/licenses/by/4.0/&gt; ;
    dcterms:title "LRMI RDF Specification"@en .
    
# CLASSES    

&lt;http://purl.org/dcx/lrmi-terms/AlignmentObject&gt; a rdfs:Class ;
    rdfs:label "Alignment Object"@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    rdfs:comment "An intangible item that describes an alignment between a learning resource and a node in an educational framework."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    rdfs:subClassOf schema:Intangible ;
    owl:equivalentClass schema:AlignmentObject .

&lt;http://purl.org/dcx/lrmi-terms/EducationalAudience&gt; a rdfs:Class ;
    rdfs:label "Educational Audience"@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    rdfs:comment "An individual or group for whom the learning resource was created or useful."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    rdfs:subClassOf schema:Intangible ;
    owl:equivalentClass schema:EducationalAudience .
    
# PROPERTIES    

&lt;http://purl.org/dcx/lrmi-terms/alignmentType&gt; a rdf:Property ;
    rdfs:label "Alignment Type"@en ;
    dcterms:description "Recommended values include: 'assesses', 'teaches', 'requires', 'textComplexity', 'readingLevel', 'educationalSubject', and 'educationLevel'."@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes &lt;http://purl.org/dcx/lrmi-terms/AlignmentObject&gt;,
        schema:AlignmentObject ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "A category of alignment between the learning resource and the framework node."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:alignmentType .

&lt;http://purl.org/dcx/lrmi-terms/educationalAlignment&gt; a rdf:Property ;
    rdfs:label "Educational Alignment"@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes schema:CreativeWork ;
    schema:rangeIncludes &lt;http://purl.org/dcx/lrmi-terms/AlignmentObject&gt;,
        schema:AlignmentObject ;
    rdfs:comment "An alignment to an established educational framework."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:educationalAlignment .

&lt;http://purl.org/dcx/lrmi-terms/educationalFramework&gt; a rdf:Property ;
    rdfs:label "Educational Framework"@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes &lt;http://purl.org/dcx/lrmi-terms/AlignmentObject&gt;,
        schema:AlignmentObject ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "The framework to which the resource being described is aligned."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:educationalFramework .

&lt;http://purl.org/dcx/lrmi-terms/educationalRole&gt; a rdf:Property ;
    rdfs:label "Educational Role"@en ;
    dcterms:description "The educational function assumed or part played by the group for whom the resource is intended."@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes &lt;http://purl.org/dcx/lrmi-terms/EducationalAudience&gt;,
        schema:EducationalAudience ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "The role that describes the target audience of the content."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:educationalRole .

&lt;http://purl.org/dcx/lrmi-terms/educationalUse&gt; a rdf:Property ;
    rdfs:label "Educational Use"@en ;
    dcterms:description "For example, 'assignment', 'group work'."@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes schema:CreativeWork ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "The purpose of a work in the context of education."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:educationalUse .

&lt;http://purl.org/dcx/lrmi-terms/interactivityType&gt; a rdf:Property ;
    rdfs:label "Interactivity Type"@en ;
    dcterms:description "Acceptable values are 'active', 'expositive', or 'mixed'."@en,
        "Based on, and mappable from, IEEE LOM 5.1: Interactivity Type."@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes schema:CreativeWork ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "The predominant mode of learning supported by the learning resource."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:interactivityType .

&lt;http://purl.org/dcx/lrmi-terms/isBasedOnUrl&gt; a rdf:Property ;
    rdfs:label "Is Based On URL"@en ;
    dcterms:description "This term can be repeated for multiple sources."@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes schema:CreativeWork ;
    schema:rangeIncludes xsd:anyURI ;
    rdfs:comment "A resource that was used in the creation of this resource."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:isBasedOnUrl .

&lt;http://purl.org/dcx/lrmi-terms/learningResourceType&gt; a rdf:Property ;
    rdfs:label "Learning Resource Type"@en ;
    dcterms:description "For example, 'presentation', 'handout'."@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes schema:CreativeWork ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "The predominant type or kind characterizing the learning resource."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:learningResourceType .

&lt;http://purl.org/dcx/lrmi-terms/targetDescription&gt; a rdf:Property ;
    rdfs:label "Target Description"@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes &lt;http://purl.org/dcx/lrmi-terms/AlignmentObject&gt;,
        schema:AlignmentObject ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "The description of a node in an established educational framework."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:targetDescription .

&lt;http://purl.org/dcx/lrmi-terms/targetName&gt; a rdf:Property ;
    rdfs:label "Target Name"@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes &lt;http://purl.org/dcx/lrmi-terms/AlignmentObject&gt;,
        schema:AlignmentObject ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "The name of a node in an established educational framework."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:targetName .

&lt;http://purl.org/dcx/lrmi-terms/targetUrl&gt; a rdf:Property ;
    rdfs:label "Target URL"@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes &lt;http://purl.org/dcx/lrmi-terms/AlignmentObject&gt;,
        schema:AlignmentObject ;
    schema:rangeIncludes xsd:anyURI ;
    rdfs:comment "The URL of a node in an established educational framework."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:targetUrl .

&lt;http://purl.org/dcx/lrmi-terms/timeRequired&gt; a rdf:Property ;
    rdfs:label "Time Required"@en ;
    dcterms:description "Based on, and mappable from, IEEE LOM 5.9: Typical Learning Time."@en,
        "For example, 'PT30M' and 'PT1H25M'"@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes &lt;http://purl.org/dcx/lrmi-terms/AlignmentObject&gt;,
        schema:AlignmentObject ;
    schema:rangeIncludes schema:Duration ;
    rdfs:comment "Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:timeRequired .

&lt;http://purl.org/dcx/lrmi-terms/typicalAgeRange&gt; a rdf:Property ;
    rdfs:label "Typical Age Range"@en ;
    dcterms:description "Based on, and mappable from, IEEE LOM 5.7: Typical Age Range."@en,
        "For example, '7-9', '18-'."@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes schema:CreativeWork ;
    schema:rangeIncludes xsd:string ;
    rdfs:comment "The typical expected age range."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    owl:equivalentProperty schema:typicalAgeRange .

&lt;http://purl.org/dcx/lrmi-terms/useRightsUrl&gt; a rdf:Property ;
    rdfs:label "Use Rights URL"@en ;
    dcterms:description "For example: 'http://creativecommons.org/licenses/by/3.0/', 'http://publisher.com/content-use-description'."@en ;
    dcterms:issued "2015-02-09"^^xsd:date ;
    schema:domainIncludes schema:CreativeWork ;
    schema:rangeIncludes schema:CreativeWork,
        xsd:anyURI ;
    rdfs:comment "The URL where the owner specifies permissions for using the resource."@en ;
    rdfs:isDefinedBy &lt;http://purl.org/dcx/lrmi-terms/&gt; ;
    rdfs:subPropertyOf schema:license .
</pre>

<p><a id="history" name="history"></a></p>

<h2 id="7-schema-history">7. Schema History</h2>

<blockquote>
<p><em>&quot;Co-led by the Association of Educational Publishers --the 501(c)(3) division of the Association of American Publishers-- and Creative Commons, and funded by the Bill &amp; Melinda Gates Foundation and the William and Flora Hewlett Foundation, the LRMI has developed a common metadata framework for describing or 'tagging' learning resources on the web. This framework is a key first step in developing a richer, more fruitful search experience for educators and learners. ... The LRMI was spurred by the announcement in 2011 of Schema.org, a project by Bing, Google, and Yahoo! to create a standard way of tagging online content. ... The metadata schema developed by the LRMI was adopted by Schema.org in April 2013, meaning that anyone who publishes or curates educational content can now use LRMI markup to provide rich, education-specific metadata about their resources with the confidence that this metadata will be recognized by major search engines.&quot;</em> — <a href="http://www.lrmi.net/about">http://www.lrmi.net/about</a></p>
</blockquote>

<p>Work on the LRMI specification began in 2011 with the creation of a <a href="http://www.lrmi.net/leadership/advisory-group">LRMI Advisory Board</a>, and a <a href="http://www.lrmi.net/leadership/technical-working-group">Technical Working Group</a> charged with developing a community-based specification as the education extension for schema.org. Engagement of the broader education metadata community was handled during development through a <a href="https://groups.google.com/forum/#!forum/lrmi">Google Group</a>. Stuart Sutton, DCMI Managing Director &amp; DC-Education Community co-chair served on the Technical Working Group. Others on the Technical Working Group with close ties to DCMI include Dan Brickley (schema.org) and Phil Barker (Cetis, UK).</p>

<p>The Association of Educational Publishers (AEP) and Creative Commons (CC) have asked that stewardship of the LRMI specification be placed with DCMI at the September closure of Gates funding for LRMI development. From inception, the overall planning for the LRMI specification included the orderly transition of development outcomes from its grant-funded beginnings under the leadership of AEP and Creative Commons to a permanent context managed by an organization with the capacity to provide ongoing stewardship for long-term sustainability, access, and orderly future development. As the funded start-up phase of LRMI was coming to a close, an exploratory team comprised of representatives from AEP, Creative Commons, and the LRMI community was formed and has been actively and systematically engaged in evaluating an array of potential candidates for such stewardship. The exploratory team recommended DCMI because it's open community goals and processes are congruent with those that have emerged within LRMI during its short development history and because of DCMI's reputation and track record in development and principled stewardship of metadata specifications used in the Web context.</p>
