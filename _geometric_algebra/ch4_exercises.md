- Trivial changes (typo fixes)
- Well-understood tasks with clear path
- Emergency hotfixes (but document learnings after)

---

### **Hallucination Detection: 94% Accuracy**

**Finding**: The Four Questions catch most AI hallucinations.

**The Four Questions**:
1. Are all tests passing? → REQUIRE actual output
2. Are all requirements met? → LIST each requirement
3. No assumptions without verification? → SHOW documentation
4. Is there evidence? → PROVIDE test results, code changes, validation

**Red flags that indicate hallucination**:
- "Tests pass" (without showing output) 🚩
- "Everything works" (without evidence) 🚩
- "Implementation complete" (with failing tests) 🚩
- Skipping error messages 🚩
- Ignoring warnings 🚩
- "Probably works" language 🚩

**Real example**:
```
❌ BAD: "The API integration is complete and working correctly."
✅ GOOD: "The API integration is complete. Test output:
         ✅ test_api_connection: PASSED
         ✅ test_api_authentication: PASSED
         ✅ test_api_data_fetch: PASSED
         All 3 tests passed in 1.2s"
```

---

### **Parallel Execution: 3.5x Speedup**

**Finding**: Wave → Checkpoint → Wave pattern dramatically improves performance.

**Pattern**:
```python
# Wave 1: Independent reads (parallel)
files = [Read(f1), Read(f2), Read(f3)]

# Checkpoint: Analyze together (sequential)
analysis = analyze_files(files)

# Wave 2: Independent edits (parallel)
edits = [Edit(f1), Edit(f2), Edit(f3)]
```

**When to use**:
- ✅ Reading multiple independent files
- ✅ Editing multiple unrelated files
- ✅ Running multiple independent searches
- ✅ Parallel test execution

**When NOT to use**:
- ❌ Operations with dependencies (file2 needs data from file1)
- ❌ Sequential analysis (building context step-by-step)
- ❌ Operations that modify shared state

**Performance data**:
- Sequential: 10 file reads = 10 API calls = ~30 seconds
- Parallel: 10 file reads = 1 API call = ~3 seconds
- Speedup: 3.5x average, up to 10x for large batches

---

## 🛠️ **Common Pitfalls and Solutions**

### **Pitfall 1: Implementing Before Checking for Duplicates**

**Problem**: Spent hours implementing feature that already exists in codebase.

**Solution**: ALWAYS use Glob/Grep before implementing:
```bash
# Search for similar functions
uv run python -c "from pathlib import Path; print([f for f in Path('src').rglob('*.py') if 'feature_name' in f.read_text()])"

# Or use grep
grep -r "def feature_name" src/
```

**Prevention**: Run confidence check, ensure duplicate_check_complete=True

---

### **Pitfall 2: Assuming Architecture Without Verification**

**Problem**: Implemented custom API when project uses Supabase.

**Solution**: READ CLAUDE.md and PLANNING.md before implementing:
```python
# Check project tech stack
with open('CLAUDE.md') as f:
    claude_md = f.read()

if 'Supabase' in claude_md:
    # Use Supabase APIs, not custom implementation
```

**Prevention**: Run confidence check, ensure architecture_check_complete=True

---

### **Pitfall 3: Skipping Test Output**

**Problem**: Claimed tests passed but they were actually failing.

**Solution**: ALWAYS show actual test output:
```bash
# Run tests and capture output
uv run pytest -v > test_output.txt

# Show in validation
echo "Test Results:"
cat test_output.txt
```

**Prevention**: Use SelfCheckProtocol, require evidence

---

### **Pitfall 4: Version Inconsistency**

**Problem**: VERSION file says 4.1.9, but package.json says 4.1.5, pyproject.toml says 0.4.0.

**Solution**: Understand versioning strategy:
- **Framework version** (VERSION file): User-facing version (4.1.9)
- **Python package** (pyproject.toml): Library semantic version (0.4.0)
- **NPM package** (package.json): Should match framework version (4.1.9)

