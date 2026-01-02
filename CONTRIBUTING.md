# Contributing to The Project

First off, thank you for considering contributing! To maintain high code quality and consistency, we enforce very strict formatting and linting standards.

## Automated CI Checks

We use GitHub Actions to automatically verify every contribution. Our `Lint Markdown` workflow triggers on every push and pull request to the `main` branch.

Your Pull Request will not be merged if these checks fail:

- **Prettier Check**: Verifies that all files match our project's style guide using `creyD/prettier_action`.
- **Markdownlint**: Verifies that all `.md` files follow strict structural rules using `davidanson/markdownlint-cli2-action`.

## Local Development

To ensure your contribution passes the automated CI checks, please run the following tools locally before pushing your code.

### Formatting (Prettier)

To check if your files meet the formatting standards:

```sh
npx prettier --check "**/*.md"
```

To automatically fix formatting issues:

```sh
npx prettier --write "**/*.md"
```

### Linting (markdownlint)

To check for structural or syntax errors:

```sh
npx markdownlint-cli2 "**/*.md"
```

## Pull Request Process

1.  Fork the repository and create your feature branch (`git checkout -b feature/AmazingFeature`).
2.  Commit your changes after verifying they pass local linting and formatting.
3.  Push to your branch and open a Pull Request.
4.  **Check Status**: Monitor the "Checks" tab on GitHub for the `Lint Markdown` job. If it fails, please correct the issues in your branch and push the updates.
5.  **Review**: Once the workflow passes (green checkmark), a maintainer will review your work.

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [LICENSE](LICENSE.md).
