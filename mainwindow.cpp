#include "mainwindow.h"
#include <QVBoxLayout>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent),
      serial(new QSerialPort(this)),
      series(new QLineSeries())
{
    // Configura a porta serial
    serial->setPortName("COM3"); // Ajuste para a porta correta
    serial->setBaudRate(QSerialPort::Baud115200);
    serial->open(QIODevice::ReadOnly);

    connect(serial, &QSerialPort::readyRead, this, &MainWindow::readSerialData);

    // Configura o gráfico
    chart = new QChart();
    chart->addSeries(series);
    chart->legend()->hide();
    chart->setTitle("Ângulo do Encoder");

    axisX = new QValueAxis;
    axisX->setTitleText("Tempo");
    axisY = new QValueAxis;
    axisY->setTitleText("Ângulo (graus)");

    chart->addAxis(axisX, Qt::AlignBottom);
    chart->addAxis(axisY, Qt::AlignLeft);
    series->attachAxis(axisX);
    series->attachAxis(axisY);

    QChartView *chartView = new QChartView(chart);
    chartView->setRenderHint(QPainter::Antialiasing);

    setCentralWidget(chartView);
}

MainWindow::~MainWindow() {}

void MainWindow::readSerialData() {
    QByteArray data = serial->readLine().trimmed();
    bool ok;
    double angle = data.toDouble(&ok);

    if(ok) {
        series->append(timeStep++, angle);

        // Mantém eixo X visível para últimos 100 pontos
        if(timeStep > 100)
            axisX->setRange(timeStep - 100, timeStep);

        // Ajusta eixo Y dinamicamente
        axisY->setRange(-180, 180); // Ajuste conforme range do encoder
    }
}
