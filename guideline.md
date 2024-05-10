# Guideline how to implement solution for Python tasks

## Prepare the project

1. Clone the repo
   ```
   git clone the-link-to-repo
   ```
2. Open the project folder in your IDE
3. Open a terminal in the project folder
4. Create a branch for the solution and switch on it
   ```
   git checkout -b develop
   ```
   - You can use any other name instead of `develop`
5. If you are using PyCharm - it may propose you to automatically create venv for your project
   and install requirements in it, but if not:
   ```
   python -m venv venv
   venv\Scripts\activate (on Windows)
   source venv/bin/activate (on macOS)
   pip install -r requirements.txt
   ```

## Implement the solution

1. Implement the solution within a function in `app/main.py`

2. Run `pytest` to check if your solution is correct (from command line, or using PyCharm `pytest` support)
   - If at least one test fails fix the solution and check again.
3. Run `flake8` to see if your code follows the [flake8 rules](https://www.flake8rules.com/)
   - If you see some errors fix them and check again
4. Save the solution
   ```
   git commit -am 'Solution'
   ```
5. Push the solution to the repo
   ```
   git push origin develop
   ```
   - If you created another branch (not `develop`) use its name instead

## Create a Pull Request (PR)

1. Open your repo on GitHub and create a `Pull Request` (PR)

2. Select your branch in the dropdown!

3. Verify the PR details and code (scroll down to see it) and confirm
