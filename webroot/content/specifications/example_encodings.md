---
title: "Serialization Examples of LRMI/Schema.org Markup"
date: 2018-02-03T09:18:17Z
draft: false
---

<p><img src="/images/lrmi-dcmi_project.png" alt="LRMI Logo" width="350" /></p>

<p>Below you will find examples of schema.org markup of learning resources using LRMI properties and types. Each example begins with simple HTML markup of a learning resource as you might find on the Web. The HTML markup is followed by semantic markup using LRMI types and properties in three of the most common serializations: (1) Microdata, (2) RDFa, and (3) JSON-LD.</p>
<p>The canonical versions of these examples can be found as annotations to the properties and classes on the <a href="schema.org" target="_blank">schema.org website</a>.</p>
<h2>EXAMPLE #1</h2>
<h3>TYPES &amp; PROPERTIES ILLUSTRATED</h3>
<p><strong>Types Used in the Example:</strong></p>
<ul>
<li>EducationalAudience</li>
<li>AlignmentObject</li>
<li>EducationalAudience</li>
</ul>
<p><strong>Properties Unsed in the Example:</strong></p>
<ul>
<li>learningResourceType</li>
<li>educationalAlignment</li>
<li>educationalFramework</li>
<li>alignmentType</li>
<li>targetName</li>
<li>targetUrl</li>
<li>audience</li>
<li>educationalRole</li>
</ul>
<h3>RESOURCE—PRE-MARKUP</h3>

<pre>
 &lt;div&gt;
   &lt;h1&gt;Designing a treasure map&lt;/h1&gt;
   &lt;p&gt;Resource type: lesson plan, learning activity&lt;/p&gt;
   &lt;p&gt;Target audience: teachers&lt;/p&gt;
   &lt;p&gt;Educational level: US Grade 2&lt;/p&gt;
   &lt;p&gt;Link to lesson plan: &lt;a href="http://example.org/lessonplan"&gt;http://example.org/lessonplan&lt;/a&gt;&lt;/p&gt;
 &lt;/div&gt;</pre>

<hr />
<h3>MICRODATA</h3>
<pre>&lt;!-- A lesson plan for US second grade teachers. --&gt;
&lt;div itemscope itemtype="http://schema.org/CreativeWork"&gt;
   &lt;h1 itemprop="name"&gt;Designing a treasure map&lt;/h1&gt;
   &lt;p&gt;Resource type:
     &lt;span itemprop="learningResourceType"&gt;lesson plan&lt;/span&gt;,
     &lt;span itemprop="learningResourceType"&gt;learning activity&lt;/span&gt;
   &lt;/p&gt;
   &lt;p&gt;Target audience:
     &lt;span itemprop="audience" itemscope itemtype="http://schema.org/EducationalAudience"&gt;
     &lt;span itemprop="educationalRole"&gt;teacher&lt;/span&gt;&lt;/span&gt;s.
   &lt;/p&gt;
   &lt;p itemprop="educationalAlignment" itemscope itemtype="http://schema.org/AlignmentObject"&gt;
     &lt;span itemprop="alignmentType"&gt;Educational level&lt;/span&gt;:
     &lt;span itemprop="educationalFramework"&gt;US Grade Levels&lt;/span&gt;
     &lt;span itemprop="targetName"&gt;2&lt;/span&gt;
     &lt;link itemprop="targetUrl" href="http://purl.org/ASN/scheme/ASNEducationLevel/2" /&gt;
   &lt;/p&gt;
   &lt;p&gt;Link to lesson plan: &lt;a itemprop="url" href="http://example.org/lessonplan"&gt;http://example.org/lessonplan&lt;/a&gt;&lt;/p&gt;
 &lt;/div&gt;</pre>
