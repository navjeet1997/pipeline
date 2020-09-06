from testsuites import Testsuites


class Obj:
    def __init__(self, name, tests, time, success, failures, errors, skipped):
        self._name = name
        self._test = tests
        self._time = time
        self._success = success
        self._failures = failures
        self._errors = errors
        self._skipped = skipped

    @property
    def name(self):
        return self._name

    @property
    def tests(self):
        return self._test

    @property
    def time(self):
        return self._time

    @property
    def success(self):
        return self._success

    @property
    def failures(self):
        return self._failures

    @property
    def errors(self):
        return self._errors

    @property
    def skipped(self):
        return self._skipped


def tester():
    obj1 = Obj(1, 1, 1, 1, 1, 1, 1)
    obj2 = Obj(2, 2, 2, 2, 2, 2, 2)
    obj3 = Obj(3, 3, 3, 3, 3, 3, 3)
    obj4 = Obj(4, 4, 4, 4, 4, 4, 4)
    testsuite1 = [obj1, obj2]
    testsuite2 = [obj3, obj4]
    tss = [testsuite1, testsuite2]
    xml = Testsuites("tss", tss).__str__
    return xml

