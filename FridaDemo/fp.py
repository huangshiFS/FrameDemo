import frida
import codecs
import sys
class FridaCore:
    def __init__(self):
        self.get_existing_device()

    def enumerate_device(self):
        self.devices = frida.get_device_manager().enumerate_devices()

    def get_existing_device(self):
        self.device = frida.get_device_manager().get_device_matching(lambda d:d.name == "Redmi Note 4X")

    def load_page_js(self,package,jscode):
        self.package = package
        f = codecs.open(jscode, "r", "utf-8")
        self.jscode = f.read()
        f.close()

    def touch_app(self,isSpawan=False):
        # 获取当前正在运行的程序星系
        # Application(identifier="com.ss.android.article.video", name="西瓜视频", pid=28502)
        # app_pro = self.device.get_frontmost_application()
        # applist = self.device.enumerate_applications()
        # print(applist)
        if isSpawan:
            app_pro = self.device.spawn(self.package)
            app_pro = self.device.attach(app_pro)
        else:
            app_pro = self.device.attach(self.package)
        script = app_pro.create_script(self.jscode)
        script.load()
        sys.stdin.read()


if __name__ == '__main__':
    fridacore = FridaCore()
    fridacore.load_page_js("com.smile.gifmaker","js/ks/kw01.js")
    fridacore.touch_app()