<hr />
<h3>RDFA</h3>
<pre>&lt;!-- A list of the issues for a single volume of a given periodical. --&gt;
&lt;div vocab="http://schema.org/" typeof="CreativeWork"&gt;
  &lt;h1 property="name"&gt;Designing a treasure map&lt;/h1&gt;
  &lt;p&gt;Resource type:
   &lt;span property="learningResourceType"&gt; lesson plan&lt;/span&gt;,
   &lt;span property="learningResourceType"&gt; learning activity&lt;/span&gt;
  &lt;/p&gt;
  &lt;p&gt;Target audience:
   &lt;span rel="audience" typeof="EducationalAudience"&gt;
      &lt;span property="educationalRole"&gt;teacher&lt;/span&gt;
   &lt;/span&gt;
  &lt;/p&gt;
  &lt;p rel="educationalAlignment" typeof="AlignmentObject"&gt;
   &lt;span property="alignmentType"&gt;Educational level&lt;/span&gt;:
   &lt;span property="educationalFramework"&gt;US Grade Levels&lt;/span&gt;
   &lt;span property="targetName"&gt;2&lt;/span&gt;
   &lt;span rel="targetUrl" resource="http://purl.org/ASN/scheme/ASNEducationLevel/2"&gt;&lt;/span&gt;
  &lt;/p&gt;
  &lt;p&gt;Link to lesson plan: &lt;a property="url" href="http://example.org/lessonplan"&gt;http://example.org/lessonplan&lt;/a&gt;&lt;/p&gt;
 &lt;/div&gt;</pre>
<hr />
<h3>JSON</h3>
<pre>&lt;script type="application/ld+json"&gt;
 {
   "@context": "http://schema.org/",
   "@type": "CreativeWork",
   "name": "Designing a treasure map",
   "learningResourceType": [
     "lesson plan",
     "learning activity"
     ],
   "audience": {
     "@type": "EducationalAudience",
     "educationalRole": "teacher"
     },
   "educationalAlignment": {
     "@type": "AlignmentObject",
     "alignmentType": "Educational level",
     "educationalFramework": "US Grade Levels",
     "targetName": "2",
     "targetUrl": {
       "@id": "http://purl.org/ASN/scheme/ASNEducationLevel/2"
       }
   },
   "url": "http://example.org/lessonplan"
  }
&lt;/script&gt;</pre>
<hr />
<h2>EXAMPLE #2</h2>
<h3>TYPES &amp; PROPERTIES ILLUSTRATED</h3>
<p><strong>Type Used in the Example:</strong></p>
<ul>
<li>AlignmentObject</li>
<li>EducationalAudience</li>
</ul>
<p><strong>Properties Unsed in the Example:</strong></p>
<ul>
<li>typicalAgeRange</li>
<li>timeRequired</li>
<li>educationalAlignment</li>
<li>educationalFramework</li>
<li>alignmentType/li&gt;</li>
<li>targetName</li>
<li>targetUrl</li>
</ul>
<h3>RESOURCE—PRE-MARKUP</h3>

<pre>&lt;div&gt;
  &lt;h1&gt;The Declaration of Arbroath&lt;/h1&gt;
    &lt;p&gt;A lesson plan for teachers with associated video.
       Typical length of lesson, 1 hour. 
       Recommended for children aged 10-12 years old.&lt;/p&gt;
    &lt;p&gt;Subject: Wars of Scottish independence&lt;/p&gt;
    &lt;p&gt;Alignment to curriculum:&lt;/p&gt;
    &lt;ul&gt;
       &lt;li&gt;England
           National Curriculum: KS 3 History: The middle ages (12th 
              to 15th century)&lt;/li&gt;
       &lt;li&gt;Scotland
           SCQF: Level 2
           Curriculum for Excellence: Social studies: people past 
              events and societies
       &lt;/li&gt;
    &lt;/ul&gt;
    &lt;p&gt;Link to lesson plan: &lt;a href="http://example.org/lessonplan"&gt;
       http://example.org/lessonplan&lt;/a&gt;&lt;/p&gt;
    &lt;video&gt;
      &lt;source src="http://example.org/movie.mp4" type="video/mp4" /&gt;
          Duration 03:12
    &lt;/video&gt;
    &lt;p&gt;This example is based on 
       &lt;a href="http://www.bbc.co.uk/education/clips/z3sjtfr"&gt;
          Declaration of Arbroath&lt;/a&gt;from BBC Bitesize&lt;/p&gt;
