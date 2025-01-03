# CHANGELOG


## v6.2.0 (2025-01-03)

### Documentation

* docs(quality): update documentation for code quality tools

- Add detailed code quality tools section to CONTRIBUTING.md
- Update Features section in README.md to include all linting tools
- Maintain Commitlint in the tooling list
- Include configuration details and usage instructions ([`d92e223`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d92e2231250e38f4b1359421c7e93776a216586b))

### Features

* feat(lint): enhance code quality with flake8 and mypy

- Add flake8 with additional plugins:
 - flake8-docstrings for docstring checks
 - flake8-bugbear for additional bug checks
 - flake8-comprehensions for list/dict/set comprehension checks
 - flake8-simplify for code simplification suggestions

 - Add mypy for static type checking with:
  - Essential type stubs (PyYAML, python-jose, requests, setuptools)

  - Pydantic plugin support
  - Configurable type checking settings

  - Fix code quality issues:
    - Convert multi-line docstrings to single-line format
    - Replace assert False with raise AssertionError()
    - Add flake8 configuration file
    - Update pre-commit hooks configuration ([`f9927df`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f9927df68539b8ac4e82a79ddb699068e6397846))

### Unknown

* Merge pull request #83 from gsinghjay/feat/add-linting-improvements

feat(lint): enhance code quality with flake8 and mypy ([`fa1fc68`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fa1fc68c737eaf43706e8386faf6ed9e61fbe99b))


## v6.1.0 (2025-01-02)

### Documentation

* docs(readme): update workflow documentation and mermaid diagram

  - Remove references to PAT tokens in favor of GITHUB_TOKEN
  - Fix Mermaid diagram syntax and improve visualization
  - Update workflow documentation to reflect current implementation
  - Add detailed security and permissions section
  - Improve environment optimization documentation ([`9a63997`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9a639970bfd7100eede59228ec1aae19b16690f0))

### Features

* feat(docs): add comprehensive CI/CD workflow visualization

- Implement detailed mermaid flowchart for CI/CD pipeline
- Add color-coded workflow stages for better readability
- Introduce skip release conditions documentation
- Detail each workflow stage with specific responsibilities ([`3da837b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3da837bd159bacb48785a0ba11fa4fdf0729d3e4))

### Unknown

* Merge pull request #82 from gsinghjay/docs/update-workflow-documentation

feat(docs): add comprehensive CI/CD workflow visualization ([`37b80a3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/37b80a359fa83921e4ad1a2aef45c3a292230774))

* Merge pull request #81 from gsinghjay/docs/update-workflow-documentation

