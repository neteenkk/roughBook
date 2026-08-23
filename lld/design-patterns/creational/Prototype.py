from abc import ABC, abstractmethod
import platform

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def on_click(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("Printing a windows style button")

    def on_click(self):
        print("Windows button clicked")

class WindowsCheckbox(CheckBox):
    def paint(self):
        print("Paintaing a windows-styled checkbox")

    def on_click(self):
        print("Windows Checkbox styled")


class MacOSButton(Button):
    def paint(self):
        print("Painting a macOS-style button")

    def on_click(self):
        print("MacOS Button selected")


class MacOSCheckbox(CheckBox):
    def paint(self):
        print("painting a macOS-styled checkbox")

    def on_click(self):
        print("macOS Checkbox selected")

# abstractFactory

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self):
        self.button.paint()
        self.checkbox.paint()

def main():
    os = platform.system()
    print(os)
    if "Windows" in os:
        factory = WindowsFactory()
    else:
        factory = MacOSFactory()

    app = Application(factory)
    app.render_ui()


if __name__ == "__main__":
    main()