&lt;/div&gt;
</pre>

<hr />
<h3>MICRODATA</h3>
<pre>&lt;div itemscope itemtype="http://schema.org/WebPage"&gt;
   &lt;h1 itemprop="name"&gt;The Declaration of Arbroath&lt;/h1&gt;
   &lt;p&gt;A &lt;span itemprop="learningResourceType"&gt;lesson plan&lt;/span&gt;
      for &lt;span itemprop="audience"
             itemscope itemtype="http://schema.org/EducationalAudience"&gt;
          &lt;span itemprop="educationalRole"&gt;teacher&lt;/span&gt;&lt;/span&gt;
             with associated video.
      Typical length of lesson, &lt;span itemprop="timeRequired"&gt;1 hour&lt;/span&gt;.
      Recommended for children aged &lt;span itemprop="typicalAgeRange"&gt;
         10-12&lt;/span&gt; years old.
   &lt;/p&gt;
   &lt;p&gt;Subject: &lt;span itemprop="about"&gt;Wars of Scottish independence&lt;/span&gt;&lt;/p&gt;
   &lt;p&gt;Alignment to curriculum:&lt;/p&gt;
   &lt;ul&gt;
      &lt;li&gt;England
          &lt;span itemprop="educationalAlignment"
                itemscope itemtype="http://schema.org/AlignmentObject"&gt;
              &lt;meta itemprop="alignmentType" content="educationalLevel" /&gt;
              &lt;span itemprop="educationalFramework"&gt;National Curriculum&lt;/span&gt;:
              &lt;span itemprop="targetName"&gt;KS 3&lt;/span&gt;
              &lt;link itemprop="targetUrl" href="http://example.org/ENC/levels/KS3"&gt;
          &lt;/span&gt;
          &lt;span itemprop="educationalAlignment"
                itemscope itemtype="http://schema.org/AlignmentObject"&gt;
              &lt;meta itemprop="alignmentType" content="educationalSubject" /&gt;
              &lt;meta itemprop="educationalFramework" content="National Curriculum" /&gt;
              &lt;span itemprop="targetName"&gt;History: The middle ages (12th to 15th 
                 century)&lt;/span&gt;
              &lt;link itemprop="targetUrl" href="http://example.org/ENC/subjects/3102"&gt;
          &lt;/span&gt;
      &lt;/li&gt;
      &lt;li&gt;Scotland
          &lt;span itemprop="educationalAlignment"
                itemscope itemtype="http://schema.org/AlignmentObject"&gt;
              &lt;meta itemprop="alignmentType" content="educationalLevel" /&gt;
              &lt;span itemprop="educationalFramework"&gt;SCQF&lt;/span&gt;:
              &lt;span itemprop="targetName"&gt;Level 2&lt;/span&gt;
              &lt;link itemprop="targetUrl" href="http://example.org/SCQF/levels/2"&gt;
          &lt;/span&gt;
          &lt;span itemprop="educationalAlignment"
                itemscope itemtype="http://schema.org/AlignmentObject"&gt;
              &lt;meta itemprop="alignmentType" content="educationalSubject" /&gt;
              &lt;span itemprop="educationalFramework"&gt; Curriculum for Excellence&lt;/span&gt;:
              &lt;span itemprop="targetName"&gt;Social studies: people past events and 
                 societies&lt;/span&gt;
              &lt;link itemprop="targetUrl" href="http://example.org/CFE/subjects/3362"&gt;
          &lt;/span&gt;
      &lt;/li&gt;
   &lt;/ul&gt;
   &lt;p&gt;Link to lesson plan: &lt;a itemprop="url" 
      href="http://example.org/lessonplan"&gt;http://example.org/lessonplan&lt;/a&gt;&lt;/p&gt;
   &lt;video itemprop="video" itemscope itemtype="http://schema.org/VideoObject"&gt;
      &lt;source itemprop="url" src="http://example.org/movie.mp4" type="video/mp4"&gt;
      &lt;span itemprop="name"&gt;Video Title&lt;/span&gt;
      &lt;span itemprop="description"&gt;Video description&lt;/span&gt;
      &lt;span itemprop="uploadDate"&gt;2000-01-01&lt;/span&gt;
      &lt;img itemprop="thumbnailUrl" src="http://example.org/thubnail.mp4" 
         alt="thumbnail" &gt;
      Duration: &lt;span itemprop="duration"&gt;03:12&lt;/span&gt;
   &lt;/video&gt;
   &lt;p&gt;This example is based on &lt;a itemprop="isBasedOnUrl" 
      href="http://www.bbc.co.uk/education/clips/z3sjtfr"&gt;Declaration of 
      Arbroath&lt;/a&gt; from BBC Bitesize&lt;/p&gt;
