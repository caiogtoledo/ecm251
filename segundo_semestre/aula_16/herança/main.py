from mimetypes import init
from documents import Document, Book, Email


def run():
    doc1 = Document()
    doc2 = Email(to='caio@email.com', authors=["Murilo Zanini"])
    doc3 = Book(title="Design Patterns", authors=[
                "Erich Gamma", "John Vlissides"])
    print(doc3)


if __name__ == "__main__":
    run()
