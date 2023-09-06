from api_collections.booking_api import BookingApi
from api_collections.data_classes.booking_data import Booking


@pytest.fixture()
def create_mock_booking(env):
    mock_data = BookingApi(env).get_booking_by_id(1)
    booking = Booking(**mock_data.json())
    return booking
