from app import (
    add_student_data,
    get_students,
    search_student_by_name,
    delete_student_by_name
)

def test_add_student():
    student = add_student_data("Gagan", "22", "DevOps")
    assert student["name"] == "Gagan"


def test_get_students():
    students = get_students()
    assert isinstance(students, list)


def test_search_student():
    add_student_data("John", "21", "Python")
    result = search_student_by_name("John")
    assert result is not None


def test_delete_student():
    add_student_data("Alice", "23", "AWS")
    result = delete_student_by_name("Alice")
    assert result is True
