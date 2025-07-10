# 🔑 Quick Guide: Getting PyPI API Tokens

## Step 1: Get PyPI API Token

### For Production PyPI (pypi.org):
1. **Go to**: [https://pypi.org/manage/account/](https://pypi.org/manage/account/)
2. **Sign in** to your PyPI account
3. **Scroll down** to "API tokens" section
4. **Click "Add API token"**
5. **Fill in**:
   - Token name: `gh-feed-github-actions`
   - Scope: `Entire account` (or specific project if you prefer)
6. **Click "Add token"**
7. **Copy the token** - it starts with `pypi-` and looks like:
   ```
   pypi-AgEIcHlwaS5vcmc...
   ```
8. **⚠️ IMPORTANT**: Save this token safely - you won't see it again!

### For Test PyPI (test.pypi.org):
1. **Go to**: [https://test.pypi.org/manage/account/](https://test.pypi.org/manage/account/)
2. **Sign in** or create an account
3. **Follow the same steps** as above
4. **Token name**: `gh-feed-test-github-actions`

## Step 2: Add Tokens to GitHub

### Navigate to Repository Settings:
1. **Go to**: [https://github.com/bhantsi/gh-feed/settings/secrets/actions](https://github.com/bhantsi/gh-feed/settings/secrets/actions)
2. **Click "New repository secret"**

### Add PyPI Token:
1. **Name**: `PYPI_API_TOKEN`
2. **Value**: Paste your PyPI token (the one starting with `pypi-`)
3. **Click "Add secret"**

### Add Test PyPI Token:
1. **Click "New repository secret"** again
2. **Name**: `TEST_PYPI_API_TOKEN`
3. **Value**: Paste your Test PyPI token
4. **Click "Add secret"**

## Step 3: Verify Setup

After adding the secrets, you should see them listed in your repository secrets (values will be hidden):
- ✅ `PYPI_API_TOKEN`
- ✅ `TEST_PYPI_API_TOKEN`

## Step 4: Test Deployment

### Option 1: Manual Test (Test PyPI)
1. **Go to**: [https://github.com/bhantsi/gh-feed/actions](https://github.com/bhantsi/gh-feed/actions)
2. **Click "Deploy to PyPI"** workflow
3. **Click "Run workflow"**
4. **Select branch**: `main`
5. **Click "Run workflow"**

### Option 2: Automatic Deployment (Production)
```bash
# In your terminal, in the gh-feed directory:
python scripts/bump_version.py patch  # This creates a tag
git push origin v0.1.4                # This triggers deployment
```

## ⚠️ Important Notes

1. **Never commit** API tokens to your repository
2. **Keep tokens secure** - treat them like passwords
3. **The lint errors** in VS Code will disappear once you add the secrets
4. **Test with Test PyPI first** before deploying to production PyPI

## 🔧 Troubleshooting

If you still get errors:
1. **Check token format**: Should start with `pypi-`
2. **Verify token scope**: Should have upload permissions
3. **Check secret names**: Must match exactly (`PYPI_API_TOKEN`, `TEST_PYPI_API_TOKEN`)
4. **Wait a few minutes**: Sometimes GitHub takes time to propagate secrets

---

Once you add these secrets, your GitHub Actions workflow will work perfectly! 🚀
