# CDAC Python - Python Assignments & Notes

Welcome! This repository contains notes, code examples, and assignment questions for the CDAC Python module at SM Vita.

**Lead/Maintainer:** Harshal More ([[Your GitHub Profile Link](https://github.com/harshalmore31)])

## How This Repository Works

This repository is designed to help you learn Python and get comfortable with GitHub.

1.  **Notes & Examples:** You'll find daily notes and code examples in the `course_content/Day_XX/` folders.
2.  **Assignments:** Assignment questions are in `course_content/Day_XX/Assignments/README.md`.
3.  **Your Solutions:** You will **fork** this repository, add your solutions to your fork, and then inform the instructor.

## For Students: Getting Started & Submitting Assignments

Follow these steps carefully!

**Phase 1: One-Time Setup**

1.  **Install Git:** If you don't have Git, download and install it from [git-scm.com](https://git-scm.com/).
    *   *Optional: Link to a simple Git installation guide here or in `General_Setup_and_Info/`*
2.  **Create a GitHub Account:** If you don't have one, sign up at [github.com](https://github.com).
3.  **Fork this Repository:**
    *   Go to the main page of *this* repository: `https://github.com/harshalmore31/cdac_python`
    *   Click the "Fork" button in the top-right corner. This creates your own copy of this repository under your GitHub account.
4.  **Clone Your Fork:**
    *   Go to *your forked repository* on GitHub (it will be `https://github.com/YOUR_USERNAME/cdac_python`).
    *   Click the green "<> Code" button.
    *   Copy the HTTPS or SSH URL.
    *   Open your terminal or Git Bash and run:
        ```bash
        git clone [URL_YOU_COPIED]
        ```
    *   This downloads your fork to your computer. You'll now have a folder named `cdac_python`.
    *   Navigate into this folder: `cd cdac_python`

**Phase 2: Daily Workflow for Assignments**

1.  **Find the Assignment:**
    *   In your local cloned folder, navigate to `course_content/Day_XX/Assignments/`.
    *   Open the `README.md` in that folder to see the assignment questions.
2.  **Create Your Solution File(s):**
    *   Inside the `course_content/Day_XX/Assignments/solutions/` directory, create your Python file(s) for the assignment.
    *   *Example: `my_solution_day1_q1.py`*
3.  **Add, Commit, and Push Your Work (to YOUR FORK):**
    *   Open your terminal/Git Bash *inside your cloned project folder*.
    *   Run these commands:
        ```bash
        # To stage your new/modified files for commit
        git add course_content/Day_XX/Assignments/solutions/your_file_name.py
        # Or, to add everything in the solutions folder for that day:
        # git add course_content/Day_XX/Assignments/solutions/

        # To commit your changes with a descriptive message
        git commit -m "Completed Day XX Assignment Question Y"

        # To push your committed changes from your local computer to your fork on GitHub
        git push origin main  # Or your default branch name
        ```
4.  **"Submitting" Your Work (Letting the Instructor Know):**
    *   **Method 1 (Preferred for learning): Update `SUBMISSIONS.md`**
        *   In *this main repository* (`https://github.com/harshalmore31/cdac_python`), open the `SUBMISSIONS.md` file.
        *   Click the "pencil" icon to edit it.
        *   Add a new line with your Name, GitHub Username, and a link to **your forked repository**.
            ```
            | Your Name | YourGitHubUsername | https://github.com/YourGitHubUsername/cdac_python |
            ```
        *   Scroll down and "Propose changes". Create a Pull Request.
        *   I (Harshal) will merge these PRs.
    *   **Method 2 (Simpler start): Tell the Instructor**
        *   Simply provide the URL to your forked repository (e.g., `https://github.com/YOUR_USERNAME/cdac_python`) to the instructor as requested.

## Keeping Your Fork Updated (Optional, but good practice)

If I make updates to the main repository (e.g., add new notes or fix an assignment question), you might want to get those changes into your fork.

1.  **Configure an "Upstream" Remote (One-time setup in your local clone):**
    ```bash
    git remote add upstream https://github.com/harshalmore31/cdac_python.git
    ```
2.  **Fetch Changes from Upstream:**
    ```bash
    git fetch upstream
    ```
3.  **Merge Changes into Your Local Branch (e.g., main):**
    ```bash
    git checkout main # Make sure you are on your main branch
    git merge upstream/main
    ```
    *   If there are conflicts (unlikely if you only add files in `solutions/`), Git will tell you. Ask for help!
4.  **Push Updates to Your Fork on GitHub:**
    ```bash
    git push origin main
    ```

## Directory Structure Overview

-   `/course_content/Day_XX/Notes/`: Daily theoretical notes.
-   `/course_content/Day_XX/Code/`: Python scripts demonstrating concepts.
-   `/course_content/Day_XX/Assignments/README.md`: Assignment questions.
-   `/course_content/Day_XX/Assignments/solutions/`: **This is where YOU add your assignment solution files in YOUR FORK.**
-   `/General_Setup_and_Info/`: Guides for setting up Python, VSCode, Git, etc.

---

Feel free to ask questions if you get stuck!