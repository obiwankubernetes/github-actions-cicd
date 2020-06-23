# unit testing app.py

from app import index
# need to set PYTHONPATH=src to get index from src/app.py module

def test_index():
    assert index() == "Hello World -- GitHub Actions is Awesome!"

# type pytest to run unit test