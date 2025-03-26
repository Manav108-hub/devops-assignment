import requests

# Define test cases
testcases = [
    ("http://127.0.0.1:8000/add/10/5", 15, "Test addition of 10 and 5"),
    ("http://127.0.0.1:8000/subtract/10/5", 5, "Test subtraction of 10 and 5"),
    ("http://127.0.0.1:8000/multiply/10/5", 50, "Test multiplication of 10 and 5"),
    ("http://127.0.0.1:8000/add/-3/3", 0, "Test addition of -3 and 3"),
    ("http://127.0.0.1:8000/multiply/0/5", 0, "Test multiplication by zero"),
]

def test_api():
    """
    Runs automated tests on API endpoints.
    Asserts that the API response matches the expected result.
    """
    for url, expected, description in testcases:
        response = requests.get(url)
        result = response.json()["result"]
        
        assert result == expected, f"{description} FAILED! Expected {expected}, got {result}"
        print(f"{description} PASSED ✅")

# Run the test function
if __name__ == "__main__":
    test_api()
