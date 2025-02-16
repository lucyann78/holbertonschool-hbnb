# HBnB Project README
Table of Contents
Project Overview
Context and Objective
Problem Description
Business Rules and Requirements
Architecture and Layers
Diagrams
High-Level Package Diagram
Detailed Class Diagram
Sequence Diagrams
Documentation Compilation
Resources
Conclusion
Project Overview
The HBnB Evolution project is a simplified version of an AirBnB-like application, designed to facilitate user management, place management, review management, and amenity management.

Context and Objective
This document serves as comprehensive technical documentation for the HBnB Evolution application, providing foundational knowledge for its development. It outlines the architecture, design, and interactions within the system.

Problem Description
The application allows users to:

Register and manage profiles (regular users or administrators).
List properties with details (name, description, price, location).
Leave reviews for places visited.
Manage amenities associated with places.
Business Rules and Requirements
User Entity
Attributes: First name, last name, email, password, administrator status.
Operations: Register, update profile, delete.
Place Entity
Attributes: Title, description, price, latitude, longitude, amenities.
Operations: Create, update, delete, list.
Review Entity
Attributes: Rating, comment associated with a place and user.
Operations: Create, update, delete, list.
Amenity Entity
Attributes: Name, description.
Operations: Create, update, delete, list.
Architecture and Layers
The application follows a layered architecture divided into:

Presentation Layer: Interfaces for user interaction (services and APIs).
Business Logic Layer: Core logic and entity models (User, Place, Review, Amenity).
Persistence Layer: Data storage and retrieval.

Diagrams


___
## High-Level Package Diagram (Three Layer Architecture and the Communication Pathways Diagram)
``` mermaid
classDiagram
class PresentationLayer {
    <<Interface>>
    +ServiceAPI
}
class BusinessLogicLayer {
    +ModelClasses
}
class PersistenceLayer {
    +DatabaseAccess
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
```
___
## Detailes Class Diagram (Outlines the Entities in the Business Logic Layer)
``` mermaid
classDiagram
class User {
    +String firstName
    +String lastName
    +String email
    +String password
    +boolean isAdmin
    +register()
    +updateProfile()
    +delete()
}
class Place {
    +String title
    +String description
    +Double price
    +Double latitude
    +Double longitude
    +List<Amenity> amenities
    +create()
    +update()
    +delete()
    +list()
}
class Review {
    +Integer rating
    +String comment
    +create()
    +update()
    +delete()
    +list()
}
class Amenity {
    +String name
    +String description
    +create()
    +update()
    +delete()
    +list()
}

User --> Place : creates
Place --> Amenity : has
Review --> Place : associated with
Review --> User : written by
```
___
## Sequence Diagrams (User Registration and Place creation)
``` mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call (Register User)
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Save User Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Return Success/Failure
```
``` mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call (Create Place)
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Save Place Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Return Success/Failure
```
___

Documentation Compilation
This document compiles all diagrams and explanatory notes, providing a detailed blueprint for the HBnB Evolution application. It serves as a reference for the implementation phases and outlines the overall architecture and design.

Resources

UML Basics
Mermaid.js Documentation
UML Class Diagram Tutorial

