# Configuration file validation

Pytest automatically picks up classes starting with Test* from test_main, 
and as soon as the class is instantiated by the test framework, common validation is performed.

A class that inherits an AbstractValidator has access to predefined 
class members to perform custom validation if needed.
