from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending Email: {message}")


class SlackNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending Slack Notification: {message}")


class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def send(self, message: str) -> None:
        notification = self.create_notification()
        notification.send(message)


class EmailNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SlackNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SlackNotification()

def main():
    slackNotify = SlackNotificationCreator()
    slackNotify.send("hey I am slack bot")

    emailNotify = EmailNotificationCreator()
    emailNotify.send("this is an email...")

if __name__ == "__main__":
    main()
