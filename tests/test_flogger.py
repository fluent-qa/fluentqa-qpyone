from qpyone.logs import flogger


def test_flogger():
    flogger.info("test {}", "test_var")
