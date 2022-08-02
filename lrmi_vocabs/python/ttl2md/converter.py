from os.path import exists, isfile
from readchar import readchar
from rdflib import Graph, Namespace
from rdflib.namespace import SKOS, RDF, RDFS, DCTERMS, DC

# the following namespaces may be used in addition to those imported above
ADMS = Namespace("http://www.w3.org/ns/adms#")
BIBO = Namespace("http://purl.org/ontology/bibo/status/")
VS = Namespace("http://www.w3.org/2003/06/sw-vocab-status/ns#")
# the following properties of a SKOS ConceptScheme will be processed if present
schemeProperties = [
    (DC.title, "Title"),
    (DCTERMS.title, "Title"),
    (DC.description, "Description"),
    (DCTERMS.description, "Description"),
    (DC.creator, "Creator"),
    (DCTERMS.creator, "Creator"),
    (DCTERMS.dateSubmitted, "Date Submitted"),
    (DCTERMS.created, "Date Created"),
    (DCTERMS.modified, "Date Modified"),
    (DC.source, "Source"),
    (DCTERMS.source, "Source"),
    (DCTERMS.license, "License"),
    (ADMS.status, "Status")
]
# the following properties of a SKOS Concept will be processed if present
conceptProperties = [
    (SKOS.prefLabel, "Label"),
    (SKOS.definition, "Definition"),
    (SKOS.scopeNote, "Scope Note"),
    (DC.source, "Source"),
    (DCTERMS.source, "Source"),
    (SKOS.exactMatch, "Exact Match"),
    (SKOS.closeMatch, "Close Match"),
    (SKOS.broadMatch, "Broad Match"),
    (SKOS.narrowMatch, "Narrow Match"),
    (SKOS.relatedMatch, "Related Match"),
    (VS.term_status, "Term Status")
]

def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])



class Converter():
    def __init__(self):
        """Set some variable for concept scheme graph and mark down"""
        self.md = []
        self.ttl = Graph()

    def readTTL(self, filename):
        """Read data from file and store as graph in self.ttl"""
        if isfile(filename):
            self.ttl.parse(filename)
            print("  file %s read." % filename)
        else:
            raise FileNotFoundError

    def printTTL(self):
        """Display the concept scheme graph."""
        print(self.ttl.serialize(format="ttl"))

    def printMD(self):
        """Display the markdown."""
        for line in self.md:
            print(line)

    def saveMD(self, filename):
        """Save the markdown text to a file."""
        if isfile(filename):
            print("    Warning file already exists")
            print("    Overwrite %s? (y/n)" % filename)
            r = readchar()
            if r == "y":
                print("    Will overwrite file " +  filename)
                pass
            else:
                print("    Will not overwrite file " +  filename)
                print("    No converted but not saved. \n")
                quit()
        with open(filename, "w") as md_file:
            md_file.writelines(self.md)
        print("    file %s written." % filename)


    def ttl2md(self):
        """Run through the ttl Concept Scheme graph and convert values to md string."""
        g = self.ttl
        table_start =  """
|               |
|--------------:|:----------------------------------------------------------
"""
        breaks = "\n<br /><br />\n\n"
        scheme = g.value(predicate=RDF.type, object=SKOS.ConceptScheme)
        # only works for one scheme in the graph
        # would be simple to extend to more by iterating over schemes
        # i.e. iterate over g.subjects(RDF.type, SKOS.ConceptScheme)
        scheme_URL = str(scheme)
        self.md.append(table_start)
        self.md.append("| URL:    | %s \n" % scheme_URL)
        self.md.append("| Type:   | SKOS:ConceptScheme \n")
        for (property, label) in schemeProperties:
            self._addPropertyRow(scheme, property, label)
        self.md.append(breaks)
        for concept in g.subjects(predicate=SKOS.inScheme, object=scheme):
            url = str(concept)
            label = str(g.value(concept, SKOS.prefLabel))
            self.md.append("### <a id=\"%s\" /> %s \n" % (to_camel_case(label), label.title()))
            self.md.append(table_start)
            self.md.append("| URL:    | %s\n" % url)
            for (property, label) in conceptProperties:
                self._addPropertyRow(concept, property, label)
            self.md.append(breaks)

    def _addPropertyRow(self, subject, property, label):
        """add a row to the MD table for the concept or scheme property"""
        g = self.ttl
        first = True
        for value in g.objects(subject, property):
            if first : # add the first column only on the vist pass
                row = "| %s: | " % label
                first = False
            row += value + " "
        # in case there are no values
        if not first:  # only end & store the row if we started it
            row += "\n"
            self.md.append(row)
        return