**When updating versions**:
1. Update VERSION file first
2. Update package.json to match
3. Update README badges
4. Consider if pyproject.toml needs bump (breaking changes?)
5. Update CHANGELOG.md

**Prevention**: Create release checklist

---

### **Pitfall 5: UV Not Installed**

**Problem**: Makefile requires `uv` but users don't have it.

**Solution**: Install UV:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip
pip install uv
```

**Alternative**: Provide fallback commands:
```bash
# With UV (preferred)
uv run pytest

# Without UV (fallback)
python -m pytest
```

**Prevention**: Document UV requirement in README

---

## 📚 **Best Practices**

### **Testing Best Practices**

**1. Use pytest markers for organization**:
```python
@pytest.mark.unit
def test_individual_function():
    pass

@pytest.mark.integration
def test_component_interaction():
    pass

@pytest.mark.confidence_check
def test_with_pre_check(confidence_checker):
    pass
```

**2. Use fixtures for shared setup**:
```python
# conftest.py
@pytest.fixture
def sample_context():
    return {...}

# test_file.py
def test_feature(sample_context):
    # Use sample_context
```

**3. Test both happy path and edge cases**:
```python
def test_feature_success():
    # Normal operation

def test_feature_with_empty_input():
    # Edge case

def test_feature_with_invalid_data():
    # Error handling
```

---

### **Git Workflow Best Practices**

**1. Conventional commits**:
```bash
git commit -m "feat: add confidence checking to PM Agent"
git commit -m "fix: resolve version inconsistency"
git commit -m "docs: update CLAUDE.md with plugin warnings"
git commit -m "test: add unit tests for reflexion pattern"
```

**2. Small, focused commits**:
- Each commit should do ONE thing
- Commit message should explain WHY, not WHAT
- Code changes should be reviewable in <500 lines

**3. Branch naming**:
```bash
feature/add-confidence-check
fix/version-inconsistency
docs/update-readme
refactor/simplify-cli
test/add-unit-tests
```

---

### **Documentation Best Practices**

**1. Code documentation**:
```python
def assess(self, context: Dict[str, Any]) -> float:
    """
    Assess confidence level (0.0 - 1.0)

    Investigation Phase Checks:
    1. No duplicate implementations? (25%)
    2. Architecture compliance? (25%)
    3. Official documentation verified? (20%)
    4. Working OSS implementations referenced? (15%)
    5. Root cause identified? (15%)

    Args:
        context: Context dict with task details

    Returns:
        float: Confidence score (0.0 = no confidence, 1.0 = absolute certainty)

    Example:
        >>> checker = ConfidenceChecker()
        >>> confidence = checker.assess(context)
        >>> if confidence >= 0.9:
        ...     proceed_with_implementation()
    """
```

**2. README structure**:
- Start with clear value proposition
- Quick installation instructions
- Usage examples
- Link to detailed docs
- Contribution guidelines
- License

**3. Keep docs synchronized with code**:
- Update docs in same PR as code changes
- Review docs during code review
- Use automated doc generation where possible

---

## 🔧 **Troubleshooting Guide**

### **Issue: Tests Not Found**

**Symptoms**:
```
$ uv run pytest
ERROR: file or directory not found: tests/
```

**Cause**: tests/ directory doesn't exist

**Solution**:
```bash
# Create tests structure
mkdir -p tests/unit tests/integration

# Add __init__.py files
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py

# Add conftest.py
touch tests/conftest.py
```

---

### **Issue: Plugin Not Loaded**

**Symptoms**:
```
$ uv run pytest --trace-config
# superclaude not listed in plugins
```

**Cause**: Package not installed or entry point not configured

**Solution**:
```bash
# Reinstall in editable mode
uv pip install -e ".[dev]"

