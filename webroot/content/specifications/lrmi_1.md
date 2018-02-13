---
title: "LRMI Version 1.1"
date: 2018-02-03T07:57:17Z
draft: false
---



<table>
  <tr>
    <th scope="row">Title:</th>
    <td property="dcterms:title">LRMI Specification Version 1.1</td>
  </tr>
  <tr>
    <th scope="row">Creator:</th>
    <td property="dcterms:creator" label="AEP and CC">Association of Educational Publishers &amp; Creative Commons</td>
  </tr>
  <tr>
    <th scope="row">Date Issued/AEP-CC:</th>
    <td>
      <time property="dcterms:issued">N/A</time>
    </td>
  </tr>
  <tr>
    <th scope="row">Date Adopted by Schema.org:</th>
    <td>
      <time property="dcterms:issued">2013-04</time>
    </td>
  </tr>
  <tr>
    <th scope="row">Date Issued/DCMI:</th>
    <td>
      <time property="dcterms:issued">2014-10-23</time>
    </td>
  </tr>
  <tr>
    <th scope="row">Document Status:</th>
    <td>[Education] Community Specification</td>
  </tr>
  <tr>
    <th scope="row">Description:</th>
    <td property="dcterms:description">The LRMI specification is a collection of classes and properties for markup and description of educational resources. The specification builds on the extensive vocabulary provided by Schema.org and other standards.</td>
  </tr>

</table>

<p><a name="specification"></a></p>

<h2 id="the-specification">The Specification</h2>

<p><em>version 1.1</em></p>

<p>The LRMI specification is a collection of properties to describe educational resources. It builds on the extensive vocabulary provided by <a href="http://schema.org">Schema.org</a>. Predominantly it uses properties of resources of type <a href="http://schema.org/CreativeWork">schema.org/CreativeWork</a> that were proposed to Schema.org by the LRMI to describe the educational characteristics of learning resources. For some of these properties it uses the LRMI-created types <a href="http://schema.org/AlignmentObject">schema.org/AlignmentObject</a> and <a href="http://schema.org/EducationalAudience">schema.org/EducationalAudience</a>.</p>

<p><a name="interoperability"></a>
The LRMI project looked for inspiration, ideas, and learnings from other projects with similar visions in furtherance of its goal of interoperating with other specifications. As much as possible, contributors on those works were invited to participate in LRMI specification development. We wish to acknowledge and thank these initiatives for informing our work:</p>

<ul>
<li><a href="http://ltsc.ieee.org/wg12/" title="IEEE Learning Object Metadata">IEEE Learning Object Metadata</a></li>
<li><a href="http://dublincore.org">Dublin Core Metadata Initiative</a></li>
<li><a href="http://www.imsproject.org/metadata/" title="IMS Global Learning Consortium Learning Resource Metadata">IMS Global Learning Consortium Learning Resource Metadata</a></li>
<li><a href="http://vs.fernuni-hagen.de/methoden/ils/Organisation/ariadne.html" title="ARIADNE Educational Metadata Recommendation">ARIADNE Educational Metadata Recommendation</a></li>
<li><a href="http://www.adlnet.gov/scorm/" title="SCORM">SCORM</a></li>
<li><a href="http://www.iso.org/iso/home/search.htm?qt=19788&amp;published=on" title="ISO/IEC Metadata for Learning Resources">ISO/IEC Metadata for Learning Resources</a></li>
</ul>

