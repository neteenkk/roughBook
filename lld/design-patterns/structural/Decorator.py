from abc import ABC, abstractmethod


class TextView(ABC):
    @abstractmethod
    def render(self):
        pass


class PlainTextView(TextView):
    def __init__(self, text):
        self._text = text

    def render(self):
        print(self._text, end="")

class TextDecorator(TextView):
    def __init__(self, inner):
        self.inner = inner

class BoldTextDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)

    def render(self):
        print("<b>", end="")
        self.inner.render()
        print("</b>", end="")

class ItalicDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)

    def render(self):
        print("<i>", end="")
        self.inner.render()
        print("</i>", end="")

class UnderLine(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)

    def render(self):
        print("<u>", end="")
        self.inner.render()
        print("</u>", end="")

def main():
    text = PlainTextView("Hello, World")

    print("Italic + Bold Font")
    italic_bold = ItalicDecorator(BoldTextDecorator(text))
    italic_bold.render()
    print()

    print("Underline + Italic + Bold Font")
    underline_italic_bold = UnderLine(ItalicDecorator(BoldTextDecorator(text)))
    underline_italic_bold.render()
    print()


if __name__ == "__main__":
    main()