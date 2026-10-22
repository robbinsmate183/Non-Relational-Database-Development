
## Task 5 - Evaluating a vague AI prompt

Prompt: Write a Flask endpoint to get students with high marks.

The prompt was too vague because it did not specify a module,
a minimum mark or the expected response format.

The example code filtered the students in Python rather than
MongoDB, did not validate inputs and included MongoDB's _id.

I did not add this code to my application because it needed
improvements before it would meet the requirements.



## Task 6 - With-mark endpoint

Date: 22 October 2026
Tool: ChatGPT

Prompt: Create a Flask GET endpoint at /students/with-mark
that accepts a required module parameter and an optional
minimum mark (default 70). Validate the minimum mark
between 0 and 100, use the existing MongoDB query
function, and return a count and results without _id.

What I got: A new Flask endpoint using the existing
mark_at_least function in queries.py.

Testing: Tested valid marks, missing parameters,
invalid marks and unknown modules using Postman.

Changes: Kept the existing API endpoints and used
port 5001 because port 5000 was unavailable.



## Task 7 - Society endpoint

Date: 22 October 2026
Tool: ChatGPT

Prompt: Create a Flask GET endpoint at
/students/in-society/<name> that finds students
belonging to a society using MongoDB. Return a count
and results sorted by surname, excluding _id.

What I got: A new endpoint that searches the
students collection by society name.

Testing: Tested Chess, Computing Society and Rowing
using Postman.

Changes: Added the endpoint to the existing app.py
without removing the previous endpoints.



## Task 8 - Reviewing AI-generated code

Date: 22 October 2026
Tool: ChatGPT

Prompt: Review the Flask API endpoints created for
Tasks 6 and 7. Check that they use MongoDB queries,
validate inputs where needed, exclude MongoDB _id,
and return the correct results.

What I got: A review of the existing endpoints
and the main requirements they needed to meet.

Testing: I tested the endpoints in Postman using
valid and invalid requests. All tests passed.

Changes: I kept the existing endpoints because
they worked correctly during testing. I also
kept Flask running on port 5001 because port
5000 was unavailable on my computer.
