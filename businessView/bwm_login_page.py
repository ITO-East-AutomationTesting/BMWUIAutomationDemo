# coding=utf-8

from baseView.baseView import BaseView, MobileBy


class LoginPage(BaseView):
    phone_number_textbox = (MobileBy.ACCESSIBILITY_ID, 'Phone Number Textbox')
    password_textbox = (MobileBy.ACCESSIBILITY_ID, 'Password Textbox')

    login_button = (MobileBy.ACCESSIBILITY_ID, 'Login Button')

    pin_circle_0 = (MobileBy.ACCESSIBILITY_ID, 'PinCircle0')
    pin_circle_1 = (MobileBy.ACCESSIBILITY_ID, 'PinCircle1')
    pin_circle_2 = (MobileBy.ACCESSIBILITY_ID, 'PinCircle2')
    pin_circle_3 = (MobileBy.ACCESSIBILITY_ID, 'PinCircle3')

    pin_label_message = (MobileBy.ACCESSIBILITY_ID, 'Pin Label')

    not_now_button = (MobileBy.ACCESSIBILITY_ID, 'Not Now Button')
    enable_touch_button = (MobileBy.ACCESSIBILITY_ID, 'Enable Touch ID Button')

    def login_bwm(self, phone_number, password):
        self.set_value(self.phone_number_textbox, phone_number)
        self.set_value(self.password_textbox, password, need_hide_keyboard=True)
        self.click(self.login_button)

    def input_pin_code(self, num):
        pinlocator = (MobileBy.ACCESSIBILITY_ID, '%s' % num)
        self.click(pinlocator)

        # self.set_value(self.pin_circle_0, num1)
        # self.set_value(self.pin_circle_1, num2)
        # self.set_value(self.pin_circle_2, num3)
        # self.set_value(self.pin_circle_3, num4)

    def get_pin_message(self):
        return self.get_attribute(self.pin_label_message, 'label')

    def is_enable_touch_id(self, enable=False):
        if enable:
            self.click(self.enable_touch_button)
        else:
            self.click(self.not_now_button)
