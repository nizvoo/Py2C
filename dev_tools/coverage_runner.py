"""Run tests under coverage's measurement system (Used in CI)
"""

import os
from os.path import join, realpath

# Third Party modules
import nose
import coverage

cov = coverage.coverage(branch=True)

cov.start()
nose.run(defaultTest=realpath(join(__file__, "..", "..", "py2c")))
cov.stop()
cov.save()

# If we are in CI environment, don't write an HTML report.
if os.environ.get("CI", None) is None:
    cov.html_report()

cov.report()