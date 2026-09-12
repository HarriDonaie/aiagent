from functions.get_file_content import get_file_content
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

test_cases = [
    get_file_content("calculator", "main.py"),
    get_file_content("calculator", "pkg/calculator.py"),
    get_file_content("calculator", "/bin/cat"),
    get_file_content("calculator", "pkg/does_not_exist.py")
]

for test_result in test_cases:
    print(test_result)