<table>
  <tbody>
    <tr>
      <th colspan="3">
        <p><strong>Table 1. LRMI Additions to Schema.org/CreativeWork</strong></p>
      </th>
    </tr>
    <tr style="background-color: #deb887;">
      <th><strong>Property</strong></th>
      <th><strong>Expected Type</strong></th>
      <th><strong>Description</strong></th>
    </tr>
    <tr>
      <td><strong>educationalAlignment</strong></td>
      <td>schema.org/<strong>AlignmentObject</strong>
      </td>
      <td>An alignment to an established educational framework.</td>
    </tr>
    <tr>
      <td><strong>educationalUse</strong></td>
      <td>schema.org/Text</td>
      <td>The purpose of the work in the context of education.
        <ul>
          <li>Ex: "assignment"</li>
          <li>Ex: "group work"</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <a name="timeRequired"></a><strong>timeRequired</strong>
      </td>
      <td>schema.org/Duration (<a href="http://en.wikipedia.org/wiki/ISO_8601#Durations">ISO</a><br>
        <a href="http://en.wikipedia.org/wiki/ISO_8601#Durations"> 8601</a>)</td>
      <td>Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience.
        <ul>
          <li>Ex: "PT30M"</li>
          <li>Ex: "PT1H25M"</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <a name="typicalAgeRange"></a><strong>typicalAgeRange</strong>
      </td>
      <td>schema.org/Text</td>
      <td>The typical range of ages the content’s intended end user.
        <ul>
          <li>Ex: "7-9"</li>
          <li>Ex: "18-"</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <a name="interactivityType"></a><strong>interactivityType</strong>
      </td>
      <td>schema.org/Text</td>
      <td>The predominant mode of learning supported by the learning resource. Acceptable values are active, expositive, or mixed.
        <ul>
          <li>Ex: "active"</li>
          <li>Ex: "mixed"</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <a name="learningResourceType"></a><strong>learningResourceType</strong>
      </td>
      <td>schema.org/Text</td>
      <td>The predominant type or kind characterizing the learning resource.
        <ul>
          <li>Ex: "presentation"</li>
          <li>Ex: "handout"</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <a name="useRightsUrl"></a><strong>useRightsUrl</strong>
      </td>
      <td>schema.org/URL</td>
      <td>The URL where the owner specifies permissions for using the resource.
        <ul>
          <li>Ex: "<a href="http://creativecommons.org/licenses/by/3.0/">http://creativecommons.org/licenses/by/3.0/</a>"</li>
          <li>Ex: "<a href="http://publisher.com/content-use-description">http://publisher.com/content-use-description</a>"</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <a name="isBasedOnUrl"></a><strong>isBasedOnUrl</strong>
      </td>
      <td>schema.org/URL</td>
      <td>A resource that was used in the creation of this resource. This term can be repeated for multiple sources.</td>
    </tr>
  </tbody>
</table>

<p><strong>A note on useRightsUrl:</strong> this property was not adopted by schema.org. Subsequently schema.org adopted a property called license which encompasses the same functions as useRightsUrl (see below). The license property is likely to be more widely understood by consumers of schema.org mark-up than the LRMI useRightsUrl property.</p>

<table>
  <tbody>
    <tr class="table-header-row">
      <th colspan="3">
        <p><strong>Table 2. Other important characteristics of learning resources that are covered by Schema.org properties of CreativeWork</strong></p>
      </th>
    </tr>
    <tr style="background-color: #deb887;">
      <th><strong>Property</strong></th>
      <th><strong>Expected Type</strong></th>
      <th><strong>Description</strong></th>
    </tr>
    <tr>
      <td><strong>name</strong></td>
      <td>schema.org/Text</td>
      <td>The title of the resource.</td>
    </tr>
    <tr>
      <td><strong>about</strong></td>
      <td>schema.org/Thing</td>
      <td>The subject of the content.</td>
    </tr>
    <tr>
      <td><strong>dateCreated</strong></td>
      <td>schema.org/Date</td>
      <td>The date on which the resource was created.</td>
    </tr>
    <tr>
      <td><strong>author</strong></td>
      <td>schema.org/Person</td>
      <td>The individual credited with the creation of the resource.</td>
    </tr>
    <tr>
      <td><strong>publisher</strong></td>
      <td>schema.org/Organization</td>
      <td>The organization credited with publishing the resource.</td>
    </tr>
    <tr>
      <td><strong>inLanguage</strong></td>
      <td>schema.org/Language</td>
      <td>The primary language of the resource.</td>
    </tr>
    <tr>
      <td><strong>accessibilityAPI</strong></td>
      <td>Text</td>
      <td>Indicates that the resource is compatible with the referenced accessibility API. (<a href="http://www.w3.org/wiki/WebSchemas/Accessibility" onclick="javascript:_gaq.push(['_trackEvent','outbound-article','http://www.w3.org']);">WebSchemas wiki lists possible values</a>).</td>
    </tr>
    <tr>
      <td><strong>accessibilityControl</strong></td>
      <td>Text</td>
      <td>Identifies input methods that are sufficient to fully control the described resource. (<a href="http://www.w3.org/wiki/WebSchemas/Accessibility" onclick="javascript:_gaq.push(['_trackEvent','outbound-article','http://www.w3.org']);">WebSchemas wiki lists possible values</a>).</td>
    </tr>
    <tr>
      <td><strong>accessibilityFeature</strong></td>
      <td>Text</td>
      <td>Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility. (<a href="http://www.w3.org/wiki/WebSchemas/Accessibility" onclick="javascript:_gaq.push(['_trackEvent','outbound-article','http://www.w3.org']);">WebSchemas wiki lists possible values</a>).</td>
    </tr>
    <tr>
      <td><strong>accessibilityHazard</strong></td>
      <td>Text</td>
      <td>A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3. (<a href="http://www.w3.org/wiki/WebSchemas/Accessibility" onclick="javascript:_gaq.push(['_trackEvent','outbound-article','http://www.w3.org']);">WebSchemas wiki lists possible values</a>).</td>
    </tr>
    <tr>
      <td><strong>license</strong></td>
      <td>Url or CreativeWork</td>
      <td>A license document that applies to this content, typically indicated by URL.</td>
    </tr>
  </tbody>