&lt;/div&gt;
</pre>
<hr />
<h3>RDFA</h3>
<pre>&lt;div vocab="http://schema.org/" typeof="WebPage"&gt;
   &lt;h1 property="name"&gt;The Declaration of Arbroath&lt;/h1&gt;
   &lt;p&gt;A &lt;span property="learningResourceType"&gt;lesson plan&lt;/span&gt;
      for &lt;span rel="audience"
             typeof="EducationalAudience"&gt;
          &lt;span property="educationalRole"&gt;teacher&lt;/span&gt;&lt;/span&gt;s with associated 
             video. 
      Typical length of lesson, &lt;span property="timeRequired"&gt;1 hour&lt;/span&gt;.
      Recommended for children aged &lt;span property="typicalAgeRange"&gt;10-12&lt;/span&gt; 
        years old.
   &lt;/p&gt;
   &lt;p&gt;Subject: &lt;span property="about"&gt;Wars of Scottish independence&lt;/span&gt;&lt;/p&gt;
   &lt;p&gt;Alignment to curriculum:&lt;/p&gt;
      &lt;ul&gt;
         &lt;li&gt;England
             &lt;span rel="educationalAlignment"
                   typeof="http://schema.org/AlignmentObject"&gt;
                 &lt;meta property="alignmentType" content="educationalLevel" /&gt;
                 &lt;span property="educationalFramework"&gt;National Curriculum&lt;/span&gt;:
                 &lt;span property="targetName"&gt;KS 3&lt;/span&gt;
                 &lt;link property="targetUrl" href="http://example.org/ENC/levels/KS3" /&gt;
             &lt;/span&gt;
             &lt;span rel="educationalAlignment"
                   typeof="http://schema.org/AlignmentObject"&gt;
                 &lt;meta property="alignmentType" content="educationalSubject" /&gt;
                 &lt;meta property="educationalFramework" content="National Curriculum" /&gt;
                 &lt;span property="targetName"&gt;History: The middle ages (12th to 15th 
                   century)&lt;/span&gt;
                 &lt;link property="targetUrl" href="http://example.org/ENC/subjects/3102" /&gt;
             &lt;/span&gt;
         &lt;/li&gt;
         &lt;li&gt;Scotland
             &lt;span rel="educationalAlignment"
                   typeof="http://schema.org/AlignmentObject"&gt;
                 &lt;meta property="alignmentType" content="educationalLevel" /&gt;
                 &lt;span property="educationalFramework"&gt;SCQF&lt;/span&gt;:
                 &lt;span property="targetName"&gt;Level 2&lt;/span&gt;
                 &lt;link property="targetUrl" href="http://example.org/SCQF/levels/2" /&gt;
             &lt;/span&gt;
             &lt;span rel="educationalAlignment"
                   typeof="http://schema.org/AlignmentObject"&gt;
                 &lt;meta property="alignmentType" content="educationalSubject" /&gt;
                 &lt;span property="educationalFramework"&gt; Curriculum for Excellence&lt;/span&gt;:
                 &lt;span property="targetName"&gt;Social studies: people past events and 
                   societies&lt;/span&gt;
                 &lt;link property="targetUrl" href="http://example.org/CFE/subjects/3362" /&gt;
             &lt;/span&gt;
         &lt;/li&gt;
      &lt;/ul&gt;
      &lt;p&gt;Link to lesson plan: &lt;a property="url" href="http://example.org/lessonplan"&gt;
         http://example.org/lessonplan&lt;/a&gt;&lt;/p&gt;
      &lt;video rel="video" typeof="http://schema.org/VideoObject"&gt;
          &lt;source property="url" src="http://example.org/movie.mp4" type="video/mp4" /&gt;
          &lt;span property="name"&gt;Video Title&lt;/span&gt;
          &lt;span property="description"&gt;Video description&lt;/span&gt;
          &lt;span property="uploadDate"&gt;2000-01-01&lt;/span&gt;
          &lt;img property="thumbnailUrl" src="http://example.org/thubnail.mp4" 
              alt="thumbnail" /&gt;
          Duration: &lt;span property="duration"&gt;03:12&lt;/span&gt;
      &lt;/video&gt;
      &lt;p&gt;This example is based on &lt;a property="isBasedOnUrl" 
         href="http://www.bbc.co.uk/education/clips/z3sjtfr"&gt;Declaration of 
         Arbroath&lt;/a&gt; from BBC Bitesize&lt;/p&gt;
