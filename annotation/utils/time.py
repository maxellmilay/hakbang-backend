from datetime import datetime
import pytz

def get_current_army_hour():
    # Define the Philippine timezone
    philippine_timezone = pytz.timezone("Asia/Manila")

    # Get the current time in the Philippine timezone
    current_time_ph = datetime.now(philippine_timezone)

    # Format the time in 24-hour military (army) format
    current_time_ph_army_format = current_time_ph.strftime("%H")

    return int(current_time_ph_army_format)
