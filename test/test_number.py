class TestCpy:
    def test_import_directly_from_c(self):
        import cbackend

        assert cbackend.answer() == 42

    def test_import_from_python_module(self):
        from cpy.number import number

        assert number() == 42