docs(readme): update workflow documentation and mermaid diagram ([`4127910`](https://github.com/gsinghjay/fast-api-ci-cd/commit/41279107fa0a8fe014e19fc85d1db02b2600c6f3))


## v6.0.0 (2025-01-02)

### Breaking

* feat(changelog): implement Keep a Changelog format

- Add missing changelog sections (deprecated, removed, security)
- Update commit parser to use angular format
- Configure changelog generation to match Keep a Changelog spec

BREAKING CHANGE: This changes the format of generated changelogs.
Previous changelog entries will remain but new entries will follow the Keep a Changelog format. ([`94c8a94`](https://github.com/gsinghjay/fast-api-ci-cd/commit/94c8a94b0641c99899c8b23e691bd01887f85d0f))

### Refactoring

* refactor(ci): simplify release workflow using semantic-release actions

- Remove virtual environment setup (handled by semantic-release Docker container)
- Add publish action for GitHub release assets
- Update to latest semantic-release action version ([`0dab11f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0dab11f8a581fde1a97e770db11f73e7dda5142e))

### Unknown

* Merge pull request #80 from gsinghjay/ci/Angular

feat(changelog): align configuration with Keep a Changelog format ([`c48b214`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c48b2141388a6770b0b24e0d2d9640e412830a39))

* Merge pull request #79 from gsinghjay/ci/venv-and-restore

refactor(ci): simplify release workflow using semantic-release actions ([`57eb79a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/57eb79a03c6fbfc574bf25424c58b6e2aa6ab261))


## v5.0.7 (2025-01-02)

### Bug Fixes

* fix(ci): correct semantic-release command flags

- Move --noop to top-level flag position
- Use correct --print flag for version display ([`a0d3c9f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a0d3c9f4e06ee806d6f378c263ca123b2f657e42))

### Unknown

* Merge pull request #78 from gsinghjay/ci/venv-and-restore

fix(ci): correct semantic-release command flags ([`3732943`](https://github.com/gsinghjay/fast-api-ci-cd/commit/373294381e0686c526461b9beff46ce74596d054))


## v5.0.6 (2025-01-02)

### Bug Fixes

* fix(ci): use direct path to semantic-release executable

- Use .venv/bin/semantic-release directly\n- Remove poetry run prefix\n- Keep consistent with lint.yml and test.yml execution style ([`c952892`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c9528926ad7239c35c621f33e3a0519eaff9c468))

### Chores

* chore: test ([`fa4e029`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fa4e0295d1bb6cc33e8782ef2f3a19a5f8c18f88))

### Unknown

* Merge pull request #77 from gsinghjay/ci/venv-and-restore

chore: test ([`0dbafd6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0dbafd637c109edde1421276b7972a920ea59620))

* Merge pull request #76 from gsinghjay/ci/venv-and-restore

fix(ci): use direct path to semantic-release executable ([`ccd56be`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ccd56be94a15313e92cabba353e2bc50ebff9839))


## v5.0.5 (2025-01-02)

### Bug Fixes

* fix(ci): remove redundant poetry installation in release job

- Use Poetry from the shared virtual environment
- Remove duplicate Poetry installation step
- Keep consistent with test and lint workflows ([`1cb11d3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1cb11d3e4f013e19749c762846874d45ac862458))

### Unknown

* Merge pull request #75 from gsinghjay/ci/venv-and-restore

fix(ci): remove redundant poetry installation in release job ([`5c87d41`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5c87d41f6d970759f41895ead77bdf271c911568))


## v5.0.4 (2025-01-02)

### Bug Fixes

* fix(ci): activate virtual environment for semantic-release commands

- Add virtual environment activation before running semantic-release
- Use full path to Poetry from virtual environment ([`1f4a63a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1f4a63a91de00ab278b186265ce36602e18b964d))

### Unknown

* Merge pull request #74 from gsinghjay/ci/venv-and-restore

fix(ci): activate virtual environment for semantic-release commands ([`9d16701`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9d16701d9525f7cf5dff5ac24d0df6ac9c6d19c4))


## v5.0.3 (2025-01-02)

### Bug Fixes

* fix(ci): add environment debugging and fix poetry commands ([`2ad33ec`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2ad33ecfc21ca2fb2f60938e12457c25b68f084f))

### Unknown

* Merge pull request #73 from gsinghjay/ci/venv-and-restore

fix(ci): add environment debugging and fix poetry commands ([`eeb4645`](https://github.com/gsinghjay/fast-api-ci-cd/commit/eeb464595cfce20009f58e79e4e7d4fcbdd6e7c1))


## v5.0.2 (2025-01-02)

### Bug Fixes

* fix(ci): use shared virtual environment for release job

- Add setup job as dependency for release job
- Use cached Poetry and dependencies from setup job
- Fix semantic-release commands to use virtual environment ([`31bc972`](https://github.com/gsinghjay/fast-api-ci-cd/commit/31bc972498925553672074073c6e0a85df88ce1b))

### Unknown

* Merge pull request #72 from gsinghjay/ci/venv-and-restore

fix(ci): use shared virtual environment for release job ([`3ffbaf0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3ffbaf010a4a86c253f257dbae92af2aa8348f89))


## v5.0.1 (2025-01-02)

### Bug Fixes

* fix: revert back before metadata ([`1851163`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1851163fb278d6e6ece245fd968ee051acb29d78))

### Unknown

* Merge pull request #71 from gsinghjay/ci/add-build-metadata

fix: revert back before metadata ([`d8a80f0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d8a80f0d3561d5ef5a7627941b1171e594ab4b3c))


## v5.0.0+build.27 (2025-01-02)

### Continuous Integration

* ci(release): add build metadata to version numbers ([`9834fcd`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9834fcd1256ad4ede9b0e86005f125ecf648762d))

### Documentation

* docs(workflow): update CI/CD pipeline architecture documentation

Update workflow architecture documentation to reflect v5.0.0 changes:

- Add integrated CI workflow as main orchestrator
- Update workflow diagram with new job structure - Add environment optimization details
- Improve workflow execution documentation ([`4f0b3e4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4f0b3e4b90ef83fb342d317e65445583e23ccf8e))

### Unknown

* Merge pull request #70 from gsinghjay/ci/add-build-metadata

ci(release): add build metadata to version numbers ([`7de88e1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7de88e115daaf335851ee68974ccc534ef4f4441))

* Merge pull request #69 from gsinghjay/docs/update-workflow-architecture

docs(workflow): update CI/CD pipeline architecture documentation ([`96e1e53`](https://github.com/gsinghjay/fast-api-ci-cd/commit/96e1e537ce3816c0ae369e65a7f1f2a5027eea16))


## v5.0.0 (2025-01-02)

### Breaking

* feat(ci): integrate release job into main CI workflow

BREAKING CHANGE: Release process now runs as part of the main CI workflow
instead of a separate workflow. This ensures proper sequencing of setup,
lint, test, and release steps.

- Adds release job that runs after lint and test
- Only executes on main branch
- Maintains all semantic-release functionality
- Removes need for separate release workflow ([`5f63e26`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5f63e26c1966661d6b725f1b304a09ce0a8fcf56))

### Bug Fixes

* fix: remove circular dependency ([`f765b8f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f765b8f628123cabde486931fb365848175e1e3e))

* fix: removed path filters ([`a3c7e61`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a3c7e617cc756ef9b8dc1f3d986b067de04eef8b))

* fix: removed the file from the paths filter ([`6dc06e8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6dc06e8af4b0798e84fe74ce8dc541d4a6a6f1e4))

* fix: add `paths` filter to the `push` trigger ([`0f1ae69`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0f1ae69c935b3a9917b7da00b4e9cee7f578cb0d))

* fix: token naming issue ([`d57959b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d57959b99a87b3c6b02ab613fe063d6849722168))

* fix: use tar to compress venv ([`78296d4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/78296d41424cee771643e62772e3e90d27cd1217))

* fix: preserve directory structure and env across jobs ([`4cdf91d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4cdf91ddc3e9b52f2a0ee8b502e259bd21602032))

* fix: properly use the cached virtual environment and its dependencies ([`35257cd`](https://github.com/gsinghjay/fast-api-ci-cd/commit/35257cd52d11f714fa9c142bccd51a9ca4b74b4a))

* fix: reserved name ([`2af0745`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2af074539ba8369c46f223ce7ede5e34aa94e61c))

* fix: changed secret name because of reserved name ([`42c8f3f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/42c8f3fcd80394eb846e692e89c8b4b5f1ad4ad9))

* fix: added `workflow_call` to trigger `ci.yml` ([`530c018`](https://github.com/gsinghjay/fast-api-ci-cd/commit/530c0188822d8785d8ca9dd9813c0d432800b69b))

* fix(ci): properly use Poetry in workflows

- Remove requirements.txt usage
- Use poetry run for commands
- Include poetry.lock and pyproject.toml in artifacts
- Remove manual venv activation ([`dfc3c13`](https://github.com/gsinghjay/fast-api-ci-cd/commit/dfc3c13f44d3870a609a06e7ae30abdd99b740ec))

* fix(ci): improve artifact sharing between workflows

- Add unique artifact names with run ID
- Pass artifact name through workflow inputs
- Add setup as dependency for release job ([`0cd29d2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0cd29d245abb28aa4b5465e9e131ffc8638931b3))

### Chores

* chore(ci): remove separate release workflow ([`f0170b6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f0170b652031630d672786d03763777410f7482c))

* chore: merge conflict ([`44a8ae1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/44a8ae14c2976fe6f791b090f53266d8a1b1cb01))

* chore: add debug output ([`083610d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/083610d9f78012a8707d2c5d5abb34a8e7340bb5))

### Continuous Integration

* ci: optimize workflow environment sharing

- Use artifacts to share virtual environment
- Remove duplicate environment setup
- Simplify job dependencies ([`6f9d94f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6f9d94f66e38b739178cde0dc182a18805c0d9b3))

* ci: optimize workflow job dependencies

- Run setup job first
- Run lint and test jobs in parallel
- Run release job after all checks pass ([`fd6cd91`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fd6cd912b8dcd362d8a18141a3af47051c70d4d7))

* ci: optimize workflow job dependencies

- Run setup job first
- Run lint and test jobs in parallel
- Run release job after all checks pass ([`8dc8182`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8dc818261224ed51f10590609a69afe769f7de17))

### Refactoring

* refactor(ci): reorganize workflow structure

- Add ci.yml as main orchestrator workflow
- Make test.yml and lint.yml purely reusable
- Update release.yml to use ci workflow
- Fix artifact upload/download order ([`d4bfd3e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d4bfd3ed2268ddf3231e34bb715e7e5f11611838))

* refactor(ci): improve reusable workflows following GitHub best practices

- Add proper input/output/secrets definitions
- Simplify workflow dependencies
- Improve Python version handling
- Add token handling for commitlint ([`ed90712`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ed90712c41b64fb269d73d278575b9d70ea5a8c6))

### Unknown

* Merge pull request #68 from gsinghjay/feat/integrate-release-workflow

Feat/integrate release workflow ([`cfdc96e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/cfdc96ebb9fdd4bcbdf2cd06b34178d8ca95c016))

* Merge pull request #67 from gsinghjay/ci/reusable-workflows

fix: remove circular dependency ([`f3a0367`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f3a0367dc40692a2750d35e2c10ac55c7d5ff591))

* Merge pull request #66 from gsinghjay/ci/reusable-workflows

fix: removed path filters ([`522a0d7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/522a0d7bd030517f4075e3c4d82ac5b6f83765a8))

* Merge pull request #65 from gsinghjay/ci/reusable-workflows

fix: removed the file from the paths filter ([`58084d7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/58084d7cb4d226af3631d554eb2c024f9e802aae))

* Merge pull request #64 from gsinghjay/ci/reusable-workflows

fix: add `paths` filter to the `push` trigger ([`34021ac`](https://github.com/gsinghjay/fast-api-ci-cd/commit/34021aca9d2bc5f08c4d54c910520c3a6fd5052c))

* Merge pull request #63 from gsinghjay/ci/reusable-workflows

chore: merge conflict ([`324e985`](https://github.com/gsinghjay/fast-api-ci-cd/commit/324e985d3437c28d262f240838dd5d834848c6db))

* Merge branch 'main' of github.com:gsinghjay/fast-api-ci-cd ([`fd926a6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fd926a61a1565e34838bdca2289dbb1eadfabe25))

* Merge pull request #62 from gsinghjay/ci/reusable-workflows

ci: optimize workflow job dependencies ([`680490d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/680490d386d04bf9d568ecec0a31678ba2c39ddd))


## v4.1.1 (2025-01-02)

### Bug Fixes

* fix(ci): improve environment handling across workflows

- Use environment variables from setup-python
- Consistent Poetry setup across all jobs
- Simplify environment activation ([`7c8a1fd`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7c8a1fdaff530bec53bdbad1f7fd172680a5d4f2))

* fix: improve poetry environment handling in workflows

- Use poetry run instead of activating venv
- Ensure proper caching of poetry environment
- Simplify setup workflow ([`9cba052`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9cba05294df046e1e972405b15b22fd074c10c89))

### Continuous Integration

* ci: implement reusable workflow for Python and Poetry setup

- Create reusable setup-python workflow
- Share Poetry virtual environment between jobs
- Update all workflows to use the reusable workflow ([`64c2fc4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/64c2fc4880a48d96fa1387a3b4c911d1aed37318))

* ci: enhance dependency caching strategy

- Configure in-project virtualenvs for better caching

- Add comprehensive caching for pip and poetry

- Update documentation with caching details ([`a38abb9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a38abb90bf1cd5edd454c97bc0b84d276be5fcc0))

### Documentation

* docs: update README to use GITHUB_TOKEN instead of PAT_TOKEN ([`97268b0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/97268b0a4f443d7988571803e0be055f554dc6f3))

### Unknown

* Merge pull request #61 from gsinghjay/ci/reusable-workflows

fix(ci): improve environment handling across workflows ([`786bd77`](https://github.com/gsinghjay/fast-api-ci-cd/commit/786bd77f12b4c7fc01bb749fe91c94b3e435e90a))

* Merge pull request #60 from gsinghjay/ci/reusable-workflows

ci: implement reusable workflow for Python and Poetry setup ([`d9f7c21`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d9f7c2148ef50cd31fa1514eea599d474df9a230))

* Merge pull request #59 from gsinghjay/ci/enhance-caching

ci: enhance dependency caching strategy ([`2cd64fb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2cd64fbcf1c374263775004d5817e58bb748b450))

* Merge pull request #58 from gsinghjay/ci/use-github-token

docs: update README to use GITHUB_TOKEN instead of PAT_TOKEN ([`b25a809`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b25a8090ad1c986ec0681f34e71df1b76369d488))


## v4.1.0 (2025-01-02)

### Continuous Integration

* ci: add poetry dependency caching to workflows ([`e779053`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e77905390bd221583665785b010f9cc069469563))

### Features

* feat: add test feature for release workflow ([`d7191ad`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d7191add229ede36d5e97c889ab4f3e356db2b1f))

### Unknown

* Merge pull request #57 from gsinghjay/ci/changelog

feat: add test feature for release workflow ([`ff4bfed`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ff4bfed887ba88ad4f9b48701f39e47dc6326905))

* Merge pull request #56 from gsinghjay/ci/add-poetry-caching

ci: add poetry dependency caching to workflows ([`efb5859`](https://github.com/gsinghjay/fast-api-ci-cd/commit/efb5859afc4848de00df89dd305752d629d86bb0))


## v4.0.0 (2025-01-02)

### Breaking

* fix: enhance semantic release configuration

- Add verbose logging with -vv flag for better debugging
- Ensure proper environment variables for GH_TOKEN
- Configure explicit version update patterns for files

BREAKING CHANGE: Version management now requires explicit version_toml configuration ([`f583e74`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f583e74095dcd0e1744c79009d523eaf3af03f6e))

### Features

* feat: add automated version management system

- Integrate Python Semantic Release for version control
- Configure automatic version bumping in CI/CD pipeline
- Enable automated changelog generation ([`6c66301`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6c66301890cd52666d0f943b41d653828003c46d))


## v3.0.0 (2025-01-02)

### Breaking

* feat!: major changes needed

BREAKING CHANGE: description of breaking changes ([`b4b8909`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b4b8909cb8970a11ea055c5082d731c2bcafb1de))

### Chores

* chore(config): update author information ([`a4e364a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a4e364a7c995d0714334ff4e9c4c6fb2be31865c))

* chore: merge changes ([`a28a970`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a28a970061ef744647ab4a2666b6eb43cb1e42b8))

### Documentation

* docs: add semantic versioning, changelog, and release automation documentation ([`fb31c4d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fb31c4d53d16cc4d300052e395cb91232d80a611))


## v2.0.1 (2025-01-02)

### Bug Fixes

* fix: added conditions to prevent release loops ([`c99a48c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c99a48c4fa37aebf191ccbf88bc106c865fcab4a))

### Continuous Integration

* ci(release): exclude semantic-release user from triggers ([`1f3ee46`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1f3ee468e34159405f0562da0ca455b40da4994e))

* ci(release): exclude semantic version commits from triggers

- Add regex pattern to exclude version number commits (e.g. 2.0.0)
- Prevent workflow loops from automated version bumps
- Keep manual workflow dispatch functionality
- Improve automated release handling

[skip ci] ([`2713e6d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2713e6d6e49ecf74471b41f17fe5adcac28638b0))

### Unknown

* Merge pull request #52 from gsinghjay/test/workflow_release

ci(release): exclude semantic version commits from triggers ([`8999a1d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8999a1dcbe6575505984150c3c0878c83863bbd5))


## v2.0.0 (2025-01-02)

### Breaking

* ci: remove redundant tag validation workflow

- Remove tag-validation.yml as validation is handled by semantic-release
- Tag signing and validation now configured in pyproject.toml
- Rely on semantic-release's built-in tag management
- Simplify CI/CD pipeline

BREAKING CHANGE: Tag validation now handled entirely by semantic-release configuration ([`c2bea40`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c2bea40cbd4ab2cc88fe3f4a08b083c393f70332))

* fix(release): pass workflow dispatch inputs to semantic-release

- Add prerelease input handling
- Add force version bump input
- Add prerelease token input
- Enable manual control of release process

BREAKING CHANGE: Manual workflow dispatch now directly controls semantic-release behavior ([`8aa77e5`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8aa77e5145bae6c721a59c700121b035b76b340a))

### Continuous Integration

* ci(release): simplify semantic release workflow

- Remove redundant git committer configuration (handled by pyproject.toml)
- Remove prerelease and force options (handled by workflow_dispatch)
- Keep publish action for GitHub release assets
- Align with python-semantic-release documentation ([`0bcbd03`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0bcbd033d44fccc0707c54275fe37e09894f48c8))

### Documentation

* docs: update workflow documentation

- Update CI/CD badge to point to release workflow
- Replace workflow diagram with new architecture
- Add detailed workflow files structure
- Add workflow execution and skip conditions
- Remove outdated workflow steps section ([`2eab334`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2eab334201a4385938515d2f762b67abda8488eb))

### Unknown

* Merge pull request #51 from gsinghjay/test/workflow_release

ci: remove redundant tag validation workflow ([`a49fabb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a49fabbcd720e8db6038a328d16c077c43d68b30))

* Merge pull request #50 from gsinghjay/test/workflow_release

fix(release): pass workflow dispatch inputs to semantic-release ([`068d5f8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/068d5f84df52d99e962ee7dd8bc0d6afc0ce0a3f))

* Merge pull request #49 from gsinghjay/test/workflow_release

ci(release): simplify semantic release workflow ([`39bc238`](https://github.com/gsinghjay/fast-api-ci-cd/commit/39bc238ee202d79fc14e3e62d82eb064bbf8967c))

* Merge pull request #48 from gsinghjay/doc/new-workflow

docs: update workflow documentation ([`9d64df9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9d64df96a2612e74ef24e9e0dd6dfdc4a292b125))


## v1.6.4 (2025-01-02)

### Bug Fixes

* fix(ci): handle concurrent changes in release workflow ([`1097ec0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1097ec07187a72c41c7c2354fcae15ac1914f47d))

### Continuous Integration

* ci: standardize Poetry usage across workflows

- Unify Poetry configuration across all workflow files
- Remove redundant pip upgrade steps
- Standardize cache configuration
- Configure virtualenvs.create false consistently
- Remove --no-root flag from poetry install commands ([`b809859`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b809859f4d476b80621a101eba50f1d142da7e39))

* ci: prevent workflow trigger loops

- Add conditions to prevent release workflow from running on automated commits
- Remove redundant CI skip conditions from test workflow
- Add explicit conditions to prevent github-actions[bot] from triggering new workflows ([`05236d0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/05236d0ab349f5a64e304443610aa836a02c19b1))

### Unknown

* Merge pull request #47 from gsinghjay/test/verify-workflows

ci: standardize Poetry usage across workflows ([`77d897d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/77d897d5d9223404a5fe06f2cc4d144db55248da))

* Merge pull request #46 from gsinghjay/test/verify-workflows

ci: prevent workflow trigger loops ([`d3798a3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d3798a36629a1fa2b6499eb4cf7779d60ad0e397))

* Merge pull request #45 from gsinghjay/test/verify-workflows

fix(ci): handle concurrent changes in release workflow ([`b2b4250`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b2b42507bfbba33fed7c5a4adfd0c82cd5286f59))


## v1.6.3 (2025-01-02)

### Bug Fixes

* fix(ci): improve tag validation by using git log for tagger info ([`56eb267`](https://github.com/gsinghjay/fast-api-ci-cd/commit/56eb2677fbfba463ac292654af3582dd24a439ac))

* fix(ci): improve tag validation logic and debugging

- Fix tag creator validation condition
- Add better error messages with expected vs actual values
- Maintain security checks
- Fix false positive validation failures ([`5bc40ca`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5bc40ca33c7107f93ca22c51369557a78c29a1f0))

* fix(ci): ensure consistent git author for releases

- Add git committer details to semantic-release step
- Ensure consistent git configuration
- Fix tag validation issues ([`de08aa0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/de08aa02fbe182b596c5457a21e186d388e436b3))

* fix(ci): add required permissions for reusable workflows

- Add pull-requests read permission for lint workflow
- Add checks write permission for test workflow
- Fix workflow permission inheritance ([`e73134a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e73134a255070a433f79f7a84b456738c8dc78fc))

* fix(ci): add workflow dependencies and commitlint configuration (#40)

- Add workflow_call triggers to lint and test workflows
- Configure proper job dependencies in release workflow
- Ensure sequential execution: lint -> test -> release
- Update commitlint rules for consistent line lengths
- Fix workflow reusability issues ([`5c46bb8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5c46bb873c549cb97c6f3e105f8096143fc6d0b4))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`61e3e84`](https://github.com/gsinghjay/fast-api-ci-cd/commit/61e3e84734b9944fcf5e3c305aa3c95b6aad0539))

* docs: update CHANGELOG.md [skip ci] ([`d30beb5`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d30beb511b53c15e5b080dbad3113ad94662625f))

* docs: update CHANGELOG.md [skip ci] ([`f3b2249`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f3b22490e84d48eb962365e5a2f6a12ee0cec1ee))

* docs: update CHANGELOG.md [skip ci] ([`43ff1c2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/43ff1c28df77b37ff8c8dfcc220e871ebf7425e8))

* docs: update CHANGELOG.md [skip ci] ([`2546b4a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2546b4a72bbb37d00b5e384dc82b6ed68d9d2715))

* docs: update CHANGELOG.md [skip ci] ([`ed9486f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ed9486f9469cccdae1ba8bb9d73865b38f0604c2))

* docs: update CHANGELOG.md [skip ci] ([`6ca62a6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6ca62a6fad0adcb501612e5b6af5b58bc99c5527))

* docs: update CHANGELOG.md [skip ci] ([`a55cde7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a55cde7a639fd56fc5c5aef522ae317d0b1bbd1b))

### Unknown

* Merge pull request #44 from gsinghjay/test/verify-workflows

fix(ci): improve tag validation by using git log for tagger info ([`3de3ddc`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3de3ddc89197cbd8e79e4e00684615e783432f62))

* Merge pull request #43 from gsinghjay/test/verify-workflows

fix(ci): improve tag validation logic and debugging ([`dc46e32`](https://github.com/gsinghjay/fast-api-ci-cd/commit/dc46e32ab20ac66f80306a89ecff964d55b92bbb))

* Merge pull request #42 from gsinghjay/test/verify-workflows

fix(ci): ensure consistent git author for releases ([`44cb977`](https://github.com/gsinghjay/fast-api-ci-cd/commit/44cb97789b8df7307107fd50912399d7d32b7e96))

* Merge pull request #41 from gsinghjay/test/verify-workflows

fix(ci): add required permissions for reusable workflows ([`94ee06b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/94ee06bdc6c7d6fa84beadf35aac96e6b22eeff1))

* ci!(workflows): split monolithic CI/CD pipeline into focused workflows (#39)

ci!(workflows): split monolithic CI/CD pipeline into focused workflows

- Split into specialized workflows:
  - lint.yml for code quality checks
  - test.yml for running tests
  - release.yml for semantic versioning and releases
  - tag-validation.yml for ensuring proper tag creation

- Enhanced workflow features:
  - Add changelog generation to release workflow
  - Configure proper npm caching with package-lock.json
  - Use npm ci for deterministic installs
  - Simplify coverage reporting
  - Update gitignore patterns

BREAKING CHANGE: CI/CD pipeline has been completely restructured into separate 
workflows for better maintainability and clarity. This improves pipeline 
reliability, resource utilization, and development experience. ([`5c259c5`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5c259c58f9a0d93aa606b9192ef08184fca32836))


## v1.6.2 (2025-01-02)

### Bug Fixes

* fix(ci): ensure changelog updates on every push

- Add explicit changelog generation step
- Update changelog regardless of release status
- Configure semantic-release to include all commits
- Separate changelog generation from release process ([`57ec646`](https://github.com/gsinghjay/fast-api-ci-cd/commit/57ec6466145f198d89c38b2b2f0f1a81cc8ca3c7))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`6382022`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6382022585ff561f7b2e2d2fb2eb8eab11d90437))

* docs(readme): fix mermaid diagram syntax

- Fix skip conditions node formatting
- Update style definitions to use classDef
- Remove special characters causing parse errors
- Improve diagram readability ([`41cd6e0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/41cd6e0a1071aa268d7f4573b54ef56b44d92ade))

* docs(readme): add workflow diagram and explanation

- Add mermaid flowchart of CI/CD pipeline
- Include detailed workflow steps explanation
- Show job dependencies and conditions
- Add color coding for different stages
- Document skip conditions ([`5e986cb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5e986cb4c4cc7b8972570141237b91ff0132343a))

### Unknown

* Merge pull request #38 from gsinghjay/fix/changelog-updates

fix(ci): ensure changelog updates on every push ([`a365fbf`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a365fbf667debb7fd03e7b9cd10d7df45749e7ab))

* Merge pull request #37 from gsinghjay/develop

Merge pull request #36 from gsinghjay/ci/parallel-jobs ([`45c593a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/45c593ad6a43b0a6861cd07809f18b132142f57e))

* Merge pull request #36 from gsinghjay/ci/parallel-jobs

Ci/parallel jobs ([`f7c80e9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f7c80e945f65dce100117cd69a0af2292472a0f0))

* Merge pull request #35 from gsinghjay/docs/add-workflow-diagram

docs(readme): add workflow diagram and explanation ([`b60a16f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b60a16fd322034fc78ddec4e954e5d1fe9c0f0cb))


## v1.6.1 (2025-01-02)

### Bug Fixes

* fix(ci): simplify release workflow

- Remove separate changelog update step
- Update release job configuration
- Configure changelog for release-only updates
- Follow semantic-release best practices ([`4b19367`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4b19367f226bdf4316015b6bb926c649f1337bb8))

* fix(config): update branch patterns with proper regex

- Use .* pattern for matching fix and feature branches
- Separate patterns for clearer branch matching
- Fix 'branch not in release groups' error ([`197246a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/197246a1163f8b7aff0f8620b21ad952ba935ebc))

* fix(config): update branch patterns for changelog generation

- Add develop branch pattern to release groups
- Include feature/fix branch patterns
- Follow semantic-release documentation recommendations ([`73c7101`](https://github.com/gsinghjay/fast-api-ci-cd/commit/73c71013b80c37e94e6db787b85a329fd1761a16))

* fix(ci): simplify release configuration

- Remove unnecessary prerelease configuration
- Keep only main branch configuration
- Simplify changelog generation command ([`8f72fa1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8f72fa11467b4f48ad4af418c6cca3c890b58340))

* fix(config): remove duplicate branch configuration

- Remove duplicate [tool.python_semantic_release.branches.main] section
- Fix TOML validation error ([`0cc9aeb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0cc9aeb3c3082a2e048b18e37e1f188293887563))

* fix(ci): improve changelog generation and remove coverage artifacts

- Add debug verbosity to semantic-release command
- Remove coverage.xml artifact upload
- Add better debug output for changelog generation
- Fix semantic-release verbose flag position ([`a4f0424`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a4f042496885409fdf7358aed307c76e02d7a4ce))

* fix(ci): add debugging for changelog generation ([`78499ed`](https://github.com/gsinghjay/fast-api-ci-cd/commit/78499ed3c5a720acfb8c8f6badda98f674cbce92))

* fix(ci): remove invalid --prerelease flag from changelog generation ([`2af8359`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2af8359581432fb01095423a5076f517af240e02))

* fix(ci): correct condition logic for github-actions bot in workflow

- Changed OR operator to AND in workflow conditions
- Ensures github-actions bot commits are properly skipped
- Prevents CI/CD infinite loops ([`c3c0db9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c3c0db9dce2ba097780d228ca654ca0c44b6e1c6))

* fix(ci): correct condition logic for github-actions bot in workflow

- Changed OR operator to AND in release job conditions
- Ensures github-actions bot commits are properly skipped
- Prevents CI/CD infinite loops ([`b742535`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b742535af3279930f1f23335ee1dc182afee34d0))

### Unknown

* Merge pull request #34 from gsinghjay/fix/ci-workflow-conditions

fix(ci): correct condition logic for github-actions bot in workflow ([`0bbcf70`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0bbcf7099882c95b412bbbfa32f466347ea3d3dc))


## v1.6.0 (2025-01-02)

### Bug Fixes

* fix(release): use both tags and commits for versioning

- Update semantic-release to use both tags and commits
- Tags for released versions
- Commits for unreleased changes tracking ([`6418e07`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6418e07827443547d90db6555a32100b98e3eaab))

* fix(ci): correct changelog generation in PRs

- Remove invalid --unreleased flag
- Use pyproject.toml configuration for unreleased changes
- Simplify changelog generation command ([`5c4c1b1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5c4c1b17834a6e71ad47b5397465355153a57797))

### Features

* feat(ci): add changelog updates for pull requests

- Add unreleased section to changelog generation
- Update changelog during PR development
- Configure semantic-release for unreleased changes ([`ed12395`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ed12395784275436148d659f3a925a1b9ef8653c))

### Unknown

* Merge pull request #33 from gsinghjay/develop

feat(ci): add changelog updates for pull requests ([`ea8d89f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ea8d89fcef0c72a02758c201f2bf065c15c45c41))


## v1.5.1 (2025-01-02)

### Bug Fixes

* fix(ci): ensure tests run on pull requests

- Fix conditional logic for PR events in workflow
- Separate PR and push event conditions
- Ensure lint and test jobs always run on PRs ([`dcd4844`](https://github.com/gsinghjay/fast-api-ci-cd/commit/dcd484442c9129df9518fbeb82b4ba9a3faa6ed4))

* fix(ci): prevent workflow recursion from bot commits

- Add paths-ignore for CHANGELOG.md updates
- Add conditional checks to skip CI on bot commits
- Add skip conditions for release and changelog updates
- Prevent workflow triggers on [skip ci] tags ([`fd2a99b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fd2a99b55ca63c03ad65df61b66fb6d6a2af0841))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`ddc80bb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ddc80bb23282263520ebe497c15de3cb798f51de))

### Unknown

* Merge pull request #32 from gsinghjay/develop

fix(ci): prevent workflow recursion from bot commits ([`a3df4a9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a3df4a94ad4fcdd27145d7c239bbbf922e87092f))


## v1.5.0 (2025-01-02)

### Chores

* chore(release): update semantic-release config for main-only releases ([`d18cf04`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d18cf04eba0355c83785433c95a3095a246dba24))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`6b62894`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6b62894aa0d09c5733d46d621c966dbe25063355))

### Features

* feat(ci): simplify release workflow to main branch only ([`6ee5af4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6ee5af43c5693d45062b7d841bc9cf3936827eef))

### Unknown

* Merge pull request #31 from gsinghjay/develop

Develop ([`b508551`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b508551f16a670ef7b5b3a7e65598a8bb085cf12))


## v1.4.0 (2025-01-02)

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`90db080`](https://github.com/gsinghjay/fast-api-ci-cd/commit/90db08060a0f7325ab489215f2f3676b0cadbf48))

### Features

* feat: add color code validation ([`32c497f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/32c497f726986a057fc314b5867e6676023fc915))

### Unknown

* Merge pull request #30 from gsinghjay/develop

Develop ([`298e091`](https://github.com/gsinghjay/fast-api-ci-cd/commit/298e0916e82c2077485c4f5e02f3560d6d3bced2))

* Merge branch 'main' into develop ([`001a3c9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/001a3c9a14e5214f48c418c47088235abe24bb02))


## v1.3.0 (2025-01-02)

### Bug Fixes

* fix(ci): update semantic-release config to handle beta versions correctly ([`0205e1b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0205e1bd2dac59dc1e3c0de4a978e7ab942503c8))

* fix(ci): improve branch handling and semantic-release configuration ([`e5135fc`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e5135fc0da76442ee7de0ba72bfd9803bb9c3247))

### Chores

* chore: merge develop and resolve conflicts ([`b48b4cc`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b48b4cc84ee315cadbe78fe8a445f7f29ecfa402))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`f6e1604`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f6e1604cdf37ead8e326f4ebd6167f3ee724c069))

* docs: add documentation for custom QR code colors (#28) ([`2f037d0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2f037d046a616df30031d2864ba340e378192ed2))

* docs: add documentation for custom QR code colors (#27) ([`28d8ca6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/28d8ca68beeb7947ac20636cdae743bf2b073464))

* docs: add workflow debugging commands ([`34b6f6d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/34b6f6dbfee768c1e091bdd395a36da89a2f80c9))

* docs: add documentation for custom QR code colors ([`5c9b512`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5c9b5127d0d6085b44d6320ef05c756a33d73d0a))

* docs: update CHANGELOG.md [skip ci] ([`5dc58d0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5dc58d0157f1d0d47904a698592dd7caffcba151))

* docs: enhance README with detailed workflow and debugging instructions ([`f6987fe`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f6987febb2112a3e1ce7119dc44d8d9887b0aad8))

### Features

* feat: add QR code size customization options ([`e1ba631`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e1ba631b99cf3eff3fc9f5c98d3678e3960fe37c))

* feat: add support for custom QR code colors ([`8697ea0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8697ea0234c945406f949d386f3a975fe9b00a37))

* feat(ci): enhance release verification with detailed status messages ([`5f00625`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5f00625eac215dea58f14327725c1e6644259763))

### Unknown

* Merge pull request #25 from gsinghjay/develop

feat(ci): enhance release workflow with semantic options ([`a49f0ed`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a49f0ed28436640916f6ef38609fcd459d8338d0))

* Merge pull request #29 from gsinghjay/feature/add-qr-size-option

feat: add QR code size customization options ([`55b2eeb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/55b2eebe1d0ad7977d6eb026ee482fa0b86744c1))

* Merge pull request #26 from gsinghjay/docs/add-custom-colors-docs

Docs/add custom colors docs ([`30445f3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/30445f3c2eaff3ecd2d0c7dadb19fc80466f5d1e))

* Merge branch 'dev' of github.com:gsinghjay/fast-api-ci-cd into develop ([`8504379`](https://github.com/gsinghjay/fast-api-ci-cd/commit/850437963d6c5245bdc9d94473f3463ac9dac2fb))

* Merge pull request #23 from gsinghjay/main

chore: sync `dev` and `main` ([`c4137b6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c4137b6224ee434a55cdffc3fe3b931444a09964))


## v1.3.0-beta.1 (2025-01-01)

### Bug Fixes

* fix(ci): simplify Git authentication and use consistent token handling ([`ad23d07`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ad23d072332ce033e20429370ae3df4ea13d3d50))

* fix(ci): improve Git authentication verification and sync ([`a072b64`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a072b6458c901b718c4a11e01b0c2ee9113dd581))

* fix(ci): improve Git authentication across all workflow steps ([`20b495b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/20b495b5c042f012068d4bda4756fc44828785fe))

* fix(ci): enhance Git authentication with PAT and add debugging steps ([`03bff11`](https://github.com/gsinghjay/fast-api-ci-cd/commit/03bff118f1f441829e576665876b80d4cc604cf9))

* fix(ci): enhance Git authentication and build configuration ([`56efc69`](https://github.com/gsinghjay/fast-api-ci-cd/commit/56efc694d46569a29ef4c9aecc7423b46b25a9d6))

* fix(ci): enhance GitHub token configuration and permissions ([`7af467c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7af467cb561a08b5b7160bce5271b09a9637670d))

* fix(ci): correct Git URL configuration for semantic release ([`022c87d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/022c87d029e46aa4405eb7daf4231107dea52f44))

* fix(ci): improve Git authentication for semantic-release

- Use Git URL rewriting for authentication
- Remove credential helper in favor of insteadOf configuration ([`009aec2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/009aec27b68cf3f589617c1929916c44542a03cd))

* fix(ci): improve Git authentication for semantic-release

- Add Git credential helper configuration
- Pass GitHub token through environment variables
- Simplify Git configuration ([`e9d8b0c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e9d8b0c7b80b7ed04f36e1b3685c8347861f8289))

* fix(ci): use official Python Semantic Release GitHub Action

- Replace custom release script with official action
- Update environment variables to use PSR_ prefix
- Add GitHub Release Assets publishing ([`78789f1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/78789f162697ff73ac1edf3a17888b9230febefd))

* fix(ci): correct git authentication for semantic-release

- Replace Git URL rewriting with direct remote URL configuration
- Use correct GitHub URL format with authentication token ([`98fe3b8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/98fe3b8d95525d822555484b1dc40878f1d9295b))

* fix(ci): handle both shallow and complete repositories in git fetch

- Remove --unshallow flag to support complete repositories
- Add explicit origin remote specification ([`642e335`](https://github.com/gsinghjay/fast-api-ci-cd/commit/642e33591146ad14e9d42b6f9e68eb8eb76851d3))

* fix(ci): improve git authentication for semantic-release

- Use Git URL rewriting for authentication
- Ensure complete repository history
- Remove redundant credentials configuration ([`fb41011`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fb41011e72160926d651c8b547315a212b44a904))

* fix(ci): update git authentication method

- Use Git credential store for authentication
- Add GIT_CREDENTIALS environment variable
- Improve branch tracking configuration ([`f2f3287`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f2f32878dcd8b5755bc51e0f4c6d09f588590dcb))

* fix(ci): improve git authentication for semantic-release

- Update Git remote configuration for better token handling
- Add explicit GITHUB_TOKEN environment variable
- Fix branch reference in git pull command ([`72eb609`](https://github.com/gsinghjay/fast-api-ci-cd/commit/72eb6092fe163cf001f8ce44e5a1b1a565832e83))

* fix(ci): configure git remote with authentication token

- Add proper HTTPS authentication for Git operations
- Use GITHUB_TOKEN for remote URL authentication ([`70a4049`](https://github.com/gsinghjay/fast-api-ci-cd/commit/70a4049760f283f39b701ff14c5fc1011ff29129))

### Continuous Integration

* ci: improve ci/cd workflow reliability and tag handling

- fix: correct dependency between tag-validation and release jobs
- feat: add annotated tag support for better validation
- fix: standardize python-semantic-release version to 9.15.0
- fix: improve GitHub CLI authentication
- chore: enhance workflow_dispatch input handling ([`bbfa061`](https://github.com/gsinghjay/fast-api-ci-cd/commit/bbfa061ccd817600bca70d0f56eec7b80870427b))

### Documentation

* docs: add branch protection rules and naming conventions ([`851e65b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/851e65b1ab265321f13fa727aff77e9d43997d64))

* docs: update CHANGELOG.md [skip ci] ([`ff10ee8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ff10ee80d64129025b50e18286368f96d7a2a262))

* docs: update mermaid diagram to show complete release flow ([`ce2ecad`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ce2ecadbd28dd9a7258197026cb64af1c34b58dc))

### Features

* feat(release): add branch-specific release configurations

- Configure main branch for regular releases
- Configure develop branch for beta releases
- Configure release/* branches for RC releases ([`b8ec310`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b8ec310ee2643add5d24e69c8c68c40f9364c22d))

* feat(ci): enhance release workflow with semantic options

- Add manual workflow trigger with configurable parameters
- Support prerelease versions with custom tokens
- Add build metadata support
- Enable commit signing with SSH keys
- Improve version control with force level options ([`0d0fb10`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0d0fb1017a72d763d34af1dbda4a53071ba32f20))


## v1.2.0 (2025-01-01)

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`c55ebf7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c55ebf7749670ea71b5b76472a7af378afc73f7a))

* docs: update CHANGELOG.md [skip ci] ([`7bc972b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7bc972b344f0bdd0ed8c8aa10a3e4a55aa40de82))

* docs: add manual release workflow documentation ([`d4e82a7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d4e82a7f10621ce3bc8a1f7652e2736ca7060af8))

### Features

* feat(ci): add automated pre-release patterns for different branches ([`7fae1bc`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7fae1bc47cac96731d3e877c80c1e297d94e16a8))


## v1.1.0 (2025-01-01)

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`09c869a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/09c869a9edc191cee2ec6ba75a8e55a06b19b35c))

### Features

* feat(ci): enhance release workflow with semantic options and manual triggers ([`0b25b9d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0b25b9d7e93d28d6e8a7c74477fc02b0ec025a5b))

* feat(ci): enhance release workflow with semantic options
- Add manual workflow trigger with configurable parameters
- Support prerelease versions with custom tokens
- Add build metadata support
- Enable commit signing with SSH keys
- Improve version control with force level options ([`b5ed280`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b5ed280626d96fe56c7a1581eaf7c395dc7a6730))


## v1.0.11 (2025-01-01)

### Bug Fixes

* fix(changelog): exclude github-actions bot commits from changelog

- Add exclusion patterns for github-actions[bot] commits
- Filter out automated changelog updates
- Maintain clean changelog without bot entries ([`52010b0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/52010b08635c1e6b034015acf1660b2e48087813))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`2ebfbde`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2ebfbde66aca1abb537c6ebeb7370c7fa9ef0222))


## v1.0.10 (2025-01-01)

### Bug Fixes

* fix(changelog): exclude [skip ci] and related patterns from changelog ([`697fd83`](https://github.com/gsinghjay/fast-api-ci-cd/commit/697fd83fd785c9b8caf1b39c1fa40f4ad90035ec))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`7c6ae65`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7c6ae65b8b02bc1f4f63556076ef28126cc675f1))

* docs(readme): add comprehensive table of contents and badges

- Add status badges for CI/CD, release, Python version, and code coverage
- Add structured table of contents with anchor links
- Add sections for security, Docker, API docs, performance, testing, and error handling ([`1d8d53d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1d8d53d911b7de7895ecba8a086a4fc076e4add4))

* docs: remove [skip ci] annotations from changelog ([`7d0e78d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7d0e78dda4346c407c897ab97c46ef56424b4910))


## v1.0.9 (2025-01-01)

### Bug Fixes

* fix(ci): remove invalid --ci flag from semantic-release commands ([`9636c0f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9636c0fdd9de821e6d42e59d2a78aaaa3ef369a7))

* fix(ci): add git sync step and use CI mode for semantic-release ([`431296c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/431296c47455bf4adaa96aea85cdee4f1d673786))

* fix(ci): correct version retrieval in release verification ([`e85e60d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e85e60d879cbcd00d133e2ebed33ed356048d6ea))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`334f0f0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/334f0f0988392e915727752b1488287ee937e3ba))

* docs: update CHANGELOG.md [skip ci] ([`293ad54`](https://github.com/gsinghjay/fast-api-ci-cd/commit/293ad54cb99b57bec730b24fab7a93457d6a901b))

* docs: update CHANGELOG.md [skip ci] ([`9aa26e9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9aa26e9f1cab790ef46d1e326333b23ba71ca411))

* docs: update CHANGELOG.md [skip ci] ([`184b292`](https://github.com/gsinghjay/fast-api-ci-cd/commit/184b2920b500b301bd03233d951456c3e218ae19))

* docs: update CHANGELOG.md [skip ci] ([`af6231a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/af6231ae1f4ade760ad01f720f6654fbe334162d))

* docs: enhance README with semantic-release command details ([`3ab6eb3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3ab6eb361490315561a9e167595a27a1476d3533))

* docs: update README with detailed versioning and CI/CD information ([`9106aa9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9106aa9eb79a1270a63904dc1519e11edd8b9e01))

### Refactoring

* refactor(ci): simplify release process using semantic-release commands ([`8225d08`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8225d087dd8437ee685d00cfc5a69ec3b11ede23))

### Unknown

* Merge branch 'main' of github.com:gsinghjay/fast-api-ci-cd ([`88f04c2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/88f04c29a130a074d86d44d785684463b9da90c5))


## v1.0.8 (2025-01-01)

### Bug Fixes

* fix(ci): correct release notes generation in CI/CD pipeline ([`9849cdb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9849cdb421a14894235c70e60beb895cac71165a))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`559bf45`](https://github.com/gsinghjay/fast-api-ci-cd/commit/559bf451e22a3f03c93a58ca1768dde118204175))


## v1.0.7 (2025-01-01)

### Bug Fixes

* fix(ci): improve changelog generation using semantic-release ([`2540961`](https://github.com/gsinghjay/fast-api-ci-cd/commit/25409613951f1d4e3dfa4452c478151457479c1a))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`d33b594`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d33b5941831facf5c874eb089dae7ee1cb596a9e))


## v1.0.6 (2025-01-01)

### Bug Fixes

* fix(ci): improve changelog generation configuration

- Add changelog components configuration
- Exclude release commits from changelog
- Configure changelog formatting ([`569e547`](https://github.com/gsinghjay/fast-api-ci-cd/commit/569e547ae6ccd4864e2d4f1673b9bbb76b2014c0))

### Chores

* chore(release): 1.0.6 [skip ci] ([`e8ee582`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e8ee58270e481c4e326e848c4cbf70d38e389ac9))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`892c342`](https://github.com/gsinghjay/fast-api-ci-cd/commit/892c34220d30ee94e96ade910a82b27d53e16464))


## v1.0.5 (2025-01-01)

### Bug Fixes

* fix(ci): add GitHub release creation to CI/CD pipeline

- Add GitHub CLI installation
- Create GitHub releases for tags
- Add release verification step ([`5a434ca`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5a434ca82fa7a95a9e1eadac4351e69102ddbb0c))

### Chores

* chore(release): 1.0.5 [skip ci] ([`0f4c74a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0f4c74a0677f7325b2181dd96224a40110924c28))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`a6d7a09`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a6d7a097a096fd683c3b34d3630f694ac35d89ae))


## v1.0.4 (2025-01-01)

### Bug Fixes

* fix(version): align version numbers with git tags

This commit fixes the version number discrepancy
between files and git tags, ensuring consistent
versioning across the project. ([`67e0852`](https://github.com/gsinghjay/fast-api-ci-cd/commit/67e0852517a7d13d2c3cb5a00ac0501d235f99dc))

### Chores

* chore(release): 1.0.4 [skip ci] ([`b8d50a7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b8d50a7fe330e21e00e6acafb2689c268088780d))

### Code Style

* style: apply pre-commit hooks and formatting

- Format code with black
- Fix flake8 violations
- Add pre-commit configuration
- Update gitignore patterns
- Fix YAML formatting
- Update documentation formatting ([`da67f7c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/da67f7c01e91141e31141231be273c6452398dfa))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`addaa9b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/addaa9ba5502fb14c3a91e9e4da042362ae55554))

* docs: update CHANGELOG.md [skip ci] ([`db0dbde`](https://github.com/gsinghjay/fast-api-ci-cd/commit/db0dbde5c77700cf764bdab678f2767910fd5bbc))


## v1.0.3 (2025-01-01)

### Bug Fixes

* fix(ci): improve version management and changelog generation

- Add proper version increment logic based on commit types
- Fix duplicate changelog entries
- Implement semantic version bumping based on conventional commits
- Add comprehensive change detection
- Improve release decision logic ([`b91516a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b91516af52d89def93abf2940996139c95566e22))

* fix(ci): prevent duplicate tag creation in release step

- Add tag existence check before creation
- Skip version update if tag exists
- Improve error handling for existing tags
- Add informative message when skipping release ([`8584c27`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8584c275d5a25ecb4c9ee784b9fc3fcf99985f20))

### Chores

* chore(release): 1.0.3 [skip ci] ([`b26ce30`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b26ce3070718d04f95c6af68a9e5a29059db3fdc))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`59f2bb2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/59f2bb2d455cf70730859144f8e47bd917fa520a))

* docs: update CHANGELOG.md [skip ci] ([`d6f8d05`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d6f8d0592c5fca5f41b83aa8a0c1a9677b9242b4))

### Unknown

* Merge branch 'main' of github.com:gsinghjay/fast-api-ci-cd ([`2f8170e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2f8170e22f4c9e0ea671222df61e699e865cc4f0))


## v1.0.2 (2025-01-01)

### Bug Fixes

* fix(ci): improve semantic release version management

- Add explicit version checking
- Use git tags for version tracking
- Implement proper semantic version bumping
- Add commit message validation ([`c55d026`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c55d0263553ac2b1d11d53bf01bae2f0427d6346))

### Chores

* chore(release): 1.0.2 [skip ci] ([`8215ee4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8215ee4aa344a48843a9a4b17c72008f1721eb24))

* chore(release): 0.1.1-dev.0 [skip ci] ([`707e682`](https://github.com/gsinghjay/fast-api-ci-cd/commit/707e682cb489d685902e5414476361147e604732))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`3e8eaf6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3e8eaf680efe7fe82ea584d00db003a54bc54650))

* docs: update CHANGELOG.md [skip ci] ([`69756f2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/69756f292abd59fc95519e1a16fd671208f7ebf3))

* docs: update CHANGELOG.md [skip ci] ([`3628a92`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3628a9263a44e96541158e63c93c4867b5d0081f))

### Refactoring

* refactor(ci): remove redundant post-merge verification

- Remove post-merge verification job
- Simplify workflow dependencies
- Reduce CI execution time
- Rely on existing test and release jobs for verification ([`ac9d317`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ac9d31755196877e7836f8e216beddda31d19ebb))

* refactor(ci): simplify release process

- Remove dev version handling
- Simplify version management
- Remove unnecessary version checks
- Streamline release process to main branch only ([`84d1be7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/84d1be73b550e1ae30d07338c47c6a4f192161c8))

* refactor(ci): remove deployment notification step

- Remove GitHub issue comment notification
- Simplify post-merge-verification job
- Remove unnecessary notification dependencies ([`b135f70`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b135f70ff0a437796a3f0913c2940d4875a67447))

### Unknown

* Merge branch 'main' of github.com:gsinghjay/fast-api-ci-cd ([`c68be39`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c68be394e11e20783c9afe9db9342b3cf1a89509))


## v1.0.1 (2025-01-01)

### Bug Fixes

* fix(ci): remove remaining dev version update configurations

- Remove update-dev-version job completely
- Clean up post-merge-verification job dependencies
- Remove dev version update logic
- Fix invalid PEP 440 version error ([`d6f0424`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d6f04247bee1a3823cfe7ab527f40acbb9fbde16))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`be9f5a9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/be9f5a97110464b0369e6d633e5a2e2a5557da95))

* docs: update CHANGELOG.md [skip ci] ([`e223933`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e223933affd531780688f03c6014e196cf6a6a1f))

### Refactoring

* refactor(ci): remove dev version updates and notifications

- Remove update-dev-version job
- Remove notification step from post-merge-verification
- Update job dependencies to reflect removed jobs
- Simplify post-merge verification process ([`6c528ce`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6c528ce86c26118e4f6895c3cdfb2b57388130b4))

### Unknown

* Merge pull request #22 from gsinghjay/dev

fix(ci): remove remaining dev version update configurations ([`25b5e9b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/25b5e9b77534d57b6f72b0fbf126393b336499b6))

* Merge pull request #21 from gsinghjay/dev

Dev ([`42f9294`](https://github.com/gsinghjay/fast-api-ci-cd/commit/42f9294cf03b7a76d6d2975f360a2caed590a55d))

* Merge branch 'main' into dev ([`e5ef30c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e5ef30c6d37a923d5e5d3b6aa18975c45eb451db))


## v1.0.0 (2025-01-01)

### Breaking

* fix(ci): remove explicit branch flag from semantic-release

- Remove redundant --branch flag as it's not needed with pyproject.toml config
- Simplify semantic-release command for better maintainability
- Ensure compatibility with semantic-release configuration in pyproject.toml

BREAKING CHANGE: Removes explicit branch flag from semantic-release command.
Branch configuration is now exclusively managed through pyproject.toml. ([`58a8169`](https://github.com/gsinghjay/fast-api-ci-cd/commit/58a8169013e0f00c70553496f27bbe28b17c7c53))

* fix(ci): improve semantic-release workflow and permissions

- Update semantic-release configuration in pyproject.toml
- Enhance release job with proper version handling
- Add dev branch version management
- Add proper git tagging and changelog updates
- Document required repository permissions

BREAKING CHANGE: This updates the semantic-release configuration and
requires specific GitHub repository permissions to be set. ([`3723090`](https://github.com/gsinghjay/fast-api-ci-cd/commit/372309076ca902404431964b9d9cebe0fb7dece0))

### Bug Fixes

* fix(ci): resolve release step git sync issues

- Add git pull with rebase to sync with remote
- Combine git pushes to reduce race conditions
- Add force flag to ensure version updates succeed
- Improve release step error handling ([`eea5188`](https://github.com/gsinghjay/fast-api-ci-cd/commit/eea5188da46653ab6922e861e3ad932d6440b582))

* fix(ci): simplify changelog update step after removing branch protection

- Remove complex PR creation logic since branch protection is disabled
- Use direct push to current branch for changelog updates
- Maintain basic git configuration for bot commits ([`4d33e06`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4d33e06c78d41004a86634daece3dc62ab4fe3ff))

* fix(ci): resolve duplicate branch configuration in pyproject.toml

- Remove duplicate branch configuration entries
- Keep single unified branch configuration under [tool.python_semantic_release.branches]
- Fix "Cannot declare branches.dev twice" error
- Ensure semantic-release can properly identify release groups

Fixes error: Cannot declare ('tool', 'python_semantic_release', 'branches', 'dev') twice ([`4691097`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4691097706204849781d84c73b8e005f588ba4e0))

* fix(ci): update semantic-release branch configuration format

- Update branch configuration format in pyproject.toml to match semantic-release 9.x expectations
- Simplify branch configuration by using direct format instead of nested sections
- Fix "branch not in release groups" error by using correct configuration structure

Related to: Previous commit that removed --branch flag from workflow ([`9b03616`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9b03616b7369c101176081218a0ce4d004fc219d))

* fix(ci): correct semantic-release version command in dev workflow

- Remove unsupported --branch flag from semantic-release command
- Rely on pyproject.toml branch configuration instead
- Maintain backward compatibility with semantic-release 9.x ([`15b6ef9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/15b6ef976a1c6fff0b42f241cf39f516cd31ee28))

* fix(ci): resolve dev branch release configuration

- Add default branch setting in pyproject.toml
- Simplify semantic-release branch configuration
- Add explicit --branch flag to release command
- Remove redundant branch configurations

This fixes the "branch 'dev' isn't in any release groups" error
and enables proper alpha releases on the dev branch. ([`bacdbb1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/bacdbb172850b0ea62052558614d09e87ec0e2f3))

* fix(ci): correct semantic-release command syntax

- Remove incorrect --prerelease flag
- Rely on branch configuration for alpha releases
- Simplify release command to use configuration

This fixes the "unexpected extra argument" error in the dev release workflow. ([`d94883b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d94883b507f1914edf2111be6b82be5b33fc0aea))

* fix(ci): resolve semantic-release configuration conflicts

- Remove duplicate branch configurations
- Add branch_patterns section for better branch matching
- Fix configuration structure to prevent value overwriting
- Clarify branch release patterns for main and dev

This fixes the "Cannot overwrite a value" error in the CI pipeline. ([`125ec19`](https://github.com/gsinghjay/fast-api-ci-cd/commit/125ec1925fcaa1115e730c588c1cc4a5fbca1b17))

* fix(ci): correct semantic-release configuration for alpha releases

- Update semantic-release branch configuration in pyproject.toml
- Add explicit branch handling for dev and main
- Add --prerelease alpha flag to dev branch releases
- Fix branch recognition issue in release workflow
- Add explicit git checkout for dev branch

This fixes the issue where no releases were being generated
on the dev branch and ensures proper alpha versioning. ([`9caebc7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9caebc78728868c93d7fa22774ce0894cf0f9d96))

* fix: update branch patterns in semantic-release config ([`fcd7f79`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fcd7f79464968680fb2c97327e5d030b9fda967e))

* fix: remove unsupported flags from semantic-release commands ([`590b51b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/590b51b9315dc1f5e4a5dd6a23b20a908d5c6444))

* fix: improve changelog generation with force flag and version print ([`4cb19ad`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4cb19ad7c146fa46fa5c7239c76ab5df02492307))

* fix: update semantic-release commands to match v9.15.0 documentation ([`41b8fe1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/41b8fe1af632998b6ac01d3ac09aad6606bd246a))

* fix: update poetry lock handling in CI/CD pipeline ([`f4de1b4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f4de1b4345566a36addd634eae2868718b950ab8))

* fix: update changelog generation to work on all branches ([`cc22720`](https://github.com/gsinghjay/fast-api-ci-cd/commit/cc227202bab703223f8f218f06f32fafeab48694))

* fix: update workflow to handle dev branch merges ([`1e269d0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1e269d0102d98c4079e9154c475f13204c30ed18))

* fix: update to python-semantic-release 9.x configuration format ([`316856b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/316856b4c52f52add7bae3dcb655721953a6c15e))

* fix: update version_toml format in semantic-release config ([`0c456ed`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0c456edbab9365a53ac0a3fe12a3d2cdbcd947cc))

* fix: update semantic-release configuration format ([`f332024`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f3320242aba7757250ef43fe52ee7bed12333056))

* fix: update semantic-release flags for version 9.x ([`2f7d7c3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2f7d7c3bd89812e6ff161d86fee8291bf798eba4))

* fix: improve changelog generation and branch handling ([`c7f0bc6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c7f0bc6f91ab2d02ade56797f6d4c72cd98d8935))

* fix: improve semantic-release configuration and workflow ([`1df8745`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1df874501667516c4b5eb4afa0b3d6277f5a2973))

* fix: update semantic-release configuration for version 9.x ([`ee23aba`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ee23ababd942ddfe685d03e2211191999c25467d))

* fix: update semantic-release version variable configuration ([`64b26e6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/64b26e68f4228c237119f6ce3bcb71ff20e90853))

* fix: update semantic-release build command configuration ([`1cd7266`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1cd7266690bf4bbf8dedb7c5772763f5ed4b6f79))

* fix: configure semantic-release for changelog generation ([`58bfc6b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/58bfc6bcaa10ec80cadc7d082565211acc8ff1c3))

* fix: use string format for Python versions in matrix ([`9a402a3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9a402a37712d1540b9c0c1c32ed143040f6d23d6))

* fix: ensure black is installed before running lint checks ([`4476fff`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4476fff05f9692005723662940d58fbabaa01f24))

* fix: update GitHub Actions workflow with correct action references ([`b81d444`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b81d444289d28d8dbbf74a2e8daee01cc9bb8695))

* fix: update dependencies and replace deprecated on_event with lifespan ([`38d748b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/38d748b1c206b34d3cfd2a397d3315814e6e8a82))

### Chores

* chore: bump version to 0.1.1-dev.0 [skip ci] ([`727dd70`](https://github.com/gsinghjay/fast-api-ci-cd/commit/727dd7047f71762a7a830bddf9dbdd53f2791afe))

* chore(release): bump version and update changelog [skip ci] ([`88aba68`](https://github.com/gsinghjay/fast-api-ci-cd/commit/88aba685be1fbafbf2956694876f3a0ea4f344ae))

* chore: re-add project files without cache ([`46f0bf7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/46f0bf7d5c0ccd7b95983f6dca8acf1347673c42))

* chore: add .gitignore file ([`ca11881`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ca1188162ac75c5e57b42c081039d4106d1ae0d5))

### Code Style

* style: format code with black ([`4c0449a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4c0449a9b4313c625575a3c5ce262cce6ec6ea80))

### Continuous Integration

* ci: enable CI/CD pipeline for all branches ([`3083dd1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3083dd1bd72ff48000e155884a6bdf5dd568753a))

* ci: standardize poetry installation and lock file handling ([`e802d7e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e802d7edc5cc431fa47eac2f17efc49c5ef6627c))

* ci: update all Python versions to 3.11 ([`cd70ae6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/cd70ae67f60c9f36fbd7e6e7a383bd159302475b))

* ci: remove Python 3.9 from test matrix ([`320239c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/320239c9e3061f8cb061b611326f22acf291c19a))

* ci: handle poetry.lock file in CI/CD pipeline ([`105f017`](https://github.com/gsinghjay/fast-api-ci-cd/commit/105f0176e6760828503b618431a528fe87a7f5fa))

* ci: update Python version matrix to 3.9-3.11 ([`ed276a1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ed276a1e5b2a4c4fcca29162bc3f9af55639c09a))

* ci: switch to wagoid/commitlint-github-action for commit linting ([`928b238`](https://github.com/gsinghjay/fast-api-ci-cd/commit/928b2385d98278ad01f49a9e96751a8162316b0f))

* ci: fix commitlint configuration and workflow ([`befcdf3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/befcdf3db1752523e6f8cf46e32638f9c10aea8f))

### Documentation

* docs: update CHANGELOG.md [skip ci] ([`0423265`](https://github.com/gsinghjay/fast-api-ci-cd/commit/04232653f0f2f0044ebfcd60d4800aa47c3e3a00))

* docs: update CHANGELOG.md [skip ci] ([`896cf4e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/896cf4e3c5228e7f0422ed0966e27b0afd0cf100))

### Features

* feat(ci): add alpha release support for dev branch

- Add semantic-release branch configuration for alpha releases
- Add dedicated release workflow for dev branch
- Configure prerelease tokens and version format
- Maintain separate version tracks for dev and main branches

This enables automatic alpha releases when merging to dev branch,
while maintaining standard releases on main. ([`1675520`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1675520d37064c770fdb8dd383e7f014a5e66063))

* feat: enable changelog updates in feature branches ([`3f98945`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3f98945546615681e5826d19586a0ce65846d800))

* feat: add changelog generation to CI/CD pipeline ([`93241cb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/93241cb66dcbaf28d2e5bfd29e956eb4cc8ea520))

* feat: add custom color support for QR codes ([`3d10cd8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3d10cd8be9fe78d429219a33e92921dc71b53b0c))

* feat: add structured logging configuration ([`a6fff8e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a6fff8e7a9ded98d0d73b0b205d2eb3f42179e3c))

* feat: add QR code generation functionality ([`9fbb062`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9fbb0627c04420588903c548c0b649ce5e7e416f))

* feat: initial project setup with basic FastAPI application ([`9b48962`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9b489623ca64b390e10124ae5d6efb0cb1ad4ad3))

### Refactoring

* refactor(ci): simplify release process and changelog generation

- Remove alpha release configuration
- Simplify semantic-release config
- Update changelog only on main branch
- Remove unnecessary release-dev job ([`73cee3f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/73cee3f3a5ae0135457783b1d6e827578edb00bc))

### Unknown

* Merge pull request #20 from gsinghjay/dev

Dev ([`b0050d0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b0050d06ff15ac1702df749a70f5ba0f50c74f4a))

* Merge pull request #17 from gsinghjay/dev

Dev ([`391f4a3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/391f4a3ee35b1477d1a6be0d4d94336550adf464))

* Merge pull request #3 from gsinghjay/dev

Dev ([`7253767`](https://github.com/gsinghjay/fast-api-ci-cd/commit/72537674273c254568e02160eb7dfff0ea46d53e))

* Merge pull request #19 from gsinghjay/ci/fix-workflow

fix(ci): resolve release step git sync issues ([`53746f3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/53746f32a511ac75e3f6a7c564fd9a99825c141b))

* Merge pull request #18 from gsinghjay/ci/fix-workflow

refactor(ci): simplify release process and changelog generation ([`9a97d18`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9a97d18f197511c5539019c44dfc2158f7f8b5a9))

* Merge pull request #16 from gsinghjay/ci/fix-workflow

fix(ci): simplify changelog update step after removing branch protection ([`bd69f13`](https://github.com/gsinghjay/fast-api-ci-cd/commit/bd69f13478adfd1aa0c216e775ad13bf856fbb3b))

* Merge pull request #15 from gsinghjay/ci/fix-workflow

fix(ci): update semantic-release branch configuration format ([`cca9c70`](https://github.com/gsinghjay/fast-api-ci-cd/commit/cca9c7017d9a5fb476a0ff2589e0db6b6b0503a3))

* Merge pull request #14 from gsinghjay/ci/fix-workflow

fix(ci): remove explicit branch flag from semantic-release ([`73003a0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/73003a0b9e482be5894bf15f585433fe3f2f123e))

* Merge pull request #13 from gsinghjay/ci/fix-workflow

fix(ci): correct semantic-release version command in dev workflow ([`ccdc474`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ccdc474201563362d4bcc82e11fb78bb3ed499c2))

* Merge pull request #12 from gsinghjay/ci/fix-workflow

fix(ci): resolve dev branch release configuration ([`7c4dd0a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7c4dd0ad0908fb77be0741e9ba1fb1ec45715625))

* Merge pull request #11 from gsinghjay/ci/fix-workflow

fix(ci): correct semantic-release command syntax ([`35b7dfb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/35b7dfb60556de765313ff4f6305e47ca9bfd662))

* Merge pull request #10 from gsinghjay/ci/fix-workflow

fix(ci): correct semantic-release configuration for alpha releases ([`3b0bb2b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3b0bb2b53c15177c01e481e4a3dbfb14c98e4cba))

* Merge pull request #9 from gsinghjay/ci/fix-workflow

fix(ci): improve semantic-release workflow and permissions ([`1932877`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1932877b5c527835016618089c457f4fbd3e4890))

* Merge pull request #8 from gsinghjay/ci/fix-workflow

Ci/fix workflow ([`dc6a951`](https://github.com/gsinghjay/fast-api-ci-cd/commit/dc6a951426993fc5f8f467e81e46a91769dc787e))

* Merge pull request #7 from gsinghjay/ci/fix-workflow

fix: improve changelog generation with force flag and version print ([`7a31f4b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7a31f4b688eebdad0d4b7516adfc7439debd1fc9))

* Merge pull request #6 from gsinghjay/ci/fix-workflow

fix: update semantic-release commands to match v9.15.0 documentation ([`09fa026`](https://github.com/gsinghjay/fast-api-ci-cd/commit/09fa02676b965400919000b088dde267423f724f))

* Merge pull request #5 from gsinghjay/ci/fix-workflow

Ci/fix workflow ([`a370d2d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a370d2d29ed5a9340606811a0dfe9bcbb701c9a4))

* Merge pull request #4 from gsinghjay/ci/fix-workflow

Ci/fix workflow ([`b5c1839`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b5c183961e340ce13c31e74cb7cf95a653a05f91))

* Merge pull request #2 from gsinghjay/feature/customize-qr-code

feat: add custom color support for QR codes ([`f3aac73`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f3aac7310c6d83fdb6218c6c6cfbd9697fdc7e20))
