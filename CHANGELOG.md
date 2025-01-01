# CHANGELOG


## Unreleased

### Bug Fixes

- **ci**: Improve changelog generation configuration
  ([`569e547`](https://github.com/gsinghjay/fast-api-ci-cd/commit/569e547ae6ccd4864e2d4f1673b9bbb76b2014c0))

- Add changelog components configuration - Exclude release commits from changelog - Configure
  changelog formatting


## v1.0.5 (2025-01-01)

### Bug Fixes

- **ci**: Add GitHub release creation to CI/CD pipeline
  ([`5a434ca`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5a434ca82fa7a95a9e1eadac4351e69102ddbb0c))

- Add GitHub CLI installation - Create GitHub releases for tags - Add release verification step

### Chores

- **release**: 1.0.5 [skip ci]
  ([`0f4c74a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0f4c74a0677f7325b2181dd96224a40110924c28))

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`a6d7a09`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a6d7a097a096fd683c3b34d3630f694ac35d89ae))


## v1.0.4 (2025-01-01)

### Bug Fixes

- **version**: Align version numbers with git tags
  ([`67e0852`](https://github.com/gsinghjay/fast-api-ci-cd/commit/67e0852517a7d13d2c3cb5a00ac0501d235f99dc))

This commit fixes the version number discrepancy between files and git tags, ensuring consistent
  versioning across the project.

### Chores

- **release**: 1.0.4 [skip ci]
  ([`b8d50a7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b8d50a7fe330e21e00e6acafb2689c268088780d))

### Code Style

- Apply pre-commit hooks and formatting
  ([`da67f7c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/da67f7c01e91141e31141231be273c6452398dfa))

- Format code with black - Fix flake8 violations - Add pre-commit configuration - Update gitignore
  patterns - Fix YAML formatting - Update documentation formatting

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`addaa9b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/addaa9ba5502fb14c3a91e9e4da042362ae55554))

- Update CHANGELOG.md [skip ci]
  ([`db0dbde`](https://github.com/gsinghjay/fast-api-ci-cd/commit/db0dbde5c77700cf764bdab678f2767910fd5bbc))


## v1.0.3 (2025-01-01)

### Bug Fixes

- **ci**: Improve version management and changelog generation
  ([`b91516a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b91516af52d89def93abf2940996139c95566e22))

- Add proper version increment logic based on commit types - Fix duplicate changelog entries -
  Implement semantic version bumping based on conventional commits - Add comprehensive change
  detection - Improve release decision logic

- **ci**: Prevent duplicate tag creation in release step
  ([`8584c27`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8584c275d5a25ecb4c9ee784b9fc3fcf99985f20))

- Add tag existence check before creation - Skip version update if tag exists - Improve error
  handling for existing tags - Add informative message when skipping release

### Chores

- **release**: 1.0.3 [skip ci]
  ([`b26ce30`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b26ce3070718d04f95c6af68a9e5a29059db3fdc))

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`59f2bb2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/59f2bb2d455cf70730859144f8e47bd917fa520a))

- Update CHANGELOG.md [skip ci]
  ([`d6f8d05`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d6f8d0592c5fca5f41b83aa8a0c1a9677b9242b4))


## v1.0.2 (2025-01-01)

### Bug Fixes

- **ci**: Improve semantic release version management
  ([`c55d026`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c55d0263553ac2b1d11d53bf01bae2f0427d6346))

- Add explicit version checking - Use git tags for version tracking - Implement proper semantic
  version bumping - Add commit message validation

### Chores

- **release**: 0.1.1-dev.0 [skip ci]
  ([`707e682`](https://github.com/gsinghjay/fast-api-ci-cd/commit/707e682cb489d685902e5414476361147e604732))

- **release**: 1.0.2 [skip ci]
  ([`8215ee4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8215ee4aa344a48843a9a4b17c72008f1721eb24))

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`3e8eaf6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3e8eaf680efe7fe82ea584d00db003a54bc54650))

- Update CHANGELOG.md [skip ci]
  ([`69756f2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/69756f292abd59fc95519e1a16fd671208f7ebf3))

- Update CHANGELOG.md [skip ci]
  ([`3628a92`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3628a9263a44e96541158e63c93c4867b5d0081f))

### Refactoring

- **ci**: Remove deployment notification step
  ([`b135f70`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b135f70ff0a437796a3f0913c2940d4875a67447))

- Remove GitHub issue comment notification - Simplify post-merge-verification job - Remove
  unnecessary notification dependencies

- **ci**: Remove redundant post-merge verification
  ([`ac9d317`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ac9d31755196877e7836f8e216beddda31d19ebb))

- Remove post-merge verification job - Simplify workflow dependencies - Reduce CI execution time -
  Rely on existing test and release jobs for verification

- **ci**: Simplify release process
  ([`84d1be7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/84d1be73b550e1ae30d07338c47c6a4f192161c8))

- Remove dev version handling - Simplify version management - Remove unnecessary version checks -
  Streamline release process to main branch only


## v1.0.1 (2025-01-01)

### Bug Fixes

- **ci**: Remove remaining dev version update configurations
  ([`d6f0424`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d6f04247bee1a3823cfe7ab527f40acbb9fbde16))

- Remove update-dev-version job completely - Clean up post-merge-verification job dependencies -
  Remove dev version update logic - Fix invalid PEP 440 version error

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`be9f5a9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/be9f5a97110464b0369e6d633e5a2e2a5557da95))

- Update CHANGELOG.md [skip ci]
  ([`e223933`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e223933affd531780688f03c6014e196cf6a6a1f))

### Refactoring

- **ci**: Remove dev version updates and notifications
  ([`6c528ce`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6c528ce86c26118e4f6895c3cdfb2b57388130b4))

- Remove update-dev-version job - Remove notification step from post-merge-verification - Update job
  dependencies to reflect removed jobs - Simplify post-merge verification process


## v1.0.0 (2025-01-01)

### Bug Fixes

- Configure semantic-release for changelog generation
  ([`58bfc6b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/58bfc6bcaa10ec80cadc7d082565211acc8ff1c3))

- Ensure black is installed before running lint checks
  ([`4476fff`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4476fff05f9692005723662940d58fbabaa01f24))

- Improve changelog generation and branch handling
  ([`c7f0bc6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c7f0bc6f91ab2d02ade56797f6d4c72cd98d8935))

- Improve changelog generation with force flag and version print
  ([`4cb19ad`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4cb19ad7c146fa46fa5c7239c76ab5df02492307))

- Improve semantic-release configuration and workflow
  ([`1df8745`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1df874501667516c4b5eb4afa0b3d6277f5a2973))

- Remove unsupported flags from semantic-release commands
  ([`590b51b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/590b51b9315dc1f5e4a5dd6a23b20a908d5c6444))

- Update branch patterns in semantic-release config
  ([`fcd7f79`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fcd7f79464968680fb2c97327e5d030b9fda967e))

- Update changelog generation to work on all branches
  ([`cc22720`](https://github.com/gsinghjay/fast-api-ci-cd/commit/cc227202bab703223f8f218f06f32fafeab48694))

- Update dependencies and replace deprecated on_event with lifespan
  ([`38d748b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/38d748b1c206b34d3cfd2a397d3315814e6e8a82))

- Update GitHub Actions workflow with correct action references
  ([`b81d444`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b81d444289d28d8dbbf74a2e8daee01cc9bb8695))

- Update poetry lock handling in CI/CD pipeline
  ([`f4de1b4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f4de1b4345566a36addd634eae2868718b950ab8))

- Update semantic-release build command configuration
  ([`1cd7266`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1cd7266690bf4bbf8dedb7c5772763f5ed4b6f79))

- Update semantic-release commands to match v9.15.0 documentation
  ([`41b8fe1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/41b8fe1af632998b6ac01d3ac09aad6606bd246a))

- Update semantic-release configuration for version 9.x
  ([`ee23aba`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ee23ababd942ddfe685d03e2211191999c25467d))

- Update semantic-release configuration format
  ([`f332024`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f3320242aba7757250ef43fe52ee7bed12333056))

- Update semantic-release flags for version 9.x
  ([`2f7d7c3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2f7d7c3bd89812e6ff161d86fee8291bf798eba4))

- Update semantic-release version variable configuration
  ([`64b26e6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/64b26e68f4228c237119f6ce3bcb71ff20e90853))

- Update to python-semantic-release 9.x configuration format
  ([`316856b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/316856b4c52f52add7bae3dcb655721953a6c15e))

- Update version_toml format in semantic-release config
  ([`0c456ed`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0c456edbab9365a53ac0a3fe12a3d2cdbcd947cc))

- Update workflow to handle dev branch merges
  ([`1e269d0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1e269d0102d98c4079e9154c475f13204c30ed18))

- Use string format for Python versions in matrix
  ([`9a402a3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9a402a37712d1540b9c0c1c32ed143040f6d23d6))

- **ci**: Correct semantic-release command syntax
  ([`d94883b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d94883b507f1914edf2111be6b82be5b33fc0aea))

- Remove incorrect --prerelease flag - Rely on branch configuration for alpha releases - Simplify
  release command to use configuration

This fixes the "unexpected extra argument" error in the dev release workflow.

- **ci**: Correct semantic-release configuration for alpha releases
  ([`9caebc7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9caebc78728868c93d7fa22774ce0894cf0f9d96))

- Update semantic-release branch configuration in pyproject.toml - Add explicit branch handling for
  dev and main - Add --prerelease alpha flag to dev branch releases - Fix branch recognition issue
  in release workflow - Add explicit git checkout for dev branch

This fixes the issue where no releases were being generated on the dev branch and ensures proper
  alpha versioning.

- **ci**: Correct semantic-release version command in dev workflow
  ([`15b6ef9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/15b6ef976a1c6fff0b42f241cf39f516cd31ee28))

- Remove unsupported --branch flag from semantic-release command - Rely on pyproject.toml branch
  configuration instead - Maintain backward compatibility with semantic-release 9.x

- **ci**: Improve semantic-release workflow and permissions
  ([`3723090`](https://github.com/gsinghjay/fast-api-ci-cd/commit/372309076ca902404431964b9d9cebe0fb7dece0))

- Update semantic-release configuration in pyproject.toml - Enhance release job with proper version
  handling - Add dev branch version management - Add proper git tagging and changelog updates -
  Document required repository permissions

BREAKING CHANGE: This updates the semantic-release configuration and requires specific GitHub
  repository permissions to be set.

- **ci**: Remove explicit branch flag from semantic-release
  ([`58a8169`](https://github.com/gsinghjay/fast-api-ci-cd/commit/58a8169013e0f00c70553496f27bbe28b17c7c53))

- Remove redundant --branch flag as it's not needed with pyproject.toml config - Simplify
  semantic-release command for better maintainability - Ensure compatibility with semantic-release
  configuration in pyproject.toml

BREAKING CHANGE: Removes explicit branch flag from semantic-release command. Branch configuration is
  now exclusively managed through pyproject.toml.

- **ci**: Resolve dev branch release configuration
  ([`bacdbb1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/bacdbb172850b0ea62052558614d09e87ec0e2f3))

- Add default branch setting in pyproject.toml - Simplify semantic-release branch configuration -
  Add explicit --branch flag to release command - Remove redundant branch configurations

This fixes the "branch 'dev' isn't in any release groups" error and enables proper alpha releases on
  the dev branch.

- **ci**: Resolve duplicate branch configuration in pyproject.toml
  ([`4691097`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4691097706204849781d84c73b8e005f588ba4e0))

- Remove duplicate branch configuration entries - Keep single unified branch configuration under
  [tool.python_semantic_release.branches] - Fix "Cannot declare branches.dev twice" error - Ensure
  semantic-release can properly identify release groups

Fixes error: Cannot declare ('tool', 'python_semantic_release', 'branches', 'dev') twice

- **ci**: Resolve release step git sync issues
  ([`eea5188`](https://github.com/gsinghjay/fast-api-ci-cd/commit/eea5188da46653ab6922e861e3ad932d6440b582))

- Add git pull with rebase to sync with remote - Combine git pushes to reduce race conditions - Add
  force flag to ensure version updates succeed - Improve release step error handling

- **ci**: Resolve semantic-release configuration conflicts
  ([`125ec19`](https://github.com/gsinghjay/fast-api-ci-cd/commit/125ec1925fcaa1115e730c588c1cc4a5fbca1b17))

- Remove duplicate branch configurations - Add branch_patterns section for better branch matching -
  Fix configuration structure to prevent value overwriting - Clarify branch release patterns for
  main and dev

This fixes the "Cannot overwrite a value" error in the CI pipeline.

- **ci**: Simplify changelog update step after removing branch protection
  ([`4d33e06`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4d33e06c78d41004a86634daece3dc62ab4fe3ff))

- Remove complex PR creation logic since branch protection is disabled - Use direct push to current
  branch for changelog updates - Maintain basic git configuration for bot commits

- **ci**: Update semantic-release branch configuration format
  ([`9b03616`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9b03616b7369c101176081218a0ce4d004fc219d))

- Update branch configuration format in pyproject.toml to match semantic-release 9.x expectations -
  Simplify branch configuration by using direct format instead of nested sections - Fix "branch not
  in release groups" error by using correct configuration structure

Related to: Previous commit that removed --branch flag from workflow

### Chores

- Add .gitignore file
  ([`ca11881`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ca1188162ac75c5e57b42c081039d4106d1ae0d5))

- Bump version to 0.1.1-dev.0 [skip ci]
  ([`727dd70`](https://github.com/gsinghjay/fast-api-ci-cd/commit/727dd7047f71762a7a830bddf9dbdd53f2791afe))

- Re-add project files without cache
  ([`46f0bf7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/46f0bf7d5c0ccd7b95983f6dca8acf1347673c42))

- **release**: Bump version and update changelog [skip ci]
  ([`88aba68`](https://github.com/gsinghjay/fast-api-ci-cd/commit/88aba685be1fbafbf2956694876f3a0ea4f344ae))

### Code Style

- Format code with black
  ([`4c0449a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4c0449a9b4313c625575a3c5ce262cce6ec6ea80))

### Continuous Integration

- Enable CI/CD pipeline for all branches
  ([`3083dd1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3083dd1bd72ff48000e155884a6bdf5dd568753a))

- Fix commitlint configuration and workflow
  ([`befcdf3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/befcdf3db1752523e6f8cf46e32638f9c10aea8f))

- Handle poetry.lock file in CI/CD pipeline
  ([`105f017`](https://github.com/gsinghjay/fast-api-ci-cd/commit/105f0176e6760828503b618431a528fe87a7f5fa))

- Remove Python 3.9 from test matrix
  ([`320239c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/320239c9e3061f8cb061b611326f22acf291c19a))

- Standardize poetry installation and lock file handling
  ([`e802d7e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e802d7edc5cc431fa47eac2f17efc49c5ef6627c))

- Switch to wagoid/commitlint-github-action for commit linting
  ([`928b238`](https://github.com/gsinghjay/fast-api-ci-cd/commit/928b2385d98278ad01f49a9e96751a8162316b0f))

- Update all Python versions to 3.11
  ([`cd70ae6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/cd70ae67f60c9f36fbd7e6e7a383bd159302475b))

- Update Python version matrix to 3.9-3.11
  ([`ed276a1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ed276a1e5b2a4c4fcca29162bc3f9af55639c09a))

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`0423265`](https://github.com/gsinghjay/fast-api-ci-cd/commit/04232653f0f2f0044ebfcd60d4800aa47c3e3a00))

- Update CHANGELOG.md [skip ci]
  ([`896cf4e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/896cf4e3c5228e7f0422ed0966e27b0afd0cf100))

### Features

- Add changelog generation to CI/CD pipeline
  ([`93241cb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/93241cb66dcbaf28d2e5bfd29e956eb4cc8ea520))

- Add custom color support for QR codes
  ([`3d10cd8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3d10cd8be9fe78d429219a33e92921dc71b53b0c))

- Add QR code generation functionality
  ([`9fbb062`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9fbb0627c04420588903c548c0b649ce5e7e416f))

- Add structured logging configuration
  ([`a6fff8e`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a6fff8e7a9ded98d0d73b0b205d2eb3f42179e3c))

- Enable changelog updates in feature branches
  ([`3f98945`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3f98945546615681e5826d19586a0ce65846d800))

- Initial project setup with basic FastAPI application
  ([`9b48962`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9b489623ca64b390e10124ae5d6efb0cb1ad4ad3))

- **ci**: Add alpha release support for dev branch
  ([`1675520`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1675520d37064c770fdb8dd383e7f014a5e66063))

- Add semantic-release branch configuration for alpha releases - Add dedicated release workflow for
  dev branch - Configure prerelease tokens and version format - Maintain separate version tracks for
  dev and main branches

This enables automatic alpha releases when merging to dev branch, while maintaining standard
  releases on main.

### Refactoring

- **ci**: Simplify release process and changelog generation
  ([`73cee3f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/73cee3f3a5ae0135457783b1d6e827578edb00bc))

- Remove alpha release configuration - Simplify semantic-release config - Update changelog only on
  main branch - Remove unnecessary release-dev job
