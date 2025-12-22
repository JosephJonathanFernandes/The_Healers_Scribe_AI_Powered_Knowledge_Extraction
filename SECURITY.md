# Security Policy for The Healer's Scribe

## Reporting a Vulnerability

If you discover a security vulnerability, please report it via GitHub Issues or email the maintainers directly. Do **not** disclose vulnerabilities publicly until they have been reviewed and patched.

- Provide a clear description and steps to reproduce
- Include relevant logs, code, or configuration (redact sensitive info)
- We aim to respond within 48 hours

## Security Best Practices

- **No hardcoded secrets**: Use environment variables and .env files
- **Input validation**: All user input is sanitized and validated
- **Dependencies**: Keep dependencies up to date and monitor for CVEs
- **Least privilege**: Services and scripts should run with minimal permissions
- **Code reviews**: All changes are reviewed for security impact

## Supported Versions

Only the latest major version is actively supported with security updates.

## Responsible Disclosure

We follow responsible disclosure and coordinate with security researchers to patch vulnerabilities before public release.
