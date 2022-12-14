from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from subwindow import bot_voice


class Sub_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.hi = bot_voice.Ui_Form()
        self.hi.setupUi(self)

    def __del__(self):
        sys.stdout = sys.__stdout__

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 650)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 521, 1000))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/see.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 71, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_5.addWidget(self.pushButton_10)

        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/bot.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QtCore.QSize(49, 30))
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.bot_window)
        self.verticalLayout_5.addWidget(self.pushButton_11)

        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(69, 0))
        self.pushButton_12.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_12.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_5.addWidget(self.pushButton_12)

        spacerItem = QtWidgets.QSpacerItem(20, 151, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)

        spacerItem1 = QtWidgets.QSpacerItem(20, 69, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem1)

        spacerItem2 = QtWidgets.QSpacerItem(13, 253, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_5.addWidget(self.pushButton_13)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 600, 351, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_14.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/lens.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon5)
        self.pushButton_14.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_14.setAutoDefault(True)
        self.pushButton_14.setDefault(True)
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)

        spacerItem3 = QtWidgets.QSpacerItem(65, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
       #Self.label_2.setPixmap(QtGui.QPixmap("D:/jarvis/Jarvis/utils/images/Speak.gif"))
        self.label_2.setText("waiting")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)

        spacerItem4 = QtWidgets.QSpacerItem(68, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)

        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_15.setText("")
        #we are applying image on our button
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/mic.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon6)
        self.pushButton_15.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_15.setAutoDefault(True)
        self.pushButton_15.setDefault(True)
        self.pushButton_15.setFlat(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_4.addWidget(self.pushButton_15)

        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 560, 351, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.textEdit_2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_5.addWidget(self.textEdit_2)

        self.pushButton_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_16.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon7)
        self.pushButton_16.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_16.setCheckable(False)
        self.pushButton_16.setAutoRepeatDelay(300)
        self.pushButton_16.setAutoDefault(True)
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setFlat(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_5.addWidget(self.pushButton_16)

        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 0, 351, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 0, 1400, 1000))
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 650, 421, 421))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/Recognizer.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.movie = QtGui.QMovie("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/AIassistant.gif")
        self.label_3.setMovie(self.movie)
        self.movie1 = QtGui.QMovie("C:/Users/Hp/OneDrive/Desktop/mini-project/image-data/Recognizer.gif")
        self.label_5.setMovie(self.movie1)
        self.startAnimation()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def startAnimation(self):
        self.movie.start()
        self.movie1.start()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JARVIS"))

    def bot_window(self):
        self.jar = Sub_Window()
        self.jar.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
