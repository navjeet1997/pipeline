class Testsuite:
    def __init__(self, name, template_summary):
        self._name = name
        self._template_summary = template_summary

    @property
    def tests(self):
        return sum(obj.tests for obj in self._template_summary)

    @property
    def time(self):
        return sum(obj.time for obj in self._template_summary)

    @property
    def success(self):
        return sum(obj.success for obj in self._template_summary)

    @property
    def failures(self):
        return sum(obj.failures for obj in self._template_summary)

    @property
    def errors(self):
        return sum(obj.errors for obj in self._template_summary)

    @property
    def skipped(self):
        return sum(obj.skipped for obj in self._template_summary)

    @property
    def __str__(self):
        return f'\n\t<testsuite name="{self._name}" tests="{self.tests}" time="{self.time}" success="{self.success}"' \
               f' failures="{self.failures}" errors="{self.errors}" skipped="{self.skipped}"></testsuite>'


