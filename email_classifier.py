def classifier(string):
    """
    This function classifies emails based on its content
    as either shared or not shared
    """
    # this is a list of words that are used to classify emails as shared
    words = ["may", "can", "if", "should", "allowed"]

    # this check if the email contains the word "share"
    if "share" in string.lower():

        # searchs is any of the word in words list is in the email
        # and uses that to determine what class the email falls under
        out = any(word in string.lower().split(' ') for word in words)
        if out:
            output = "Student has shared"

        else:
            output =  "Student wants to know if can share"

    return output

if __name__=="__main__":
    out = classifier(input("Enter your message:"))
    print(out)
