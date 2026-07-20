## Intro to LLD
- HLD answers: "What components do we need and how do they communicate?"
- LLD answers: "How do we actually implement each component?"

## LLD
- What are the specific classes, and what are their responsibilities?
- What are the attributes and methods of each class?
- How do these classes relate to each other (inheritance, composition)?
- What design patterns are most suitable (e.g., Factory, Singleton, Strategy)?
- What are the specific method signatures, including parameters, return types, and exceptions?

## Where LLD Fits in the Development Process
- Requirements -> HLD -> LLD -> Code Implementation

## Key relationships include:
- Association: A general "uses-a" relationship. A Doctor uses a Stethoscope.
- Aggregation (Weak "has-a"): An object contains other objects, but they can exist independently. A Department has Professors. If the department is closed, the professors still exist.
- Composition (Strong "has-a"): An object is composed of other objects, and their lifecycles are tied. A House is composed of Rooms. If you demolish the house, the rooms are destroyed with it.
- Inheritance ("is-a"): A class inherits properties and behaviors from a parent. A Car is a Vehicle.

## Types of LLD Interviews
![s](./img/type-of-lld.png)

## What Interviewers Evaluate - OOD

| Skill | Weight | What They Look For |
| --- | --- | --- |
| OOP Fundamentals | High | Proper use of inheritance, encapsulation, polymorphism |
| Design Patterns | High | Recognizing when patterns fit naturally |
| SOLID Principles | High | Single responsibility, open/closed, etc. |
| Communication | High | Explaining decisions, responding to feedback |
| Trade-off Discussion | Medium | Justifying choices, considering alternatives |

## What Interviewers Evaluate - Machine Coding

| Skill | Weight | What They Look For |
| --- | --- | --- |
| Coding Speed | High | Can you implement under time pressure? |
| Code Quality | High | Can you write clean, readable, maintainable code? |
| Correctness | High | Does your code work for given test cases? |
| Testing | High | Writing test cases or driver code |
| Project Structure | Medium | Using proper packages, separation of concerns |
| Edge Cases | Medium | Handling invalid inputs gracefully |

## How to Identify Your Interview Type
- “What type of LLD round should I expect?”
- “Will this be whiteboard-style discussion, or will I code in an IDE?”
- “How long is the LLD round?”
- “Should I expect concurrency topics like race conditions or deadlocks?”
- “Will there be any database or schema design in this round?”


### Classes and Objects
- Classes is blueprint.
- Object is instance of class.

eg:
```
class Car:
	def __init__(self, brand, model):
		self._brand = brand
		self._model = model
		self._speed = 0

	def accelerate(self, increment):
		self._speed+=increment


	def display_status(self):
		print(f"Brand {self._brand} 's model {self._model} is running at {self._speed} km/h.")


if __name__ == "__main__":
	corolla = Car("Toyota", "Corolla")
	mustang = Car("Ford", "Mustang")
	corolla.display_status()
	corolla.accelerate(20)
	corolla.display_status()
```