&lt;/div&gt;
</pre>
<hr />
<h3>JSON</h3>
<pre>&lt;script type="application/ld+json"&gt;
{
   "@context": "http://schema.org/",
   "@type": "WebPage",
   "name": "The Declaration of Arbroath",
   "about": "Wars of Scottish independence",
   "learningResourceType": "lesson plan",
   "timeRequired": "1 hour",
   "typicalAgeRange": "10-12",
   "audience": {
      "@type": "EducationalAudience",
      "educationalRole": "teacher"
   },
   "educationalAlignment": [
      {
       "@type": "AlignmentObject",
       "alignmentType": "educationalSubject",
       "educationalFramework": " Curriculum for Excellence",
       "targetName": "Social studies: people past events and societies",
       "targetUrl": "http://example.org/CFE/subjects/3362"
      },
      {
       "@type": "AlignmentObject",
       "alignmentType": "educationalLevel",
       "educationalFramework": "SCQF",
       "targetName": "Level 2",
       "targetUrl": "http://example.org/SCQF/levels/2"
      },
      {
       "@type": "AlignmentObject",
       "alignmentType": "educationalLevel",
       "educationalFramework": "National Curriculum",
       "targetName": "KS 3",
       "targetUrl": "http://example.org/ENC/levels/KS3"
      },
      {
       "@type": "AlignmentObject",
       "alignmentType": "educationalSubject",
       "educationalFramework": "National Curriculum",
       "targetName": "History: The middle ages (12th to 15th century)",
       "targetUrl" : "http://example.org/ENC/subjects/3102"
      }
   ],
   "url" : "http://example.org/lessonplan",
   "video": {
      "@type": "VideoObject",
      "description": "Video description",
      "duration": "03:12",
      "name": "Video Title",
      "thumbnailUrl": "http://example.org/thubnail.mp4",
      "uploadDate": "2000-01-01",
      "url" : "http://example.org/movie.mp4"
   },
   "isBasedOnUrl": "http://www.bbc.co.uk/education/clips/z3sjtfr"
}
&lt;/script&gt;
</pre>