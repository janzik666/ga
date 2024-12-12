# 🔍 Python for Developers - Step 2 Project

## Project Brief

1. Every application that you encounter is generally a CRUD app and we've developed skills throughout this course to be able to do this on your own. Take this opportunity to pick a problem that you want to solve with the implementation of an application for users. 
2. **You don’t have to do this alone! Partner with someone if you want or go solo.**
3.  You’ll have the opportunity to meet with a Prudential developer who will be available to answer any questions you may have.
    - Your course
    - Recently covered content
    - Questions you may have while working on your PluralSight assignments or Step 2 Project
    - **Prepare your questions in advance and bring them with you to the session.** 
4. **Commit** Your Work To GitHub, **Submit** Your Work via Pull Request


## Project Requirements
1. **Data Model:** 
    - Implement a PostgreSQL database and use SQLAlchemy ORM to perform CRUD. 
    - Set up at least one one-to-many relationship, correctly associating tables.
2. **Endpoints:**
   - Complete implementation of CRUD (Create, Read, Update, Delete) endpoints, each working correctly with the database.
3. **Error Handling:**
    - Comprehensive error handling. Server doesn't crash, provides helpful and specific error messages and handles edge cases gracefully.
4. **Authentication/Authorization:**
    - JWT Authentication
    - Protected routes.
    - Object-level permissioning.

 
## Grading Rubric
1. Your project will be evaluated according to the rubric below. 
2. You will receive a score of 0-3 points for each criterion.
3. You need to score at least **10** out of **12** possible points to earn a passing grade.
4. Your TB and classmates will also provide you with qualitative feedback on your final presentation.

<br>
<br>

| Criterion| 0 | 1 | 2 | 3 | Score |
| :-------:|:-:|:-:|:-:|:-:|:-----:|
| **Rubric**   | Something is missing or it is incomplete | Something is there but not all of it | Most if it is there | Everything is there||
| **DB, Models**| No DB implemented or incorrect DB used. | PostgreSQL DB w/ one table, no relationships. | PostgreSQL DB w/ multiple tables, missing / incorrect relationships. | PostgreSQL DB w/ one-to-many relationship, correctly associated. ||
| **Endpoints**| Missing / Incorrect API endpoints.| Basic GET endpoint, working DB connection.| Multiple types of endpoints, but not functioning, or lack DB connection| Complete implementation of CRUD endpoints, each working w/ DB. ||
| **Error Handling** | No error handling. Server crashes. Unhelpful error msgs.| Basic error handling. Server doesn't crash. Unhelpful error msgs. | Advanced error handling. Server doesn't crash. Helpful error msgs. No handling of edge cases. | Comprehensive error handling. Server doesn't crash. Helpful error messages, handles edge cases gracefully. ||
| **Authorization**  | No authentication / authorization. | Basic Auth, but not all necessary routes protected. | Basic Auth, all necessary routes protected, lacks object-level permissioning. | Basic Auth, all necessary routes protected, Object-level permissioning. || 
|  **TOTAL SCORE**   | | | | | **_____** |