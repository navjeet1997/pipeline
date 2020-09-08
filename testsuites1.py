from testsuite1 import Testsuite


class Testsuites:
    def __init__(self, name, testsuite_list):
        self._name = name
        self._testsuite_list = testsuite_list

    @property
    def tests(self):
        return sum(Testsuite(testsuite).tests for testsuite in self._testsuite_list)

    @property
    def time(self):
        return sum(Testsuite(testsuite).time for testsuite in self._testsuite_list)

    @property
    def success(self):
        return sum(Testsuite(testsuite).success for testsuite in self._testsuite_list)

    @property
    def failures(self):
        return sum(Testsuite(testsuite).failures for testsuite in self._testsuite_list)

    @property
    def errors(self):
        return sum(Testsuite(testsuite).errors for testsuite in self._testsuite_list)

    @property
    def skipped(self):
        return sum(Testsuite(testsuite).skipped for testsuite in self._testsuite_list)

    @property
    def __str__(self):
        testsuite_xml = ""
        for testsuite in self._testsuite_list:
            testsuite_xml = testsuite_xml + Testsuite(testsuite).__str__

        return f'<?xml version="1.0" encoding="UTF-8" ?>\n' \
               f'<testsuites name="{self._name}">\n' \
               f'{testsuite_xml}' \
               f'</testsuites>\n'


