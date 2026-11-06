# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_Formulario(object):
    def setupUi(self, Formulario):
        if not Formulario.objectName():
            Formulario.setObjectName(u"Formulario")
        Formulario.resize(182, 320)
        self.centralwidget = QWidget(Formulario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 121, 244))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.txt_nombre = QLineEdit(self.layoutWidget)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.txt_nombre)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.txt_apellido = QLineEdit(self.layoutWidget)
        self.txt_apellido.setObjectName(u"txt_apellido")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.txt_apellido)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.txt_matricula = QLineEdit(self.layoutWidget)
        self.txt_matricula.setObjectName(u"txt_matricula")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.txt_matricula)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.btn_guardar = QPushButton(self.layoutWidget)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.btn_guardar)

        self.txt_telefono = QLineEdit(self.layoutWidget)
        self.txt_telefono.setObjectName(u"txt_telefono")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.txt_telefono)

        Formulario.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Formulario)
        self.statusbar.setObjectName(u"statusbar")
        Formulario.setStatusBar(self.statusbar)

        self.retranslateUi(Formulario)

        QMetaObject.connectSlotsByName(Formulario)
    # setupUi

    def retranslateUi(self, Formulario):
        Formulario.setWindowTitle(QCoreApplication.translate("Formulario", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Formulario", u"Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("Formulario", u"Apellido", None))
        self.label_3.setText(QCoreApplication.translate("Formulario", u"Matricula", None))
        self.label_4.setText(QCoreApplication.translate("Formulario", u"Telefono", None))
        self.btn_guardar.setText(QCoreApplication.translate("Formulario", u"PushButton", None))
    # retranslateUi

