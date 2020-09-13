from jinja2 import Environment, FileSystemLoader


class Document():
    """The Document class to render and save SOPs

    The Document class is used to instantiate an SOP, render the final SOP
    and save it into a specified location.

    Attributes
    ----------
    doc_name: str
        The main file which is to be rendered
    template_location: str
        The location of all the saved templates
    rendered_document: str
        The final rendered version of the document
    """
    def __init__(self, doc_name, template_location="sops"):
        """Initializes the Document object

        Parameters
        ----------

        doc_name: str
            The main file which is to be rendered
        template_location: str
            The location of all the saved templates
        """
        with open(doc_name) as doc:
            self.document = doc.read()

        self.template_location = template_location

    def render_document(self, gizooglify=False, **kwargs):
        """Function to render the final document

        This function uses the Jinja engine to include templates and fill
        in variable names to render the final version of the document

        Parameters
        ----------
        gizooglify: bool, optional
            Boolean value indicating whether the final document is to be
            "gizooglified". Check out http://www.gizoogle.net/ for
            what this means.
        kwargs: dict
            All the variable names mentioned in the templates and their values

        Returns
        -------
        rendered_document: str
            The final version of the document
        """
        loader = FileSystemLoader(self.template_location)
        template = Environment(loader=loader).from_string(self.document)
        self.rendered_document = template.render(**kwargs)
        return self.rendered_document

    def save_file(self, location):
        """Function to save the final document at a specified location

        If the filename is given directly, it will save in the root folder.
        If you want to save into a subdirectory, it will have to be created
        beforehand otherwise an error is raised.

        Parameters
        ----------
        location: str
            The location and filename of the final document that is to be saved
        """
        with open(location, "w+") as doc:
            doc.write(self.rendered_document)
