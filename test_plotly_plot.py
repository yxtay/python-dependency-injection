from datetime import datetime, timezone

from plotly_plot import Plot


def test_draw(mocker):
    figure_mock = mocker.patch("plotly_plot.plotly.graph_objects.Figure")
    scatter_mock = mocker.patch("plotly_plot.plotly.graph_objects.Scatter")

    plot = Plot()
    hours = [datetime.now(timezone.utc)]
    temperatures = [14.52]
    plot.draw(hours, temperatures)

    call_kwargs = scatter_mock.call_args[1]
    assert (
        call_kwargs["y"] == temperatures
    )  # check that plot_date was called with temperatures as second arg
    figure_mock().show.assert_called()  # check that show is called
