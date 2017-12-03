import unittest
try:
    import mock
except ImportError as e:
    print "mock not found. Please install by `pip install mock`"
    exit(1)

from package.lib import client
client.disableSSL()
from requests.exceptions import HTTPError

class ClientTestCase(unittest.TestCase):
    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):
        """
        since we typically test a bunch of different
        requests calls for a service, we are going to do
        a lot of mock responses, so its usually a good idea
        to have a helper function that builds these things
        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_google(self):
        r = client.get_google();
        self.assertEquals(200, r.status_code);

    @mock.patch('package.lib.client.get_google')
    def test_patch_google(self, mock_get_google):
        mock_resp = self._mock_response(status=500, raise_for_status=HTTPError("server is down"))
        mock_get_google.return_value = mock_resp
        r = client.patch_google();
        self.assertEquals(200, r.status_code);

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ClientTestCase('test_get_google'))
    suite.addTest(ClientTestCase('test_patch_google'))
    unittest.TextTestRunner(verbosity=2).run(suite)
