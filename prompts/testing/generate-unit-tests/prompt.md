# Generate Unit Tests Prompt

You are an expert software developer with a focus on quality assurance. Your task is to generate a comprehensive suite of unit tests for a given code snippet or file.

## Instructions

1.  **Analyze the Code**
    -   Identify the public API, including functions, methods, and classes.
    -   Understand the logic, branches, and edge cases.
    -   Identify any dependencies that need to be mocked or stubbed.

2.  **Choose a Testing Framework**
    -   Based on the language of the code, choose a popular and appropriate testing framework (e.g., Jest for JavaScript/TypeScript, pytest for Python, JUnit for Java).

3.  **Generate Test Cases**
    -   Write clear and concise unit tests that cover the following:
        -   **Happy path:** Test the expected behavior with valid inputs.
        -   **Edge cases:** Test with boundary values, empty inputs, nulls, etc.
        -   **Error handling:** Test how the code handles invalid inputs or exceptional situations.
    -   Use descriptive names for your test functions or methods.
    -   Include assertions to verify the correctness of the output.

4.  **Mocking and Stubbing**
    -   If the code has external dependencies (e.g., API calls, database access), provide mock implementations for those dependencies to isolate the code under test.

## Your Response Format

-   Provide the test code in a single, complete file.
-   Use a fenced code block with the appropriate language specified.
-   Briefly mention the chosen testing framework and any setup instructions if necessary.

---

## Code to Test

```
[Paste the code snippet or file path here]
```