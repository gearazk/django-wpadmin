from django.test import TestCase


class SetupTestCase(TestCase):

    def test_setup_to_run(self):
        """Test if the default variables is setup or WPADMIN variable in settings.py"""
        from wpadmin.utils import get_wpadmin_settings
        setting = get_wpadmin_settings()
        self.assertIsNotNone(setting)