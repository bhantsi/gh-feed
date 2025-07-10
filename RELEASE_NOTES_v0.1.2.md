# 🚀 gh-feed v0.1.2 Release Notes

## What's New in v0.1.2

This release focuses on improving user experience with better help documentation, version management, and automatic update notifications.

### ✨ New Features

#### 📖 Comprehensive Help System
- **`--help` / `-h`**: Added detailed help command with usage examples, options, and supported event types
- **Enhanced documentation**: Complete guide for all available commands and flags
- **Examples included**: Real-world usage examples in help output

#### 🏷️ Version Management  
- **`--version` / `-v`**: Check current installed version instantly
- **Version display**: Clear version information for debugging and support

#### 🔔 Automatic Update Notifications
- **Smart update checking**: Automatically checks PyPI for newer versions
- **Non-intrusive notifications**: Shows update availability without interrupting workflow
- **Easy upgrade instructions**: Provides exact command to upgrade (`pip install --upgrade gh-feed`)
- **Offline resilient**: Silently fails if no internet connection available

### 🐛 Bug Fixes

#### Interactive Mode Improvements
- **Fixed empty username handling**: No longer allows proceeding with empty username
- **Better exit mechanism**: Press ENTER without input to exit gracefully
- **Improved user guidance**: Clear instructions for exiting interactive mode

#### Package Installation Issues
- **Fixed help command**: `--help` now works correctly with installed package (previously showed "User '--help' not found")
- **Proper argument parsing**: Fixed argument precedence to check help/version flags before username processing

### 🎨 Enhancements

#### User Experience
- **Better error messages**: More helpful error descriptions
- **Improved validation**: Better input validation throughout the application  
- **Enhanced feedback**: Clearer status messages and notifications

#### Documentation
- **Updated README**: Comprehensive feature list and usage examples
- **Complete help text**: Detailed in-app documentation
- **Installation guide**: Updated installation instructions

## 📦 Installation & Upgrade

### New Installation
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps gh-feed==0.1.2
```

### Upgrade from Previous Version
```bash
pip install --upgrade --index-url https://test.pypi.org/simple/ gh-feed
```

### From Source
```bash
git clone https://github.com/bhantsi/gh-feed.git
cd gh-feed
pip install .
```

## 🔧 Usage Examples

### Check Version
```bash
gh-feed --version
# Output: gh-feed version 0.1.2
```

### Get Help
```bash
gh-feed --help
# Shows comprehensive usage guide
```

### Get User Activity with Update Check
```bash
gh-feed octocat
# Automatically checks for updates and shows activity
```

## 🧪 What's Tested

- ✅ All existing functionality preserved
- ✅ Help command works in both direct script and installed package
- ✅ Version command functionality
- ✅ Update checking mechanism
- ✅ Interactive mode improvements
- ✅ Backward compatibility maintained

## 🔗 Links

- **Package**: https://test.pypi.org/project/gh-feed/0.1.2/
- **Source Code**: https://github.com/bhantsi/gh-feed
- **Issues**: https://github.com/bhantsi/gh-feed/issues
- **Documentation**: https://github.com/bhantsi/gh-feed#readme

## 🙏 Acknowledgments

Thanks to the Python packaging community and PyPI for making distribution easy, and to GitHub for providing the excellent API that powers this tool.

---

**Full Changelog**: https://github.com/bhantsi/gh-feed/compare/v0.1.1...v0.1.2
