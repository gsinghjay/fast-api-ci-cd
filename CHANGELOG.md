# CHANGELOG


## Unreleased

### Bug Fixes

- **ci**: Add required permissions for reusable workflows
  ([`e73134a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e73134a255070a433f79f7a84b456738c8dc78fc))

- Add pull-requests read permission for lint workflow - Add checks write permission for test
  workflow - Fix workflow permission inheritance

- **ci**: Add workflow dependencies and commitlint configuration
  ([#40](https://github.com/gsinghjay/fast-api-ci-cd/pull/40),
  [`5c46bb8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5c46bb873c549cb97c6f3e105f8096143fc6d0b4))

- Add workflow_call triggers to lint and test workflows - Configure proper job dependencies in
  release workflow - Ensure sequential execution: lint -> test -> release - Update commitlint rules
  for consistent line lengths - Fix workflow reusability issues

- **ci**: Ensure consistent git author for releases
  ([`de08aa0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/de08aa02fbe182b596c5457a21e186d388e436b3))

- Add git committer details to semantic-release step - Ensure consistent git configuration - Fix tag
  validation issues

- **ci**: Improve tag validation logic and debugging
  ([`5bc40ca`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5bc40ca33c7107f93ca22c51369557a78c29a1f0))

- Fix tag creator validation condition - Add better error messages with expected vs actual values -
  Maintain security checks - Fix false positive validation failures

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`f3b2249`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f3b22490e84d48eb962365e5a2f6a12ee0cec1ee))

- Update CHANGELOG.md [skip ci]
  ([`43ff1c2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/43ff1c28df77b37ff8c8dfcc220e871ebf7425e8))

- Update CHANGELOG.md [skip ci]
  ([`2546b4a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2546b4a72bbb37d00b5e384dc82b6ed68d9d2715))

- Update CHANGELOG.md [skip ci]
  ([`ed9486f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ed9486f9469cccdae1ba8bb9d73865b38f0604c2))

- Update CHANGELOG.md [skip ci]
  ([`6ca62a6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6ca62a6fad0adcb501612e5b6af5b58bc99c5527))

- Update CHANGELOG.md [skip ci]
  ([`a55cde7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a55cde7a639fd56fc5c5aef522ae317d0b1bbd1b))


## v1.6.2 (2025-01-02)

### Bug Fixes

- **ci**: Ensure changelog updates on every push
  ([`57ec646`](https://github.com/gsinghjay/fast-api-ci-cd/commit/57ec6466145f198d89c38b2b2f0f1a81cc8ca3c7))

- Add explicit changelog generation step - Update changelog regardless of release status - Configure
  semantic-release to include all commits - Separate changelog generation from release process

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`6382022`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6382022585ff561f7b2e2d2fb2eb8eab11d90437))

- **readme**: Add workflow diagram and explanation
  ([`5e986cb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5e986cb4c4cc7b8972570141237b91ff0132343a))

- Add mermaid flowchart of CI/CD pipeline - Include detailed workflow steps explanation - Show job
  dependencies and conditions - Add color coding for different stages - Document skip conditions

- **readme**: Fix mermaid diagram syntax
  ([`41cd6e0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/41cd6e0a1071aa268d7f4573b54ef56b44d92ade))

- Fix skip conditions node formatting - Update style definitions to use classDef - Remove special
  characters causing parse errors - Improve diagram readability


## v1.6.1 (2025-01-02)

### Bug Fixes

