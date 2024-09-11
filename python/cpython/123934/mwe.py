from unittest import mock

mm = mock.MagicMock()
print(type(mm.__str__()))
mm.reset_mock(return_value=True)
print(type(mm.__str__()))
print(type(mm.__hash__()))
mm.reset_mock(return_value=True)
print(type(mm.__hash__()))