</table>

<p>&nbsp;</p>

<h3 id="alignment-object">Alignment Object</h3>

<p>An alignment object is an intangible item that describes an alignment between a learning resource and a node in an educational framework. AlignmentObject is a subtype of <a href="http://schema.org/Intangible">schema.org/Intangible</a></p>

<table>
  <tbody>
    <tr class="table-header-row">
      <th colspan="3">
        <p>Table 3. LRMI properties of AlignmentObject</p>
      </th>
    </tr>
    <tr style="background-color: #deb887;">
      <th><strong>Property</strong></th>
      <th><strong>Expected Type</strong></th>
      <th><strong>Description</strong></th>
    </tr>
    <tr>
      <td>
        <a name="alignmentType"></a><strong>alignmentType</strong>
      </td>
      <td>Text</td>
      <td>A category of alignment between the learning resource and the framework node. Recommended values include: 'assesses', 'teaches', 'requires', 'textComplexity', 'readingLevel', 'educationalSubject', and 'educationLevel'.</td>
    </tr>
    <tr>
      <td>
        <a name="educationalFramework"></a><strong>educationalFramework</strong>
      </td>
      <td>Text</td>
      <td>The framework to which the resource being described is aligned.</td>
    </tr>
    <tr>
      <td>
        <a name="targetDescription"></a><strong>targetDescription</strong>
      </td>
      <td>Text</td>
      <td>The description of a node in an established educational framework.</td>
    </tr>
    <tr>
      <td>
        <a name="targetName"></a><strong>targetName</strong>
      </td>
      <td>Text</td>
      <td>The name of a node in an established educational framework.</td>
    </tr>
    <tr>
      <td>
        <a name="targetUrl"></a><strong>targetUrl</strong>
      </td>
      <td>URL</td>
      <td>The URL of a node in an established educational framework.</td>
    </tr>
  </tbody>
</table>

<p>&nbsp;</p>

<p><a name="educationalAudience"></a></p>

<h3 id="educational-audience">Educational Audience</h3>

<p>Educational Audience may be used with the <a href="http://schema.org/audience">audience</a> property of a creative work. Note: <a href="http://schema.org/EducationalAudience">schema.org/EducationalAudience</a> is a subtype of <a href="http://schema.org/Audience">Schema.org/Audience</a></p>

<table>
  <tbody>
    <tr class="table-header-row">
      <th colspan="3">
        <p><strong>Table 4. LRMI properties of EducationalAudience</strong></p>
      </th>
    </tr>
    <tr style="background-color: #deb887;">
      <th><strong>Property</strong></th>
      <th><strong>Expected Type</strong></th>
      <th><strong>Description</strong></th>
    </tr>
    <tr>
      <td>
        <a name="educationalRole"></a><strong>educationalRole</strong>
      </td>
      <td>schema.org/Text</td>
      <td>The role that describes the target audience of the content.</td>
    </tr>
  </tbody>
</table>

<p>&nbsp;</p>