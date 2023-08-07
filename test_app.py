from datetime import datetime, timezone

from app import App


def test_read(mocker):
    hour = datetime.now(timezone.utc).isoformat()
    temperature = 14.52
    temperature_by_hour = {hour: temperature}

    data_source = mocker.MagicMock()
    data_source.read.return_value = temperature_by_hour
    app = App(
        data_source=data_source,
        plot=mocker.MagicMock(),
    )
    assert app.read(file_name="something.csv") == temperature_by_hour


def test_draw(mocker):
    plot_mock = mocker.MagicMock()
    app = App(
        data_source=mocker.MagicMock(),
        plot=plot_mock,
    )
    hour = datetime.now(timezone.utc)
    iso_hour = hour.isoformat()
    temperature = 14.52
    temperature_by_hour = {iso_hour: temperature}

    app.draw(temperature_by_hour)
    plot_mock.draw.assert_called_with([hour], [temperature])


def test_configure():
    app = App.configure("config.json")

    assert isinstance(app, App)
