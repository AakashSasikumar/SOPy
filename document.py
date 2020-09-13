from jinja2 import Environment, FileSystemLoader
import os


class Document():
    def __init__(self, doc_name, template_location="sops"):
        with open(doc_name) as doc:
            self.document = doc.read()

        self.template_location = template_location

    def render_document(self, gizoogle=False, **kwargs):
        template = Environment(loader=FileSystemLoader(self.template_location)).from_string(self.document)
        self.rendered_document = template.render(**kwargs)

    def save_file(self, location):
        with open(location, "w+") as doc:
            doc.write(self.rendered_document)
