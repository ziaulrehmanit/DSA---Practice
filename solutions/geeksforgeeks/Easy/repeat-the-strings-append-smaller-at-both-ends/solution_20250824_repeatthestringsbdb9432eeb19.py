# Function to join given strings
def combo_string(a, b):
    if len(a)<len(b):
        short=a
        longer=b
    else:
        short=b
        longer=a

    return short + longer + short
