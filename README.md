# Foondamate_ML_Engineer_Task

This function "email_classifier" tries to classify an email and state if Marry's email address has been share to another student or if the student is checking in with marry before sharing her email address.

The function first checks if the word "share" exists in a email, then it uses a list of words from a word bank/list(this words or sequence of words are usually used to either seek permission or ask questions) to look through the email message and tries to see if a word or sequence of words from the word bank exists in the email message.

# requirements
```
python3+
```

    # create a virtual environment
    python3.9 -m venv .venv

# To run the project

    #run the program
    python email_classifier.py

# To run the tests in project

    #run the program's test
    python test_email_classifier.py