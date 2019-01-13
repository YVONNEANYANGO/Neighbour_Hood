from django.test import TestCase

# Create your tests here.
class ProfileTestClass(TestCase): 

    # Set up method
    def setUp(self):

        # Creating profile and saving it
        self.Ivy= Profile(profile = 'photo')
        self.Ivy.save_profile()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pic,Image))


    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()