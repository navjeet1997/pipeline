class Testsuite:
    def __init__(self, template_summary):
        # self._name = name
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
        success = self.success
        success_xml = ""
        for i in range(success):
            success_xml = success_xml + '\t\t<testcase />\n'

        failure = self.failures
        failure_xml = ""
        for i in range(failure):
            failure_xml = failure_xml + '\t\t<testcase><failure /></testcase>\n'

        error = self.errors
        error_xml = ""
        for i in range(error):
            error_xml = error_xml + '\t\t<testcase><error /></testcase>\n'

        skipped = self.skipped
        skipped_xml = ""
        for i in range(skipped):
            skipped_xml = skipped_xml + '\t\t<testcase><skipped /></testcase>\n'

        return f'\t<testsuite>\n' \
               f'{success_xml}' \
               f'{failure_xml}' \
               f'{error_xml}' \
               f'{skipped_xml}' \
               f'\t</testsuite>\n'


