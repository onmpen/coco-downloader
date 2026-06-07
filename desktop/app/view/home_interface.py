# coding: utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from qfluentwidgets import ScrollArea, setFont

from ..common.style_sheet import StyleSheet
from ..components import SearchCard, PlaceholderWidget


class HomeInterface(ScrollArea):
    """Home interface"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.vBoxLayout = QVBoxLayout(self.scrollWidget)

        self.searchCard = SearchCard(self)
        self.placeholderWidget = PlaceholderWidget(self)

        self._init_widget()
        self._connect_signals()

    def _init_widget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 0, 0, 0)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setObjectName('homeInterface')

        self.scrollWidget.setObjectName('scrollWidget')

        StyleSheet.HOME_INTERFACE.apply(self)
        self.scrollWidget.setStyleSheet("QWidget{background:transparent}")

        self._init_layout()

    def _init_layout(self):
        self.vBoxLayout.setSpacing(24)
        self.vBoxLayout.setContentsMargins(24, 10, 24, 10)

        self.vBoxLayout.addWidget(self.searchCard)
        self.vBoxLayout.addWidget(self.placeholderWidget, 1)

    def _connect_signals(self):
        self.searchCard.searchRequested.connect(self._on_search)

    def _on_search(self, keyword: str, platform: str):
        """Handle search request"""
        # TODO: 实现搜索逻辑
        # 隐藏占位图，显示搜索结果
        self.placeholderWidget.hide()
        print(f"搜索: {keyword}, 平台: {platform}")
