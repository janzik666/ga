![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png)

# Testing in FastAPI (180 minutes)

## Guided Walkthrough (60-90min)

We'll be using Pytest to help us to test our FastAPI API. Pytest is a popular Python testing framework that is used to write and execute unit tests.

When using pytest and FastAPI together, you can use pytest to write and run tests for your FastAPI web app. This allows you to verify that your app is working correctly, and to identify and fix any bugs or other issues before deploying to production.

To use pytest, you will need to install it along with a few other packages that will be necessary to run our tests: `pipenv install pytest starlette httpx`. Once you have done this, you can write tests for your FastAPI application using pytest's built-in assert statements and other features, such as fixtures. 

You can then run these tests using `pipenv run pytest` command, which will automatically execute your tests and provide feedback on their results.

### Pytest Setup and Configuration

- [pytest](https://docs.pytest.org/en/7.2.x/) is our testing library.
- We can run it with `pipenv run pytest`
- Pytest will look inside a `tests` directory in the root of our project.

### `pytest.ini`

We need to add this `pytest.ini` file to our project root. This will make debugging our tests easier, as we can print out information in both successful and failing tests.

```ini
[pytest]
; ! Adding command line arguments to pytest...
; ! rP -> when do you print() in your tests, it will show even if the test succeeded.
; ! -p no:warnings -> Disable a warning about postgres drivers that doesn't really make a diff.
addopts = -rP -p no:warnings
```

### `tests/conftest.py`

_Make sure to create a `tests` directory in the root of your project._

- Inside that directory, pytest will run the `conftest.py` file before anything else! This is important so we can change the database that we run tests against to be SQLite, which is an in-memory database you can use in Python. This is different to postgres, which is an application you actually to run independently on your API. SQLite will be managed completely within the testing program and stop as soon as your tests stop.
- We use this `conftest.py` file to override our environment database.

Here are the contents of `tests/conftest.py`

```py
# tests/conftest.py

import pytest
from starlette.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from database import get_db
from models.base import BaseModel
from tests.lib import seed_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def test_db() -> Session:
    # drop all tables in the database
    BaseModel.metadata.drop_all(bind=engine)
    # create all tables in the database
    BaseModel.metadata.create_all(bind=engine)
    # initiate a new session
    db = TestingSessionLocal()
    seed_db(db)
    yield db
    db.close()

@pytest.fixture(scope="module")
def override_get_db(test_db):
    def _get_db_override():
        return test_db
    app.dependency_overrides[get_db] = _get_db_override
    yield
    app.dependency_overrides = {}

```

### `tests/lib.py`

`lib.py` is going to contain our general library functions that we can use in each test, specifically seeding our database and being able to login when needed.


```py
# tests/lib.py

from fastapi.testclient import TestClient
from models.tea import TeaModel
from models.user import UserModel
from models.comment import CommentModel
from data.tea_data import teas_list, comments_list
from data.user_data import user_list

def seed_db(db):
    db.commit()

    db.add_all(user_list)
    db.commit()

    db.add_all(teas_list)
    db.commit()

    db.add_all(comments_list)
    db.commit()


def login(test_app: TestClient, username: str):
    response = test_app.post("/api/login", json={"username": username})
    token = response.json()['token']
    headers = {"Authorization": f"Bearer {token}"}
    return headers

```

### `tests/test_****.py`

There are some rules pytest follows to know which files and functions to run as tests:
- Test files should have the prefix `test_` or end with the suffix `test.py`. For example: `test_my_module.py` or `my_module_test.py`.
- Test functions should have the prefix `test_`. For example: `def test_my_function():`.

We'll be creating a `test_teas.py` file to test getting and creating teas.

### Fixtures

Pytest provides a feature called Fixtures, that allow us to run some code before our tests run and after they are complete. Looking at our `conftest.py` file you'll see that there are certain fixtures declared there.

This is often called `setup` and `teardown`.

The reason we need this is because before every test we want to seed our database with some teas and some users. We _could_ do this at the start of every single test, but this would be slow and cumbersome. With the pytest fixtures feature we can ensure that before every test we seed our database with some users and teas, and then after every test we remove all the teas and users from the test db. 

This is important because we want our tests to work independently of each other. We want them to be pure. The side effects of running one tests should not effect all other tests.

The `yield` statement is going to pass control flow to the test function that's currently running. In other words, everything that happens in this fixture BEFORE the yield, will run BEFORE the test, then the test code gets run, and finally, yield will jump back into this fixture and run the code AFTER the yield. In this case, we're clearing out the database of all test data.

This is our complete fixture. We can now use this in every test we want to run!

### The tests themselves

Now we've done all that setup, time to create the tests themselves.

First we're going to make a test to GET all our teas from our test database.

Here's our test:

```python
# tests/test_teas.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from models.tea import TeaModel
from tests.lib import login
from main import app

def test_get_teas(test_app: TestClient, override_get_db):
    response = test_app.get("/api/teas")
    assert response.status_code == 200
    teas = response.json()
    assert isinstance(teas, list)
    assert len(teas) is 2
    for tea in teas:
        assert 'id' in tea
        assert 'name' in tea
        assert 'in_stock' in tea
        assert 'rating' in tea
        assert 'user' in tea
        assert 'email' in tea['user']
        assert 'username' in tea['user']
```

See that we start with the `test` prefix on the function name. This is for `pytest` to know its a test.

The `assert` statements assert if various things are true. This is how we check our expectations against the actual result of running the test.

Here we're testing how many teas should be in the test database, and the correct response code as well as the actual contents of the response itself.

We can now run `pipenv run pytest`, to check if this test passes. If successful, pytest will give us a green success message. And if it fails, it'll show us which assertion failed in which test.

### Create tea test
Next, we make a test to create our tea. This one is a bit more complex, because you need to login to obtain a token first, before you can post one. Put this code in the same file:

Here is some code:

```python

def test_create_tea(test_app: TestClient, test_db: Session):
    headers = login(test_app, 'nick123')

    tea_data = {
        "name": "Test Tea",
        "in_stock": True,
        "rating": 4
    }

    response = test_app.post("/api/teas", headers=headers, json=tea_data)

    # Assert that the tea was created
    assert response.status_code == 200

    # # Assert that the returned data matches the tea_data
    assert response.json()["name"] == tea_data["name"]
    assert response.json()["in_stock"] == tea_data["in_stock"]
    assert response.json()["rating"] == tea_data["rating"]
    assert "id" in response.json()
    assert "user" in response.json()
    assert response.json()['user']["username"] == 'nick123'

    # Now, check if the tea was actually created in the database:
    tea_id = response.json()["id"]
    tea = test_db.query(TeaModel).filter(TeaModel.id == tea_id).first()

    # Assert that the tea is not None (meaning it exists in the DB)
    assert tea is not None

    # Assert that the tea in the DB has the same data as what we sent
    assert tea.name == tea_data["name"]
    assert tea.in_stock == tea_data["in_stock"]
    assert tea.rating == tea_data["rating"]

```


If we run `pipenv run pytest` again, it should succeed in the same way!

## Testing Lab (60 - 90min)

Your goal is to aim for 70-80% coverage of your API. That means you should be writing tests for 70-80% of the possible actions on your API. This is a good balance between being thorough but also being realistic. Remember, the goal of testing is to help ensure your API is functioning correctly. Testing 100% of all possible edge cases is often impractical and doesn't necessarily provide a proportional increase in confidence in your code.

Make sure to have tests for the following:

* Get all teas (We completed this above)
* Get a single tea
* Get a single tea when it's not found
* Create a tea (We completed this above)
* Create a tea but user is not logged in
* Update a tea
* Update a tea that is not found
* Update a tea for logged in user who does not have permission
* Delete a tea
* Delete a tea that is not found
* Delete a tea for logged in user who does not have permission

---

## Additional Resources

1. [pytest](https://docs.pytest.org/en/7.2.x/)
2. [Testing FastAPI](https://fastapi.tiangolo.com/tutorial/testing/)
3. [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)
