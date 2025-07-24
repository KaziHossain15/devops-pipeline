# this is the unit test that imports the app from the main python file

import app

def test_home(): # this will check if the home function works correctly
    assert app.home() == "Hello from DevOps world!"

