import logging
import enum

class Aircraft:
    """
    Aircraft contains information of a aircraft and states that the pilot
    knows. It won't obtain information other than its own state and operation.
    """

    class State(enum.Enum):
        unknown = 0
        scheduled = 1
        arriving = 2
        parked = 3
        departing = 4

    def __init__(self, callsign, model, state, location):

        # Setups the logger
        self.logger = logging.getLogger(__name__)

        self.itineraries = []
        self.velocity = 0

        self.callsign = callsign
        self.model = model
        self.state = state
        self.location = location
        self.pilot = Pilot()

    def set_location(self, location):
        self.logger.debug("%s changed location to %s" % (self, location))
        self.location = location

    def add_itinerary(self, itinerary):
        self.itineraries.append(itinerary)

    def tick(self):
        pass

    """
    def tick(self, delta_time, now):

        return

        # If there's no ongoing itinerary, do nothing
        # FIXME: we assume that the pilot always makes the velocity = 0 before
        # finishing a itinerary
        if len(self.itineraries) < 1:
            return

        # Gets expected v from the pilot
        itinerary = self.itineraries[0]
        expected_v = self.pilot.get_decision(itinerary, self.v, now)

        # Tries the operate the aircraft using the expected v and a, gets back
        # the real distance that the aircraft moved within `delta_time`
        distance = self.operate(expected_v, delta_time)

        # Updates the location
        self.location = itinerary.move_distance_feet(distance)

        # Removes itinerary if we've arrived the end of the current itinerary
        if (itinerary.is_completed()):
            self.itineraries = self.itineraries[1:]
            """

    def operate(self, expected_v, delta_time):
        # TODO
        MAX_ACC = 0
        acc = max(MAX_ACC, (expected_v - self.v) / delta_time)
        # d = v * t + 0.5 * a * t^2
        distance = self.v * delta_time + 0.5 * acc * delta_time * delta_time
        self.v += acc * delta_time
        return distance

class Pilot:

    """
    Gets the decision from pilot for the expected velocity based on current
    states including itinerary status, current aircraft velocity, and the time.
    """
    def get_decision(self, itinerary, v, now):
        # TODO
        return 40
