---
class: note
tags:
source: https://www.geeksforgeeks.org/software-engineering/mvc-framework-introduction/
related:
author:
date: 2026-03-11
updated: 2026-03-11 20:05:45
aliases:
---
## MVC: Model-View-Controller

![[Pasted image 20260311200633.png]]

**CONTROLLER:**

- receives user input and interprets it
- updates the **Model** based on user actions
- selects and displays the appropriate **View**
- doesn’t have to worry about handling data logic, just tells model what to do
- _eg. in a bookstore application, controller handles actions such as searching for book, adding book to cart, or checking out_

**VIEW:**

- renders data to the user in a specific format
- displays the user interface elements
- updates the display when the model changes
- created by the data which is collected by the model but this data isn’t taken directly, instead only through controller
- _eg. view displays the list of books, book details, provides input fields for searching or filtering books_

**MODEL:**

- manages data: CRUD operations
- enforces business rules
- notifies the view and controller of state changes
- can add / retrieve data from the database
- responds to the controller’s request because the controller can’t interact with the database by itself
- _eg. model handles data related to books, such as book title, author, price and stock level_

**Example:**

![image.png](attachment:000074cb-b945-4c73-9c95-b796a3bf2b44:image.png)

**Design Principles:**

1. **Divide and conquer.**
    - The three components can be somewhat independently designed.
2. **Increase cohesion.**
    - The components have stronger layer cohesion than if the view and controller were together in a single UI layer.
3. **Reduce coupling.**
    - The communication channels between the three components are minimal and easy to find.
4. **Increase reuse.**
    - The view and controller normally make extensive use of reusable components for various kinds of UI controls. The UI, however, will become application-specific, therefore it will not be easily reusable.
5. **Design for flexibility.**
    - It is usually quite easy to change the UI by changing the view, the controller, or both.

| **Advantages**                                                                                                    | **Disadvantages**                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Codes are easy to maintain and they can be extended easily.                                                       | It is difficult to read, change, test, and reuse this model                                                                                            |
| The MVC **model** component can be tested separately.                                                             | It is not suitable for building small applications.                                                                                                    |
| The components of MVC can be developed simultaneously.                                                            | The inefficiency of data access in view.                                                                                                               |
| It reduces complexity by dividing an application into three units. **Model, view, and controller.**               | The framework navigation can be complex as it introduces new layers of abstraction which requires users to adapt to the decomposition criteria of MVC. |
| It supports **Test Driven Development (TDD).**                                                                    | Increased complexity and Inefficiency of data                                                                                                          |
| It works well for Web apps that are supported by large teams of web designers and developers.                     |                                                                                                                                                        |
| This architecture helps to test components independently as all classes and objects are independent of each other |                                                                                                                                                        |
| **Search Engine Optimization (SEO)** Friendly.                                                                    |                                                                                                                                                        |
