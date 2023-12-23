import datetime

import pytz
import tzlocal


def get_offset_time_zone() -> datetime.timedelta:
    """
    Get the offset of the local time zone.

    Returns:
        datetime.timedelta: The offset of the local time zone.
    """
    local_timezone = pytz.timezone(str(tzlocal.get_localzone()))
    local_time = datetime.datetime.now(local_timezone)
    return local_time.utcoffset()
