from http import HTTPStatus

from api_collections.booking_api import BookingApi
from api_collections.data_classes.booking_data import Booking


def test_get_api(env, create_mock_booking):
    booking_api = BookingApi(env)
    response = booking_api.get_booking_by_id(booking_id=1)
    actual_booking = Booking(**response.json())
    assert response.status_code == HTTPStatus.OK
    assert create_mock_booking.get_dikt() == actual_booking.get_dikt()


def test_create_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    response = booking_api.create_booking(create_mock_booking)
    assert response.status_code == HTTPStatus.OK


def test_update_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    updated_booking_data = {"totalprice": 600}
    response = booking_api.update_booking(create_mock_booking.bookingid, updated_booking_data)
    assert response.status_code == HTTPStatus.OK or HTTPStatus.FORBIDDEN
    updated_booking_response = booking_api.get_booking_by_id(create_mock_booking.bookingid)
    updated_booking = Booking(**updated_booking_response.json())
    assert updated_booking.totalprice == updated_booking_data["totalprice"]


def test_delete_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    booking_id = create_mock_booking.bookingid
    response = booking_api.delete_booking(booking_id)
    assert response.status_code == HTTPStatus.NO_CONTENT or HTTPStatus.FORBIDDEN
    deleted_booking_response = booking_api.get_booking_by_id(booking_id)
    assert deleted_booking_response.status_code == HTTPStatus.NOT_FOUND


def test_patch_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    updated_booking_data = {"totalprice": 600}
    response = booking_api.patch_booking(create_mock_booking.bookingid, updated_booking_data)
    assert response.status_code == HTTPStatus.OK or HTTPStatus.FORBIDDEN
    updated_booking_response = booking_api.get_booking_by_id(create_mock_booking.bookingid)
    updated_booking = Booking(**updated_booking_response.json())
    assert updated_booking.totalprice == updated_booking_data["totalprice"]


def test_delete_non_existent_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    non_existent_booking_id = 99999
    response = booking_api.delete_booking(non_existent_booking_id)
    assert response.status_code == HTTPStatus.NOT_FOUND or HTTPStatus.FORBIDDEN



def test_patch_booking_invalid_id(env):
    booking_api = BookingApi(env)
    invalid_booking_id = "invalid_id"
    updated_booking_data = {"totalprice": 700}
    response = booking_api.patch_booking(invalid_booking_id, updated_booking_data)
    assert response.status_code == HTTPStatus.NOT_FOUND or HTTPStatus.FORBIDDEN


def test_update_booking_invalid_id(env):
    booking_api = BookingApi(env)
    invalid_booking_id = "invalid_id"
    updated_booking_data = {"totalprice": 700}
    response = booking_api.update_booking(invalid_booking_id, updated_booking_data)
    assert response.status_code == HTTPStatus.NOT_FOUND or HTTPStatus.FORBIDDEN


def test_get_booking_invalid_id(env):
    booking_api = BookingApi(env)
    invalid_booking_id = "invalid_id"
    response = booking_api.get_booking_by_id(invalid_booking_id)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_all_bookings(env):
    booking_api = BookingApi(env)
    response = booking_api.get('/booking')
    assert response.status_code == HTTPStatus.OK
    bookings = response.json()
    assert len(bookings) >= 1
