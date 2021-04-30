from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Tracking, Checkpoint


class TrackingMigrationTest(TestCase):
    """
    Test that the data was loaded in migrations.
    This test assumes some constant values in data/tracking.csv
    and will fail if those values are changed in the admin panel
    or elsewhere after an initial migration.
    """

    def test_at_least_three_tracking_objects(self):
        tracking_objects = Tracking.objects.all()
        self.assertGreaterEqual(3, len(tracking_objects))

    def test_julian_in_tracking_objects(self):
        tracking_objects = Tracking.objects.all()
        julian_objects = [
            t for t in tracking_objects if t.email == 'julian@parcellab.com']
        self.assertGreaterEqual(len(julian_objects), 1)


class CheckpointMigrationTest(TestCase):
    """
    Test that the data was loaded in migrations.
    This test assumes some constant values in data/tracking.csv
    and will fail if those values are changed in the admin panel
    or elsewhere after an initial migration.
    """

    def test_at_least_three_tracking_objects(self):
        checkpoint_objects = Checkpoint.objects.all()
        self.assertGreaterEqual(7, len(checkpoint_objects))

    def test_new_checkpoints_must_have_tracking_fk(self):
        '''
        Test that checkpoints must have a tracking number.
        Without a tracking number, full_clean should raise
        a ValidationError
        '''
        c = Checkpoint(tracking_number=None)
        with self.assertRaises(ValidationError):
            c.full_clean()
