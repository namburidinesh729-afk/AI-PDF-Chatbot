from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def create_pdf(text, filename):
    """
    Creates a PDF from the given text.

    Parameters:
        text (str): Content to write.
        filename (str): Output PDF filename.
    """

    document = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))

    document.build(story)

    return filename