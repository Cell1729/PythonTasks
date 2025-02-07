import unittest
from unittest.mock import MagicMock
import customtkinter as ctk
from PIL import Image
import window_state_monitor as wsm
from widget import MainFrameWidget

class TestMainFrameWidget(unittest.TestCase):
    def setUp(self):
        self.master = ctk.CTk()
        self.master.withdraw()  # メインウィンドウを表示しないようにする
        self.main_frame_widget = MainFrameWidget(self.master)
        self.main_frame_widget.pack()

    def tearDown(self):
        self.master.destroy()  # テスト後にウィンドウを破棄する

    def test_buttons_initialization(self):
        # ボタンが正しく初期化されているかをテスト
        self.assertEqual(len(self.main_frame_widget.buttons), 20)
        for button_id, button in self.main_frame_widget.buttons.items():
            self.assertIsInstance(button, ctk.CTkButton)

    def test_image_initialization(self):
        # 画像が正しく初期化されているかをテスト
        self.assertIsInstance(self.main_frame_widget.image, ctk.CTkImage)
        self.assertIsInstance(self.main_frame_widget.image_label, ctk.CTkLabel)

    def test_window_state_monitor_initialization(self):
        # WindowStateMonitorが正しく初期化されているかをテスト
        self.assertIsInstance(self.main_frame_widget.window_state_monitor, wsm.WindowStateMonitor)
        self.assertEqual(self.main_frame_widget.window_state_monitor.buttons, self.main_frame_widget.buttons)
        self.assertEqual(self.main_frame_widget.window_state_monitor.image_label, self.main_frame_widget.image_label)

    def test_window_state_monitor_types(self):
        # WindowStateMonitorのself.buttonsとself.image_labelの型をテスト
        self.assertIsInstance(self.main_frame_widget.window_state_monitor.buttons, dict)
        self.assertIsInstance(self.main_frame_widget.window_state_monitor.image_label, ctk.CTkLabel)
        print(f"Type of self.buttons: {type(self.main_frame_widget.window_state_monitor.buttons)}")
        print(f"Type of self.image_label: {type(self.main_frame_widget.window_state_monitor.image_label)}")

if __name__ == '__main__':
    unittest.main()