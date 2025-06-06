# CDAC Python - Python Assignments & Notes

Welcome! This repository contains notes, code examples, and assignment questions for the CDAC Python module at SM Vita.

**Lead/Maintainer:** Harshal More ([[Link](https://github.com/harshalmore31)])

## How This Repository Works

This repository is designed to help you learn Python and get comfortable with GitHub.

1.  **Notes & Examples:** You'll find daily notes and code examples in the `course_content/Python_Day_XX/` folders.
2.  **Assignments:** Assignment questions are in `course_content/Python_Day_XX/Assignments/README.md`.
3.  **Your Solutions:** You will **fork** this repository, add your solutions to your fork, and then inform the instructor.

## For Students: Getting Started & Submitting Assignments

Follow these steps carefully! **Choose either Method A (GitHub Desktop - Easier) or Method B (Command Line - Traditional).**

### Phase 1: One-Time Setup

#### Step 1: Create a GitHub Account
If you don't have one, sign up at [github.com](https://github.com).

#### Step 2: Fork this Repository
1. Go to the main page of *this* repository: `https://github.com/harshalmore31/cdac_python`
2. Click the "Fork" button in the top-right corner. This creates your own copy of this repository under your GitHub account.

#### Step 3: Clone Your Fork (Choose Your Method)

**Method A: Using GitHub Desktop (Recommended for Beginners)**

1. **Download and Install GitHub Desktop:**
   - Go to [desktop.github.com](https://desktop.github.com)
   - Download and install GitHub Desktop for your operating system
   - Sign in with your GitHub account

2. **Clone Your Fork:**
   - Go to *your forked repository* on GitHub (it will be `https://github.com/YOUR_USERNAME/cdac_python`)
   - Click the green "<> Code" button
   - Click "Open with GitHub Desktop"
   - Choose a location on your computer to save the project
   - Click "Clone"

**Method B: Using Command Line (Traditional Git)**

1. **Install Git:** If you don't have Git, download and install it from [git-scm.com](https://git-scm.com/).
2. **Clone Your Fork:**
   - Go to *your forked repository* on GitHub (it will be `https://github.com/YOUR_USERNAME/cdac_python`)
   - Click the green "<> Code" button
   - Copy the HTTPS or SSH URL
   - Open your terminal or Git Bash and run:
     ```bash
     git clone [URL_YOU_COPIED]
     ```
   - Navigate into the folder: `cd cdac_python`

### Phase 2: Daily Workflow for Assignments

#### Step 1: Find the Assignment
- In your local cloned folder, navigate to `course_content/Python_Day_XX/Assignments/`
- Open the `README.md` in that folder to see the assignment questions

#### Step 2: Create Your Solution File(s)
- Inside the `course_content/Python_Day_XX/Assignments/solutions/` directory, create your Python file(s) for the assignment
- *Example: `your_name_day1_q1.py`, `your_name_day1_q2.py`*

#### Step 3: Save and Push Your Work (Choose Your Method)

**Method A: Using GitHub Desktop**

1. **See Your Changes:**
   - Open GitHub Desktop
   - You'll see your new/modified files listed under "Changes"

2. **Commit Your Changes:**
   - Add a descriptive message in the "Summary" box (e.g., "Completed Day 1 Assignment Question 1")
   - Optionally add more details in the "Description" box
   - Click "Commit to main"

3. **Push to GitHub:**
   - Click "Push origin" (or "Publish branch" if it's your first push)
   - Your changes are now saved to your fork on GitHub!

**Method B: Using Command Line**

1. **Add, Commit, and Push:**
   ```bash
   # Stage your new/modified files
   git add course_content/Python_Day_XX/Assignments/solutions/your_file_name.py
   
   # Commit with a descriptive message
   git commit -m "Completed Day XX Assignment Question Y"
   
   # Push to your fork on GitHub
   git push origin main
   ```

### Phase 3: "Submitting" Your Work

#### Method 1: Update SUBMISSIONS.md (Preferred for learning)
1. In *this main repository* (`https://github.com/harshalmore31/cdac_python`), open the `SUBMISSIONS.md` file
2. Click the "pencil" icon to edit it
3. Add a new line with your Name, GitHub Username, and link to **your forked repository**:
   ```
   | Your Name | YourGitHubUsername | https://github.com/YourGitHubUsername/cdac_python |
   ```
4. Scroll down and "Propose changes". Create a Pull Request
5. I (Harshal) will merge these PRs

#### Method 2: Tell the Instructor (Simpler start)
Simply provide the URL to your forked repository (e.g., `https://github.com/YOUR_USERNAME/cdac_python`) to the instructor as requested.

## Keeping Your Fork Updated (Optional, but good practice)

If I make updates to the main repository (e.g., add new notes or fix an assignment question), you might want to get those changes into your fork.

**Using GitHub Desktop:**
1. In GitHub Desktop, go to Branch → Merge into current branch
2. Select "upstream/main" (you may need to add the upstream remote first via Repository → Repository settings → Remote)
3. Click "Merge upstream/main into main"
4. Push the changes to your fork

**Using Command Line:**
1. **Configure an "Upstream" Remote (One-time setup):**
   ```bash
   git remote add upstream https://github.com/harshalmore31/cdac_python.git
   ```
2. **Fetch and Merge Changes:**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   git push origin main
   ```

## Directory Structure Overview

-   `/course_content/Python_Day_XX/Notes/`: Daily theoretical notes.
-   `/course_content/Python_Day_XX/Code/`: Python scripts demonstrating concepts.
-   `/course_content/Python_Day_XX/Assignments/README.md`: Assignment questions.
-   `/course_content/Python_Day_XX/Assignments/solutions/`: **This is where YOU add your assignment solution files in YOUR FORK.**
-   `/General_Setup_and_Info/`: Guides for setting up Python, VSCode, Git, etc.

## Need Help?

- **GitHub Desktop Issues:** Check the [GitHub Desktop docs](https://docs.github.com/en/desktop)
- **Git Command Line Issues:** Check the [Git documentation](https://git-scm.com/doc)
- **Python Issues:** Ask in class or check our `General_Setup_and_Info/` folder
- **General Questions:** Feel free to ask Harshal or create an issue in this repository

---

**Pro Tip:** Start with GitHub Desktop if you're new to Git. Once you're comfortable, you can always learn command line Git later!

Feel free to ask questions if you get stuck!