from datetime import datetime

def generate_race_id(track: str) -> str:
    now = datetime.now()
    return f"{track}_{now.strftime('%Y%m%d')}_{now.hour}{now.minute}"

def format_race_time(time_str: str) -> str:
    # Format time as HH:MM
    return time_str[:5]
