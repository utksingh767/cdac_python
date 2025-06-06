# 🆘 Troubleshooting Guide

Don't panic! This guide will help you solve common issues you might encounter during the course. Remember: every developer faces these problems - you're not alone!

## 🎯 Quick Problem Finder

**Click on your issue to jump to the solution:**

### 🐍 Python Issues
- [Python command not found](#python-command-not-found)
- [Import errors](#import-errors)
- [Indentation errors](#indentation-errors)
- [Package installation issues](#package-installation-issues)

### 💻 VSCode Issues
- [VSCode not recognizing Python](#vscode-not-recognizing-python)
- [Extensions not working](#extensions-not-working)
- [IntelliSense not working](#intellisense-not-working)
- [Terminal not opening](#terminal-not-opening)

### 🔧 Git/GitHub Issues
- [Git command not found](#git-command-not-found)
- [Authentication problems](#authentication-problems)
- [Permission denied errors](#permission-denied-errors)
- [Merge conflicts](#merge-conflicts)
- [Push rejected](#push-rejected)

### 🖱️ GitHub Desktop Issues
- [Repository not found](#repository-not-found-desktop)
- [Changes not showing](#changes-not-showing)
- [Sync issues](#sync-issues)

---

## 🐍 Python Issues

### Python command not found

**Problem**: When you type `python --version`, you get "command not found" or similar error.

**Solutions**:

#### Windows 🪟
1. **Check if Python is installed**:
   - Try `py --version` instead of `python --version`
   - Try `python3 --version`

2. **Reinstall Python**:
   - Download from [python.org](https://python.org)
   - **IMPORTANT**: Check "Add Python to PATH" during installation
   - Restart your computer after installation

3. **Manual PATH fix**:
   - Open System Properties → Environment Variables
   - Add Python installation directory to PATH
   - Usually: `C:\Users\YourName\AppData\Local\Programs\Python\Python311\`

#### Mac 🍎
1. **Use python3**:
   ```bash
   python3 --version
   pip3 --version
   ```

2. **Install via Homebrew**:
   ```bash
   brew install python
   ```

#### Linux 🐧
1. **Install Python**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Create alias** (add to ~/.bashrc):
   ```bash
   alias python=python3
   alias pip=pip3
   ```

### Import errors

**Problem**: `ModuleNotFoundError: No module named 'some_module'`

**Solutions**:

1. **Install missing package**:
   ```bash
   pip install package_name
   # or
   pip3 install package_name
   ```

2. **Check Python environment**:
   - Make sure you're using the same Python that has the packages installed
   - In VSCode: `Ctrl+Shift+P` → "Python: Select Interpreter"

3. **Virtual environment issues**:
   ```bash
   # Create virtual environment
   python -m venv myenv
   
   # Activate it
   # Windows:
   myenv\Scripts\activate
   # Mac/Linux:
   source myenv/bin/activate
   
   # Install packages
   pip install package_name
   ```

### Indentation errors

**Problem**: `IndentationError: expected an indented block`

**Solutions**:

1. **Use consistent indentation**:
   - Python uses 4 spaces per indentation level
   - Don't mix tabs and spaces
   - Configure VSCode to show whitespace: View → Render Whitespace

2. **Fix in VSCode**:
   - Select all code: `Ctrl+A`
   - Format document: `Shift+Alt+F`
   - Or right-click → Format Document

3. **Check your code structure**:
   ```python
   # ❌ Wrong:
   if True:
   print("Hello")  # Missing indentation
   
   # ✅ Correct:
   if True:
       print("Hello")  # 4 spaces indentation
   ```

### Package installation issues

**Problem**: `pip install` fails or packages don't install

**Solutions**:

1. **Update pip**:
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Use correct pip**:
   ```bash
   # Make sure you're using the right pip
   python -m pip install package_name
   ```

3. **Permission issues**:
   ```bash
   # Install for current user only
   pip install --user package_name
   ```

4. **Network issues**:
   ```bash
   # Use different index
   pip install -i https://pypi.org/simple/ package_name
   ```

---

## 💻 VSCode Issues

### VSCode not recognizing Python

**Problem**: VSCode doesn't run Python code or shows "Python not found"

**Solutions**:

1. **Select Python interpreter**:
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose your Python installation

2. **Check PATH**:
   - Open VSCode terminal: `Ctrl+` `
   - Type `python --version`
   - If it doesn't work, fix your PATH (see Python section above)

3. **Reinstall Python extension**:
   - Go to Extensions (`Ctrl+Shift+X`)
   - Uninstall Python extension
   - Restart VSCode
   - Reinstall Python extension

### Extensions not working

**Problem**: VSCode extensions don't seem to be working

**Solutions**:

1. **Restart VSCode**: Sometimes extensions need a restart to work properly

2. **Check extension status**:
   - Go to Extensions (`Ctrl+Shift+X`)
   - Look for any error messages
   - Try disabling and re-enabling problematic extensions

3. **Update extensions**:
   - Click on Extensions
   - Look for "Update" buttons
   - Update all extensions

4. **Clear extension cache**:
   - Close VSCode
   - Delete the extensions folder:
     - Windows: `%USERPROFILE%\.vscode\extensions`
     - Mac: `~/.vscode/extensions`
     - Linux: `~/.vscode/extensions`
   - Restart VSCode and reinstall extensions

### IntelliSense not working

**Problem**: No auto-completion or code suggestions

**Solutions**:

1. **Check Python interpreter**: Make sure correct interpreter is selected

2. **Install Pylance**: Make sure Pylance extension is installed and enabled

3. **Restart language server**:
   - `Ctrl+Shift+P` → "Python: Restart Language Server"

4. **Check file association**:
   - Make sure your file has `.py` extension
   - Check bottom-right corner of VSCode shows "Python"

### Terminal not opening

**Problem**: Integrated terminal doesn't open or shows errors

**Solutions**:

1. **Try different terminal**:
   - `Ctrl+Shift+P` → "Terminal: Select Default Profile"
   - Choose Command Prompt, PowerShell, or Git Bash

2. **Reset terminal**:
   - Close all terminal tabs
   - `Ctrl+Shift+P` → "Terminal: Kill All Terminals"
   - Open new terminal: `Ctrl+` `

3. **Check terminal settings**:
   - File → Preferences → Settings
   - Search "terminal integrated shell"
   - Make sure path is correct

---

## 🔧 Git/GitHub Issues

### Git command not found

**Problem**: `git --version` shows "command not found"

**Solutions**:

1. **Install Git**:
   - Windows: Download from [git-scm.com](https://git-scm.com)
   - Mac: `brew install git` or download installer
   - Linux: `sudo apt install git`

2. **Restart terminal/computer** after installation

3. **Check PATH**: Make sure Git is in your system PATH

### Authentication problems

**Problem**: "Authentication failed" when pushing to GitHub

**Solutions**:

1. **Use Personal Access Token**:
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Use username + token (not password) when prompted

2. **Set up SSH keys** (alternative):
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   # Add public key to GitHub
   ```

3. **Clear stored credentials**:
   - Windows: Control Panel → Credential Manager → Remove GitHub entries
   - Mac: Keychain Access → Remove GitHub entries
   - Linux: `git config --global --unset credential.helper`

### Permission denied errors

**Problem**: "Permission denied (publickey)" when accessing GitHub

**Solutions**:

1. **Use HTTPS instead of SSH**:
   ```bash
   git remote set-url origin https://github.com/username/repository.git
   ```

2. **Fix SSH keys**:
   ```bash
   # Test SSH connection
   ssh -T git@github.com
   
   # If it fails, regenerate SSH key
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```

3. **Check SSH agent**:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

### Merge conflicts

**Problem**: Git says there are conflicts when merging

**Solutions**:

1. **In VSCode**:
   - Open conflicted files
   - Look for `<<<<<<<`, `=======`, `>>>>>>>` markers
   - Choose which version to keep
   - Remove conflict markers
   - Save and commit

2. **Using Git commands**:
   ```bash
   # See conflicted files
   git status
   
   # Edit files manually
   # Then mark as resolved
   git add filename
   git commit
   ```

3. **Abort merge** (if you want to start over):
   ```bash
   git merge --abort
   ```

### Push rejected

**Problem**: "Updates were rejected because the remote contains work..."

**Solutions**:

1. **Pull first, then push**:
   ```bash
   git pull origin main
   git push origin main
   ```

2. **If you're sure your changes are correct**:
   ```bash
   git push --force-with-lease origin main
   ```
   ⚠️ **Warning**: Only use force push on your own fork!

---

## 🖱️ GitHub Desktop Issues

### Repository not found (Desktop)

**Problem**: Can't find your repository in GitHub Desktop

**Solutions**:

1. **Make sure you forked first**: 
   - Go to the original repository on GitHub
   - Click "Fork" button
   - Then clone YOUR fork, not the original

2. **Refresh repository list**:
   - File → Clone repository
   - Click refresh button
   - Look for your username/repository

3. **Clone manually**:
   - Get the URL from your GitHub fork
   - File → Clone repository → URL tab
   - Paste the URL

### Changes not showing

**Problem**: Made changes but GitHub Desktop doesn't show them

**Solutions**:

1. **Check you're in the right repository**:
   - Look at "Current Repository" dropdown
   - Make sure it's your fork

2. **Refresh**: Press `F5` or restart GitHub Desktop

3. **Check file location**: Make sure you saved files in the right directory

4. **File permissions**: Make sure files aren't read-only

### Sync issues

**Problem**: Can't sync with upstream repository

**Solutions**:

1. **Add upstream remote**:
   - Repository → Repository settings
   - Remote → Add
   - Name: upstream
   - URL: `https://github.com/harshalmore31/cdac_python.git`

2. **Fetch and merge**:
   - Branch → Merge into current branch
   - Select "upstream/main"

3. **Manual sync**:
   - Go to your fork on GitHub.com
   - Click "Sync fork" button

---

## 🎯 General Problem-Solving Strategy

### 1. Read the Error Message 📖
- Error messages usually tell you exactly what's wrong
- Copy the exact error message for searching online

### 2. Check the Basics ✅
- Is your file saved?
- Are you in the right directory?
- Is your internet connection working?
- Did you restart after installing software?

### 3. Search Online 🔍
- Copy the error message and search on Google
- Stack Overflow is your friend
- Look for recent answers (tools update frequently)

### 4. Ask for Help 🤝
- Ask Harshal or classmates
- Create an issue in the repository
- Include:
  - What you were trying to do
  - Exact error message
  - Your operating system
  - Screenshots if helpful

### 5. Document Your Solution 📝
- When you solve a problem, write down what worked
- Share solutions with classmates
- You might face the same issue again later

---

## 🆘 When All Else Fails

### Emergency Reset Procedures:

#### Nuclear Option 1: Fresh Git Clone
```bash
# Backup your work first!
# Then delete local repository and clone again
git clone https://github.com/YOUR_USERNAME/cdac_python.git
```

#### Nuclear Option 2: Fresh Python Installation
1. Uninstall Python completely
2. Delete all Python folders
3. Restart computer
4. Install Python fresh from python.org
5. Don't forget to check "Add to PATH"!

#### Nuclear Option 3: Fresh VSCode Setup
1. Backup your settings (if you want)
2. Uninstall VSCode
3. Delete VSCode folders:
   - Windows: `%APPDATA%\Code`
   - Mac: `~/Library/Application Support/Code`
   - Linux: `~/.config/Code`
4. Install VSCode fresh
5. Reinstall extensions

---

## 🎉 Remember

- **Every developer faces these issues** - you're not alone!
- **Google is your friend** - most problems have been solved before
- **Don't be afraid to ask** - your classmates probably face similar issues
- **Take breaks** - sometimes stepping away helps you see the solution
- **Document what works** - help your future self and others

**💪 You've got this!** These are just temporary roadblocks on your coding journey! 