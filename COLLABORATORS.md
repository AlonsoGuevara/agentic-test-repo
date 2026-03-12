# 👥 Collaborators & Contributors

<div align="center">

> *Agentic CAFE is built by engineers, for engineers — and it thrives because of its community.*
> Every pull request, bug report, and idea makes this framework better for everyone. ☕

</div>

---

## 🌍 About Our Community

Agentic CAFE is an open, welcoming project that values collaboration, curiosity, and craftsmanship. Our contributors come from all walks of engineering — from backend architects to ML researchers to DevOps specialists. Whether you're fixing a typo or designing a new orchestration pattern, **you belong here**.

We recognize and celebrate every contributor — no contribution is too small.

---

## 🌟 Core Team

| Avatar | Name | Role | GitHub |
|:---:|---|---|---|
| 👤 | **Your Name** | Core Maintainer | [@yourhandle](https://github.com/yourhandle) |
| 👤 | **Jane Engineer** | Framework Architect | [@jane-engineer](https://github.com/jane-engineer) |
| 👤 | **Alex Dev** | Tooling & Observability Lead | [@alex-dev](https://github.com/alex-dev) |

> 💡 *Want to join the core team? Start by making consistent, high-quality contributions and open a discussion!*

---

## 🤝 How to Contribute

Follow these steps to get your contribution merged smoothly:

1. **🍴 Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/agentic-cafe.git
   cd agentic-cafe
   ```

2. **🌿 Create a feature branch**
   ```bash
   git checkout -b feat/your-awesome-feature
   # or for fixes:
   git checkout -b fix/the-thing-that-was-broken
   ```

3. **💻 Write your code**
   - Follow the style and architecture patterns already in the project
   - Add docstrings, type hints, and inline comments where appropriate
   - Keep changes focused — one feature or fix per PR

4. **🧪 Write & run tests**
   ```bash
   pip install -e ".[dev]"
   pytest tests/ -v --cov=src/agentic_cafe
   ```
   Make sure all existing tests still pass, and add new tests for your changes.

5. **📬 Open a Pull Request**
   - Push your branch and open a PR against `main`
   - Fill out the PR template (description, motivation, testing notes)
   - Link any related issues
   - Request a review from a core team member

---

## 📋 Contribution Guidelines

### 🎨 Code Style

- All Python code must follow **[PEP 8](https://peps.python.org/pep-0008/)**.
- Use **type hints** on all function signatures and class attributes.
- Format your code with [`black`](https://black.readthedocs.io/) and lint with [`flake8`](https://flake8.pycqa.org/):
  ```bash
  black src/ tests/
  flake8 src/ tests/
  ```
- Write **Google-style docstrings** for all public functions, methods, and classes.

### 🧪 Test Coverage

- Aim for **≥ 90% test coverage** on new code.
- All tests must pass in CI before a PR can be merged.
- Use `pytest` with `pytest-asyncio` for async tests.

### 📝 PR Description Format

Please use the following format when opening a Pull Request:

```markdown
## 📌 Summary
A brief description of what this PR does.

## 🎯 Motivation
Why is this change needed? What problem does it solve?

## 🔬 Testing
Describe how you tested this change. Include test commands.

## 🔗 Related Issues
Closes #<issue-number>
```

---

## 🏆 All Contributors

All contributors are recognized and celebrated! ✨

We use the **All Contributors** spec to acknowledge every type of contribution — code, docs, design, ideas, and more.

👉 See the full list of contributors on our [**GitHub Contributors page**](https://github.com/agentic-cafe/agentic-cafe/graphs/contributors).

---

## 📜 Code of Conduct

Agentic CAFE is committed to providing a **welcoming, inclusive, and respectful** environment for everyone — regardless of experience level, background, identity, or affiliation.

We do not tolerate harassment, discrimination, or exclusionary behavior of any kind. By participating in this project, you agree to uphold these values in all interactions: in issues, PRs, discussions, and beyond.

If you experience or witness a violation, please report it to the core team. We take all reports seriously and will respond promptly.

*Let's build something great — together.* ☕🤝

---

<div align="center">

Thank you for being part of Agentic CAFE. Every ☕ helps.

</div>
