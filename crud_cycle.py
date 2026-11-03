import requests

# Step 1: CREATE
# POST a new todo item for user 1 (title: "Complete Module 4", completed: false)

new_todo = {
    "userId": 1,
    "title": "Complete Module 4",
    "completed": False
}

response = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_todo)

print(f"\nPOST /todos")
print(f"Status: {response.status_code}")
if response.status_code != 201:
    response.raise_for_status()
    raise RuntimeError(f"POST failed with status {response.status_code}.")

created = response.json()
created_id = created['id']
print(f"Created todo with ID: {created_id}")
print(f"Title: {created['title']} \nCompletion Status: {created['completed']}")
print()

# Step 2: READ
# GET the todo you just created (use the ID from the POST response)
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{created_id}")

print(f"\nGET /todos/{created_id}")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    todo = response.json()
    print(f"Title: {todo['title']}, \nCompletion Status: {todo['completed']}")
else:
    print("JSONPlaceholder simulates creation but does not persist new todos, so this GET can return 404.")

# Step 3: UPDATE
# PATCH the todo to mark it as completed (completed: true)
updated_todo = {
    "completed": True
}

response = requests.patch(
    f"https://jsonplaceholder.typicode.com/todos/{created_id}",
    json=updated_todo
)

print(f"\nPATCH /todos/{created_id}")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print(f"Updated completion status: {result['completed']}")
else:
    print(f"PATCH failed - id {created_id} does not exist in the mock dataset.")

# Step 4: READ AGAIN
# GET the todo once more to verify the update
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{created_id}")

print(f"\nGET /todos/{created_id}")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    todo = response.json()
    print(f"Title: {todo['title']}, \nCompletion Status: {todo['completed']}")
else:
    print("JSONPlaceholder simulates creation but does not persist new todos, so this GET can return 404.")

# Step 5: DELETE
# DELETE the todo
response = requests.delete(f"https://jsonplaceholder.typicode.com/todos/{created_id}")

print(f"\nDELETE /todos/{created_id}")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    print("Todo item deleted successfully.")
else:
    print(f"DELETE failed for todo with ID {created_id}.")
print()

# Step 6: VERIFY
# Try to GET the deleted todo and handle the response
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{created_id}")

print(f"\nGET /todos/{created_id}")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    todo = response.json()
    print(f"Title: {todo['title']}, \nCompletion Status: {todo['completed']}")
else:
    print(f"ToDo item not found under /todos/{created_id}.")
