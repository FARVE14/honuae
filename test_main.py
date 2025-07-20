from main import measure_browser_load_times


def test_measure_browser_load_times():
    load_times = measure_browser_load_times(
        url="https://www.honuae.com",
        n= 2
    )
    assert all(load_times) < 10
    valid_times = [t for t in load_times if t is not None]
    mean_time = sum(valid_times) / len(valid_times) if valid_times else 0
    assert mean_time < 10