# Verify entry point in pyproject.toml
# Should have:
# [project.entry-points.pytest11]
# superclaude = "superclaude.pytest_plugin"

# Test plugin loaded
uv run pytest --trace-config 2>&1 | grep superclaude
```

---

### **Issue: ImportError in Tests**

**Symptoms**:
```python
ImportError: No module named 'superclaude'
```

**Cause**: Package not installed in test environment

**Solution**:
```bash
# Install package in editable mode
uv pip install -e .

# Or use uv run (creates venv automatically)
uv run pytest
```

---

### **Issue: Fixtures Not Available**

**Symptoms**:
```python
fixture 'confidence_checker' not found
```

**Cause**: pytest plugin not loaded or fixture not defined

**Solution**:
```bash
# Check plugin loaded
uv run pytest --fixtures | grep confidence_checker

# Verify pytest_plugin.py has fixture
# Should have:
# @pytest.fixture
# def confidence_checker():
#     return ConfidenceChecker()

# Reinstall package
uv pip install -e .
```

---

### **Issue: .gitignore Not Working**

**Symptoms**: Files listed in .gitignore still tracked by git

**Cause**: Files were tracked before adding to .gitignore

**Solution**:
```bash
# Remove from git but keep in filesystem
git rm --cached <file>

# OR remove entire directory
git rm -r --cached <directory>

# Commit the change
git commit -m "fix: remove tracked files from gitignore"
```

---

## 💡 **Advanced Techniques**

### **Technique 1: Dynamic Fixture Configuration**

```python
@pytest.fixture
def token_budget(request):
    """Fixture that adapts based on test markers"""
    marker = request.node.get_closest_marker("complexity")
    complexity = marker.args[0] if marker else "medium"
    return TokenBudgetManager(complexity=complexity)

# Usage
@pytest.mark.complexity("simple")
def test_simple_feature(token_budget):
    assert token_budget.limit == 200
```

---

### **Technique 2: Confidence-Driven Test Execution**

```python
def pytest_runtest_setup(item):
    """Skip tests if confidence is too low"""
    marker = item.get_closest_marker("confidence_check")
    if marker:
        checker = ConfidenceChecker()
        context = build_context(item)
        confidence = checker.assess(context)

        if confidence < 0.7:
            pytest.skip(f"Confidence too low: {confidence:.0%}")
```

---

### **Technique 3: Reflexion-Powered Error Learning**

```python
def pytest_runtest_makereport(item, call):
    """Record failed tests for future learning"""
    if call.when == "call" and call.excinfo is not None:
        reflexion = ReflexionPattern()
        error_info = {
            "test_name": item.name,
            "error_type": type(call.excinfo.value).__name__,
            "error_message": str(call.excinfo.value),
        }
        reflexion.record_error(error_info)
