import employee_info as info

def test_get_employees_by_age_range():
    result = []
    age_lower_limit = 20
    age_upper_limit = 30

    result = info.get_employees_by_age_range(age_lower_limit, age_upper_limit)

    chosen_employees = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
            ]
    
    assert (result == chosen_employees) 


def test_calculate_average_salary():
    result = 0
    average = 60166.666666666664

    result = info.calculate_average_salary()

    assert (result == average)


def test_get_employees_by_dept():
    result = []
    department = "Engineering"

    result = info.get_employees_by_dept(department)

    chosen_employees = [
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
            ]

    assert (result == chosen_employees)   