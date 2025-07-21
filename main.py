"""

"""

__author__ = "Faisal Ahmed"

import os
from dotenv import load_dotenv
from pathlib import Path
from src import *


def main() -> None:
    """

    """
    load_dotenv()
    current_working_directory = Path().absolute()
    results_path = current_working_directory / ".results"
    results_path.mkdir(parents=True, exist_ok=True)

    graph_path = results_path / "load_times.png"
    graph_path = graph_path.absolute().as_posix()

    host_url = os.getenv("HOST_URL", "https://www.google.com")
    no_of_attempts = os.getenv("NO_OF_ATTEMPTS", 1)
    load_times = measure_browser_load_time(
        host_url=host_url,
        no_of_attempts=int(no_of_attempts)
    )

    time_parameters = plot_results(
        load_times=load_times,
        host_url=host_url,
        output_graph_path=graph_path
    )

    send_email_with_attachment(
        time_dict=time_parameters,
        host_url=host_url,
        no_of_attempts=int(no_of_attempts),
        file_path=graph_path

    )


if __name__ == '__main__':
    main()