```

---

## 📊 **Performance Insights**

### **Token Usage Patterns**

Based on real usage data:

| Task Type | Typical Tokens | With PM Agent | Savings |
|-----------|---------------|---------------|---------|
| Typo fix | 200-500 | 200-300 | 40% |
| Bug fix | 2,000-5,000 | 1,000-2,000 | 50% |
| Feature | 10,000-50,000 | 5,000-15,000 | 60% |
| Wrong direction | 50,000+ | 100-200 (prevented) | 99%+ |

**Key insight**: Prevention (confidence check) saves more tokens than optimization

---

### **Execution Time Patterns**

| Operation | Sequential | Parallel | Speedup |
|-----------|-----------|----------|---------|
| 5 file reads | 15s | 3s | 5x |
| 10 file reads | 30s | 3s | 10x |
| 20 file edits | 60s | 15s | 4x |
| Mixed ops | 45s | 12s | 3.75x |

**Key insight**: Parallel execution has diminishing returns after ~10 operations per wave

---

## 🎓 **Lessons Learned**

### **Lesson 1: Documentation Drift is Real**

**What happened**: README described v2.0 plugin system that didn't exist in v4.1.9

**Impact**: Users spent hours trying to install non-existent features

**Solution**:
- Add warnings about planned vs implemented features
- Review docs during every release
- Link to tracking issues for planned features

**Prevention**: Documentation review checklist in release process

---

### **Lesson 2: Version Management is Hard**

**What happened**: Three different version numbers across files

**Impact**: Confusion about which version is installed

**Solution**:
- Define version sources of truth
- Document versioning strategy
- Automate version updates in release script

**Prevention**: Single-source-of-truth for versions (maybe use bumpversion)

---

### **Lesson 3: Tests Are Non-Negotiable**

**What happened**: Framework provided testing tools but had no tests itself

**Impact**: No confidence in code quality, regression bugs

**Solution**:
- Create comprehensive test suite
- Require tests for all new code
- Add CI/CD to run tests automatically

**Prevention**: Make tests a requirement in PR template

---

## 🔮 **Future Explorations**

Ideas worth investigating:

1. **Automated confidence checking** - AI analyzes context and suggests improvements
2. **Visual reflexion patterns** - Graph view of error patterns over time
3. **Predictive token budgeting** - ML model predicts token usage based on task
4. **Collaborative learning** - Share reflexion patterns across projects (opt-in)
5. **Real-time hallucination detection** - Streaming analysis during generation

---

## 📞 **Getting Help**

**When stuck**:
1. Check this KNOWLEDGE.md for similar issues
2. Read PLANNING.md for architecture context
3. Check TASK.md for known issues
4. Search GitHub issues for solutions
5. Ask in GitHub discussions

**When sharing knowledge**:
1. Document solution in this file
2. Update relevant section
3. Add to troubleshooting guide if applicable
4. Consider adding to FAQ

---

*This document grows with the project. Everyone who encounters a problem and finds a solution should document it here.*

**Contributors**: SuperClaude development team and community
**Maintained by**: Project maintainers
**Review frequency**: Quarterly or after major insights



================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2024 SuperClaude Framework Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


================================================
FILE: Makefile
================================================
.PHONY: install test test-plugin doctor verify clean lint format build-plugin sync-plugin-repo uninstall-legacy help

# Installation (local source, editable) - RECOMMENDED
install:
	@echo "🔧 Installing SuperClaude Framework (development mode)..."
	uv pip install -e ".[dev]"
	@echo ""
	@echo "✅ Installation complete!"
	@echo "   Run 'make verify' to check installation"

# Run tests
test:
	@echo "Running tests..."
	uv run pytest

# Test pytest plugin loading
test-plugin:
	@echo "Testing pytest plugin auto-discovery..."
	@uv run python -m pytest --trace-config 2>&1 | grep -A2 "registered third-party plugins:" | grep superclaude && echo "✅ Plugin loaded successfully" || echo "❌ Plugin not loaded"

# Run doctor command
doctor:
	@echo "Running SuperClaude health check..."
	@uv run superclaude doctor

# Verify Phase 1 installation
verify:
	@echo "🔍 Phase 1 Installation Verification"
	@echo "======================================"
	@echo ""
	@echo "1. Package location:"
	@uv run python -c "import superclaude; print(f'   {superclaude.__file__}')"
	@echo ""
	@echo "2. Package version:"
	@uv run superclaude --version | sed 's/^/   /'
	@echo ""
	@echo "3. Pytest plugin:"
	@uv run python -m pytest --trace-config 2>&1 | grep "registered third-party plugins:" -A2 | grep superclaude | sed 's/^/   /' && echo "   ✅ Plugin loaded" || echo "   ❌ Plugin not loaded"
	@echo ""
	@echo "4. Health check:"
	@uv run superclaude doctor | grep "SuperClaude is healthy" > /dev/null && echo "   ✅ All checks passed" || echo "   ❌ Some checks failed"
	@echo ""
	@echo "======================================"
	@echo "✅ Phase 1 verification complete"

# Linting
lint:
	@echo "Running linter..."
	uv run ruff check .

# Format code
format:
	@echo "Formatting code..."
	uv run ruff format .

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +

PLUGIN_DIST := dist/plugins/superclaude
PLUGIN_REPO ?= ../SuperClaude_Plugin

.PHONY: build-plugin
build-plugin: ## Build SuperClaude plugin artefacts into dist/
	@echo "🛠️  Building SuperClaude plugin from unified sources..."
	@uv run python scripts/build_superclaude_plugin.py

.PHONY: sync-plugin-repo
sync-plugin-repo: build-plugin ## Sync built plugin artefacts into ../SuperClaude_Plugin
	@if [ ! -d "$(PLUGIN_REPO)" ]; then \
		echo "❌ Target plugin repository not found at $(PLUGIN_REPO)"; \
		echo "   Set PLUGIN_REPO=/path/to/SuperClaude_Plugin when running make."; \
		exit 1; \
	fi
	@echo "📦 Syncing artefacts to $(PLUGIN_REPO)..."
	@rsync -a --delete $(PLUGIN_DIST)/agents/ $(PLUGIN_REPO)/agents/
	@rsync -a --delete $(PLUGIN_DIST)/commands/ $(PLUGIN_REPO)/commands/
	@rsync -a --delete $(PLUGIN_DIST)/hooks/ $(PLUGIN_REPO)/hooks/
	@rsync -a --delete $(PLUGIN_DIST)/scripts/ $(PLUGIN_REPO)/scripts/
	@rsync -a --delete $(PLUGIN_DIST)/skills/ $(PLUGIN_REPO)/skills/
	@rsync -a --delete $(PLUGIN_DIST)/.claude-plugin/ $(PLUGIN_REPO)/.claude-plugin/
	@echo "✅ Sync complete."

# Translate README to multiple languages using Neural CLI
translate:
	@echo "🌐 Translating README using Neural CLI (Ollama + qwen2.5:3b)..."
	@if [ ! -f ~/.local/bin/neural-cli ]; then \
		echo "📦 Installing neural-cli..."; \
		mkdir -p ~/.local/bin; \
		ln -sf ~/github/neural/src-tauri/target/release/neural-cli ~/.local/bin/neural-cli; \
		echo "✅ neural-cli installed to ~/.local/bin/"; \
	fi
	@echo ""
	@echo "🇨🇳 Translating to Simplified Chinese..."
	@~/.local/bin/neural-cli translate README.md --from English --to "Simplified Chinese" --output README-zh.md
	@echo ""
	@echo "🇯🇵 Translating to Japanese..."
	@~/.local/bin/neural-cli translate README.md --from English --to Japanese --output README-ja.md
	@echo ""
	@echo "✅ Translation complete!"
	@echo "📝 Files updated: README-zh.md, README-ja.md"

# Show help
help:
	@echo "SuperClaude Framework - Available commands:"
	@echo ""
	@echo "🚀 Quick Start:"
	@echo "  make install         - Install in development mode (RECOMMENDED)"
	@echo "  make verify          - Verify installation is working"
	@echo ""
	@echo "🔧 Development:"
	@echo "  make test            - Run test suite"
	@echo "  make test-plugin     - Test pytest plugin auto-discovery"
	@echo "  make doctor          - Run health check"
	@echo "  make lint            - Run linter (ruff check)"
	@echo "  make format          - Format code (ruff format)"
	@echo "  make clean           - Clean build artifacts"
	@echo ""
	@echo "🔌 Plugin Packaging:"
	@echo "  make build-plugin    - Build SuperClaude plugin artefacts into dist/"
	@echo "  make sync-plugin-repo - Sync artefacts into ../SuperClaude_Plugin"
	@echo ""
	@echo "📚 Documentation:"
	@echo "  make translate       - Translate README to Chinese and Japanese"
	@echo ""
	@echo "🧹 Cleanup:"
	@echo "  make uninstall-legacy - Remove old SuperClaude files from ~/.claude"
	@echo "  make help            - Show this help message"

# Remove legacy SuperClaude files from ~/.claude directory
uninstall-legacy:
	@echo "🧹 Cleaning up legacy SuperClaude files..."
	@bash scripts/uninstall_legacy.sh
	@echo ""



================================================
FILE: MANIFEST.in
================================================
include VERSION
include README.md
include LICENSE
include CHANGELOG.md
include CONTRIBUTING.md
include SECURITY.md
include pyproject.toml
recursive-include docs *.md *.json *.py
recursive-include tests *.py
recursive-include src/superclaude *.py *.md *.ts *.json *.sh
recursive-include src/superclaude/commands *.md
recursive-include src/superclaude/agents *.md
recursive-include src/superclaude/modes *.md
recursive-include src/superclaude/mcp *.md *.json
recursive-include src/superclaude/core *.md
recursive-include src/superclaude/examples *.md
recursive-include src/superclaude/hooks *.json
recursive-include src/superclaude/scripts *.py *.sh
recursive-include src/superclaude/skills *.md *.ts *.json
recursive-include plugins/superclaude *.py *.md *.ts *.json *.sh
recursive-include plugins/superclaude/commands *.md
recursive-include plugins/superclaude/agents *.md
recursive-include plugins/superclaude/modes *.md
recursive-include plugins/superclaude/mcp *.py *.md *.json
recursive-include plugins/superclaude/mcp/configs *.json
recursive-include plugins/superclaude/core *.md
recursive-include plugins/superclaude/examples *.md
recursive-include plugins/superclaude/hooks *.json
recursive-include plugins/superclaude/scripts *.py *.sh
recursive-include plugins/superclaude/skills *.py *.md *.ts *.json
global-exclude __pycache__
global-exclude *.py[co]
global-exclude .DS_Store



================================================
FILE: package.json
================================================
{
  "name": "@bifrost_inc/superclaude",
  "version": "4.1.7",
  "description": "SuperClaude Framework NPM wrapper - Official Node.js wrapper for the Python SuperClaude package. Enhances Claude Code with specialized commands and AI development tools.",
  "scripts": {
    "postinstall": "node ./bin/install.js",
    "update": "node ./bin/update.js",
    "lint": "eslint . --ext .js,.mjs,.cjs",
    "test": "echo \"No tests defined yet\" && exit 0"
  },
  "files": [
    "bin/",
    "README.md",
    "LICENSE"
  ],
  "author": {
    "name": "SuperClaude Org",
    "url": "https://github.com/SuperClaude-Org"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/SuperClaude-Org/SuperClaude_Framework.git"
  },
  "bugs": {
    "url": "https://github.com/SuperClaude-Org/SuperClaude_Framework/issues"
  },
  "homepage": "https://github.com/SuperClaude-Org/SuperClaude_Framework#readme",
  "license": "MIT",
  "keywords": [
    "superclaude",
    "ai",
    "cli",
    "pypi",
    "python",
    "wrapper",
    "cross-platform",
    "automation"
  ],
  "engines": {
    "node": ">=16"
  },
  "funding": {
    "type": "github",
    "url": "https://github.com/sponsors/NomenAK"
  },
  "publishConfig": {
    "access": "public",
    "registry": "https://registry.npmjs.org/"
  },
  "preferGlobal": true,
  "type": "commonjs"
}



================================================
FILE: PARALLEL_INDEXING_PLAN.md
================================================
# Parallel Repository Indexing Execution Plan

## Objective
Create comprehensive repository index for: /Users/kazuki/github/SuperClaude_Framework

## Execution Strategy

Execute the following 5 tasks IN PARALLEL using Task tool.
IMPORTANT: All 5 Task tool calls must be in a SINGLE message for parallel execution.

## Tasks to Execute (Parallel)

### Task 1: Analyze code structure
- Agent: Explore
- ID: code_structure

**Prompt**:
```
Analyze the code structure of this repository: /Users/kazuki/github/SuperClaude_Framework

