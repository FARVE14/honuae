# 📊 Website Load Monitor

This repository runs **automated website load-time tests** and generates performance reports via **Python and GitHub Actions**.

Each run:
- Loads a list of websites multiple times
- Measures page load time per attempt
- Generates a performance graph
- Sends an **email report** with:
  - Mean, max, and min load times
  - Graph of load times

> 💡 This workflow runs **daily at 5:00 AM UTC** or can be triggered manually.

---

## 🚀 Features

- ✅ Measures website load time using headless Chrome
- 📈 Generates line chart of load time per attempt
- 📧 Emails performance reports with graph attached
- 🔁 Automated via GitHub Actions (`cron` + manual dispatch)
- 🔐 Secrets-based secure email configuration

---

## 📬 Example Email

**Subject:**
```
📊 Automated Generated Mail - Load Time Report
```

**Body:**
```
The website https://openai.com was tested 5 times.
Mean Load Time: 2.32s
Min Load Time: 1.87s
Max Load Time: 2.94s

This report was automatically generated using GitHub Actions.
🔗 https://github.com/FARVE14/website-load-monitor
```

**Attachment:** `load_times_openai_com.png`

---

## ⚙️ Setup Instructions

### 1. 📦 Add GitHub Secrets

Go to: `Repo > Settings > Secrets and variables > Actions`  
Add:

| Name         | Description                         |
|--------------|-------------------------------------|
| `EMAIL_USER` | Email address used to send reports  |
| `EMAIL_PASS` | App password or email password      |

---

### 2. 🛠️ Configure URLs and Attempts

Edit `.github/workflows/test.yaml`:

```yaml
strategy:
  matrix:
    site: ["https://openai.com", "https://example.com"]
    attempts: [5]
```

Set number of load attempts and list of sites. Each combination will be tested separately.

---

### 3. 👥 Set Recipients

Edit in `env:` section of the workflow file:

```yaml
RECIPIENT_EMAIL: "you@example.com,team@example.com"
```

---

## 🧪 Technologies Used

- Python
- Selenium + Headless Chrome
- Matplotlib
- GitHub Actions
- SMTP (email)

---

## 🕒 Scheduled Execution

This workflow is scheduled to run **daily at 5:00 AM UTC**:

```yaml
on:
  schedule:
    - cron: '0 5 * * *'
```

Manual runs are also supported via the GitHub Actions UI.

---

## 📂 Repository

> 📡 [FARVE14/website-load-monitor](https://github.com/FARVE14/website-load-monitor)

This report is automatically generated using GitHub Actions.  
For more info, view the [Actions tab](https://github.com/FARVE14/website-load-monitor/actions).

---

---

## 🤝 Contributing

We welcome contributions to improve and expand this project!

### How to Contribute

1. **Fork the repository**  
2. **Create a new branch** for your changes  
3. **Commit** your updates with clear messages  
4. **Push** your branch to your fork  
5. **Create a Pull Request** with a description of your changes

### Ideas for Contributions

- Add new performance metrics
- Improve graphing and visualizations
- Support additional browser configurations
- Enhance reporting and email formatting
- Add dashboard or web interface

Please ensure all code follows good practices and is tested before submission.

For major feature ideas or questions, feel free to open an issue first to discuss.

---

Looking forward to your contributions! ⭐

---

## 📜 Contribution Rules

To maintain the quality and security of this project, we kindly ask all contributors to follow these rules when submitting pull requests:

### ✅ Pull Request Requirements

- Use **descriptive branch names** (e.g., `fix/load-time-bug`, `feature/add-dashboard`)
- Ensure your code is **well-documented and tested**
- Pull Requests must be **linked to an open issue** if applicable
- All PRs should pass existing **CI workflows** and **linter checks**
- Avoid committing directly to `main` or `master`

### 🔐 Signed Commits

We require **signed commits** to ensure the authenticity of contributions.  
To sign a commit:

```bash
git commit -S -m "Your commit message"
```

Make sure you’ve [set up GPG signing](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) in your GitHub account.

---

Thank you for helping keep this project high quality and secure!
