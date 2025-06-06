# 🐍 CDAC Python - Course Repository

Welcome to the **CDAC Python Course Repository**! This is your one-stop destination for notes, code examples, assignments, and collaboration for the Python module at SM Vita.

**👨‍💻 Lead/Maintainer:** Harshal More ([GitHub Profile](https://github.com/harshalmore31))

---

## 🎯 Quick Start Guide

### New to GitHub? Start Here! 👇
1. **Setup Guides**: Check [`General_Setup_and_Info/`](./General_Setup_and_Info/) for complete setup instructions
2. **Fork This Repo**: Follow the instructions below to get your own copy
3. **Submit Assignments**: Use the [`assignment_submission/`](./assignment_submission/) folder
4. **Get Help**: Read this README or ask questions!

---

## 📚 How This Repository Works

### 🔍 Repository Structure
```
cdac_python/
├── 📝 README.md (this file)
├── 📋 SUBMISSIONS.md (student submission tracker)
├── 🎒 assignment_submission/ (👈 YOUR WORK GOES HERE!)
│   ├── Python_Day_1/
│   ├── Python_Day_2/
│   └── Python_Day_X/
├── 📖 course_content/ (notes, examples, questions)
│   ├── Python_Day_1/
│   └── Python_Day_2/
├── ⚙️ General_Setup_and_Info/ (setup guides)
└── 📦 archives/ (backup materials)
```

### 🎯 What Goes Where?
- **📖 Course Content**: Notes, examples, and assignment questions
- **🎒 Assignment Submissions**: YOUR completed assignments (in your fork)
- **⚙️ Setup Guides**: How to install Python, Git, VSCode, etc.
- **📋 Submissions Tracker**: Links to everyone's forks

---

## 🚀 For Students: Getting Started

### 🔧 Phase 1: One-Time Setup

#### Step 1: Choose Your Method
- **🖱️ GitHub Desktop** (Recommended for beginners)
- **💻 Command Line** (For those comfortable with terminal)

#### Step 2: Complete Setup
📋 Follow our detailed guides in [`General_Setup_and_Info/`](./General_Setup_and_Info/):
- [🔧 Python & VSCode Setup](./General_Setup_and_Info/python_vscode_setup.md)
- [📱 Git & GitHub Setup](./General_Setup_and_Info/git_github_setup_guide.md)
- [🖱️ GitHub Desktop Guide](./General_Setup_and_Info/github_desktop_guide.md)
- [💻 Command Line Git Guide](./General_Setup_and_Info/command_line_git_guide.md)

#### Step 3: Create GitHub Account & Fork
1. **Create Account**: Sign up at [github.com](https://github.com) if you don't have one
2. **Fork This Repository**: 
   - Go to: `https://github.com/harshalmore31/cdac_python`
   - Click the "Fork" button (top-right corner)
   - This creates YOUR own copy!

#### Step 4: Clone Your Fork

**🖱️ Using GitHub Desktop (Easier)**
1. Go to YOUR forked repository: `https://github.com/YOUR_USERNAME/cdac_python`
2. Click green "Code" button → "Open with GitHub Desktop"
3. Choose location on your computer → Click "Clone"

**💻 Using Command Line**
```bash
git clone https://github.com/YOUR_USERNAME/cdac_python.git
cd cdac_python
```

---

## 📝 Daily Assignment Workflow

### Step 1: Find Today's Assignment 🔍
Navigate to: `course_content/Python_Day_X/Assignments/README.md`

### Step 2: Create Your Solution 💻
- Go to: `assignment_submission/Python_Day_X/`
- Create file: `your_name_qX.py` (e.g., `john_doe_q1.py`)
- Write your solution with comments!

### Step 3: Save Your Work 💾

**🖱️ Using GitHub Desktop**
1. Open GitHub Desktop
2. See your changes listed
3. Add commit message: "Completed Day X Assignment Q1"
4. Click "Commit to main"
5. Click "Push origin"

**💻 Using Command Line**
```bash
git add assignment_submission/Python_Day_X/your_file.py
git commit -m "Completed Day X Assignment Q1"
git push origin main
```

### Step 4: Let Everyone Know 📢
Update [`SUBMISSIONS.md`](./SUBMISSIONS.md) with link to your fork (creates a Pull Request - great practice!)

---

## 🔄 Keeping Your Fork Updated

### When I Add New Content...

**🖱️ GitHub Desktop Method**
1. Repository → Repository Settings → Remote
2. Add upstream: `https://github.com/harshalmore31/cdac_python.git`
3. Branch → Merge into current branch → Select "upstream/main"
4. Push changes

**💻 Command Line Method**
```bash
git remote add upstream https://github.com/harshalmore31/cdac_python.git
git fetch upstream
git merge upstream/main
git push origin main
```

---

## 🗂️ Repository Navigation Guide

### 📖 Course Materials
| Day | Notes | Code Examples | Assignments |
|-----|-------|---------------|-------------|
| Day 1 | [📝 Notes](./course_content/Python_Day_1/Notes/) | [💻 Code](./course_content/Python_Day_1/Code/) | [📋 Questions](./course_content/Python_Day_1/Assignments/) |
| Day 2 | [📝 Notes](./course_content/Python_Day_2/Notes/) | [💻 Code](./course_content/Python_Day_2/Code/) | [📋 Questions](./course_content/Python_Day_2/Assignments/) |

### 🎒 Your Assignment Folders
| Day | Your Submission Folder |
|-----|----------------------|
| Day 1 | [📁 Python_Day_1](./assignment_submission/Python_Day_1/) |
| Day 2 | [📁 Python_Day_2](./assignment_submission/Python_Day_2/) |

### ⚙️ Setup & Help
| Resource | Description |
|----------|-------------|
| [🔧 Setup Guides](./General_Setup_and_Info/) | Python, Git, VSCode installation |
| [📋 Submissions](./SUBMISSIONS.md) | Track everyone's progress |
| [❓ Troubleshooting](./General_Setup_and_Info/troubleshooting.md) | Common issues & solutions |

---

## 🆘 Need Help?

### 📞 Quick Help Options
- **🤔 Git/GitHub Issues**: Check our [setup guides](./General_Setup_and_Info/)
- **🐍 Python Problems**: Look at [code examples](./course_content/) or ask in class
- **💻 Technical Issues**: See [troubleshooting guide](./General_Setup_and_Info/troubleshooting.md)
- **👥 General Questions**: Ask Harshal or create an issue in this repository

### 🎯 Pro Tips
1. **🔄 Commit Often**: Save your work frequently
2. **📝 Write Comments**: Explain your code for better understanding
3. **🧪 Test Your Code**: Make sure it runs before submitting
4. **📁 Organize Files**: Use clear, descriptive filenames
5. **🤝 Help Others**: Collaboration makes everyone better!

---

**🚀 Ready to get started?** Jump to our [setup guides](./General_Setup_and_Info/) and begin your Python journey!

**❓ Questions?** Don't hesitate to ask - we're all here to learn together! 🤝