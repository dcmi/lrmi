[![hackmd-github-sync-badge](https://hackmd.io/qHforXA3Q4Cm052G98qafA/badge)](https://hackmd.io/qHforXA3Q4Cm052G98qafA)

# Context and Background

We take advantage of the search and retrieval capabilities of computer networks and the Internet every
day, and most of the time we easily get the kind of results we expect. In education, however, the existing
search and retrieval capacities of these systems are inadequate. Teachers need to find educational
resources that precisely meet the distinct needs of their students. They need to be able to search based
on education-specific attributes such as the student’s age, the academic subject area of interest, the level
of learning, the relevance to curriculum standards or objectives, or the type of learning activity. Publishers
need to communicate the usage rights of their content and ensure that educators can easily find the
resources that they are searching for. The Learning Resource Metadata Initiative (LRMI), a collaboration
led by the Association of Educational Publishers—the 501(c)(3) arm of the Association of American
Publishers—and Creative Commons, and funded by the Bill & Melinda Gates Foundation, is working to
address these needs and make it easier to develop, deliver, and discover quality educational resources on
the web and other search and delivery platforms.

This document is a supplement to ongoing LRMI metatagging efforts and is intended for educational content publishers and curators, as well as those who provide metadata services to the education community.

Other resources available for the educational content development community include:
* **LRMI Project:** 
The LRMI Web Site (http://www.lrmi.net) provides background information about LRMI, the Specification, details about LRMI leadership, a discussion forum, and additional resources. For those interested in the details, review the LRMI specifications at http://www.lrmi.net/the-specification.
* **Workshops, Presentations, and Webinars:**
The LRMI web site provides information about LRMI events, including workshops, presentations at industry conferences, and webinars: http://www.lrmi.net/category/news/events
* **Community:**
The LRMI discussion forum (http://www.lrmi.net/discuss) currently includes topics ranging from detailed implementation and tagging questions, to broader discussions about the Initiative. Other resources of interest include the Association of Educational Publishers (AEP), (www.aepweb.org) and the Bill & Melinda Gates Foundation (www.gatesfoundation.org). Additional related information can be found at the Creative Commons LRMI wiki site (http://wiki.creativecommons.org/LRMI) and the Common Core State Standards (http://corestandards.org)

## About Metadata and Metatagging

“Metadata” is simply “data about data.” Within the context of educational content, metadata is sometimes referred to as a “digital library card” that contains the detailed information that describes the learning resource. For example, simple metadata about a textbook might include the publish date, the author, the number of pages, and so on. Metadata does not include the learning resource’s content—the actual text or lesson data from the learning resource.  Rather, metadata consists of various descriptors about the learning resource. The creation of metadata is known as “metatagging.” Each “tag” is an attribute, such as the number of pages that are associated with a learning resource. Historically, and with varying success, educational content developers have used metatagging to facilitate learning resource discovery within closed systems—that is, within systems over which they have control.

In some cases, educational content development organizations (“publishers”) use enterprise scale content management systems (CMS’s) as workflow tools to develop, manage, and distribute their learning resources, and a key part of the CMS’s success (or not) is metatagging. Since nearly every organization has developed its own approach to metatagging, educational content is not easily shareable in open network systems or over the Internet. In other words, since each content developer’s approach to metatagging has been unique, there has been no uniform way to search for content from multiple publishers. Therefore, one important objective for LRMI is to standardize a basic metatagging approach that enables the search and discovery of learning resources from multiple publishers in open networks and over the Internet.

Another major use of metatagging in education has been the alignment (or correlation) between learning resources and state and national curriculum standards. Some publishers use this kind of mapping to guide their product development process. It is often used as a marketing tool to emphasize the depth and breadth of coverage of learning resources.  Closer to the learning activity, it is particularly important for teachers who need to find learning resources that map to curriculum standards within their district’s scope and sequence. 

Depending on the details of the metatagging system, the complete range of learning resources—from textbooks to web pages to media files—can be metatagged and successfully searched and retrieved. If the learning resource is digital, then that resource’s metadata can include a URL pointer to where the asset can be retrieved. If the learning resource is not digital (like a print-only book or document), the metadata can include information about where it is physically located (like on a particular shelf in a library), how it can be purchased, or there can be a URL pointer to a unique landing page that describes the product.

## LRMI and Related Projects to Support the Search and Retrieval of Educational Content on the Web

LRMI is one of several interrelated projects intended to support the search and retrieval of educational content in networked environments and on the Internet.

### Schema.org http://schema.org

The LRMI project is an educational extension of Schema.org, a Bing/Google/Yahoo! collaboration to develop and encourage the use of metadata to make it easier to find web pages that more closely match search criteria. To support the objectives of Schema.org, LRMI metadata is based on contributions from experts and organizations that have worked with metadata and metatagging since the early 1990s and, as such, it is comprised of the “best” of existing systems rather than a reinvention.

### Learning Registry http://www.learningregistry.org

The Learning Registry is an open source technical system designed to facilitate the exchange of metadata about learning resources. The Learning Registry is creating a set of technical protocols for how to organize, exchange, and retrieve learning resource metadata in an open network, using the Internet. It serves as a platform for innovation for content authors and aggregators, including publishers, states, districts, teachers, etc. The Learning Registry’s vision is that web-based applications will harness the power of the Learning Registry metadata to allow educators to quickly find learning resources that meet their unique needs. The Learning Registry plans to leverage the LRMI standard to increase the ease of metadata usage within the education industry. In addition to storing metadata, the Learning Registry will also have a community network that will allow the sharing of ratings, comments, downloads, standards alignment, etc.

The Learning Registry is not a specific destination, portal, or application that educators will “go to.”  Rather, it is an open technology framework to which any content creator can publish, and any technology vendor (e.g., learning management system, content aggregators, or application developers) can leverage for learning resource discovery and delivery within their applications.

To help companies and organizations try out the tagging process in a safe, low-pressure environment,
the LRMI is developing a unique resource that will help content publishers and curators visualize the
benefits of LRMI-tagged content. The LRMI Sandbox Node will offer organizations a secure, private space
to publish and review the results of their tagging efforts within the framework of the Learning Registry.
Companies and organizations interested in learning more about the LRMI Sandbox Node can contact
Dave Gladney, LRMI Project Director for AEP, at dgladney@publishers.org.

### Shared Learning Collaborative (SLC) http://slcedu.org

The SLC provides resources to help developers, courseware designers, and educators create tools and services in alignment with the Common Core State Standards. The SLC is working to make personalized learning a reality for every U.S. student by improving the usefulness, variety, and affordability of education technology. The SLC is organizing data about students and learning resources. The SLC plans to use the Learning Registry framework for discovery and delivery of learning resources, and as stated above, LRMI is an important element within the metadata definition of the learning resources.

### GIM-CCSS http://www.setda.org/web/guest/Interoperability

The “Granular Identifiers and Metadata for the Common Core State Standards” (GIM-CCSS) project is working to facilitate the long-term technical implementation of the Common Core State Standards (CCSS) in a digital format that preserves their conceptual and structural integrity. The LRMI specification consists of elements that permit tagging to (“aligning to”) published educational standards.  Thus, the efforts of the GIM-CCSS project will increase the ability of publishers to meaningfully tag (“align”) their learning resources to CCSS.  This project is a collaboration among the Partnership for the Assessment of Readiness for College and Careers (PARCC), the Smarter Balanced Assessment Consortium (Smarter Balanced), the State Educational Technology Directors Association (SETDA), and the Council of Chief State School Officers (CCSSO).

### Schools Interoperability Framework Association (SIFA) http://www.sifinfo.org

The SIF Association is comprised of K-12 organizations that have created a set of rules and definitions that enable software programs from different companies to share information. This set of platform-independent, vendor-neutral rules and definitions is called the SIF Implementation Specification. The SIF Specification makes it possible for programs within a school or district to share data without additional programming.

## Context: How it all Fits Together

LRMI is a way for communicating instructional intent and it can be used in a number of ways. The
diagram below is one example of how metatagging could be deployed in order to facilitate the search
and retrieval of instructional resources. Working from right to left, educational publishers develop
instructional materials that are then tagged to learning standards and other metadata, which are stored in
the Learning Registry. Working from left to right, educators and students search for educational resources
and find exactly what they are looking for in the Learning Registry. Without a standardized metatagging
approach, it would not be possible to easily find the right resources.

![](https://hackmd.io/_uploads/rJUo8-fd3.png)


## Best Practices and Metatagging Workflow

There is no one “right way” to organize your metatagging process and workflow. You will need to develop
a process that works for the unique characteristics of your organization. Based on decades of metatagging
experience, we recommend that you consider the best practices below during your LRMI planning and
implementation process.

## Tagging Checklist
As a starting point for developing your own metatagging process, here is a high-level checklist of the
typical steps. More detailed recommendations can be found in the tables that follow:

### Planning
1. Familiarize yourself with the LRMI metadata to get an idea of the task ahead.
2. Develop a metatagging workflow plan for your organization.
3. Assign roles and responsibilities to the people who will be involved in metatagging.

### Organizing
4. Review the inventory of instructional resources you plan to metatag.
5. Determine the level of granularity at which the resources should be tagged.
6. Ensure that you have the necessary metadata. In many cases you may need to develop new metadata.
7. Identify or create a unique URL/landing page for each resource component that is tagged.
8. Fill in the spreadsheet provided by the LRMI or create your own, then populate it with the metadata you have.
9. Organize and sort any existing metadata so that you can do as much batch or sequential processing as possible.

### Tagging and Quality Assurance
10. Assign the metatags by completing the gaps in the LRMI metadata spreadsheet.
11. Perform a quality check on the curriculum standards alignments. To ensure accuracy, this is best done by a subject area curriculum expert.
12. Perform a final internal review to ensure the tags are accurate and consistent. To ensure consistency, this is best done by the owner of the metatagging project.





## Step One: Planning

Before you start working with LRMI, you should spend time planning the implementation and how it will fit
into your existing workflow. Here are some common issues publishers will want to consider.

### 1. What is the nature of your organization? 
Are you a “mom and pop shop” with relatively few products or are you part of a large organization with myriad disparate products and bureaucracies?

* If you are part of a small organization, you’ll likely be working on LRMI in between all the other important things on your plate. Schedule a regular time to work on LRMI-related issues and stick to your schedule. 

* If you are part of a large organization, you may have to deal with any number of bureaucratic issues. To facilitate LRMI in a larger organization it often makes sense to have someone (or a dedicated crew) whose sole responsibility is the metatagging process, and get buy-in from every key stakeholder including managers and executives. It’s beneficial to have representation from both your content and technical team during these discussions.
*  Alternatively, as a resource moves through stages of production, and if the inputting system allows, metadata can be added as appropriate at each stage by those who have most knowledge about a particular aspect of the resource, e.g., those who have contributed to the resource, the use rights associated with the resource, or alignment with educational level, curriculum standards, and so on.

* Regardless of whether you’re small or large, take advantage of the LRMI documents and community listed earlier to ensure that you can leverage the experience of those leading and implementing LRMI.

### 2. Is the educational content you produce print, digital, or both?

* To get the greatest benefit from LRMI, you’ll need to consider the nature of the content you plan to tag so that it is accurately represented to the educators searching for resources in a digital environment. In other words, the main goal of LRMI is to promote meaningful discovery of learning resources for teachers and students who have very specific needs. Precise descriptions of your learning resources will promote greater success for the teachers and students who are searching for “just the right” resource.

* If your educational content is print, it is in your best interest to create a unique landing page for the learning resource and incorporate LRMI metatags in the HTML of the web page. Even a simple web page with a couple of sentences describing your learning resource would suffice.

### 3. How do educators purchase, access, and use your content?

* As the Internet becomes a more prevalent sales and distribution channel, older channels are changing or going away. Make it easy for educators to purchase, access, and use your content by providing unique, public URLs for each learning resource or unique identifiers such as ISBN or ISSN. If the learning resource is not digital, or if it exists online behind a paywall, you should consider having unique, publicly accessible web pages that describe the learning resource and give teachers and students the opportunity to learn about and purchase them.

### 4. What are your organization’s objectives for metatagging?

* Historically, publishers’ metatagging requirements — especially for alignments/correlations to curriculum standards — have been driven by sales and marketing. As the LRMI and related technologies become more widespread, metatagging that is solely focused on sales and marketing is likely to have adverse results on educators’ perceptions about your products. End users are searching for learning resources that match their unique needs, so the more specific you can be with your metatags, the better impression you will make on the end users.

* We propose that you think about metatagging from the perspective of personalized learning. What is the best way to represent your content when viewed through the lens of providing solutions that are personalized for individual learners?

* One approach would be to develop use cases as a way to frame your approach to metatagging. For example, imagine yourself as an overwhelmed educator who is trying to find the best resources for a new lesson plan that addresses fractions for grade four math students. Or consider the case of a high school student looking for resources about algebraic expressions. In any event, you will need to establish who the audience will be for your metadata — teachers, students, parents, or a general audience that may incorporate all of those. Text descriptions may need to be adjusted accordingly.

### 5. Organizing the content by similar groups of metatags

* As you plan your metatagging process, incorporate steps that will make it more efficient. In many cases there can be quite a bit of repetition from one learning resource to the next, which means you can simply copy and paste metadata from one learning resource to the next. Consider adding a duplicating function to your metadata tool if it doesn’t have one.

## Step Two: Organizing the Information about the Resources to be Metatagged

A key step in the metatagging process is organizing the information about your content so that it can be easily referenced when coding the descriptions.

### 1. Granularity
Granularity refers to the size
of the items referenced in the
metatagging system. Determining
the level of granularity of the
items to be metatagged typically
involves breaking up a product
into smaller component parts.
Determining the size of those
chunks is the crux of this issue.

* Determining a resource’s level of granularity is one of the main challenges in the organizing process. Folks new to metatagging are often tempted to avoid the issue altogether and not break up the educational resource into component parts on the assumption that a large resource will be “all things to all learners.”
* Unfortunately, this violates the personalization principle described earlier. In most cases, the optimal granularity for educational content is, for example, a unit plan (i.e., for a unit of work around a topic or theme), a lesson plan, chapter of a book, or an activity.
* In general it is most useful to tag at resource level rather than just collection level. A simple example would be a textbook that can be broken up into component parts that are the size of sections within chapters—or the content a teacher would cover in a single lesson or small group of lessons on a single topic. Each of the sections—the components—can then be tagged with metadata that precisely describe that component and will address a learner’s specific needs.
* It can also be very useful to refer to the greater part that a “component” has been taken from so that people can see it in its wider context and choose to also use other components of that resource if they wish. Likewise, it can enrich the metadata to provide more information about the resource component’s origin or if it is associated with other material from the publisher.
* A complicated example would be one in which there are no discrete activities or lessons, such as in a gaming or simulation environment. In this case, one option is to metatag the teacher guide or user guide, which typically provides the necessary educational context to understand how the resource can be integrated into the curriculum.
* For marketing purposes, we understand that businesses sell their products in packages. If this is the case, you can create landing pages for each lesson or chapter with a reference to the larger material (or book). This will help ends users find the specific resource lesson they need, while keeping your total product offering as is. To expedite the process you can simply duplicate the URL for each resource component.

### 2. Discoverability
Discoverability refers to the
ease with which a resource or its
component parts can be found in
a networked environment or on
the Internet.

* It’s important to keep in mind the kind of results that end users expect to find when they perform a search.

* To be discoverable, each resource and its component parts must have a unique URL. If the resource is not digital, or if the resource resides behind a network firewall, you may need to create a unique landing page with appropriate information about how to access and/or purchase the resource.

### 3. Sequence
Sequence refers to a curricular
sequence that you, as the curriculum
developer, believe should be
employed in order to get the most
benefit from your resource.

* LRMI provides a way to tag (or in this case “align,” or “correlate”) learning resources to educational content standards, which may contain explicit or implicit curricular sequencing. However, there is no way to indicate publisher-specific curricular sequencing within the current LRMI specification. As a workaround, we suggest you use a naming convention in the title field such as “Title, Part 7 of 25.”

## Step Three: Tagging your Content
In this step the content is tagged with the appropriate metadata.

### 1. Missing metadata
I’ve reviewed
the LRMI specification and I
don’t have all the metadata
listed in the specification for my
learning resources.

* The implementation of LRMI metadata is quite flexible. There are no “required” elements of LRMI. For example, if you don’t have any formal usage rights or terms of use, you can omit this element from your metatagging.
*  In addition, if you wish to tag your learning resource today with some of the metadata elements, you can return to the learning resource at a later date and add or remove metadata elements.

### 2. Tagging curriculum standards
This involves selecting the best
matches between the educational
content and curriculum standards
documents.

**Note:** The GIM-CCSS project
listed earlier is developing a more
granular digital representation
of the Common Core State
Standards. Current digital
representations of the CCSS and
other curriculum standards exist
and can be used to align your
learning resources within the
LRMI metadata.

* Tagging to curriculum standards is typically the most confusing aspect of the LRMI specification, yet alignment to curriculum standards is often THE element educators use to search for learning resources.
* You can tag (“align”) your learning resource to one or more curriculum standards. However, if you are not using a professional service to do this part of the metatagging, we recommend that you become intimately familiar with the standards documents and only select the matches that best represent the learning resource. While selecting standards that touch on concepts or skills addressed by the learning resource, be aware that educators could interpret these resources as “false positives” in their search results and your learning resources could be viewed as inaccurately aligned to the standards.

### 3. Subject area 
Subject area does not appear
to be part of the LRMI
specification, but it is important
for me to communicate this
to people searching for my
educational resources.
Subject area does not appear
to be part of the LRMI
specification, but it is important
for me to communicate this
to people searching for my
educational resources.

* The “about” property that is a part of Schema.org adequately accomplishes this goal. The LRMI only adds properties that are not already covered. So, although it is not part of the LRMI specification, you can add this metadata for your learning resource using the existing “about” property. Where possible, the use of controlled vocabularies adds consistency to search results.

### 4. Age and grade
LRMI includes an
element for “typicalAgeRange”
specification but not “grade
level.” What is the recommended
way to handle this?

* It is true there is no property called “grade level” in the LRMI specification, because the LRMI is a global standard. Different countries use different names to label stages of learning as students progress through their formal education, and the material taught at a given level varies dramatically from country to country. This makes use of the term “grade level” problematic on a global scale even though most publishers include this data when tagging their content. Here are some recommendations for using typicalAgeRange effectively and for using LRMI to represent grade level(s).
* Use “typicalAgeRange” when that information is known and available. This can even be used when the only text visible on a webpage is the grade level, as long as you leverage a known and relatively agreed upon mapping between grade level and age range at the time the resource is being tagged.
* An example would look like:
`<p>This resource was written for an audience of <span
itemprop=”typicalAgeRange” content=”12-13”>6th graders</span></p>`
* To represent grade levels, it is possible to use the “educationalAlignment” term in combination with “alignmentObject.” In order to do so, there must be an applicable standard in your jurisdiction/country/state/etc. to model the grade level. This grade-level standard must be in a published format with URL/URI representations for the grade level(s). So, instead of using “alignmentObject” to align to academic standards, you are using it to align to grade levels. More specifically, within “alignmentType” (which is part of “alignmentObject”), you select “educationalLevel” to indicate that the tagging alignment refers to some standard level (in this case, grade level). Then, within “alignmentObject,” you use the “educationalFramework,” “targetDescription,” “targetName,” and “targetURL” to refer to the particular grade level(s) and the URL/URI where that standard definition is located.
* If there is no web-published URL/URI standard to which you can create an alignment to grade level, it is useful to note that tagging to curriculum standards often associates the learning resource to specific grade levels because the curriculum standards are often organized by grade level.

### 5. Usage rights
* This element of the LRMI was defined to enable publishers to specifically list usage rights whether they are selected from Creative Commons or their own. Often, publishers have Terms of Use pages that can be specifically listed within this element, providing a broad applicability for multiple learning resources with a common set of usage rights.
* Including a URL that points to conditions of usage ensures that the accuracy and currency of this information is maintained in the metadata.

For examples of learning resources tagged to the LRMI specification, please refer to the appendix. For
further information about metadata, the LRMI, and the Learning Registry, visit the LRMI website at
www.lrmi.net

**Version history**

| Date | Author | Note |
| -------- | -------- | -------- |
| Jan 2013     | Association of Educational Publishers, Educational Systemics, and Knovation     | Original version     |


Acknowledgements

We gratefully acknowledge the contributions of the following individuals, who provided material or
editorial guidance for this project.

Contributors/Advisors/Reviewers

Holly Cefrey, Rosen Publishing
Teila Evans, Educational Systemics, Inc.
Dave Gladney, LRMI, Association of American
Publishers PreK–12 Learning Group
Michael Jay, Educational Systemics, Inc.
Mary LeDonne, Educational Systemics, Inc.
David Longdon, Educational Systemics, Inc.
John Micklos, Jr., LRMI, Association of
American Publishers PreK–12 Learning Group
Charles Myers, Benetech
Steve Nordmark, Knovation