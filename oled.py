# 导入必要的模块
from machine import Pin
import time
from machine import SoftI2C
from ssd1306 import SSD1306_I2C  # 使用I2C接口的OLED选择此方法

def run_oled_display():
    # 创建软件I2C对象
    i2c = SoftI2C(sda=Pin(23), scl=Pin(18))
    # 创建OLED对象，指定分辨率和I2C接口
    oled = SSD1306_I2C(128, 64, i2c)

    # 清空屏幕
    oled.fill(0)
    oled.show()
    
    # 显示欢迎信息
    oled.text("welcome use boom system", 0, 0, 1)
    oled.text("system", 0, 6, 1)
    oled.show()  # 执行显示

    # 等待2秒以显示欢迎信息
    time.sleep(2)
    
    # 初始化进度条参数
    total_time = 10  # 总时间10秒
    start_time = time.time()
    end_time = start_time + total_time
    current_time = start_time
    
    while current_time < end_time:
        # 计算已过去的时间
        elapsed_time = current_time - start_time
        # 计算进度百分比
        progress = (elapsed_time / total_time) * 100
        # 限制进度不超过100%
        progress = min(progress, 100)
        
        # 清空进度条区域（保留欢迎信息）
        oled.fill_rect(0, 10, 128, 54, 0)
        
        # 绘制进度条背景
        oled.rect(10, 40, 108, 10, 1)
        
        # 绘制进度条填充
        fill_width = int((progress / 100) * 108)
        oled.fill_rect(10, 40, fill_width, 10, 1)
        
        # 显示进度百分比
        oled.text(f"{int(progress)}%", 10, 30, 1)
        
        oled.show()  # 执行显示
        
        # 更新时间
        time.sleep(0.1)  # 每100毫秒更新一次
        current_time = time.time()
    
    # 最终显示100%
    oled.fill_rect(0, 10, 128, 54, 0)  # 清除进度条区域
    oled.rect(10, 40, 108, 10, 1)  # 绘制进度条边框
    oled.fill_rect(10, 40, 108, 10, 1)  # 填充整个进度条
    oled.text("100%", 10, 30, 1)
    oled.show()
    
    # 可选：保持显示一段时间
    time.sleep(2)
    
    # 可选：清空屏幕或进行其他操作
    oled.fill(0)
    oled.show()

# 程序入口
if __name__ == "__main__":
    run_oled_display()
    # 进入主循环（根据需要添加其他功能）
    while True:
        pass