from project import suggest_activities, get_local_time_utc, WEATHER_CODES

def test_weather_code_mapping():
    assert WEATHER_CODES[0] == "Clear"
    assert WEATHER_CODES[3] == "Cloudy"
    assert WEATHER_CODES[61] == "Rain"

def test_suggest_activities_known_condition():
    activities = suggest_activities("Clear")
    assert isinstance(activities, list)
    assert len(activities) > 0
    assert "Go for a walk" in activities

def test_suggest_activities_unknown_condition():
    activities = suggest_activities("Blizzard")
    assert isinstance(activities, list)
    assert "Try a new hobby" in activities

def test_get_local_time_utc_basic():
    time_str = get_local_time_utc(0)
    assert isinstance(time_str, str)
    assert len(time_str) == 19  # Format: "YYYY-MM-DD HH:MM:SS"

    time_str_pos = get_local_time_utc(45)
    assert isinstance(time_str_pos, str)
    assert len(time_str_pos) == 19

    time_str_neg = get_local_time_utc(-45)
    assert isinstance(time_str_neg, str)
    assert len(time_str_neg) == 19
