from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def get_data(self):
        pass


class Editable(Document):
    @abstractmethod
    def save(self, data):
        pass


class EditableDocument(Editable):
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Editable document opened. Data: ", self._preview())


    def save(self, data):
        self.data = data
        print("Document Saved")

    def get_data(self):
        return self.data

    def _preview(self):
        return self.data[:50] + "..."


class ReadOnlyDocument(Document):
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Read-only document opened, Data: ", self._preview())


    def get_data(self):
        return self.data
    
    def _preview(self):
        return self.data[:20] + "..."


class DocumentProcessor:
    def process(self, doc: Document):
        doc.open()
        print("Document processed")

    def process_and_save(self, doc: Editable, additional_info: str):
        doc.open()
        current_data = doc.get_data()
        new_data = current_data + " | Processed: " + additional_info
        doc.save(new_data)
        print(doc._preview())
        print("Editabled document processed and saved")


if __name__ == "__main__":
    editable = EditableDocument("document for Q3")
    read_only = ReadOnlyDocument("top secret streategy")
    processor = DocumentProcessor()

    print("--- Processing Editable Document ---- ")
    processor.process_and_save(editable, "Reviewed by nitin")

    print("\n ---- Processing Read-only Document ----")
    processor.process(read_only)
