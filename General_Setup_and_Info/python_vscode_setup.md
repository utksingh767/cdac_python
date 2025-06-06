# 🐍 Python & VSCode Setup Guide

Welcome to your Python development setup guide! By the end of this, you'll have a professional Python development environment.

## 🎯 What You'll Get
- ✅ Python installed and working on your computer
- ✅ VSCode (Visual Studio Code) as your code editor
- ✅ Essential VSCode extensions for Python
- ✅ A test Python program to verify everything works
- ✅ Tips for an efficient coding workflow

---

## 🐍 Step 1: Install Python

### Check If Python Is Already Installed

Open your terminal/command prompt and type:
```bash
python --version
# or
python3 --version
```

If you see something like `Python 3.11.0`, you might already have Python! Skip to Step 2.

### Download and Install Python

1. **Go to**: [python.org/downloads](https://www.python.org/downloads/)
2. **Download**: The latest version (should be Python 3.11+ or newer)
3. **IMPORTANT**: During installation, check "Add Python to PATH" ✅

### Installation by Operating System:

#### Windows 🪟
1. Download from python.org
2. Run the installer
3. **✅ CHECK**: "Add python.exe to PATH" (very important!)
4. Click "Install Now"
5. **Verify**: Open Command Prompt and type `python --version`

#### Mac 🍎
**Option 1: From python.org (Recommended)**
1. Download from python.org
2. Run the installer package
3. Follow installation wizard

**Option 2: Using Homebrew**
```bash
# Install Homebrew first (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

#### Linux 🐧
Most Linux distributions come with Python. If not:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**CentOS/RHEL/Fedora:**
```bash
sudo dnf install python3 python3-pip
```

---

## 💻 Step 2: Install VSCode

### Download VSCode
1. **Go to**: [code.visualstudio.com](https://code.visualstudio.com/)
2. **Download**: Click the big download button for your OS
3. **Install**: Run the installer with default settings

### First Time Setup
1. **Open**: VSCode
2. **Skip**: The welcome tutorial for now (you can always come back)
3. **Theme**: Choose your preferred theme (Dark+ is popular with developers)

---

## 🔧 Step 3: Install Essential Extensions

Extensions make VSCode super powerful for Python development!

### Method 1: Using VSCode Interface
1. **Open VSCode**
2. **Click**: Extensions icon (left sidebar) or press `Ctrl+Shift+X`
3. **Search and Install** these extensions:

#### Essential Extensions:
- **Python** (by Microsoft) - Main Python support
- **Pylance** (by Microsoft) - Advanced Python language server
- **Python Debugger** (by Microsoft) - Debugging support

#### Recommended Extensions:
- **indent-rainbow** - Makes indentation visible (helpful for Python!)
- **Bracket Pair Colorizer** - Colors matching brackets
- **GitLens** - Enhanced Git capabilities
- **Better Comments** - Improved comment formatting
- **Error Lens** - Shows errors inline
- **Material Icon Theme** - Better file icons

### Method 2: Quick Install (Copy-Paste)
Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac), type "Extensions: Install Extensions" and paste these one by one:
```
ms-python.python
ms-python.vscode-pylance
ms-python.debugpy
oderwat.indent-rainbow
aaron-bond.better-comments
eamodio.gitlens
```

---

## ⚙️ Step 4: Configure VSCode for Python

### Set Python Interpreter
1. **Open VSCode**
2. **Press**: `Ctrl+Shift+P` (Command Palette)
3. **Type**: "Python: Select Interpreter"
4. **Choose**: The Python version you installed (usually shows the path)

### Configure Settings
Press `Ctrl+,` to open settings, then search for and configure:

#### Recommended Settings:
```json
{
    "python.defaultInterpreterPath": "python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.autopep8Path": "autopep8",
    "python.autoComplete.addBrackets": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "editor.fontSize": 14,
    "editor.minimap.enabled": true,
    "editor.wordWrap": "on"
}
```

---

## 🧪 Step 5: Test Your Setup

### Create a Test Project
1. **Create folder**: Make a new folder called `python_test` on your desktop
2. **Open in VSCode**: File → Open Folder → Select your `python_test` folder
3. **Create file**: Right-click in Explorer → New File → `hello.py`

### Write Test Code
Add this code to `hello.py`:
```python
# This is a test Python program
def greet(name):
    """
    This function greets a person
    """
    print(f"Hello, {name}! Welcome to Python programming!")
    print(f"Python is working correctly on your system! 🐍")

def main():
    # Test basic Python features
    print("=" * 50)
    print("🐍 PYTHON SETUP TEST 🐍")
    print("=" * 50)
    
    # Variables and data types
    name = "Python Programmer"
    version = 3.11
    is_awesome = True
    
    # Function call
    greet(name)
    
    # List and loop
    languages = ["Python", "JavaScript", "Java", "C++"]
    print(f"\nPopular programming languages:")
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang}")
    
    # Dictionary
    info = {
        "language": "Python",
        "version": version,
        "awesome": is_awesome
    }
    
    print(f"\nCurrent info: {info}")
    
    # Mathematical operations
    result = 2 ** 10
    print(f"\n2^10 = {result}")
    
    print("\n✅ If you can see this, Python is working perfectly!")
    print("🎉 You're ready to start coding!")

