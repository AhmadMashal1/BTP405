# Building a RESTful API with CRUD Operations

This project is a simple API for managing notes. It allows users to create, read, update, and delete notes using HTTP requests.

## Features

- Create a new note
- Read all notes
- Read a specific note by ID
- Update a note
- Delete a note

## Technologies Used

- Python
- PostgreSQL
- Docker

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install Docker if you haven't already.
4. Run `docker compose up` to build and start the containers.
5. The API server will be accessible at `http://localhost:8000`.

## Endpoints

- GET /notes: Retrieve all notes.
- GET /notes/{id}: Retrieve a specific note by ID.
- POST /notes: Create a new note.
- PUT /notes/{id}: Update a note by ID.
- DELETE /notes/{id}: Delete a note by ID.

## Testing

You can test the API using tools like Postman or by sending HTTP requests directly. Here are some sample requests:

1. **GET /notes**: Retrieve all notes.
2. **GET /notes/{id}**: Retrieve a specific note by ID.
3. **POST /notes**: Create a new note.
   - Request body:
     ```json
     {
       "title": "Meeting Notes",
       "content": "Discuss project timelines and deadlines"
     }
     ```
4. **PUT /notes/{id}**: Update a note by ID.
   - Request body:
     ```json
     {
       "title": "Updated Title",
       "content": "Updated content"
     }
     ```
5. **DELETE /notes/{id}**: Delete a note by ID.

## Dummy Data

Dummy Note 1:
- Title: "Meeting Notes"
- Content: "Discuss project timelines and deadlines"

Dummy Note 2:
- Title: "Shopping List"
- Content: "Milk, eggs, bread, vegetables"

...
(Provide dummy data for testing purposes)

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for any bugs or feature requests.

