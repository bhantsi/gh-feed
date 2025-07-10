# 🚀 gh-feed v0.1.3 Release Notes

## What's New in v0.1.3

This release prepares the project for production PyPI publication with improved package standards, better user experience, and enhanced reliability.

### ✨ New Features

#### 📦 PyPI Production Ready
- **Production packaging**: Optimized for main PyPI publication
- **Smart update checking**: Intelligent fallback between PyPI and TestPyPI
- **Professional metadata**: Proper repository URLs and package information

#### 💾 Improved Cache Management
- **User cache directory**: Cache now stored in `~/.cache/gh-feed/` (standard location)
- **Cross-platform compatibility**: Works properly on all operating systems
- **Better permissions**: Respects user cache directory standards

#### 🔄 Enhanced Update System
- **Dual repository support**: Checks both PyPI and TestPyPI automatically
- **Fallback mechanism**: Graceful fallback if one repository is unavailable
- **Better error handling**: Improved resilience for network issues

### 🐛 Bug Fixes

#### Version Consistency
- **Fixed version mismatches**: All files now have consistent version numbers
- **Updated installation docs**: Corrected version references in README
- **Proper package metadata**: Fixed repository URLs in pyproject.toml

#### Cache Location Issues
- **Moved cache directory**: From project directory to proper user cache location
- **Fixed permissions**: No more cache files cluttering project directories
- **Better cleanup**: Cache management follows system standards

### 🎨 Enhancements

#### Package Quality
- **Professional standards**: Meets PyPI publication requirements
- **Better documentation**: Updated installation instructions for both PyPI and TestPyPI
- **Improved metadata**: Proper homepage and repository links

#### User Experience
- **Cleaner project structure**: No more cache files in working directories
- **Better installation options**: Clear instructions for production vs testing
- **Enhanced reliability**: More robust update checking mechanism

## 📦 Installation & Upgrade

### From PyPI (Production)
```bash
pip install gh-feed
```

### From TestPyPI (Testing)
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps gh-feed==0.1.3
```

### Upgrade Existing Installation
```bash
pip install --upgrade gh-feed
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
# Output: gh-feed version 0.1.3
```

### Get Help
```bash
gh-feed --help
# Shows comprehensive usage guide
```

### Normal Usage (with automatic update check)
```bash
gh-feed octocat
# Checks for updates from PyPI/TestPyPI and shows activity
```

## 🧪 What's Tested

- ✅ All existing functionality preserved from v0.1.2
- ✅ New cache directory location working correctly
- ✅ Update checking works with both PyPI and TestPyPI
- ✅ Version consistency across all components
- ✅ Package builds successfully for PyPI
- ✅ Installation works from both repositories
- ✅ Backward compatibility maintained

## 📊 Migration Notes

### Cache Directory Migration
Users upgrading from previous versions will notice:
- Old cache location: `.gh_feed_cache/` (in current directory)
- New cache location: `~/.cache/gh-feed/` (in user cache directory)
- **No action needed**: Old cache will be ignored, new cache created automatically

### Update Checking
- Now checks PyPI first for updates, then falls back to TestPyPI
- Works regardless of which repository the package is installed from
- More reliable and faster update detection

## 🔗 Links

- **Package (PyPI)**: https://pypi.org/project/gh-feed/
- **Package (TestPyPI)**: https://test.pypi.org/project/gh-feed/0.1.3/
- **Source Code**: https://github.com/bhantsi/gh-feed
- **Issues**: https://github.com/bhantsi/gh-feed/issues
- **Documentation**: https://github.com/bhantsi/gh-feed#readme

## 🏗️ Technical Improvements

### Package Structure
- Fixed repository URLs in package metadata
- Proper homepage pointing to GitHub repository
- Enhanced classifiers for better discoverability

### Code Quality
- Improved error handling in update checking
- Better fallback mechanisms for API calls
- More robust cache directory management

### Documentation
- Updated README with PyPI installation instructions
- Clear distinction between production and testing installations
- Comprehensive feature documentation

## 🙏 Acknowledgments

Thanks to the Python packaging community for the excellent tooling that makes distribution seamless, and to all users who provided feedback to improve the package quality.

---

**Full Changelog**: https://github.com/bhantsi/gh-feed/compare/v0.1.2...v0.1.3
