from jinja2 import Environment, FileSystemLoader
import bs4
import requests


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
        document = template.render(**kwargs)
        if gizooglify:
            document = self.gizooglify(document)
        self.rendered_document = document
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

    def gizooglify(self, text):
        """
        Gizoogles a given piece of text using https://gizoogle.net

        Parameters
        ----------
        text: str
            The text which is to be converted


        Returns
        -------
        text: str
            The gizoogled version of the text
        """

        params = {"translatetext": text}
        target_url = "http://www.gizoogle.net/textilizer.php"
        response = requests.post(target_url, data=params)
        soup = bs4.BeautifulSoup(response.content, "html.parser")

        # Hacky, but consistent.
        return soup.text.split("Advertise")[1].split('Use')[0].strip()
