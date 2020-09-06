# import xml.etree.ElementTree as xml
from testsuite import Testsuite


class Testsuites:
    def __init__(self, name, testsuite_list):
        self._name = name
        self._testsuite_list = testsuite_list

    @property
    def tests(self):
        return sum(Testsuite("ts", testsuite).tests for testsuite in self._testsuite_list)

    @property
    def time(self):
        return sum(Testsuite("ts", testsuite).time for testsuite in self._testsuite_list)

    @property
    def success(self):
        return sum(Testsuite("ts", testsuite).success for testsuite in self._testsuite_list)

    @property
    def failures(self):
        return sum(Testsuite("ts", testsuite).failures for testsuite in self._testsuite_list)

    @property
    def errors(self):
        return sum(Testsuite("ts", testsuite).errors for testsuite in self._testsuite_list)

    @property
    def skipped(self):
        return sum(Testsuite("ts", testsuite).skipped for testsuite in self._testsuite_list)

    @property
    def __str__(self):
        testsuite_xml = ""
        for testsuite in self._testsuite_list:
            testsuite_xml = testsuite_xml + Testsuite('ts', testsuite).__str__

        return f'''<?xml version="1.0" encoding="UTF-8" ?>
<testsuites name="{self._name}" tests="{self.tests}" time="{self.time}" success="{self.success}" failures="{self.failures}" errors="{self.errors}" skipped="{self.skipped}">{testsuite_xml}
</testsuites>
'''


    # @property
    # def generate_xml(self):
    #
    #     testsuites = xml.Element("testsuite")
    #     testsuites.set("name", self._name)
    #     testsuites.set("tests", self.tests)
    #     testsuites.set("time", self.time)
    #     testsuites.set("success", self.success)
    #     testsuites.set("failure", self.failures)
    #     testsuites.set("errors", self.errors)
    #     testsuites.set("skipped", self.skipped)
    #     # testsuite = xml.SubElement(testsuites, "testsuite")
    #     tree = xml.ElementTree(testsuites)
    #     tree.write("try.xml",
    #                xml_declaration=True, encoding='utf-8',
    #                method="xml")
    #
    #     with open('try.xml', "wb") as file:
    #         file.write('\n')
    #         tree.write(file)
    #     return tree

