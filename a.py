class Document:
    def __init__(self, content: str):
        self.__content = content
    
    def get_content(self) -> str:
        return self.__content


class Printer:
    def print_document(self, document: Document):
        print("Printing... "+ document.get_content())


if __name__ == "__main__":
    doc = Document("Hello, World!")
    printer = Printer()
    printer.print_document(doc)