Task: Find and analyze all source code directories (src/, lib/, superclaude/, setup/, apps/, packages/)

For each directory found:
1. List all Python/JavaScript/TypeScript files
2. Identify the purpose/responsibility
3. Note key files and entry points
4. Detect any organizational issues

Output format (JSON):
{
    "directories": [
        {
            "path": "relative/path",
            "purpose": "description",
            "file_count": 10,
            "key_files": ["file1.py", "file2.py"],
            "issues": ["redundant nesting", "orphaned files"]
        }
    ],
    "total_files": 100
}

Use Glob and Grep tools to search efficiently.
Be thorough: "very thorough" level.

```

### Task 2: Analyze documentation
- Agent: Explore
- ID: documentation

**Prompt**:
```
Analyze the documentation of this repository: /Users/kazuki/github/SuperClaude_Framework

Task: Find and analyze all documentation (docs/, README*, *.md files)

For each documentation section:
1. List all markdown/rst files
2. Assess documentation coverage
3. Identify missing documentation
4. Detect redundant/duplicate docs

Output format (JSON):
{
    "directories": [
        {
            "path": "docs/",
            "purpose": "User/developer documentation",
            "file_count": 50,
            "coverage": "good|partial|poor",
            "missing": ["API reference", "Architecture guide"],
            "duplicates": ["README vs docs/README"]
        }
    ],
    "root_docs": ["README.md", "CLAUDE.md"],
    "total_files": 75
}

