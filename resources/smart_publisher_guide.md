# Context and Background

We take advantage of the search and retrieval capabilities of computer networks and the Internet every day, and most of the time we easily get the kind of results we expect. In education, however, the existing search and retrieval capacities of these systems are inadequate. Teachers need to find educational resources that precisely meet the distinct needs of their students. They need to be able to search based on education-specific attributes such as the student’s age, the academic subject area of interest, or the type of learning activity. Publishers need to communicate the usage rights of their content and ensure that educators can easily find exactly the resources that they are searching for. The Learning Resource Metadata Initiative (LRMI), a collaboration led by the Association of Educational Publishers (AEP) and Creative Commons, and funded by the Bill & Melinda Gates Foundation and the William and Flora Hewlett Foundation, is working to address these needs and make it easier to develop, deliver, and discover quality educational resources on the web.

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

### Shared Learning Collaborative (SLC) http://slcedu.org

The SLC provides resources to help developers, courseware designers, and educators create tools and services in alignment with the Common Core State Standards. The SLC is working to make personalized learning a reality for every U.S. student by improving the usefulness, variety, and affordability of education technology. The SLC is organizing data about students and learning resources. The SLC plans to use the Learning Registry framework for discovery and delivery of learning resources, and as stated above, LRMI is an important element within the metadata definition of the learning resources.

### GIM-CCSS http://www.setda.org/web/guest/Interoperability

The “Granular Identifiers and Metadata for the Common Core State Standards” (GIM-CCSS) project is working to facilitate the long-term technical implementation of the Common Core State Standards (CCSS) in a digital format that preserves their conceptual and structural integrity. The LRMI specification consists of elements that permit tagging to (“aligning to”) published educational standards.  Thus, the efforts of the GIM-CCSS project will increase the ability of publishers to meaningfully tag (“align”) their learning resources to CCSS.  This project is a collaboration among the Partnership for the Assessment of Readiness for College and Careers (PARCC), the Smarter Balanced Assessment Consortium (Smarter Balanced), the State Educational Technology Directors Association (SETDA), and the Council of Chief State School Officers (CCSSO).

### Schools Interoperability Framework Association (SIFA) http://www.sifinfo.org

The SIF Association is comprised of K-12 organizations that have created a set of rules and definitions that enable software programs from different companies to share information. This set of platform-independent, vendor-neutral rules and definitions is called the SIF Implementation Specification. The SIF Specification makes it possible for programs within a school or district to share data without additional programming.

## Context: How it all Fits Together

![](https://hackmd.io/_uploads/rJUo8-fd3.png)

The diagram above provides some context about the important role metatagging plays in the search and retrieval of instructional resources. Working from right to left on the diagram, educational publishers develop instructional materials that are then tagged to learning standards and other metadata, which are stored in the Learning Registry. Working from left to right, educators and students search for educational resources and find exactly what they are looking for in the Learning Registry. Without a standard metatagging approach it would not be possible to easily find the right resources.

## Best Practices and Metatagging Workflow

There is no one “right way” to organize your metatagging process and workflow. You will need to develop a process that works for the unique characteristics of your organization. Based on decades of metatagging experience, we recommend that you consider the best practices below during your LRMI planning and implementation process.

Before you start working with LRMI, you should spend time planning the implementation and how it will fit into your existing workflow. 

Here are some common issues publishers will want to consider.



| Issue to consider: | Considerations and advice |
| -------- | -------- |
| What is the nature of your organization?
Are you a “mom and pop shop” with relatively few products or are you part of a large organization with myriad disparate products and bureaucracies?     | If you are part of a small organization, you’ll likely be working on LRMI in between all the other important things on your plate. Schedule a regular time to work on LRMI-related issues and stick to your schedule.
If you are part of a large organization you may have to deal with any number of bureaucratic issues. To facilitate LRMI in a larger organization it often makes sense to have someone (or a dedicated crew) whose sole responsibility is the metatagging process, and get buy-in from every key stakeholder including managers and executives. It’s beneficial to have representation from both your content and technical team during these discussions.      |


### Step One: Planning

**Version history**

| Date | Author | Note |
| -------- | -------- | -------- |
| Jan 2013     | Association of Educational Publishers, Educational Systemics, and Knovation     | Original version     |
