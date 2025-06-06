# 🔧 Git & GitHub Setup Guide

Welcome! This guide will help you set up Git and GitHub on your computer. Don't worry if you're new to this - we'll go step by step!

## 🎯 What You'll Learn
- ✅ What Git and GitHub are (and why they're awesome!)
- ✅ How to install Git on your computer
- ✅ How to create a GitHub account
- ✅ How to configure Git with your details
- ✅ How to verify everything is working

---

## 🤔 What are Git and GitHub?

### Git 🔧
- **What**: A tool that tracks changes in your code
- **Why**: Never lose your work, see what you changed, collaborate with others
- **Think of it as**: A super-powered "Save" button with history

### GitHub 🌐
- **What**: A website that stores your Git repositories online
- **Why**: Backup your code, share with others, collaborate on projects
- **Think of it as**: Google Drive, but for programmers

---

## 🚀 Step 1: Create GitHub Account

1. **Go to**: [github.com](https://github.com)
2. **Click**: "Sign up" (top-right corner)
3. **Choose**:
   - **Username**: Pick something professional (e.g., `john_doe`, `jane_smith`)
   - **Email**: Use your real email (you'll need to verify it)
   - **Password**: Make it strong!
4. **Verify**: Check your email and click the verification link
5. **Done**: You now have a GitHub account! 🎉

### 💡 GitHub Username Tips:
- ✅ Use your real name if possible (employers like this)
- ✅ Keep it simple and professional
- ❌ Avoid special characters or numbers if possible
- ❌ Don't use temporary email addresses

---

## 💻 Step 2: Install Git

### For Windows 🪟

1. **Download**: Go to [git-scm.com](https://git-scm.com/)
2. **Click**: "Download for Windows"
3. **Run**: The downloaded installer
4. **Installation Options** (recommended settings):
   - ✅ Git Bash Here (adds right-click option)
   - ✅ Git GUI Here
   - ✅ Git LFS (Large File Support)
   - ✅ Associate .git* configuration files
   - ✅ Associate .sh files to be run with Bash
   - Choose: "Use Git from Git Bash only" (safest option)
   - Choose: "Use the OpenSSL library"
   - Choose: "Checkout Windows-style, commit Unix-style line endings"
   - Choose: "Use MinTTY"
   - ✅ Enable file system caching
   - ✅ Enable Git Credential Manager

5. **Finish**: Complete the installation

### For Mac 🍎

**Option 1: Using Homebrew (Recommended)**
```bash
# Install Homebrew first (if you don't have it)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Git
brew install git
```

**Option 2: Download Installer**
1. Go to [git-scm.com](https://git-scm.com/)
2. Click "Download for Mac"
3. Run the installer

### For Linux 🐧

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install git
```

**CentOS/RHEL/Fedora:**
```bash
sudo yum install git
# or for newer versions:
sudo dnf install git
```

---

## ⚙️ Step 3: Configure Git

After installing Git, you need to tell it who you are:

### Open Terminal/Command Prompt
- **Windows**: Search for "Git Bash" and open it
- **Mac**: Open "Terminal" application
- **Linux**: Open your terminal

### Set Your Identity
```bash
# Set your name (use your real name)
git config --global user.name "Your Full Name"

# Set your email (use the same email as your GitHub account)
git config --global user.email "your.email@example.com"

# Set default branch name to 'main' (modern standard)
git config --global init.defaultBranch main
```

### Verify Configuration
```bash
# Check if everything is set correctly
git config --list --global

# Should show something like:
# user.name=Your Full Name
# user.email=your.email@example.com
# init.defaultbranch=main
```

---

## 🔐 Step 4: Set Up Authentication

### Option 1: HTTPS with Personal Access Token (Recommended)

1. **Go to GitHub**: [github.com](https://github.com)
2. **Navigate**: Settings → Developer settings → Personal access tokens → Tokens (classic)
3. **Create**: "Generate new token (classic)"
4. **Configure**:
   - **Note**: "CDAC Python Course"
   - **Expiration**: 90 days (or custom)
   - **Scopes**: Check "repo" (gives full repository access)
5. **Generate**: Click "Generate token"
6. **Save**: Copy the token immediately (you won't see it again!)

**When cloning/pushing**: Use your GitHub username and the token as password.

### Option 2: SSH Keys (Advanced)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Copy public key (then paste in GitHub)
cat ~/.ssh/id_ed25519.pub
```

Add the public key to GitHub: Settings → SSH and GPG keys → New SSH key

---

## ✅ Step 5: Test Your Setup

### Test Git Installation
```bash
# Check Git version
git --version

# Should output something like: git version 2.40.0
```

### Test GitHub Connection

**For HTTPS:**
```bash
# Try cloning a test repository
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
ls
```

**For SSH:**
```bash
# Test SSH connection
ssh -T git@github.com

# Should output: Hi username! You've successfully authenticated...
```

---

## 🎉 Success! What's Next?

If you've made it this far, congratulations! 🎊 You now have:
- ✅ A GitHub account
- ✅ Git installed on your computer
- ✅ Git configured with your details
- ✅ Authentication set up

### Next Steps:
1. **Go back to**: [Main README](../README.md)
2. **Fork**: The course repository
3. **Clone**: Your fork to start working
4. **Start**: Your Python journey with proper version control!

---

## 🆘 Troubleshooting

### Common Issues:

**❓ "git: command not found"**
- **Solution**: Git isn't installed or not in PATH. Reinstall Git and restart terminal.

**❓ "Permission denied (publickey)"**
- **Solution**: SSH key isn't set up correctly. Use HTTPS instead or follow SSH setup again.

**❓ "Authentication failed"**
- **Solution**: 
  - For HTTPS: Use personal access token, not your password
  - For SSH: Check if your SSH key is added to GitHub

**❓ "fatal: not a git repository"**
- **Solution**: You're not in a Git repository folder. Navigate to the right folder or clone a repository first.

### Get Help:
- **Ask**: Harshal or classmates
- **Check**: [GitHub's documentation](https://docs.github.com/)
- **Search**: Stack Overflow for specific error messages

---

**💡 Pro Tip**: Don't worry if this seems overwhelming! Git has a learning curve, but once you get it, you'll wonder how you ever coded without it!
