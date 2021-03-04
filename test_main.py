import pytest

from .test_helpers import AbstractValidator


class TestDbRoleMapping(AbstractValidator):
    """
    Custom validators for a specific configuration file.
    """

    def test_combinations(self):
        allowed_value_combinations = self.get_validation_data(self.config_name)['allowed_value_combinations']

        def callback(x):
            return x['grantLevel'] == privilege['grantLevel'] and privilege['objectType'] in x['objectType']

        for config in self.json_config:
            for privilege in config['privileges']:
                try:
                    filtered = next(filter(callback, allowed_value_combinations))
                    assert privilege['privilege'] in filtered['privilege']
                except StopIteration:
                    pytest.fail(f'Value combination not allowed {privilege}')


class TestSchemaList(AbstractValidator):
    """
    Custom validators for SchemaList configuration file.
    """


class TestAccessRoleInheritances(AbstractValidator):
    """
    Custom validators for AccessRoleInheritances configuration file.
    """


class TestDataAccessRequest(AbstractValidator):
    """
    Custom validators for TestDataAccessRequest configuration file.
    """


class TestDataClassification(AbstractValidator):
    """
    Custom validators for DataClassification configuration file.
    """


class TestUseCaseRoles(AbstractValidator):
    """
    Custom validators for UseCaseRoles configuration file.
    """


class TestUsertodataUsecase(AbstractValidator):
    """
    Custom validators for UsertodataUsecase configuration file.
    """