- **ci**: Add debugging for changelog generation
  ([`78499ed`](https://github.com/gsinghjay/fast-api-ci-cd/commit/78499ed3c5a720acfb8c8f6badda98f674cbce92))

- **ci**: Correct condition logic for github-actions bot in workflow
  ([`c3c0db9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c3c0db9dce2ba097780d228ca654ca0c44b6e1c6))

- Changed OR operator to AND in workflow conditions - Ensures github-actions bot commits are
  properly skipped - Prevents CI/CD infinite loops

- **ci**: Correct condition logic for github-actions bot in workflow
  ([`b742535`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b742535af3279930f1f23335ee1dc182afee34d0))

- Changed OR operator to AND in release job conditions - Ensures github-actions bot commits are
  properly skipped - Prevents CI/CD infinite loops

- **ci**: Improve changelog generation and remove coverage artifacts
  ([`a4f0424`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a4f042496885409fdf7358aed307c76e02d7a4ce))

- Add debug verbosity to semantic-release command - Remove coverage.xml artifact upload - Add better
  debug output for changelog generation - Fix semantic-release verbose flag position

- **ci**: Remove invalid --prerelease flag from changelog generation
  ([`2af8359`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2af8359581432fb01095423a5076f517af240e02))

- **ci**: Simplify release configuration
  ([`8f72fa1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8f72fa11467b4f48ad4af418c6cca3c890b58340))

- Remove unnecessary prerelease configuration - Keep only main branch configuration - Simplify
  changelog generation command

- **ci**: Simplify release workflow
  ([`4b19367`](https://github.com/gsinghjay/fast-api-ci-cd/commit/4b19367f226bdf4316015b6bb926c649f1337bb8))

- Remove separate changelog update step - Update release job configuration - Configure changelog for
  release-only updates - Follow semantic-release best practices

- **config**: Remove duplicate branch configuration
  ([`0cc9aeb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0cc9aeb3c3082a2e048b18e37e1f188293887563))

- Remove duplicate [tool.python_semantic_release.branches.main] section - Fix TOML validation error

- **config**: Update branch patterns for changelog generation
  ([`73c7101`](https://github.com/gsinghjay/fast-api-ci-cd/commit/73c71013b80c37e94e6db787b85a329fd1761a16))

- Add develop branch pattern to release groups - Include feature/fix branch patterns - Follow
  semantic-release documentation recommendations

- **config**: Update branch patterns with proper regex
  ([`197246a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/197246a1163f8b7aff0f8620b21ad952ba935ebc))

- Use .* pattern for matching fix and feature branches - Separate patterns for clearer branch
  matching - Fix 'branch not in release groups' error


## v1.6.0 (2025-01-02)

### Bug Fixes

- **ci**: Correct changelog generation in PRs
  ([`5c4c1b1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5c4c1b17834a6e71ad47b5397465355153a57797))

- Remove invalid --unreleased flag - Use pyproject.toml configuration for unreleased changes -
  Simplify changelog generation command

- **release**: Use both tags and commits for versioning
  ([`6418e07`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6418e07827443547d90db6555a32100b98e3eaab))

- Update semantic-release to use both tags and commits - Tags for released versions - Commits for
  unreleased changes tracking

### Features

- **ci**: Add changelog updates for pull requests
  ([`ed12395`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ed12395784275436148d659f3a925a1b9ef8653c))

- Add unreleased section to changelog generation - Update changelog during PR development -
  Configure semantic-release for unreleased changes


## v1.5.1 (2025-01-02)

### Bug Fixes

- **ci**: Ensure tests run on pull requests
  ([`dcd4844`](https://github.com/gsinghjay/fast-api-ci-cd/commit/dcd484442c9129df9518fbeb82b4ba9a3faa6ed4))

- Fix conditional logic for PR events in workflow - Separate PR and push event conditions - Ensure
  lint and test jobs always run on PRs

- **ci**: Prevent workflow recursion from bot commits
  ([`fd2a99b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fd2a99b55ca63c03ad65df61b66fb6d6a2af0841))

- Add paths-ignore for CHANGELOG.md updates - Add conditional checks to skip CI on bot commits - Add
  skip conditions for release and changelog updates - Prevent workflow triggers on [skip ci] tags

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`ddc80bb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ddc80bb23282263520ebe497c15de3cb798f51de))


## v1.5.0 (2025-01-02)

### Chores

- **release**: Update semantic-release config for main-only releases
  ([`d18cf04`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d18cf04eba0355c83785433c95a3095a246dba24))

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`6b62894`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6b62894aa0d09c5733d46d621c966dbe25063355))

### Features

- **ci**: Simplify release workflow to main branch only
  ([`6ee5af4`](https://github.com/gsinghjay/fast-api-ci-cd/commit/6ee5af43c5693d45062b7d841bc9cf3936827eef))


## v1.4.0 (2025-01-02)

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`90db080`](https://github.com/gsinghjay/fast-api-ci-cd/commit/90db08060a0f7325ab489215f2f3676b0cadbf48))

### Features

- Add color code validation
  ([`32c497f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/32c497f726986a057fc314b5867e6676023fc915))


## v1.3.0 (2025-01-02)

### Bug Fixes

- **ci**: Improve branch handling and semantic-release configuration
  ([`e5135fc`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e5135fc0da76442ee7de0ba72bfd9803bb9c3247))

- **ci**: Update semantic-release config to handle beta versions correctly
  ([`0205e1b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0205e1bd2dac59dc1e3c0de4a978e7ab942503c8))

### Chores

- Merge develop and resolve conflicts
  ([`b48b4cc`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b48b4cc84ee315cadbe78fe8a445f7f29ecfa402))

### Documentation

- Add documentation for custom QR code colors
  ([`5c9b512`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5c9b5127d0d6085b44d6320ef05c756a33d73d0a))

- Add documentation for custom QR code colors
  ([#27](https://github.com/gsinghjay/fast-api-ci-cd/pull/27),
  [`28d8ca6`](https://github.com/gsinghjay/fast-api-ci-cd/commit/28d8ca68beeb7947ac20636cdae743bf2b073464))

- Add documentation for custom QR code colors
  ([#28](https://github.com/gsinghjay/fast-api-ci-cd/pull/28),
  [`2f037d0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2f037d046a616df30031d2864ba340e378192ed2))

- Add workflow debugging commands
  ([`34b6f6d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/34b6f6dbfee768c1e091bdd395a36da89a2f80c9))

- Enhance README with detailed workflow and debugging instructions
  ([`f6987fe`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f6987febb2112a3e1ce7119dc44d8d9887b0aad8))

- Update CHANGELOG.md [skip ci]
  ([`f6e1604`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f6e1604cdf37ead8e326f4ebd6167f3ee724c069))

- Update CHANGELOG.md [skip ci]
  ([`5dc58d0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5dc58d0157f1d0d47904a698592dd7caffcba151))

### Features

- Add QR code size customization options
  ([`e1ba631`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e1ba631b99cf3eff3fc9f5c98d3678e3960fe37c))

- Add support for custom QR code colors
  ([`8697ea0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8697ea0234c945406f949d386f3a975fe9b00a37))

- **ci**: Enhance release verification with detailed status messages
  ([`5f00625`](https://github.com/gsinghjay/fast-api-ci-cd/commit/5f00625eac215dea58f14327725c1e6644259763))


## v1.3.0-beta.1 (2025-01-01)

### Bug Fixes

- **ci**: Configure git remote with authentication token
  ([`70a4049`](https://github.com/gsinghjay/fast-api-ci-cd/commit/70a4049760f283f39b701ff14c5fc1011ff29129))

- Add proper HTTPS authentication for Git operations - Use GITHUB_TOKEN for remote URL
  authentication

- **ci**: Correct git authentication for semantic-release
  ([`98fe3b8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/98fe3b8d95525d822555484b1dc40878f1d9295b))

- Replace Git URL rewriting with direct remote URL configuration - Use correct GitHub URL format
  with authentication token

- **ci**: Correct Git URL configuration for semantic release
  ([`022c87d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/022c87d029e46aa4405eb7daf4231107dea52f44))

- **ci**: Enhance Git authentication and build configuration
  ([`56efc69`](https://github.com/gsinghjay/fast-api-ci-cd/commit/56efc694d46569a29ef4c9aecc7423b46b25a9d6))

- **ci**: Enhance Git authentication with PAT and add debugging steps
  ([`03bff11`](https://github.com/gsinghjay/fast-api-ci-cd/commit/03bff118f1f441829e576665876b80d4cc604cf9))

- **ci**: Enhance GitHub token configuration and permissions
  ([`7af467c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7af467cb561a08b5b7160bce5271b09a9637670d))

- **ci**: Handle both shallow and complete repositories in git fetch
  ([`642e335`](https://github.com/gsinghjay/fast-api-ci-cd/commit/642e33591146ad14e9d42b6f9e68eb8eb76851d3))

- Remove --unshallow flag to support complete repositories - Add explicit origin remote
  specification

- **ci**: Improve Git authentication across all workflow steps
  ([`20b495b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/20b495b5c042f012068d4bda4756fc44828785fe))

- **ci**: Improve Git authentication for semantic-release
  ([`009aec2`](https://github.com/gsinghjay/fast-api-ci-cd/commit/009aec27b68cf3f589617c1929916c44542a03cd))

- Use Git URL rewriting for authentication - Remove credential helper in favor of insteadOf
  configuration

- **ci**: Improve Git authentication for semantic-release
  ([`e9d8b0c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e9d8b0c7b80b7ed04f36e1b3685c8347861f8289))

- Add Git credential helper configuration - Pass GitHub token through environment variables -
  Simplify Git configuration

- **ci**: Improve git authentication for semantic-release
  ([`fb41011`](https://github.com/gsinghjay/fast-api-ci-cd/commit/fb41011e72160926d651c8b547315a212b44a904))

- Use Git URL rewriting for authentication - Ensure complete repository history - Remove redundant
  credentials configuration

- **ci**: Improve git authentication for semantic-release
  ([`72eb609`](https://github.com/gsinghjay/fast-api-ci-cd/commit/72eb6092fe163cf001f8ce44e5a1b1a565832e83))

- Update Git remote configuration for better token handling - Add explicit GITHUB_TOKEN environment
  variable - Fix branch reference in git pull command

- **ci**: Improve Git authentication verification and sync
  ([`a072b64`](https://github.com/gsinghjay/fast-api-ci-cd/commit/a072b6458c901b718c4a11e01b0c2ee9113dd581))

- **ci**: Simplify Git authentication and use consistent token handling
  ([`ad23d07`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ad23d072332ce033e20429370ae3df4ea13d3d50))

- **ci**: Update git authentication method
  ([`f2f3287`](https://github.com/gsinghjay/fast-api-ci-cd/commit/f2f32878dcd8b5755bc51e0f4c6d09f588590dcb))

- Use Git credential store for authentication - Add GIT_CREDENTIALS environment variable - Improve
  branch tracking configuration

- **ci**: Use official Python Semantic Release GitHub Action
  ([`78789f1`](https://github.com/gsinghjay/fast-api-ci-cd/commit/78789f162697ff73ac1edf3a17888b9230febefd))

- Replace custom release script with official action - Update environment variables to use PSR_
  prefix - Add GitHub Release Assets publishing

### Continuous Integration

- Improve ci/cd workflow reliability and tag handling
  ([`bbfa061`](https://github.com/gsinghjay/fast-api-ci-cd/commit/bbfa061ccd817600bca70d0f56eec7b80870427b))

- fix: correct dependency between tag-validation and release jobs - feat: add annotated tag support
  for better validation - fix: standardize python-semantic-release version to 9.15.0 - fix: improve
  GitHub CLI authentication - chore: enhance workflow_dispatch input handling

### Documentation

- Add branch protection rules and naming conventions
  ([`851e65b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/851e65b1ab265321f13fa727aff77e9d43997d64))

- Update CHANGELOG.md [skip ci]
  ([`ff10ee8`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ff10ee80d64129025b50e18286368f96d7a2a262))

- Update mermaid diagram to show complete release flow
  ([`ce2ecad`](https://github.com/gsinghjay/fast-api-ci-cd/commit/ce2ecadbd28dd9a7258197026cb64af1c34b58dc))

### Features

- **ci**: Enhance release workflow with semantic options
  ([`0d0fb10`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0d0fb1017a72d763d34af1dbda4a53071ba32f20))

- Add manual workflow trigger with configurable parameters - Support prerelease versions with custom
  tokens - Add build metadata support - Enable commit signing with SSH keys - Improve version
  control with force level options

- **release**: Add branch-specific release configurations
  ([`b8ec310`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b8ec310ee2643add5d24e69c8c68c40f9364c22d))

- Configure main branch for regular releases - Configure develop branch for beta releases -
  Configure release/* branches for RC releases


## v1.2.0 (2025-01-01)

### Documentation

- Add manual release workflow documentation
  ([`d4e82a7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d4e82a7f10621ce3bc8a1f7652e2736ca7060af8))

- Update CHANGELOG.md [skip ci]
  ([`c55ebf7`](https://github.com/gsinghjay/fast-api-ci-cd/commit/c55ebf7749670ea71b5b76472a7af378afc73f7a))

- Update CHANGELOG.md [skip ci]
  ([`7bc972b`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7bc972b344f0bdd0ed8c8aa10a3e4a55aa40de82))

### Features

- **ci**: Add automated pre-release patterns for different branches
  ([`7fae1bc`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7fae1bc47cac96731d3e877c80c1e297d94e16a8))


## v1.1.0 (2025-01-01)

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`09c869a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/09c869a9edc191cee2ec6ba75a8e55a06b19b35c))

### Features

- **ci**: Enhance release workflow with semantic options
  ([`b5ed280`](https://github.com/gsinghjay/fast-api-ci-cd/commit/b5ed280626d96fe56c7a1581eaf7c395dc7a6730))

- **ci**: Enhance release workflow with semantic options and manual triggers
  ([`0b25b9d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/0b25b9d7e93d28d6e8a7c74477fc02b0ec025a5b))


## v1.0.11 (2025-01-01)

### Bug Fixes

- **changelog**: Exclude github-actions bot commits from changelog
  ([`52010b0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/52010b08635c1e6b034015acf1660b2e48087813))

- Add exclusion patterns for github-actions[bot] commits - Filter out automated changelog updates -
  Maintain clean changelog without bot entries

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`2ebfbde`](https://github.com/gsinghjay/fast-api-ci-cd/commit/2ebfbde66aca1abb537c6ebeb7370c7fa9ef0222))


## v1.0.10 (2025-01-01)

### Bug Fixes

- **changelog**: Exclude [skip ci] and related patterns from changelog
  ([`697fd83`](https://github.com/gsinghjay/fast-api-ci-cd/commit/697fd83fd785c9b8caf1b39c1fa40f4ad90035ec))

### Documentation

- Remove [skip ci] annotations from changelog
  ([`7d0e78d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7d0e78dda4346c407c897ab97c46ef56424b4910))

- Update CHANGELOG.md [skip ci]
  ([`7c6ae65`](https://github.com/gsinghjay/fast-api-ci-cd/commit/7c6ae65b8b02bc1f4f63556076ef28126cc675f1))

- **readme**: Add comprehensive table of contents and badges
  ([`1d8d53d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/1d8d53d911b7de7895ecba8a086a4fc076e4add4))

- Add status badges for CI/CD, release, Python version, and code coverage - Add structured table of
  contents with anchor links - Add sections for security, Docker, API docs, performance, testing,
  and error handling


## v1.0.9 (2025-01-01)

### Bug Fixes

- **ci**: Add git sync step and use CI mode for semantic-release
  ([`431296c`](https://github.com/gsinghjay/fast-api-ci-cd/commit/431296c47455bf4adaa96aea85cdee4f1d673786))

- **ci**: Correct version retrieval in release verification
  ([`e85e60d`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e85e60d879cbcd00d133e2ebed33ed356048d6ea))

- **ci**: Remove invalid --ci flag from semantic-release commands
  ([`9636c0f`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9636c0fdd9de821e6d42e59d2a78aaaa3ef369a7))

### Documentation

- Enhance README with semantic-release command details
  ([`3ab6eb3`](https://github.com/gsinghjay/fast-api-ci-cd/commit/3ab6eb361490315561a9e167595a27a1476d3533))

- Update CHANGELOG.md [skip ci]
  ([`334f0f0`](https://github.com/gsinghjay/fast-api-ci-cd/commit/334f0f0988392e915727752b1488287ee937e3ba))

- Update CHANGELOG.md [skip ci]
  ([`293ad54`](https://github.com/gsinghjay/fast-api-ci-cd/commit/293ad54cb99b57bec730b24fab7a93457d6a901b))

- Update CHANGELOG.md [skip ci]
  ([`9aa26e9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9aa26e9f1cab790ef46d1e326333b23ba71ca411))

- Update CHANGELOG.md [skip ci]
  ([`184b292`](https://github.com/gsinghjay/fast-api-ci-cd/commit/184b2920b500b301bd03233d951456c3e218ae19))

- Update CHANGELOG.md [skip ci]
  ([`af6231a`](https://github.com/gsinghjay/fast-api-ci-cd/commit/af6231ae1f4ade760ad01f720f6654fbe334162d))

- Update README with detailed versioning and CI/CD information
  ([`9106aa9`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9106aa9eb79a1270a63904dc1519e11edd8b9e01))

### Refactoring

- **ci**: Simplify release process using semantic-release commands
  ([`8225d08`](https://github.com/gsinghjay/fast-api-ci-cd/commit/8225d087dd8437ee685d00cfc5a69ec3b11ede23))


## v1.0.8 (2025-01-01)

### Bug Fixes

- **ci**: Correct release notes generation in CI/CD pipeline
  ([`9849cdb`](https://github.com/gsinghjay/fast-api-ci-cd/commit/9849cdb421a14894235c70e60beb895cac71165a))

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`559bf45`](https://github.com/gsinghjay/fast-api-ci-cd/commit/559bf451e22a3f03c93a58ca1768dde118204175))


## v1.0.7 (2025-01-01)

### Bug Fixes

- **ci**: Improve changelog generation using semantic-release
  ([`2540961`](https://github.com/gsinghjay/fast-api-ci-cd/commit/25409613951f1d4e3dfa4452c478151457479c1a))

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`d33b594`](https://github.com/gsinghjay/fast-api-ci-cd/commit/d33b5941831facf5c874eb089dae7ee1cb596a9e))


## v1.0.6 (2025-01-01)

### Bug Fixes

- **ci**: Improve changelog generation configuration
  ([`569e547`](https://github.com/gsinghjay/fast-api-ci-cd/commit/569e547ae6ccd4864e2d4f1673b9bbb76b2014c0))

- Add changelog components configuration - Exclude release commits from changelog - Configure
  changelog formatting

### Chores

- **release**: 1.0.6 [skip ci]
  ([`e8ee582`](https://github.com/gsinghjay/fast-api-ci-cd/commit/e8ee58270e481c4e326e848c4cbf70d38e389ac9))

### Documentation

- Update CHANGELOG.md [skip ci]
  ([`892c342`](https://github.com/gsinghjay/fast-api-ci-cd/commit/892c34220d30ee94e96ade910a82b27d53e16464))


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
