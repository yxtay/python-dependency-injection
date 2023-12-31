from datetime import datetime, timezone

from matplotlib_plot import Plot


def test_draw(mocker):
    plot_date_mock = mocker.patch("matplotlib_plot.matplotlib.pyplot.plot_date")
    show_mock = mocker.patch("matplotlib_plot.matplotlib.pyplot.show")

    plot = Plot()
    hours = [datetime.now(tz=timezone.utc)]
    temperatures = [14.52]
    plot.draw(hours, temperatures)

    _, called_temperatures = plot_date_mock.call_args[0]
    assert (
        called_temperatures == temperatures
    )  # check that plot_date was called with temperatures as second arg
    show_mock.assert_called()  # check that show is called
