# changelogger
Cutting down CHANGELOGs. changelogger exists to extract changes from a specific release in your CHANELOG.md file for use as release notes. changelogger is designed to work with CHANGELOGs created by [github-changelog-generator](https://github.com/skywinder/github-changelog-generator).

## Example
Given the following CHANGELOG

```
## [v1.14.3](https://github.com/skywinder/github-changelog-generator/tree/v1.14.3) (2016-12-31)
[Full Changelog](https://github.com/skywinder/github-changelog-generator/compare/v1.14.2...v1.14.3)

**Fixed bugs:**

- Use Octokit::Client for both .com and Enterprise [\#455](https://github.com/skywinder/github-changelog-generator/pull/455) ([eliperkins](https://github.com/eliperkins))

**Closed issues:**

- Last tag contains too many PRs [\#291](https://github.com/skywinder/github-changelog-generator/issues/291)

**Merged pull requests:**

- CodeClimate configuration file [\#465](https://github.com/skywinder/github-changelog-generator/pull/465) ([olleolleolle](https://github.com/olleolleolle))
- Travis: Build against 2.4.0 [\#464](https://github.com/skywinder/github-changelog-generator/pull/464) ([olleolleolle](https://github.com/olleolleolle))
- Travis: add jruby-head, 2.4.0-rc1 [\#463](https://github.com/skywinder/github-changelog-generator/pull/463) ([olleolleolle](https://github.com/olleolleolle))
- Gemfiles for building versions separately dropped [\#461](https://github.com/skywinder/github-changelog-generator/pull/461) ([olleolleolle](https://github.com/olleolleolle))
- Order Gemfile gems A-Z; add ruby version marker [\#460](https://github.com/skywinder/github-changelog-generator/pull/460) ([olleolleolle](https://github.com/olleolleolle))
- README: Documentation update about RakeTask params and how to translate labels [\#454](https://github.com/skywinder/github-changelog-generator/pull/454) ([edusantana](https://github.com/edusantana))
- Travis: Use ruby 2.3.3 and 2.2.6 [\#452](https://github.com/skywinder/github-changelog-generator/pull/452) ([olleolleolle](https://github.com/olleolleolle))
```

changelogger will strip everything away except for what's important for creating release notes:

```
- Use Octokit::Client for both .com and Enterprise
- Last tag contains too many PRs
- CodeClimate configuration file
- Travis: Build against 2.4.0
- Travis: add jruby-head, 2.4.0-rc1
- Gemfiles for building versions separately dropped
- Order Gemfile gems A-Z; add ruby version marker
- README: Documentation update about RakeTask params and how to translate labels
- Travis: Use ruby 2.3.3 and 2.2.6
```

## Usage

```
changelogger [OPTIONS] FILE TAG
```

### Example

```
changelogger CHANGELOG.md v1.0.0
```

## Install

Installation is done through [Easy Install](http://setuptools.readthedocs.io/en/latest/easy_install.html#id8).

```
easy_install https://github.com/alexfu/changelogger/archive/v0.0.1.tar.gz
```