if __name__ == "__main__":
    main()
```

### Run Your Test
1. **In VSCode**: Press `F5` or `Ctrl+F5` to run
2. **Or use terminal**: Open terminal in VSCode (`Ctrl+` `) and type:
   ```bash
   python hello.py
   ```

### Expected Output
If everything works, you should see:
```
==================================================
🐍 PYTHON SETUP TEST 🐍
==================================================
Hello, Python Programmer! Welcome to Python programming!
Python is working correctly on your system! 🐍

Popular programming languages:
1. Python
2. JavaScript
3. Java
4. C++

Current info: {'language': 'Python', 'version': 3.11, 'awesome': True}

2^10 = 1024

✅ If you can see this, Python is working perfectly!
🎉 You're ready to start coding!
```

---

## 💡 VSCode Tips for Python Development

### Essential Keyboard Shortcuts:
- `Ctrl+F5`: Run without debugging
- `F5`: Run with debugging
- `Ctrl+Shift+P`: Command Palette (your best friend!)
- `Ctrl+` `: Toggle terminal
- `Ctrl+/`: Comment/uncomment line
- `Alt+Up/Down`: Move line up/down
- `Ctrl+D`: Select next occurrence of word
- `F12`: Go to definition

### Useful Features:
1. **IntelliSense**: Auto-completion as you type
2. **Error Squiggles**: Red underlines show errors
3. **Debugger**: Set breakpoints by clicking line numbers
4. **Integrated Terminal**: Run Python directly in VSCode
5. **Git Integration**: Built-in version control

### Python-Specific Features:
1. **Linting**: Automatic code quality checks
2. **Formatting**: Auto-format code on save
3. **Testing**: Run unit tests directly in VSCode
4. **Debugging**: Step through code line by line

---

## 📦 Bonus: Package Management with pip

Python comes with `pip` (Python Package Installer). Test it:

```bash
# Check pip version
pip --version

# Install a useful package
pip install requests

# List installed packages
pip list

# Create requirements file (for sharing dependencies)
pip freeze > requirements.txt
```

---

## 🎉 Congratulations!

You now have a professional Python development environment! 🎊

### What you've achieved:
- ✅ Python installed and working
- ✅ VSCode configured for Python development
- ✅ Essential extensions installed
- ✅ Test program running successfully
- ✅ Ready for the CDAC Python course!

### Next Steps:
1. **Return to**: [Main README](../README.md)
2. **Set up**: Git and GitHub
3. **Fork**: The course repository
4. **Start**: Your coding journey!

---

## 🆘 Troubleshooting

### Common Issues:

**❓ "python: command not found"**
- **Windows**: Python wasn't added to PATH during installation. Reinstall and check "Add to PATH"
- **Mac/Linux**: Try `python3` instead of `python`

**❓ "VSCode doesn't recognize Python"**
- **Solution**: Press `Ctrl+Shift+P` → "Python: Select Interpreter" → Choose your Python installation

**❓ "Extensions not working"**
- **Solution**: Restart VSCode after installing extensions

**❓ "Import errors in VSCode"**
- **Solution**: Make sure you've selected the correct Python interpreter

**❓ "Code runs in terminal but not in VSCode"**
- **Solution**: Check your Python interpreter setting in VSCode

### Get Help:
- **Ask**: Harshal or classmates
- **Check**: [VSCode Python documentation](https://code.visualstudio.com/docs/python/python-tutorial)
- **Search**: Stack Overflow for specific issues

---

**🚀 Happy Coding!** You're now equipped with industry-standard tools used by professional developers worldwide! 