from functions.write_file import write_file

test_cases = [
    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
]

for test_result in test_cases:
    print(test_result)