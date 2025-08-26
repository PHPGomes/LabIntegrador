#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtCharts/QChartView>
#include <QtCharts/QLineSeries>
#include <QtCharts/QValueAxis>
#include <QSerialPort>
#include <QTimer>

QT_CHARTS_USE_NAMESPACE

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void readSerialData();

private:
    QSerialPort *serial;
    QLineSeries *series;
    QChart *chart;
    QValueAxis *axisX;
    QValueAxis *axisY;
    int timeStep = 0;
};

#endif // MAINWINDOW_H