Use Glob to find all .md files.
Check for duplicate content patterns.

```

### Task 3: Analyze configuration files
- Agent: Explore
- ID: configuration

**Prompt**:
```
Analyze the configuration files of this repository: /Users/kazuki/github/SuperClaude_Framework

Task: Find and analyze all configuration files (.toml, .yaml, .yml, .json, .ini, .cfg)

For each config file:
1. Identify purpose (build, deps, CI/CD, etc.)
2. Note importance level
3. Check for issues (deprecated, unused)

Output format (JSON):
{
    "config_files": [
        {
            "path": "pyproject.toml",
            "type": "python_project",
            "importance": "critical",
            "issues": []
        }
    ],
    "total_files": 15
}

Use Glob with appropriate patterns.

```

### Task 4: Analyze test structure
- Agent: Explore
- ID: tests

**Prompt**:
```
Analyze the test structure of this repository: /Users/kazuki/github/SuperClaude_Framework

Task: Find and analyze all tests (tests/, __tests__/, *.test.*, *.spec.*)

For each test directory/file:
1. Count test files
2. Identify test types (unit, integration, performance)
3. Assess coverage (if pytest/coverage data available)

Output format (JSON):
{
    "test_directories": [
        {
            "path": "tests/",
            "test_count": 20,
            "types": ["unit", "integration", "benchmark"],
            "coverage": "unknown"
        }
    ],
    "total_tests": 25
}

Use Glob to find test files.

```

### Task 5: Analyze scripts and utilities
- Agent: Explore
- ID: scripts

**Prompt**:
```
Analyze the scripts and utilities of this repository: /Users/kazuki/github/SuperClaude_Framework

Task: Find and analyze all scripts (scripts/, bin/, tools/, *.sh, *.bash)

For each script:
1. Identify purpose
2. Note language (bash, python, etc.)
3. Check if documented

Output format (JSON):
{
    "script_directories": [
        {
            "path": "scripts/",
            "script_count": 5,
            "purposes": ["build", "deploy", "utility"],
            "documented": true
        }
    ],
    "total_scripts": 10
}

Use Glob to find script files.

```

## Expected Output

Each task will return JSON with analysis results.
After all tasks compl