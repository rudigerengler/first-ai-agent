
import datetime
import pytz
from smolagents import tool


@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """Returns the current local time in a specified timezone.

    Args:
        timezone: A valid timezone name, such as 'Africa/Johannesburg'.
    """
    try:
        tz = pytz.timezone(timezone)
        local_time = datetime.datetime.now(tz)

        return local_time.isoformat(timespec="seconds")

    except pytz.UnknownTimeZoneError:
        return f"Invalid timezone: {timezone}"
