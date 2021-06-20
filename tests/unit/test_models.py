from api.todo.models import Todo


def test_new_todo():
    """
    GIVEN a Todo model
    WHEN a new Todo is created
    THEN check the id, name, description, and completed fields are defined correctly
    """
    todo = Todo(name="foo", description="bar", completed=False)
    assert todo.name == "foo"
    assert todo.description == "bar"
    assert todo.completed == False
