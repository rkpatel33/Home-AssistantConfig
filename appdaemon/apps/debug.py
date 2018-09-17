import appdaemon.plugins.hass.hassapi as hass
from pushbullet import Pushbullet
from constants import CustomEvents, Keys


class Debug(hass.Hass):
    """
    Debugging app for testing purposes.
    """
    def initialize(self):
        # register callback
        self.listen_event(
            self.handle_test_event,
            CustomEvents.TEST_APP
        )

    def handle_test_event(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        self.log('------------------------------------------------')
        self.log(event_name)
        self.log(data)
        self.log(kwargs)
        self.log('------------------------------------------------')
        self.notify('Success!')
        self.log('Success!')

        pb = Pushbullet(Keys.PUSHBULLET)
        pb.push_note('Success!', None)