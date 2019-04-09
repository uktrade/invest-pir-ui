# invest-pir-ui

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gitflow-image]][gitflow]
[![calver-image]][calver]

**Personalised investment report UI - the Department for International Trade (DIT)**

---

## Development

### Installing
    $ git clone https://github.com/uktrade/invest-pir-ui
    $ cd invest-pir-ui
    $ virtualenv .venv -p python3.6
    $ source .venv/bin/activate
    $ pip install -r requirements_test.txt


### Requirements
[Python 3.6](https://www.python.org/downloads/release/python-368/)

## Running the webserver
    $ source .venv/bin/activate
    $ make debug_webserver

## Running the tests

    $ make debug_test

## Helpful links
* [Developers Onboarding Checklist](https://uktrade.atlassian.net/wiki/spaces/ED/pages/32243946/Developers+onboarding+checklist)
* [Gitflow branching](https://uktrade.atlassian.net/wiki/spaces/ED/pages/737182153/Gitflow+and+releases)
* [GDS service standards](https://www.gov.uk/service-manual/service-standard)
* [GDS design principles](https://www.gov.uk/design-principles)

## Related projects:
https://github.com/uktrade?q=directory
https://github.com/uktrade?q=great

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-cms/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/invest-pir-ui/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/invest-pir-ui/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/invest-pir-ui

[gitflow-image]: https://img.shields.io/badge/Branching%20strategy-gitflow-5FBB1C.svg
[gitflow]: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

[calver-image]: https://img.shields.io/badge/Versioning%20strategy-CalVer-5FBB1C.svg
[calver]: https://calver.org