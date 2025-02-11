def handle_error(error):
    if isinstance(error, FileNotFoundError):
        return {"error": "File not found. Please check the file path."}
    elif isinstance(error, ValueError):
        return {"error": "Invalid value provided. Please check your input."}
    elif isinstance(error, KeyError):
        return {"error": "Key not found in the data. Please verify the keys."}
    elif isinstance(error, Exception):
        return {"error": "An unexpected error occurred: " + str(error)}
    return {"error": "An unknown error occurred."}

def fallback_response():
    return "Sorry, something went wrong. Please try again later."