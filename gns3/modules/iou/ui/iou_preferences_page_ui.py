# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/iou/ui/iou_preferences_page.ui'
#
# Created: Tue Sep 30 19:03:23 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IOUPreferencesPageWidget(object):
    def setupUi(self, IOUPreferencesPageWidget):
        IOUPreferencesPageWidget.setObjectName(_fromUtf8("IOUPreferencesPageWidget"))
        IOUPreferencesPageWidget.resize(432, 508)
        self.vboxlayout = QtGui.QVBoxLayout(IOUPreferencesPageWidget)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.uiTabWidget = QtGui.QTabWidget(IOUPreferencesPageWidget)
        self.uiTabWidget.setObjectName(_fromUtf8("uiTabWidget"))
        self.uiGeneralSettingsTabWidget = QtGui.QWidget()
        self.uiGeneralSettingsTabWidget.setObjectName(_fromUtf8("uiGeneralSettingsTabWidget"))
        self.gridLayout = QtGui.QGridLayout(self.uiGeneralSettingsTabWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.uiIOURCPathLineEdit = QtGui.QLineEdit(self.uiGeneralSettingsTabWidget)
        self.uiIOURCPathLineEdit.setObjectName(_fromUtf8("uiIOURCPathLineEdit"))
        self.horizontalLayout_5.addWidget(self.uiIOURCPathLineEdit)
        self.uiIOURCPathToolButton = QtGui.QToolButton(self.uiGeneralSettingsTabWidget)
        self.uiIOURCPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIOURCPathToolButton.setObjectName(_fromUtf8("uiIOURCPathToolButton"))
        self.horizontalLayout_5.addWidget(self.uiIOURCPathToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 2)
        self.uiIouyapPathLabel = QtGui.QLabel(self.uiGeneralSettingsTabWidget)
        self.uiIouyapPathLabel.setObjectName(_fromUtf8("uiIouyapPathLabel"))
        self.gridLayout.addWidget(self.uiIouyapPathLabel, 4, 0, 1, 1)
        self.uiIOURCPathLabel = QtGui.QLabel(self.uiGeneralSettingsTabWidget)
        self.uiIOURCPathLabel.setObjectName(_fromUtf8("uiIOURCPathLabel"))
        self.gridLayout.addWidget(self.uiIOURCPathLabel, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(390, 193, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.uiIouyapPathLineEdit = QtGui.QLineEdit(self.uiGeneralSettingsTabWidget)
        self.uiIouyapPathLineEdit.setObjectName(_fromUtf8("uiIouyapPathLineEdit"))
        self.horizontalLayout_6.addWidget(self.uiIouyapPathLineEdit)
        self.uiIouyapPathToolButton = QtGui.QToolButton(self.uiGeneralSettingsTabWidget)
        self.uiIouyapPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIouyapPathToolButton.setObjectName(_fromUtf8("uiIouyapPathToolButton"))
        self.horizontalLayout_6.addWidget(self.uiIouyapPathToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 2)
        self.uiTabWidget.addTab(self.uiGeneralSettingsTabWidget, _fromUtf8(""))
        self.uiServerSettingsTabWidget = QtGui.QWidget()
        self.uiServerSettingsTabWidget.setObjectName(_fromUtf8("uiServerSettingsTabWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.uiServerSettingsTabWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uiUseLocalServercheckBox = QtGui.QCheckBox(self.uiServerSettingsTabWidget)
        self.uiUseLocalServercheckBox.setChecked(True)
        self.uiUseLocalServercheckBox.setObjectName(_fromUtf8("uiUseLocalServercheckBox"))
        self.gridLayout_2.addWidget(self.uiUseLocalServercheckBox, 0, 0, 1, 1)
        self.uiRemoteServersGroupBox = QtGui.QGroupBox(self.uiServerSettingsTabWidget)
        self.uiRemoteServersGroupBox.setObjectName(_fromUtf8("uiRemoteServersGroupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.uiRemoteServersGroupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.uiRemoteServersTreeWidget = QtGui.QTreeWidget(self.uiRemoteServersGroupBox)
        self.uiRemoteServersTreeWidget.setEnabled(False)
        self.uiRemoteServersTreeWidget.setObjectName(_fromUtf8("uiRemoteServersTreeWidget"))
        self.horizontalLayout_3.addWidget(self.uiRemoteServersTreeWidget)
        self.gridLayout_2.addWidget(self.uiRemoteServersGroupBox, 1, 0, 1, 1)
        self.uiTabWidget.addTab(self.uiServerSettingsTabWidget, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiConsolePortRangeGroupBox = QtGui.QGroupBox(self.tab)
        self.uiConsolePortRangeGroupBox.setObjectName(_fromUtf8("uiConsolePortRangeGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.uiConsolePortRangeGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiConsoleStartPortSpinBox = QtGui.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 4001)
        self.uiConsoleStartPortSpinBox.setObjectName(_fromUtf8("uiConsoleStartPortSpinBox"))
        self.horizontalLayout.addWidget(self.uiConsoleStartPortSpinBox)
        self.uiConsolePortRangeLabel = QtGui.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName(_fromUtf8("uiConsolePortRangeLabel"))
        self.horizontalLayout.addWidget(self.uiConsolePortRangeLabel)
        self.uiConsoleEndPortSpinBox = QtGui.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 4500)
        self.uiConsoleEndPortSpinBox.setObjectName(_fromUtf8("uiConsoleEndPortSpinBox"))
        self.horizontalLayout.addWidget(self.uiConsoleEndPortSpinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.uiConsolePortRangeGroupBox)
        self.uiUDPPortRangeGroupBox = QtGui.QGroupBox(self.tab)
        self.uiUDPPortRangeGroupBox.setObjectName(_fromUtf8("uiUDPPortRangeGroupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uiUDPStartPortSpinBox = QtGui.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(_fromUtf8(" UDP"))
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 30001)
        self.uiUDPStartPortSpinBox.setObjectName(_fromUtf8("uiUDPStartPortSpinBox"))
        self.horizontalLayout_4.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtGui.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName(_fromUtf8("uiUDPPortRangeLabel"))
        self.horizontalLayout_4.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtGui.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(_fromUtf8(" UDP"))
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 40000)
        self.uiUDPEndPortSpinBox.setObjectName(_fromUtf8("uiUDPEndPortSpinBox"))
        self.horizontalLayout_4.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem2 = QtGui.QSpacerItem(147, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.uiUDPPortRangeGroupBox)
        spacerItem3 = QtGui.QSpacerItem(20, 304, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.uiTabWidget.addTab(self.tab, _fromUtf8(""))
        self.vboxlayout.addWidget(self.uiTabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(164, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.uiTestSettingsPushButton = QtGui.QPushButton(IOUPreferencesPageWidget)
        self.uiTestSettingsPushButton.setObjectName(_fromUtf8("uiTestSettingsPushButton"))
        self.horizontalLayout_2.addWidget(self.uiTestSettingsPushButton)
        self.uiRestoreDefaultsPushButton = QtGui.QPushButton(IOUPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName(_fromUtf8("uiRestoreDefaultsPushButton"))
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.vboxlayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(IOUPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IOUPreferencesPageWidget)

    def retranslateUi(self, IOUPreferencesPageWidget):
        IOUPreferencesPageWidget.setWindowTitle(_translate("IOUPreferencesPageWidget", "IOS on UNIX", None))
        self.uiIOURCPathToolButton.setText(_translate("IOUPreferencesPageWidget", "...", None))
        self.uiIouyapPathLabel.setText(_translate("IOUPreferencesPageWidget", "Path to iouyap (local Linux server only):", None))
        self.uiIOURCPathLabel.setText(_translate("IOUPreferencesPageWidget", "Path to IOURC (pushed to the server):", None))
        self.uiIouyapPathToolButton.setText(_translate("IOUPreferencesPageWidget", "...", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiGeneralSettingsTabWidget), _translate("IOUPreferencesPageWidget", "General settings", None))
        self.uiUseLocalServercheckBox.setText(_translate("IOUPreferencesPageWidget", "Use the local server (Linux only)", None))
        self.uiRemoteServersGroupBox.setTitle(_translate("IOUPreferencesPageWidget", "Remote servers", None))
        self.uiRemoteServersTreeWidget.headerItem().setText(0, _translate("IOUPreferencesPageWidget", "Host", None))
        self.uiRemoteServersTreeWidget.headerItem().setText(1, _translate("IOUPreferencesPageWidget", "Port", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiServerSettingsTabWidget), _translate("IOUPreferencesPageWidget", "Server settings", None))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("IOUPreferencesPageWidget", "Console port range", None))
        self.uiConsolePortRangeLabel.setText(_translate("IOUPreferencesPageWidget", "to", None))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("IOUPreferencesPageWidget", "UDP tunneling port range", None))
        self.uiUDPPortRangeLabel.setText(_translate("IOUPreferencesPageWidget", "to", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab), _translate("IOUPreferencesPageWidget", "Advanced settings", None))
        self.uiTestSettingsPushButton.setText(_translate("IOUPreferencesPageWidget", "Test settings", None))
        self.uiRestoreDefaultsPushButton.setText(_translate("IOUPreferencesPageWidget", "Restore defaults", None))

