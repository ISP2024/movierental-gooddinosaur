## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

### 2.1 Refactoring Signs (Code Smells)

Ans :  
- **Unnecessary Attribute**: The `price_code` in the `Movie` class didn't really belong there because the class was meant to hold information about the movie itself, like its title. This made the class less clear.

- **Low Cohesion**: The `price_code` was more related to rentals than to the movie itself. Moving it to the `Rental` class makes the code clearer because each class does one specific job.

- **Increased Complexity**: Having the `price_code` in `Movie` made it harder to get rental prices. This added unnecessary steps when working with rentals, making the code harder to follow.

### 2.2 What design principle suggests this refactoring? Why?

Ans : 
The **Single Responsibility Principle (SRP)** suggests this refactoring. This principle means that a class should only do one thing. By moving `price_code` to the `Rental` class, we make sure that `Movie` only deals with movie details (like the title), while `Rental` handles how much it costs to rent a movie. This makes the code simpler and easier to manage.

- The `Movie` class is simplified, allowing it to focus solely on representing the movie's title and details.
- The `Rental` class is made responsible for pricing logic and determining rental costs, aligning its responsibilities more clearly with its purpose.



